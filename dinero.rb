# frozen_string_literal: true

UNIDADES = ['', 'UN ', 'DOS ', 'TRES ', 'CUATRO ', 'CINCO ', 'SEIS ', 'SIETE ',
            'OCHO ', 'NUEVE ', 'DIEZ ', 'ONCE ', 'DOCE ', 'TRECE ', 'CATORCE ',
            'QUINCE ', 'DIECISEIS ', 'DIECISIETE ', 'DIECIOCHO ', 'DIECINUEVE ',
            'VEINTE '].freeze
DECENAS = ['VENTI', 'TREINTA ', 'CUARENTA ', 'CINCUENTA ', 'SESENTA ', 'SETENTA ',
           'OCHENTA ', 'NOVENTA ', 'CIEN '].freeze

CENTENAS = ['CIENTO ', 'DOSCIENTOS ', 'TRESCIENTOS ', 'CUATROCIENTOS ', 'QUINIENTOS ',
            'SEISCIENTOS ', 'SETECIENTOS ', 'OCHOCIENTOS ', 'NOVECIENTOS '].freeze

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

# Convierte un numero en representación alfabética
def a_palabras(number)
  converted = ''
  return 'No es posible convertir el numero a letras' unless number.between?(0, 999_999_999)

  number_str = number.to_s.zfill(9)
  millones = number_str[0..3]
  miles = number_str[3..6]
  cientos = number_str[6..]
  converted << str_millones(millones)
  converted << str_miles(miles)
  converted << str_cientos(cientos)
  converted << 'PESOS'
  converted.capitalize
end

# largo máximo 3 dígitos
def convertir_numero(num)
  output = ''
  if num == '100'
    output = 'CIEN '
  elsif num[0] != '0'
    output = CENTENAS[num[0].to_i - 1]
  end
  k = num[1..].to_i
  output << if k <= 20
              UNIDADES[k]
            elsif (k > 30) && (num[2] != '0')
              "#{DECENAS[num[1].to_i - 2]}Y #{UNIDADES[num[2].to_i]}"
            else
              "#{DECENAS[num[1].to_i - 2]}#{UNIDADES[num[2].to_i]}"
            end
end

# Rutina par redondeo de cifras decimales como para uso en contabilidad
def redondeo(cifra, digitos = 2)
  # Rendondeo aritmético para números decimales
  cifra = decimal.Decimal(cifra.to_s) unless cifra.instace_of? BigDecimal
  nume = decimal.Decimal('1')
  denomi = (decimal.Decimal('10')**digitos)
  cifra.quantize(nume / denomi, decimal.ROUND_HALF_UP)
end
