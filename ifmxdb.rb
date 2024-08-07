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
  def initialize(odbc_dsn='nombre_del_dsn')
    #Conexión a informix con configuración de codificación de caracteres
    # hecha a prueba y error. Probablemente se pueda configurar mejor con la
    # documentación adecuada
    @dsn = odbc_dsn
    # Conexión
    @resultado = {}
    @columnas = []
    @error = nil
    @decoding_wmetadata = 'utf-32le'
    @decoding_char = 'utf-16'
    @decoding_wchar = 'utf-32le'
    @encoding = 'utf-8'
    @dsn = 'camcel'
    self.conectar()
    @cursor = nil
  end

  def conectar
    # Conecta a BDD Informix
    begin
      cone = ODBC.connect("DSN=#{@dsn}")
      # DECODING
      cone.setdecoding(pyodbc.SQL_WMETADATA, encoding=@decoding_wmetadata)
      cone.setdecoding(pyodbc.SQL_CHAR, encoding=@decoding_char)
      cone.setdecoding(pyodbc.SQL_WCHAR, encoding=@decoding_wchar)
      # SQL_CHAR: 'utf-16' -> ANDA en algunos casos de error de codif
      # SQL_CHAR: 'utf-32le' -> ANDA en la mayoría de los casos
      # ENCODING
      cone.setencoding(@encoding)
      cone.setencoding(encoding='utf-8')
      @cursor = cone.cursor()
    rescue
      puts "Error"
    end

    def campos_a_sql
      # Convierte lista de campos informix a SQL compatible con SQLITE
      #  devuelve ina cadena pronta para hacer un INSERT en SQLITE"""
      fragmento = ''
      @cursor.description.each do |item|
        campo = item[0]
        tipo = 'NUMERIC'
        case item[1]
        when decimal.Decimal
          tipo = 'REAL'
          if item[5] == 255
            tipo = "INTEGER"
          end
        when string
          tipo = 'TEXT'
        when datetime.date:
          tipo = "DATE"
        when datetime.datetime:
          tipo = "DATETIME"
        end
        fragmento = "#{fragmento}#{campo} #{tipo},"
        # eliminar la coma al final
      end
      fragmento[0..-2]
    end

    def consulta(sql)
      # Ejecutar el sql y devuelve resultado como diccionario"""
      self.ejecutar(sql)
      cons = [dict(zip([column[0] for column in self.cursor.description], row))
                for row in self.cursor.fetchall()]
      return cons
    end
    
  def registro(sql)
    # Ejecuta SQL y devuelve UN registro como diccionario"""
    self.ejecutar(sql)
    uno = @cursor.fetchone()
    if uno
      reg = dict(zip([column[0] for column in self.cursor.description], uno))
    else
      reg = False
    end
    reg
  end

  def ejecutar(sql)
    # Ejecuta SQL y actualiza nombre de columnas
    begin
      self.cursor.execute(sql)
      @columnas = [column[0] for column in self.cursor.description]
    rescue pyodbc.Error as exce:
      print(exce)
    end
  end
 end
