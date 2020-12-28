#!/usr/bin/env python3
"""
Conexiones: librería con conexiones a sqlite e informix
clases con cursoresy operaciones básicas sobre tablas
@author: mescobal
version 7.00
"""
import logging
import datetime
import decimal
import sqlite3
import os.path
import pyodbc

from lib import htm

logging.basicConfig(filename="general.log", level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Dbsqlite(object):
    """Conexión a BDD sqlite"""
    # Conecta a base de datos sqlite3
    def __init__(self, archivo):
        self.conectado = False
        if os.path.isfile(archivo):
            self.archivo = archivo
            self.database = sqlite3.connect(archivo)
            self.database.row_factory = sqlite3.Row
            self.cursor = self.database.cursor()
            self.conectado = True
        else:
            raise ValueError("Archivo SQLITE no encontrado." + archivo)

    def insertar(self, tabla, columnas, fila):
        """ devuelve SQL de inserción para SQLITE"""
        valores = ""
        cadena = "INSERT INTO %s (" % tabla
        for item in columnas:
            cadena = cadena + item + ","
            # valor = getattr(fila, item)
            valor = fila[item]
            if isinstance(valor, str):
                valor = valor.replace("'", "''")
                valor = valor.replace('"', "''")
                valor = htm.limpiar_html(valor)
            else:
                valor = str(valor)
            valores = valores + '"' + valor + '",'
            # Saca la ultima coma
        cadena = cadena[:-1] + ") VALUES ("
        valores = valores.replace("\0", "")
        valores = valores[:-1] + ")"
        # logging.debug(cadena + valores)
        self.cursor.execute(cadena + valores)
        self.database.commit()

    def crear_estructura(self, tabla, cadena):
        """Crea una TABLA con la estructura de CADENA"""
        self.cursor.execute("DROP TABLE IF EXISTS '%s';" % tabla)
        self.cursor.execute(cadena)
        self.database.commit()
        return True


class Dbinformix(object):
    """COnexión a BDD informix"""
    def __init__(self, odbc_dsn="camcel"):
        """Conecta a BDD Informix usando ODBC en /etc/odbc.ini"""
        dsn = "DSN=" + odbc_dsn
        # Conexión
        conn = pyodbc.connect(dsn)
        conn.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-32le')
        conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-32le')
        # conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-32le')
        conn.setencoding(str, 'utf-8')
        self.cursor = conn.cursor()
        self.columnas = []

    def ejecutar(self, sql):
        """Ejecuta SQL y actualiza nombre de columnas"""
        self.cursor.execute(sql)
        self.columnas = [column[0] for column in self.cursor.description]

    def campos_a_sql(self):
        """Convierte lista de campos informix a SQL compatible con SQLITE
        devuelve ina cadena pronta para hacer un INSERT en SQLITE"""
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
                tipo = "DATETIME"
            fragmento = fragmento + campo + " " + tipo + ","
        # eliminar la coma al final
        return fragmento[:-1]


if __name__ == "__main__":
    print("Para usar solo como módulo")
