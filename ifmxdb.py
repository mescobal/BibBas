#!/usr/bin/env python3
""" Nota: para ejecutar via servidor web, hay que habilitar a www-data: poner en
    /etc/environment las lineas
    ODBCINI=/etc/odbc.ini
    INFORMIXSERVER=nombre_del_servidor
    INFORMIXDIR=/opt/IBM/Informix_Client-SDK
    INFORMIXSQLHOSTS=/opt/IBM/Informix_Client-SDK/etc/sqlhosts
    LD_LIBRARY_PATH=/opt/IBM/Informix_Client-SDK/lib:/opt/IBM/Informix_Client-SDK/lib/esql:
    /opt/IBM/Informix_Client-SDK/lib/cli:/opt/IBM/Informix_Client-SDK/lib/client
"""
from __future__ import print_function
import datetime
import decimal
import pyodbc


class Ifmx:
    """Clase para conectarse a Informix"""
    def __init__(self, odbc_dsn="nombre_del_dsn"):
        """Conexión a informix con configuración de codificación de caracteres
        hecha a prueba y error. Probablemente se pueda configurar mejor con la
        documentación adecuada"""
        self.dsn = odbc_dsn
        # Conexión
        self.resultado = {}
        self.columnas = []
        self.error = None
        self.decoding_wmetadata = 'utf-32le'
        self.decoding_char = 'utf-16'
        self.decoding_wchar = 'utf-32le'
        self.encoding = 'utf-8'
        self.dsn = "camcel"
        self.conectar()
        self.cursor = None

    def conectar(self):
        """Conecta a BDD Informix"""
        try:
            cone = pyodbc.connect("DSN=" + self.dsn)
            # DECODING
            cone.setdecoding(pyodbc.SQL_WMETADATA, encoding=self.decoding_wmetadata)
            cone.setdecoding(pyodbc.SQL_CHAR, encoding=self.decoding_char)
            cone.setdecoding(pyodbc.SQL_WCHAR, encoding=self.decoding_wchar)
            # SQL_CHAR: 'utf-16' -> ANDA en algunos casos de error de codif
            # SQL_CHAR: 'utf-32le' -> ANDA en la mayoría de los casos
            # ENCODING
            cone.setencoding(self.encoding)
            cone.setencoding(encoding='utf-8')
            self.cursor = cone.cursor()
        except pyodbc.Error as exce:
            self.error = exce

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
            self.columnas = [column[0] for column in self.cursor.description]
        except pyodbc.Error as exce:
            print(exce)
