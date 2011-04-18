#!/usr/bin/env ruby
# Funciones generales
import datetime
import decimal
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
        "julio", "agosto", "setiembre", "octubre", "noviembre", 
        "diciembre"]

UNIDADES = (
    '',
    'UN ',
    'DOS ',
    'TRES ',
    'CUATRO ',
    'CINCO ',
    'SEIS ',
    'SIETE ',
    'OCHO ',
    'NUEVE ',
    'DIEZ ',
    'ONCE ',
    'DOCE ',
    'TRECE ',
    'CATORCE ',
    'QUINCE ',
    'DIECISEIS ',
    'DIECISIETE ',
    'DIECIOCHO ',
    'DIECINUEVE ',
    'VEINTE '
)
DECENAS = (
    'VENTI',
    'TREINTA ',
    'CUARENTA ',
    'CINCUENTA ',
    'SESENTA ',
    'SETENTA ',
    'OCHENTA ',
    'NOVENTA ',
    'CIEN '
)
CENTENAS = (
    'CIENTO ',
    'DOSCIENTOS ',
    'TRESCIENTOS ',
    'CUATROCIENTOS ',
    'QUINIENTOS ',
    'SEISCIENTOS ',
    'SETECIENTOS ',
    'OCHOCIENTOS ',
    'NOVECIENTOS '
)
 
def a_palabras(number):
    """Convierte un número en representación alfabética"""
    converted = ''
    if not (0 < number < 999999999):
        return 'No es posible convertir el numero a letras'
    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]
    if(millones):
        if(millones == '001'):
            converted += 'UN MILLON '
        elif(int(millones) > 0):
            converted += '%sMILLONES ' % __convertNumber(millones)
    if(miles):
        if(miles == '001'):
            converted += 'MIL '
        elif(int(miles) > 0):
            converted += '%sMIL ' % __convertNumber(miles)
    if(cientos):
        if(cientos == '001'):
            converted += 'UN '
        elif(int(cientos) > 0):
            converted += '%s ' % __convertNumber(cientos)
    converted += 'PESOS'
    return converted.title()
 
def __convertNumber(n):
    """
    Max length must be 3 digits
    """
    output = ''
 
    if(n == '100'):
        output = "CIEN "
    elif(n[0] != '0'):
        output = CENTENAS[int(n[0])-1]
 
    k = int(n[1:])
    if(k <= 20):
        output += UNIDADES[k]
    else:
        if((k > 30) & (n[2] != '0')):
            output += '%sY %s' % (DECENAS[int(n[1])-2], UNIDADES[int(n[2])])
        else:
            output += '%s%s' % (DECENAS[int(n[1])-2], UNIDADES[int(n[2])])
 
    return output


def moneda(num):
    """transforma un número en una cadena con formato moneda"""
    mon = numero(num, 2, th_sep=True)
    mon = '$' + mon
    return mon
def substr_replace(cadena, reemplazo, posicion):
    """Reemplaza CADENA con REEMPLAZO en POSICION, sin alterar la longitud de la cadena"""
    s = cadena[:posicion] + reemplazo + cadena[posicion + len(reemplazo):]
    return s
def to_decimal(float_price):
    """convierte un flotante en decimal"""
    return decimal.Decimal('%.2f' % float_price)
def mysql_a_fecha(fecha):
    """Convierte fecha en formato mysql a legible"""
    if type(fecha) == type(None):
        return ""
    if (type(fecha) is (datetime.date) or (type(fecha) is datetime.datetime)):
        ano = str(fecha.year)
        mes = str(fecha.month)
        if len(mes)==1:
            mes = "0" + mes
        dia = str(fecha.day)
        if len(dia)==1:
            dia = "0" + dia
    else:
        ano = fecha[0:4]
        mes = fecha[5:7]
        dia = fecha[8:11]
    fecha2 = dia + "/" + mes + "/" + ano
    return fecha2
def fecha_a_mysql(fecha):
    """Convierte fecha legible a fecha aceptable por mysql"""
    if (type(fecha) is (datetime.date) or (type(fecha) is datetime.datetime)):
        ano = str(fecha.year)
        mes = str(fecha.month)
        if len(mes)==1:
            mes = "0" + mes
        dia = str(fecha.day)
        if len(dia)==1:
            dia = "0" + dia
        fecha2 = ano + "-" + mes + "-" + dia
    elif type(fecha) is type(None):
        fecha2 = None
    else:
        fec = fecha.split("/")
        dia = fec[0]
        mes = fec[1]
        ano = fec[2]
        if len(ano) == 2:
            if int(ano) < 40:
                ano = "20" + ano
            else:
                ano = "19" + ano
        fecha2 = ano + "-" + mes + "-" + dia
    return fecha2

def numero(num, places=2, th_sep=False):
    """Format a number with grouped thousands and given decimal places"""
    if type(num) is str:
        num = float(num)
    elif type(num) == type(None):
        num = 0
    elif type(num) == decimal.Decimal:
        num = float(num)
    places = max(0, places)
    tmp = "%.*f" % (places, num)
    point = tmp.find(".")
    integer = (point == -1) and tmp or tmp[:point]
    deci = (point != -1) and tmp[point:] or ""
    count =  0
    formatted = []
    if th_sep:
        for i in range(len(integer), 0, -1):
            count += 1
            formatted.append(integer[i - 1])
            if count % 3 == 0 and i - 1:
                formatted.append(",")
        integer = "".join(formatted[::-1])
    return integer + deci
def hoy():
    """Devuelve el día de hoy en formato estándard"""
    return datetime.date.today().strftime("%d/%m/%y")
def redondeo(cifra, digitos=0):
    """Rutina par redondeo de cifras decimales como para uso en contabilidad"""
    # Symmetric Arithmetic Rounding for decimal numbers
    if type(cifra) != decimal.Decimal:
        cifra = decimal.Decimal(str(cifra)) 
    return cifra.quantize(decimal.Decimal("1") / (decimal.Decimal('10') ** digitos), decimal.ROUND_HALF_UP) 
def diff_years(date1, date2):
    """Calcula la diferencia en años entre 2 fechas en formato mysql"""
    # Devuelve en formato entero
    diff  = date2 - date1
    diff_y = int((diff.days + diff.seconds/86400.0)/365.2425)
    return diff_y

if __name__ == 'main':
    print "Es un módulo no ejecutable"
