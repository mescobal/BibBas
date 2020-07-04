class Dinero
  def initialize(entrada)
    # si entrada es entero
    case entrada.class
    when Integer
      @entero = entrada
      @flotante = entrada.to_f
      @cadena = entrada.to_s + '.00'
      @decimal = BigDecimal(@cadena)
    when Float
      # si entrada es float
      @entero = entrada.to_i
      @flotante = entrada
      @cadena = format('%.2f', entrada)
      @decimal = BigDecimal(entrada, 2)
    when String
      # si entrada es string
      @entero = entrada.to_i
      @flotante = entrada.to_f
      @cadena = entrada
      @decimal = BigDecimal(entrada)
    when BigDecimal
      # si entrada es bigdecimal
      @entero = entrada.to_i
      @flotante = entrada.to_f
      @cadena = entrada.to_s('F')
      @decimal = entrada
    else
      # si entrada no es numero
      @entero = 0
      @flotante = 0.00
      @cadena = '0.00'
      @decimal = 0.00
    end
  end
end
