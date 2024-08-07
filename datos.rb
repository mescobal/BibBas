"""Modulo para interactuar con base de datos. Puede definirse un motor
Version 5.23: autofiltrar al buscar por indice (ir_a)
"""
require 'sqlite3'
require 'psycopg2'
require_relative 'lib/ifmxdb'

# Encapsula llamadas al motor de base de datos
class Datos
  # Asigna valores a atributos del objeto Datos   
  def initialize(motor, data="")
    @motor = motor
    @num_filas = 0
    if @motor == "ifmx"
      # Falta adecuar la configuracion de informix
      @ifmx = ifmxdb.Ifmx()
    elsif @motor == "pg"
      @datab = psycopg2.connect(host='100.0.2.65', database="magik", user="postgres", password="postgres")
      # noinspection PyArgumentList
      @cursor = self.datab.cursor(cursor_factory=psycopg2.extras.DictCursor)
    else
      # la opcion por defecto es sqlite
      # la extensión es "db"
      @data = data
      begin
        # Directorio por defecto "./datos"
        @datab = sqlite3.connect("./datos/" + self.data + ".db",  detect_types=sqlite3.PARSE_DECLTYPES)
        @datab.row_factory = sqlite3.Row
        @cursor = self.datab.cursor()
      rescue
        puts 'error sqlite 3'
      end
    end
  end
  # Rutina genérica de ejecución de SQL levanta error si corresponde
  def ejecutar(sql)
    begin
      @cursor.execute(sql)
      @datab.commit()
    rescue
      puts 'Error al ejecutar sql'
    end
  end
end

