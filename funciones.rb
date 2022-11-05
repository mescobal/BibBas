# frozen_string_literal: true

# Funciones generales
# Version 0.12: ajusto fechas / horas / combo box / radio buttons
# Version 1.04: soluciono error en str_to_float
# Version 1.10: agrego funcion para poner valor a checkboxes IMPORTANTE

require 'date'
require 'bigdecimal'

# Devuelve enter sin comas ni puntos
def entero_pelado(num)
  if num.is_a? String
    num.replace(',', '') if num.include? ','
    num = num.to_f if num.include? '.'
  end
  num.to_i
end

def str_to_float(cadena)
  # Ojo: probable falla cuando es $ 1.234.567,89 -> solucion
  # usar GSUB en lugar de SUB
  # Elimina espacios
  cad2 = cadena.nil? ? '' : cadena.gsub(' ', '')
  # cadena = cadena.replace("-","")
  # Elimina signo de $
  cad2 = cad2.empty? ? '' : cad2.gsub('$', '')
  # Devuelve CERO is está vacío o solo tiene un guión
  return 0.00 if cad2 == '' || cad2.nil? || cad2 == '-'

  # Elimina paréntesis y sustituye por signo de menos
  if cad2[0] == '('
    cad2 = cad2.sub '(', ''
    cad2 = cad2.sub ')', ''
    cad2 = "-#{cad2}"
  end
  # Evaluar separador de decimlaes
  case cad2[-3..-3]
  when '.'
    # entonces remover coma como separador de miles
    cad2 = cad2.gsub ',', ''
  when ','
    # sacar punto como separador de miles
    cad2 = cad2.gsub '.', ''
    # luego poner punto como separador decimal
    cad2 = cad2.sub! ',', '.'
  end
  cad2.to_f
end

# Devuelve decimal sin separador de miles
def decimal_pelado(num)
  num.sub! ',', '' if num.is_a?(String) && num.include?(',')
  num.to_f
end

# transforma un numero en una cadena con formato moneda
def moneda(num)
  mon = if num.instance_of? BigDecimal
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
  decimal.Decimal('%<float_price>.2f', float_price: float_price)
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

# Formatea un numero con decimales
def numero(num, places = 0)
  num = num.to_f if num.is_a? String
  num = num.to_f if num.is_a? BigDecimal
  num = 0 if num.nil?
  places = [0, places].max
  # "%.#{places}f" % num.round(places)
  # sprintf("%#{places}f", num.round(places))
  format("%.#{places}f", num.round(places))
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

def valor_checkbox(parametro)
  parametro.nil? ? nil : parametro.to_i
end
