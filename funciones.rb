# frozen_string_literal: true

# Funciones generales 
# Version 0.12: ajusto fechas / horas / combo box / radio buttons

require 'date'
require 'bigdecimal'

MESES = [[1, 'enero'], [2, 'febrero'], [3, 'marzo'], [4, 'abril'], [5, 'mayo'], [6, 'junio'],
         [7, 'julio'], [8, 'agosto'], [9, 'setiembre'], [10, 'octubre'], [11, 'noviembre'],
         [12, 'diciembre']].freeze

UNIDADES = ['', 'UN ', 'DOS ', 'TRES ', 'CUATRO ', 'CINCO ', 'SEIS ', 'SIETE ',
            'OCHO ', 'NUEVE ', 'DIEZ ', 'ONCE ', 'DOCE ', 'TRECE ', 'CATORCE ',
            'QUINCE ', 'DIECISEIS ', 'DIECISIETE ', 'DIECIOCHO ', 'DIECINUEVE ',
            'VEINTE '].freeze
DECENAS = ['VENTI', 'TREINTA ', 'CUARENTA ', 'CINCUENTA ', 'SESENTA ', 'SETENTA ',
           'OCHENTA ', 'NOVENTA ', 'CIEN '].freeze

CENTENAS = ['CIENTO ', 'DOSCIENTOS ', 'TRESCIENTOS ', 'CUATROCIENTOS ', 'QUINIENTOS ',
            'SEISCIENTOS ', 'SETECIENTOS ', 'OCHOCIENTOS ', 'NOVECIENTOS '].freeze

def meses_ejercicio
  %w[Oct Nov Dic Ene Feb Mar Abr May Jun Jul Ago Set]
end

def meses
  %w[Enero Febrero Marzo Abril Mayo Junio Julio Agosto Setiembre Octubre Noviembre Diciembre]
end

def meses_abrev
  %w[Ene Feb Mar Abr May Jun Jul Ago Set Oct Nov Dic]
end

def dias_semana
  %w[Domingo Lunes Martes Miércoles Jueves Viernes Sábado]
end

# Devuelve el primer día del mes
def inicio_de_mes(fecha)
  Date.new(fecha.year, fecha.month, 1)
end

# Devuelve el ultimo dia del mes
def fin_de_mes(fecha)
  Date.new(fecha.year, fecha.month, -1)
end

def utc_a_local(hora)
  return hora.localtime if hora.is_a? Time
end

# Convierte fecha formato cadena a fecha formato DATE
def str_to_date(strfecha)
  return strfecha if strfecha.is_a? Date

  return None unless strfecha.is_a? String

  if strfecha.include? '/'
    fec = strfecha.split '/'
    case fec[2].length
    when 2
      Date.strptime(strfecha, '%d/%m/%y')
    when 4
      Date.strptime(strfecha, '%d/%m/%Y')
    else
      None
    end
  elsif strfecha.include? '-'
    fec = strfecha.split '-'
    if fec[0].length == 4
      Date.strptime(strfecha, '%Y-%m-%d')
    else
      None
    end
  end
end

def str_millones(millones)
  cadena = ''
  return unless millones

  if millones == '001'
    cadena << 'UN MILLON '
  elsif millones.to_i.positive?
    cadena << "#{convertir_numero(millones)}MILLONES "
  end
end

def str_miles(miles)
  cadena = ''
  return unless miles

  if miles == '001'
    cadena << 'MIL '
  elsif miles.to_i.positive?
    cadena << "#{convertir_numero(miles)}MIL "
  end
end

def str_cientos(cientos)
  cadena = ''
  return unless cientos

  if cientos == '001'
    cadena << 'UN '
  elsif cientos.to_i.positive?
    converted << "#{convertir_numero(cientos)} "
  end
end

# Convierte un numero en representacion alfabetica
def a_palabras(number)
  converted = ''
  return 'No es posible convertir el numero a letras' unless number.between?(0, 999_999_999)

  number_str = number.to_s.zfill(9)
  millones = number_str[0..3]
  miles = number_str[3..6]
  cientos = number_str[6..-1]
  converted << str_millones(millones)
  converted << str_miles(miles)
  converted << str_cientos(cientos)
  converted << 'PESOS'
  converted.capitalize
end

# largo maximo 3 digitos
def convertir_numero(num)
  output = ''
  if num == '100'
    output = 'CIEN '
  elsif num[0] != '0'
    output = CENTENAS[num[0].to_i - 1]
  end
  k = num[1..-1].to_i
  output << if k <= 20
              UNIDADES[k]
            elsif (k > 30) && (num[2] != '0')
              "#{DECENAS[num[1].to_i - 2]}Y #{UNIDADES[num[2].to_i]}"
            else
              "#{DECENAS[num[1].to_i - 2]}#{UNIDADES[num[2].to_i]}"
            end
end

# Devuelve enter sin comas ni puntos
def entero_pelado(num)
  if num.is_a? String
    num.replace(',', '') if num.include? ','
    num = num.to_f if num.include? '.'
  end
  num.to_i
end

def str_to_float(cadena)
  cadena.replace(' ', '')
  # cadena = cadena.replace("-","")
  cadena.replace('$', '')
  return 0.00 if cadena == '' || cadena.nil? || cadena == '-'

  if cadena[0] == '('
    cadena.sub! '(', ''
    cadena.sub! ')', ''
    cadena = "-#{cadena}"
  end
  case cadena[-3..-2]
  when '.'
    # entonces remover coma como separador de miles
    cadena.sub! ',', ''
  when ','
    # sacar punto como separador de miles
    cadena.sub! '.', ''
    # luego poner punto como separador decimal
    cadena.sub! ',', '.'
  end
  cadena.to_f
end

