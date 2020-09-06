#!/usr/bin/env ruby

require 'time'
require 'bigdecimal'

# Varias funciones usadas por emovil en general
module Funciones
  extend self
  def self.meses
    %w[Enero Febrero Marzo Abril Mayo Junio Julio Agosto Setiembre Octubre Noviembre Diciembre]
  end

  def self.meses_abrev
    %w[Ene Feb Mar Abr May Jun Jul Ago Set Oct Nov Dic]
  end

  def self.meses_ejercicio
    %w[Oct Nov Dic Ene Feb Mar Abr May Jun Jul Ago Set]
  end

  # UNIDADES = ['', 'UN ', 'DOS ', 'TRES ', 'CUATRO ', 'CINCO ', 'SEIS ', 'SIETE ',
  #             'OCHO ', 'NUEVE ', 'DIEZ ', 'ONCE ', 'DOCE ', 'TRECE ', 'CATORCE ',
  #             'QUINCE ', 'DIECISEIS ', 'DIECISIETE ', 'DIECIOCHO ',
  #             'DIECINUEVE ', 'VEINTE '].freeze
  # DECENAS = ['VENTI', 'TREINTA ', 'CUARENTA ', 'CINCUENTA ', 'SESENTA ',
  #           'SETENTA ', 'OCHENTA ', 'NOVENTA ', 'CIEN '].freeze
  # CENTENAS = ['CIENTO ', 'DOSCIENTOS ', 'TRESCIENTOS ', 'CUATROCIENTOS ',
  #             'QUINIENTOS ', 'SEISCIENTOS ', 'SETECIENTOS ', 'OCHOCIENTOS ',
  #             'NOVECIENTOS '].freeze

  # # Convierte un numero en representacion alfabetica
  # def a_palabras(number)
  #   converted = ''
  #   return 'No es posible convertir numero a letras' unless (number > 0) && (number < 999_999_999)
  #   number_str = number.to_s.rjust(9, '0')
  #   millones = number_str[0..2]
  #   miles = number_str[3..5]
  #   cientos = number_str[6..-1]
  #   if millones
  #     if millones == '001'
  #       converted << 'UN MILLON '
  #     elsif millones.to_i > 0
  #       converted << "#{convert_number(millones)}MILLONES "
  #     end
  #   end
  #   if miles
  #     if miles == '001'
  #       converted << 'MIL '
  #     elsif miles.to_i > 0
  #       converted << "#{convert_number(miles)}MIL "
  #     end
  #   end
  #   if cientos
  #     if cientos == '001'
  #       converted << 'UN '
  #     elsif cientos.to_i > 0
  #       converted << "#{convert_number(cientos)} "
  #     end
  #   end
  #   converted << 'PESOS'
  # end

  # def convert_number(n)
  #   # Max length must be 3 digits
  #   output = ''
  #   if n == '100'
  #     output = 'CIEN '
  #   elsif n[0] != '0'
  #     output = CENTENAS[n[0].to_i - 1]
  #   end
  #   k = n[1..-1].to_i
  #   if k <= 20
  #     output += UNIDADES[k]
  #   elsif (k > 30) && (n[2] != '0')
  #     output << "#{DECENAS[n[1].to_i - 2]}Y #{UNIDADES[n[2].to_i]}"
  #   else
  #     output << "#{DECENAS[n[1].to_i - 2]}#{UNIDADES[n[2].to_i]}"
  #   end
  #   output
  # end

  # # Devuelve ano actual
  # def ano_actual
  #   ahora = Time.now
  #   ahora.year
  # end

  # transforma un numero en una cadena con formato moneda
  def self.moneda(num)
    mon = if num.class == BigDecimal
            format('%.2f', num.truncate(2))
          else
            numero(num, 2)
          end
    mon = '$ ' + mon
    mon
  end

  # # Reemplaza CADENA con REEMPLAZO en POSICION, sin alterar la longitud de la cadena
  # def substr_replace(cadena, reemplazo, posicion)
  #   cadena[0..posicion] + reemplazo + cadena[posicion + reemplazo.length..-1]
  # end

  # # convierte un flotante en decimal
  # def to_decimal(float_price)
  #   BigDecimal(float_price, 2)
  # end

  # Convierte a string, si es None queda cadena vacia
  def self.nstr(item)
    resultado = item.nil? ? '' : item.to_s
    resultado
  end

  # Convierte fecha en formato sql a legible 2018-12-31 a 31/12/18
  def self.sql_a_fecha(fecha)
    return '' if fecha.nil?

    if (fecha.is_a? Date) || (fecha.is_a? DateTime) || (fecha.is_a? Time)
      ano = fecha.year.to_s
      mes = fecha.month.to_s
      mes = '0' + mes if mes.length == 1
      dia = fecha.day.to_s
      dia = '0' + dia if dia.length == 1
    else
      ano = fecha[0..3]
      mes = fecha[5..6]
      dia = fecha[8..9]
    end
    fecha2 = "#{dia}/#{mes}/#{ano}"
    fecha2
  end

  def self.iso_a_fecha(fecha)
    sql_a_fecha(fecha)
  end

  # convierte fecha dd/mm/aa a iso AAAA-MM-DD
  def self.fecha_a_iso(fecha)
    return '' if fecha.nil?

    if (fecha.is_a? Date) || (fecha.is_a? DateTime) || (fecha.is_a? Time)
      ano = fecha.year.to_s
      mes = fecha.month.to_s
      mes = '0' + mes if mes.length == 1
      dia = fecha.day.to_s
      dia = '0' + dia if dia.length == 1
    else
      fec = fecha.split('/')
      dia = fec[0]
      mes = fec[1]
      ano = fec[2]
      if ano.length == 2
        ano = ano.to_i < 40 ? '20' + ano : '19' + ano
      end
    end
    ano + '-' + mes + '-' + dia
  end

  # Convierte fecha iso completa a fecha iso corta
  def self.fecha_iso_corta(fecha)
    fecha[0..9]
  end

  #  ano = fecha.year.to_s
  # # Convierte fecha legible a fecha aceptable por mysql
  # def fecha_a_sql(fecha)
  #   if (fecha.is_a? Date) || (fecha.is_a? DateTime)
  #     ano = fecha.year.to_s
  #     mes = fecha.month.to_s
  #     mes = '0' + mes if mes.length == 1
  #     dia = str(fecha.day)
  #     dia = '0' + dia if dia.length == 1
  #     fecha2 = ano + '-' + mes + '-' + dia
  #   elsif fecha.nil?
  #     fecha2 = nil
  #   else
  #     fec = fecha.split('/')
  #     dia = fec[0]
  #     mes = fec[1]
  #     ano = fec[2]
  #     if ano.length == 2
  #       ano = ano.to_i < 40 ? '20' + ano : '19' + ano
  #     end
  #     fecha2 = ano + '-' + mes + '-' + dia
  #   end
  #   fecha2
  # end

  # def estampa_a_hora(estampa)
  #   estampa.strftime('%H:%M')
  # end

  # def estampa_tiempo(fecha = nil)
  #   fecha = Time.now if fecha.nil?
  #   fecha.strftime('%Y-%m-%dT%H:%M')
  # end

  def self.entero_pelado(num)
    num = num.is_a?(String) ? num.tr(',', '').to_i : num.to_i
    num
  end

  def self.decimal_pelado(num)
    num = num.is_a?(String) ? num.tr(',', '').to_f : num.to_f
    num
  end

  # Convierte un numero a cadena con decimal y separador de miles
  def self.numero(num, lugares = 0)
    num = 0 if num.nil?
    # Sacarle las comas. Solo puntos son sep dec
    num = num.tr(',', '') if num.is_a?(String)
    # todo a float
    num = num.to_f
    # formatear segun lugares
    tmp = format("%.#{lugares}f", num)
    # separar entero/decimal
    partes = tmp.split('.')
    # convertir todo a cadena
    entero = partes[0].to_s
    decimal = partes[1].to_s
    # Agregar coma separando miles
    ent = ts(entero)
    # agregar punto al final de enteros
    ent << '.' if decimal != ''
    # juntar todo
    ent + decimal
  end

  def self.numero_ss(num, lugares=0)
    num = 0 if num.nil?
    # Sacarle las comas. Solo puntos son sep dec
    num = num.tr(',', '') if num.is_a?(String)
    # todo a float
    num = num.to_f
    # formatear segun lugares
    format("%.#{lugares}f", num)
  end

  # # Devuelve el dia de hoy en formato estandar
  def self.hoy
    Time.now.strftime('%d/%m/%y')
  end

  def self.hoy_iso
    Time.now.strftime('%Y-%m-%d')
  end

  def self.hora
    Time.now.strftime('%H:%M')
  end

  # def redondeo(cifra, digitos = 0)
  #   # Rutina par redondeo de cifras decimales como para uso en contabilidad
  #   # Symmetric Arithmetic Rounding for decimal numbers
  #   cifra = BigDecimal(cifra) if cifra.class != BigDecimal
  #   cifra.round(digitos)
  #   # cifra.quantize(decimal.Decimal('1') / (decimal.Decimal('10') ** digitos), decimal.ROUND_HALF_UP)
  # end

  # # Calcula la diferencia en anos entre 2 fechas en formato mysql
  # def diff_years(date1, date2)
  #   # Devuelve en formato entero
  #   diff = date2 - date1
  #   diff_y = int((diff.days + diff.seconds / 86_400.0) / 365.2425)
  #   diff_y
  # end

  # Numero con separadores de miles
  def self.ts(st)
    st = st.reverse
    r = ''
    max = if st[-1].chr == '-'
            st.size - 1
          else
            st.size
          end
    if st.to_i == st.to_f
      # 1.upto(st.size) { |i| r << st[i - 1].chr; r << ',' if (i % 3).zero? && i < max }
      1.upto(st.size) do |i|
        r << st[i - 1].chr
        r << ',' if (i % 3).zero? && i < max
      end
    else
      start = nil
      1.upto(st.size) do |i|
        r << st[i - 1].chr
        start = 0 if r[-1].chr == '.' && !start
        if start
          r << ',' if (start % 3).zero? && start != 0 && i < max
          start += 1
        end
      end
    end
    r.reverse
  end

  def self.vacio(variable)
    case variable.class
    when String
      valor = variable.nil? || variable.empty? ? true : false
    when Integer
      valor = variable.nil? ? true : false
    when NilClass
      valor = true
    else
      valor = variable.nil? || variable.empty? ? true : false
    end
    valor
  end

  def self.to_boolean(variable)
    case variable
    when true, 'true', 1, '1' then valor = true
    when false, 'false', 0, '0', nil then valor = false
    else valor = true
    end
    valor
  end
end
