#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Modulo para interactuar con base de datos. Puede definirse un motor"""
# import warnings ; warnings.filterwarnings('ignore')
import MySQLdb
import MySQLdb.cursors
import sqlite3
import ConfigParser
#import os
class Datos():
    """Encapsula llamadas al motor de base de datos"""
    def __init__(self, host = "",  data = "", motor = ""):
        """Experimental: posibilidad de inclir como motor SQLite"""
        # Lee valores por defecto desde archivo de configuracion
        # Seguridad: posibilidad de colocar el archivo en /etc
        config = ConfigParser.ConfigParser()
        config.readfp(open("./conf/geined.conf"))
        if host == "":
            host = config.get("mysql","host")
        if data == "":
            data = config.get("mysql","schema")
        if motor == "":
            motor = "mysql"
        # Asigna valores a atributos del objeto Datos
        self.host = host
        self.motor = motor
        self.user = config.get("mysql","user")
        self.passwd = config.get("mysql","password")
        self.data = data
        self.num_filas = 0
        if self.motor == "mysql":
            # Aun no está pronta la posibilidad de SQLite3
            try:
                self.db = MySQLdb.connect(self.host, self.user, self.passwd,
                    db=self.data)
                self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
                self.lista = self.db.cursor()
            except MySQLdb.Error ,  e:
                self.error(e)
        else:
            try:
                self.db = sqlite3.connect(self.data + ".sq3")
                self.db.row_factory = sqlite3.Row
                self.cursor = self.db.cursor()
            except sqlite3.Error, e:
                self.error(e)

    def ejecutar(self, sql):
        """Rutina genérica de ejecución de SQL levanta error si corresponde"""
        try:
            self.cursor.execute(sql)
        except MySQLdb.Error, e:
            self.error(e)

    def error(self, error):
        """Página web mostrando error de acceso a base de datos"""
        print 'Content-Type: text/html; charset=utf-8'
        print ""
        print '<head>'
        print '<script type="text/javascript" src="geined.js" charset="utf-8"></script>'
        print "<title>Error</title>"
        print '<link type="text/css" href="./css/geined.css" rel="stylesheet" />'
        print '</head>'
        print '<body><div id="env_fina">'
        print "<h1>Entrada al sistema</h1>"
        print "No se pudo estabecer la conexion con la base de datos por " + str(error) + ".<br />"
        print "</div></body></html>"