# Devuelve decimal sin separador de miles
def decimal_pelado(num)
  num.sub! ',', '' if num.is_a?(String) && num.include?(',')
  num.to_f
end

# transforma un numero en una cadena con formato moneda
def moneda(num)
  mon = if num.class == BigDecimal
          num.to_s
        else
          numero(num, 2)
        end
  "$#{mon}"
end

# Reemplaza CADENA con REEMPLAZO en POSICION, sin alterar la longitud de la cadena
def substr_replace(cadena, reemplazo, posicion)
  cadena[:posicion] + reemplazo + cadena[posicion + len(reemplazo)..-1]
end

# convierte un flotante en decimal
def to_decimal(float_price)
  decimal.Decimal('%.2f' % float_price)
end

def to_boolean(variable)
  return False if ['False', 'false', 0, '0', nil].include? variable

  true
end

# Convierte a string, si es None queda cadena vacia
def nstr(item)
  return if item.nil?

  item.to_s
end

# ===================== FECHA y HORA ======================

# Devuelve año actual
def ano_actual
  aactual = datetime.datetime.now
  aactual.year
end

# Convierte fecha en formato mysql a legible
def sql_a_fecha(fecha)
  return '' if fecha.nil?

  if fecha.instance_of?(Date) || fecha.instance_of?(Time)
    ano = fecha.year.to_s
    mes = fecha.month.to_s
    mes = "0#{mes}" if mes.length == 1
    dia = fecha.day.to_s
    dia = "0#{dia}" if dia.length == 1
  else
    ano = fecha[0..4]
    mes = fecha[5..7]
    dia = fecha[8..11]
  end
  "#{dia}/#{mes}/#{ano}"
end

# Convierte fecha en formato iso a legible
def iso_a_fecha(fecha)
  if fecha.instance_of? String
    fecharr = fecha.split('-')
    valor = "#{fecharr[2]}/#{fecharr[1]}/#{fecharr[0]}"
  elsif fecha.instance_of? Date
    valor = fecha.strftime('%d/%m/%y') if fecha.instance_of? Date
  else
    valor = fecha.class.to_s
  end
  valor
end

# Convierte fecha en formato Date a ISO
def fecha_a_iso(fecha)
  fecha.strftime('%Y-%m-%d')
end

# convierte fecha ISO a datetime de python
def iso_a_datetime(fecha)
  case fecha.class
  when String
    fecha.sub!('/', '-') if fecha.include?('/')
    arrfecha = fecha.split('-')
    valor = Date.new(arrfecha[0].to_i, arrfecha[1].to_i, arrfecha[2].to_i)
  when Date
    valor = fecha
  else
    valor = Date.today
  end
  valor
end

# Convierte fecha legible a fecha aceptable por mysql
def fecha_a_sql(fecha)
  return nil if fecha.nil?

  if (fecha.is_a? Date) || (fecha.is_a? DateTime)
    ano = fecha.year.to_s
    mes = fecha.month.to_s.rjust(2, '0')
    dia = fecha.day.to_s.rjust(2, '0')
  else
    fec = fecha.split('/')
    dia = fec[0]
    mes = fec[1]
    ano = fec[2]
    if len(ano) == 2
      ano = if int(ano) < 40
              "20#{ano}"
            else
              "19#{ano}"
            end
    end
  end
  "#{ano}-#{mes}-#{dia}"
end

# Devuelve el día de hoy en formato estándard
def hoy
  Date.today
end

# Devuelve el día de hoy en formato ISO
def hoy_iso
  Time.now.strftime('%Y-%m-%d')
end

# Devuelve la hora de hoy en formato HH:MM
def ahora
  Time.now.strftime('%H:%M')
end

# Devuelve el TS actual en formato ISO
def timestamp
  a = DateTime.now
  a.iso8601.gsub('T', ' ')
end

def hms(tstamp)
  if tstamp.class == DateTime
    tstamp.strftime('%d/%m/%Y %H:%M:%S')
  else
    ''
  end
end

# devuelve una fecha sumando años, si llega a ser 29 de febrero lo pasa a 1 de marzo
def sumar_anos(fecha, anos)
  return fecha.next_year(anos) if fecha.is_a? Date

  false
end

# Formatea un numero con decimales
def numero(num, places = 0)
  num = num.to_f if num.is_a? String
  num = num.to_f if num.is_a? BigDecimal
  num = 0 if num.nil?
  places = [0, places].max
  "%.#{places}f" %num.round(places)
end

# Rutina par redondeo de cifras decimales como para uso en contabilidad
def redondeo(cifra, digitos = 2)
  # Symmetric Arithmetic Rounding for decimal numbers
  cifra = decimal.Decimal(cifra.to_s) unless cifra.class == BigDecimal
  nume = decimal.Decimal('1')
  denomi = (decimal.Decimal('10')**digitos)
  cifra.quantize(nume / denomi, decimal.ROUND_HALF_UP)
end

# Calcula la diferencia en años entre 2 fechas en formato mysql
def diff_years(date1, date2)
  # Devuelve en formato entero
  diff = date2 - date1
  ((diff.days + diff.seconds / 86_400.0) / 365.2425).to_i
end

# barra de progreso
def progreso(cuenta, total, estado = '')
  largo = 50
  largo_lleno = round(largo * cuenta / total.to_f).to_i
  porcentaje = round(100.0 * cuenta / total.to_f, 1)
  barra = '=' * largo_lleno + '-' * (largo - largo_lleno)
  print "[#{barra}] #{porcentaje}% ...#{estado}"
  $stdout.flush
end

# Cargar datos de un formulario a un registro active_record
def cargar_datos(formulario, registro, indice)
  formulario.each do |llave, valor|
    next if llave == indice

    registro.send("#{llave}=", valor)
  end
end