# Clase para interactuar con una tabla genérica
class Tabla < Datos
  # Al inicializar debería ini el diccionario y cargar un registro con valores
  def initialize(motor, table, clave="id", data="", ins_clave=false)
    # Ojo! debería rise un error si tabla no existe
    # Si no se especifica nada el campo Key es ID
    @id_insertada = 0
    @bdd = data
    @tabla = table
    @estructura = {}
    @orden = ""
    @limite = ""
    @filtro = ""
    @encontrado = False
    @campos = {}
    Datos.__init__(self, motor, data=self.bdd)
    # Campo que funciona como clave
    @clave = clave
    # define si al insertar se inserta o no el valor del campo clave (x ej si es autonum)
    @insertar_clave = ins_clave
    # Lee un registro y lo almacena en el diccionario interno
    # si la tabla no existe, DEBERIA dar un mensaje de error
    @registro = {}
    @resultado = {}
    sql = "SELECT * FROM " + self.tabla + " LIMIT 1"
    @cursor.execute(sql)
    @asignar_campos()
    @asignar_datos(sql)
  end
  # Asigna descripciones de campos de la tabla abierta"""
  def asignar_campos        
    tipos = {5: "DOUBLE", 7: "TIMESTAMP", 8: "BIGINT", 10: "DATE",
             246: "DECIMAL", 253: "VARCHAR", 254: "CHAR"}
    # Fin de asignación de datos de campos ===================
    @cursor.description.each do |item|
      campo = item[0]
      @registro[campo] = nil
      if tipos.include? item[1]
        # si item 1 está en la lista de tipos, ponerlo
        tipo = tipos[item[1]]
      else
        tipo = str(item[1])
      end
      datos = {"tipo": tipo, "muestra": item[2], "longitud": item[3],
                "decimales": item[5], "nulo": item[6]}
      @campos[campo] = datos
      # poner nombres de campos en self.registro
      # Esta hecho así para que existan nombres a pesar de que la tabla
      # esté vacía
    end
  end
  #Poner un nuevo registro con valores nulos
  def nuevo
    @campos.each do |item|
      @registro[item] = nil
    end
  end
  # inserta una lista de campos en una tabla
  def insertar
    sql = 'INSERT INTO ' + self.tabla + ' ('
    valores = ' VALUES ('
        @registro.each do |campo|
            valor = @registro[campo]
            if valor.nil?
                continue
            end
            if not @registro[campo].nil?
                # Ojo: Mysql Levanta un WARNING si el registro que se va a
                # insertar - excluye un campo que no tiene valor DEFAULT
                if not isinstance(self.registro[campo], str):
                    reg = str(self.registro[campo])
                else
                    reg = "'" + self.registro[campo] + "'"
                end
                if not self.insertar_clave:
                    if campo != self.clave and self.campos[campo]["tipo"] != "TIMESTAMP":
                        # Excluir de la inserción campos CLAVE y TIMESTAMP
                        # sql = sql + " " + campo + " = '" + reg + "',"
                        sql = sql + " " + campo + ","
                        valores = valores + reg + ","
                    end
                else
                    sql = sql + " " + campo + ","
                    valores = valores + reg + ","
                end
            end
        end
        sql = sql[0:-1] + ")"
        valores = valores[0:-1] + ")"
        self.ejecutar(sql + valores)
        self.id_insertada = self.cursor.lastrowid
      end
    # Actualiza una lista de campos en una tabla
    def actualizar
      sql = 'UPDATE ' + self.tabla + " SET "
        @registro.each do |campo|
            if campo != @clave
                if isinstance(self.registro[campo], str)
                    valor = self.registro[campo]
                else
                    valor = str(self.registro[campo])
                end
                sql = sql + " " + campo + " = '" + valor + "',"
            end
        end
        sql = sql[0:-1] + " "
        if not isinstance(self.registro[self.clave], str)
            llave = str(self.registro[self.clave])
        else
            llave = self.registro[self.clave]
        end
        sql = sql + " WHERE " + self.clave + " = '" + llave + "'"
        self.ejecutar(sql)
        self.id_insertada = 0
    end
    # Equivalente al SEEK() de dBase, busca por campo indexado
    def ir_a(valor)
        if valor.nil?
            @encontrado = False
            return
        end
        if isinstance(valor, str)
            svalor = valor
            self.filtro = self.clave + " = '" + svalor + "'"
        else
            svalor = str(valor)
            self.filtro = self.clave + " = " + svalor
        end
        self.filtrar()
    end
    # Asigna el resultado de ejecutar sql a RESULTADO, REGISTRO y ENCONTRADO
    def asignar_datos(sql)
        self.cursor.execute(sql)
        self.resultado = self.cursor.fetchall()
        if not self.resultado
            self.encontrado = False
            self.num_filas = 0
        else
            self.num_filas = len(self.resultado)
            self.encontrado = True
            # pone el primer encontrado como campo SI el número de registros lo permite
            # Ver salidas elegantes para búsquedas de registro que arrojan resultados 0
            begin
                self.cursor.execute(sql)
                fila = self.cursor.fetchone()
                for item in self.registro:
                    self.registro[item] = fila[item]
                end
            rescue
              puts 'Error MySQL'
            end
        end
    end
    # Equivalente a SEARCH de dBase, busca un VALOR por cualquier CAMPO
    def buscar(campo, valor, operador="=")
        if isinstance(valor, str)
            svalor = "'" + valor + "'"
        else
            svalor = str(valor)  # si valor no es tipo string, convertirlo en uno
        end
        sql = "SELECT * FROM " + self.tabla + " WHERE " + campo + operador + svalor
        # agregar posibilidad de ORDEN
        if self.orden != "":
            sql = sql + " ORDER BY " + self.orden
        end
        # agregar posibilidad de LIMITE
        if self.limite != "":
            sql = sql + " LIMIT " + str(self.limite) + " "
        end
        self.asignar_datos(sql)
      end
    # Ejecuta un filtrado segun self.filtro y lo pone como resultado y como registro
    def filtrar
        sql = "SELECT * FROM " + self.tabla + " "
        if self.filtro != "":
            sql = sql + " WHERE " + self.filtro + " "
        end
        # agregar posibilidad de ORDEN
        if self.orden != "":
            sql = sql + " ORDER BY " + self.orden + " "
        end
        # agregar posibilidad de LIMITE
        if self.limite != "":
            sql = sql + " LIMIT " + str(self.limite) + " "
        end
        @asignar_datos(sql)
    end
  # Borra un registro proporcionando el valor de la clave
  def borrar(key)
    if isinstance(key, str)
      sql = "DELETE FROM " + self.tabla + " WHERE " + self.clave + " = '" + key + "'"
    elsif isinstance(key, int)
      sql = "DELETE FROM " + self.tabla + " WHERE " + self.clave + " = " + str(key)
    else
      sql = "DELETE FROM " + self.tabla + " WHERE " + self.clave + " = '" + key + "'"
    end
    ejecutar(sql)
  end
  # borra uno mas registros proporcionando un campo, una condicion y un valor
  def borrar_busqueda(campo, operador, valor)
    sql = "DELETE FROM #{@tabla} WHERE #{campo}#{operador}'#{valor}'"
    .ejecutar(sql)
  end
  # OJO rutina potente que borrar los datos de la tabla que coinciden con self.filtro"""
  def borrar_filtro
    sql = "DELETE FROM #{@tabla} WHERE #{@filtro}"
    ejecutar(sql)
  end
  # OJO rutina que vacía la tabla
  def borrar_tabla
    sql = "TRUNCATE TABLE #{@tabla}"
    ejecutar(sql)
  end
  # A partir de una ID devuelve el valor del campo encontrado
  def obtener(campo, numeroid)
    ir_a(numeroid)
    return @registro[campo] if @registro[campo]
    return "S/D"
  end
  # carga datos a la tabla a partir de un formulario web (bottle)
  def cargar_datos(formulario)
    @registro.each do |item|
      next if item == @clave
      # Si no lo hago así, no registra UNICODE
      @registro[item] = formulario.send(item)
    end
  end
end