#!/usr/bin/env ruby
""" Nota: para ejecutar via servidor web, hay que habilitar a www-data: poner en
    /etc/environment las lineas
    ODBCINI=/etc/odbc.ini
    INFORMIXSERVER=nombre_del_servidor
    INFORMIXDIR=/opt/IBM/Informix_Client-SDK
    INFORMIXSQLHOSTS=/opt/IBM/Informix_Client-SDK/etc/sqlhosts
    LD_LIBRARY_PATH=/opt/IBM/Informix_Client-SDK/lib:/opt/IBM/Informix_Client-SDK/lib/esql:
    /opt/IBM/Informix_Client-SDK/lib/cli:/opt/IBM/Informix_Client-SDK/lib/client
"""
require 'datetime'
require 'decimal'
require 'odbc'

# Clase para conectarse a Informix
class Ifmx
    def initialize(odbc_dsn="nombre_del_dsn")
        """Conexión a informix con configuración de codificación de caracteres
        hecha a prueba y error. Probablemente se pueda configurar mejor con la
        documentación adecuada"""
        @dsn = odbc_dsn
        # Conexión
        @resultado = {}
        @columnas = []
        @error = nil
        @decoding_wmetadata = 'utf-32le'
        @decoding_char = 'utf-16'
        @decoding_wchar = 'utf-32le'
        @encoding = 'utf-8'
        @dsn = "camcel"
        conectar
        @cursor = nil
    end
    # Conecta a BDD Informix"
    def conectar
        begin
            cone = pyodbc.connect("DSN=" + @dsn)
            # DECODING
            cone.setdecoding(pyodbc.SQL_WMETADATA, encoding=@decoding_wmetadata)
            cone.setdecoding(pyodbc.SQL_CHAR, encoding=@decoding_char)
            cone.setdecoding(pyodbc.SQL_WCHAR, encoding=@decoding_wchar)
            # SQL_CHAR: 'utf-16' -> ANDA en algunos casos de error de codif
            # SQL_CHAR: 'utf-32le' -> ANDA en la mayoría de los casos
            # ENCODING
            cone.setencoding(@encoding)
            cone.setencoding(encoding='utf-8')
            @cursor = cone.cursor
        rescue
            puts odbc.Error
        end
    end
    def campos_a_sql
        """Convierte lista de campos informix a SQL compatible con SQLITE
        devuelve ina cadena pronta para hacer un INSERT en SQLITE"""
        fragmento = ""
        @cursor.description.each do |item|
            campo = item[0]
            tipo = "NUMERIC"
            tipo = "REAL" if item[1] == decimal.Decimal
            tipo = "INTEGER" if item[5] == 255
            tipo = "TEXT" if item[1] == str
            tipo = "DATE" if item[1] == datetime.date
            tipo = "DATETIME" if item[1] == datetime.datetime
            fragmento = fragmento + campo + " " + tipo + ","
        # eliminar la coma al final
        return fragmento[:-1]
    end
    def consulta(sql)
        """Ejecutar el sql y devuelve resultado como diccionario"""
        ejecutar(sql)
        cons = [dict(zip([column[0] for column in @cursor.description], row))
                for row in @cursor.fetchall()]
        return cons
    end
    def registro(sql)
        """Ejecuta SQL y devuelve UN registro como diccionario"""
        ejecutar(sql)
        uno = @cursor.fetchone()
        if uno:
            reg = dict(zip([column[0] for column in @cursor.description], uno))
        else:
            reg = false
        end
        return reg
    end
    def ejecutar(self, sql)
        """Ejecuta SQL y actualiza nombre de columnas"""
        begin
            @cursor.execute(sql)
            @columnas = [column[0] for column in self.cursor.description]
        rescue
            puts odbc.Error
        end
    end
end