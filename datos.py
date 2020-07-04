#!/usr/bin/env python3
"""Modulo para interactuar con base de datos. Puede definirse un motor
Version 5.23: autofiltrar al buscar por indice (ir_a)
"""
import sqlite3
import psycopg2
import psycopg2.extras
from lib import ifmxdb


class Datos(object):
    """Encapsula llamadas al motor de base de datos"""
    def __init__(self, motor, data=""):
        # Asigna valores a atributos del objeto Datos
        self.motor = motor
        self.num_filas = 0
        if self.motor == "ifmx":
            # Falta adecuar la configuracion de informix
            self.ifmx = ifmxdb.Ifmx()
        elif self.motor == "pg":
            self.datab = psycopg2.connect(host='100.0.2.65', database="magik", user="postgres", password="postgres")
            self.cursor = self.datab.cursor(cursor_factory=psycopg2.extras.DictCursor)
        else:
            # la opcion por defecto es sqlite
            # la extensión es "db"
            self.data = data
            try:
                # Directorio por defecto "./datos"
                self.datab = sqlite3.connect("./datos/" + self.data + ".db")
                self.datab.row_factory = sqlite3.Row
                self.cursor = self.datab.cursor()
            except sqlite3.Error as error:
                print(error)

    def ejecutar(self, sql):
        """Rutina genérica de ejecución de SQL levanta error si corresponde"""
        try:
            self.cursor.execute(sql)
            self.datab.commit()
        except RuntimeError as error:
            print(error)


class Tabla(Datos):
    """Clase para interactuar con una tabla genérica"""
    def __init__(self, motor, table, clave="id", data="", ins_clave=False):
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
        Datos.__init__(self, motor, data=self.bdd)
        # Campo que funciona como clave
        self.clave = clave
        # define si al insertar se inserta o no el valor del campo clave (x ej si es autonum)
        self.insertar_clave = ins_clave
        # Lee un registro y lo almacena en el diccionario interno
        # si la tabla no existe, DEBERIA dar un mensaje de error
        self.registro = {}
        self.resultado = {}
        sql = "SELECT * FROM " + self.tabla + " LIMIT 1"
        self.cursor.execute(sql)
        self.asignar_campos()
        self.asignar_datos(sql)

    def asignar_campos(self):
        """Asigna descripciones de campos de la tabla abierta"""
        tipos = {5: "DOUBLE", 7: "TIMESTAMP", 8: "BIGINT", 10: "DATE",
                 246: "DECIMAL", 253: "VARCHAR", 254: "CHAR"}
        # Fin de asignación de datos de campos ===================
        for item in self.cursor.description:
            campo = item[0]
            self.registro[campo] = None
            if item[1] in tipos:
                # si item 1 está en la lista de tipos, ponerlo
                tipo = tipos[item[1]]
            else:
                tipo = str(item[1])
            datos = {"tipo": tipo, "muestra": item[2], "longitud": item[3],
                     "decimales": item[5], "nulo": item[6]}
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
        sql = 'INSERT INTO ' + self.tabla + ' ('
        valores = ' VALUES ('
        for campo in self.registro:
            valor = self.registro[campo]
            if valor is None:
                continue
            if self.registro[campo] is not None:
                # Ojo: Mysql Levanta un WARNING si el registro que se va a
                # insertar - excluye un campo que no tiene valor DEFAULT
                if not isinstance(self.registro[campo], str):
                    reg = str(self.registro[campo])
                else:
                    reg = "'" + self.registro[campo] + "'"
                if not self.insertar_clave:
                    if campo != self.clave and self.campos[campo]["tipo"] != "TIMESTAMP":
                        # Excluir de la inserción campos CLAVE y TIMESTAMP
                        # sql = sql + " " + campo + " = '" + reg + "',"
                        sql = sql + " " + campo + ","
                        valores = valores + reg + ","
                else:
                    sql = sql + " " + campo + ","
                    valores = valores + reg + ","
        sql = sql[0:-1] + ")"
        valores = valores[0:-1] + ")"
        self.ejecutar(sql + valores)
        self.id_insertada = self.cursor.lastrowid

    def actualizar(self):
        """Actualiza una lista de campos en una tabla"""
        sql = 'UPDATE ' + self.tabla + " SET "
        for campo in self.registro:
            if campo != self.clave:
                if isinstance(self.registro[campo], str):
                    valor = self.registro[campo]
                else:
                    valor = str(self.registro[campo])
                sql = sql + " " + campo + " = '" + valor + "',"
        sql = sql[0:-1] + " "
        if not isinstance(self.registro[self.clave], str):
            llave = str(self.registro[self.clave])
        else:
            llave = self.registro[self.clave]
        sql = sql + " WHERE " + self.clave + " = '" + llave + "'"
        self.ejecutar(sql)
        self.id_insertada = 0

    def ir_a(self, valor):
        """Equivalente al SEEK() de dBase, busca por campo indexado"""
        if valor is None:
            self.encontrado = False
            return
        if isinstance(valor, str):
            svalor = valor
            self.filtro = self.clave + " = '" + svalor + "'"
        else:
            svalor = str(valor)
            self.filtro = self.clave + " = " + svalor
        self.filtrar()

    def asignar_datos(self, sql):
        """Asigna el resultado de ejecutar sql a RESULTADO, REGISTRO y ENCONTRADO"""
        self.cursor.execute(sql)
        self.resultado = self.cursor.fetchall()
        if not self.resultado:
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
            except RuntimeError as error:
                # Except MySQLdb.Error as e:
                print(error)

    def buscar(self, campo, valor, operador="="):
        """Equivalente a SEARCH de dBase, busca un VALOR por cualquier CAMPO"""
        if isinstance(valor, str):
            svalor = "'" + valor + "'"
        else:
            svalor = str(valor)  # si valor no es tipo string, convertirlo en uno
        sql = "SELECT * FROM " + self.tabla + " WHERE " + campo + operador + svalor
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
        if isinstance(key, str):
            sql = "DELETE FROM " + self.tabla + " WHERE " + self.clave + " = '" + key + "'"
        elif isinstance(key, int):
            sql = "DELETE FROM " + self.tabla + " WHERE " + self.clave + " = " + str(key)
        else:
            sql = "DELETE FROM " + self.tabla + " WHERE " + self.clave + " = '" + key + "'"
        self.ejecutar(sql)

    def borrar_busqueda(self, campo, operador, valor):
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

    def obtener(self, campo, numeroid):
        """A partir de una ID devuelve el valor del campo encontrado"""
        self.ir_a(numeroid)
        if self.registro[campo]:
            return self.registro[campo]
        return "S/D"

    def cargar_datos(self, formulario):
        """carga datos a la tabla a partir de un formulario web (bottle)"""
        for item in self.registro:
            if item == self.clave:
                continue
            # Si no lo hago así, no registra UNICODE
            self.registro[item] = getattr(formulario, item)


if __name__ == "__main__":
    print("Para usar solo como módulo")
