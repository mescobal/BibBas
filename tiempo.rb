# frozen_string_literal: true

# Funciones de tiempo
# Ver 1.02 las descuelgo de "funciones"
# Ver 1.12: creo la clase Tiempo, para manejo de todas las fechas

require 'date'

MESES = [[1, 'enero'], [2, 'febrero'], [3, 'marzo'], [4, 'abril'], [5, 'mayo'], [6, 'junio'],
         [7, 'julio'], [8, 'agosto'], [9, 'setiembre'], [10, 'octubre'], [11, 'noviembre'],
         [12, 'diciembre']].freeze

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

def utc_a_local(hora)
  return hora.localtime if hora.is_a? Time
end

# ===================== FECHA y HORA ======================

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
  if tstamp.instance_of? DateTime
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

# Calcula la diferencia en años entre 2 fechas en formato mysql
def diff_years(date1, date2)
  # Devuelve en formato entero
  diff = date2 - date1
  ((diff.days + diff.seconds / 86_400.0) / 365.2425).to_i
end

# Para manejo de date-time de sqlite. Bien trucho, no chequea limites
class Tiempo
  attr_accessor :ano, :mes, :dia, :hora, :minuto, :fecha, :ahora

  def initialize(inicial = nil)
    @fecha = case inicial
             when String
               parsestring(inicial)
             when DateTime
               inicial
             when Date
               DateTime.parse(inicial.to_s)
             when NilClass
               DateTime.now
             else
               DateTime.new(1000, 1, 1)
             end
    distribuir
  end

  def distribuir
    @ano = @fecha.year
    @mes = @fecha.month
    @dia = @fecha.day
    @hora = @fecha.hour
    @minuto = @fecha.minute
    @ahora = "#{@hora}:#{@minuto}"
  end

  def justificar(numero)
    numero.to_s.rjust(2, '0')
  end

  def cadena
    "#{@ano}-#{justificar(@mes)}-#{justificar(@dia)} #{justificar(@hora)}:#{justificar(@minuto)}"
  end

  def a_hora
    "#{justificar(@hora)}:#{justificar(@minuto)}"
  end

  def a_fecha_local
    "#{justificar(@dia)}/#{justificar(@mes)}/#{@ano}"
  end

  def a_iso
    "#{@ano}-#{justificar(@mes)}-#{justificar(@dia)}"
  end

  def parsestring(strfecha)
    if strfecha.include? '/'
      fec = strfecha.split '/'
      fecha = case fec[2].length
              when 2
                DateTime.strptime(strfecha, '%d/%m/%y')
              when 4
                DateTime.strptime(strfecha, '%d/%m/%Y')
              else
                DateTime.new(1, 1, 1)
              end
    elsif strfecha.include? '-'
      fec = strfecha.split '-'
      fecha = case fec[0].length
              when 4
                DateTime.strptime(strfecha, '%Y-%m-%d')
              when 2
                DateTime.strptime(strfecha, '%y-%m-%d')
              else
                DateTime.new(1, 1, 1)
              end
    else
      fecha = DateTime.new(1000, 1, 1)
    end
    fecha
  end

  def inicio_de_mes
    Date.new(@fecha.year, @fecha.month, 1)
  end

  def fin_de_mes
    Date.new(@fecha.year, @fecha.month, -1)
  end
end