class Tabla(Datos):
    """Clase para interactuar con una tabla genérica"""
    def __init__(self, table = "clientes", clave="id", data="", ins_clave=False):
        """Al inicializar debería ini el diccionario y cargar un registro con valores"""
        # Ojo! debería rise un error si tabla no existe
        # Si no se especifica nada el campo Key es ID
        self.id_insertada = 0
        self.bdd = data
        self.tabla = table
        self.estructura = {}
        self.orden = ""
        self.limite = ""
        self.filtro = ""
        self.encontrado = False
        self.campos = {}
        Datos.__init__(self, data = self.bdd)
        # Campo que funciona como clave
        self.clave = clave
        # define si al insertar se inserta o no el valor del campo clave (x ej si es autonum)
        self.insertar_clave = ins_clave
        # Lee un registro y lo almacena en el diccionario interno
        # TODO: si la tabla no existe, dar un mensaje de error
        self.registro = {}
        self.resultado = {}
        sql = "SELECT * FROM " + self.tabla + " LIMIT 1"
        self.cursor.execute(sql)
        self.asignar_campos()
        self.asignar_datos(sql)
    def asignar_campos(self):
        """Asigna descripciones de campos de la tabla abierta"""
        datos = {}
        tipos = {5:"DOUBLE", 7:"TIMESTAMP", 8:"BIGINT", 10:"DATE",
            246:"DECIMAL", 253:"VARCHAR", 254:"CHAR"}
        # Fin de asignación de datos de campos ===================
        for item in self.cursor.description:
            campo = item[0]
            self.registro[campo] = None
            if item[1] in tipos:
                # si item 1 está en la lista de tipos, ponerlo
                tipo = tipos[item[1]]
            else:
                tipo = str(item[1])
            datos = {"tipo":tipo, "muestra":item[2], "longitud":item[3],
                "decimales":item[5], "nulo":item[6]}
            self.campos[campo] = datos
            # poner nombres de campos en self.registro
            # Esta hecho así para que existan nombres a pesar de que la tabla
            # esté vacía
    def nuevo(self):
        """Poner un nuevo registro con valores nulos"""
        for item in self.campos:
            self.registro[item] = None
    def insertar(self):
        """inserta una lista de campos en una tabla"""
        sql = 'INSERT INTO ' + self.tabla + ' SET '
        for campo in self.registro:
            if self.registro[campo] != None:
                # Ojo: Mysql Levanta un WARNING si el registro que se va a
                # insertar - excluye un campo que no tiene valor DEFAULT
                if type(self.registro[campo]) != "str":
                    reg = str(self.registro[campo])
                else:
                    reg = self.registro[campo]
                if not self.insertar_clave:
                    if campo != self.clave and self.campos[campo]["tipo"] != "TIMESTAMP":
                        # Excluir de la inserción campos CLAVE y TIMESTAMP
                        sql = sql + " " + campo + " = '" + reg + "',"
                else:
                    sql = sql + " " + campo + " = '" + reg + "',"
        sql = sql[0:-1] + " "
        self.ejecutar(sql)
        self.id_insertada = self.cursor.lastrowid
    def actualizar(self):
        """Actualiza una lista de campos en una tabla"""
        sql = 'UPDATE ' + self.tabla + " SET "
        for campo in self.registro:
            if campo != self.clave:
                if type(self.registro[campo]) != "str":
                    valor = str(self.registro[campo])
                else:
                    valor = self.registro[campo]
                sql = sql + " " + campo + " = '" + valor + "',"
        sql = sql[0:-1] + " "
        if type(self.registro[self.clave]) != "str":
            llave = str(self.registro[self.clave])
        else:
            llave = self.registro[self.clave]
        sql = sql + " WHERE " + self.clave + " = '" + llave + "'"
        self.ejecutar(sql)

    def ir_a(self, valor):
        """Equivalente al SEEK() de dBase, busca por campo indexado"""
        if type(valor) != "str":
            svalor = str(valor)
        else:
            svalor = valor
        self.filtro = self.clave + " = '" + svalor + "'"
        self.filtrar()

    def asignar_datos(self, sql):
        """Asigna el resultado de ejecutar sql a RESULTADO, REGISTRO y ENCONTRADO"""
        self.cursor.execute(sql)
        self.resultado = self.cursor.fetchall()
        if len(self.resultado) == 0:
            self.encontrado = False
            self.num_filas = 0
        else:
            self.num_filas = len(self.resultado)
            self.encontrado = True
            # pone el primer encontrado como campo SI el número de registros lo permite
            # Ver salidas elegantes para búsquedas de registro que arrojan resultados 0
            try:
                self.cursor.execute(sql)
                fila = self.cursor.fetchone()
                for item in self.registro:
                    self.registro[item] = fila[item]
            except MySQLdb.Error ,  e:
                self.error(e)
    def buscar(self, campo, valor, operador = " = "):
        """Equivalente a SEARCH de dBase, busca un VALOR por cualquier CAMPO"""
        if type(valor)!= "str":
            svalor = str(valor) # si valor no es tipo string, convertirlo en uno
        else:
            svalor = valor
        sql = "SELECT * FROM " + self.tabla + " WHERE " + campo + operador + "'" + svalor + "'"
        # agregar posibilidad de ORDEN
        if self.orden != "":
            sql = sql + " ORDER BY " + self.orden
        # agregar posibilidad de LIMITE
        if self.limite != "":
            sql = sql + " LIMIT " + str(self.limite) + " "
        self.asignar_datos(sql)

    def filtrar(self):
        """Ejecuta un filtrado segun self.filtro y lo pone como resultado y como registro"""
        sql = "SELECT * FROM " + self.tabla + " "
        if self.filtro != "":
            sql = sql + " WHERE " + self.filtro + " "
        # agregar posibilidad de ORDEN
        if self.orden != "":
            sql = sql + " ORDER BY " + self.orden + " "
        # agregar posibilidad de LIMITE
        if self.limite != "":
            sql = sql + " LIMIT " + str(self.limite) + " "
        self.asignar_datos(sql)
    def borrar(self, key):
        """Borra un registro proporcionando el valor de la clave"""
        sql = "DELETE FROM " + self.tabla + " WHERE " + self.clave + " = '" + key + "'"
        self.ejecutar(sql)

    def borrar_busqueda(self, campo , operador, valor):
        """borra uno mas registros proporcionando un campo, una condicion y un valor"""
        sql = "DELETE FROM " + self.tabla + " WHERE " + campo + operador + "'" + valor + "'"
        self.ejecutar(sql)

    def borrar_filtro(self):
        """OJO rutina potente que borrar los datos de la tabla que coinciden con self.filtro"""
        sql = "DELETE FROM " + self.tabla + " WHERE " + self.filtro
        self.ejecutar(sql)

    def borrar_tabla(self):
        """OJO rutina que vacía la tabla"""
        sql = "TRUNCATE TABLE " + self.tabla
        self.ejecutar(sql)

if __name__ == "__main__":
    print "Para usar solo como módulo"

