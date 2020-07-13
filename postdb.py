#!/usr/bin/env python3
""" Para conectar a postgres
version 0.6
"""
import configparser
import datetime
import decimal
import psycopg2


class Post(object):
    """Clase para conectarse a Postgres"""
    def __init__(self, bdd='postgres', usuario='postgres', clave=''):
        """Conexión a posgres con parametros genericos
        el resto se lee de archivo de configuracion"""
        self.resultado = {}
        self.columnas = []
        self.error = None
        # Configuracion
        config = configparser.ConfigParser()
        config.read('./config/dmcamcel.conf')
        host = config['postgres']['host']
        if bdd == '':
            bdd = config.get('postgres', 'database')
        if usuario == '':
            usuario = config.get('postgres', 'user')
        if clave == '':
            clave = config.get('postgres', 'password')
        # Conexión
        try:
            self.conexion = psycopg2.connect(host=host, database=bdd, user=usuario, password=clave)
            self.cursor = self.conexion.cursor()
        except psycopg2.Error as exce:
            print(exce)

    def campos_a_sql(self):
        """Convierte lista de campos INFORMIX a SQL compatible con POSTRGRESQL devuelve una cadena pronta para hacer un
        INSERT en POSTGRES"""
        fragmento = ""
        for item in self.cursor.description:
            campo = item[0]
            tipo = "NUMERIC"
            if item[1] == decimal.Decimal:
                tipo = "REAL"
                if item[5] == 255:
                    tipo = "INTEGER"
            if item[1] == str:
                tipo = "TEXT"
            if item[1] == datetime.date:
                tipo = "DATE"
            if item[1] == datetime.datetime:
                tipo = "TIMESTAMP"
            fragmento = fragmento + campo + " " + tipo + ","
        # eliminar la coma al final
        return fragmento[:-1]

    def consulta(self, sql):
        """Ejecutar el sql y devuelve resultado como diccionario"""
        self.ejecutar(sql)
        cons = [dict(zip([column[0] for column in self.cursor.description], row))
                for row in self.cursor.fetchall()]
        return cons

    def registro(self, sql):
        """Ejecuta SQL y devuelve UN registro como diccionario"""
        self.ejecutar(sql)
        uno = self.cursor.fetchone()
        if uno:
            reg = dict(zip([column[0] for column in self.cursor.description], uno))
        else:
            reg = False
        return reg

    def ejecutar(self, sql):
        """Ejecuta SQL y actualiza nombre de columnas"""
        try:
            self.cursor.execute(sql)
            self.conexion.commit()
            self.columnas = [column[0] for column in self.cursor.description]
        except psycopg2.Error as exce:
            print(exce)


if __name__ == "__main__":
    print("Para usar solo como módulo")
