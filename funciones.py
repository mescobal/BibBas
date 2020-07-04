#!/usr/bin/env python3
"""Funciones generales version 19.12 """
from __future__ import print_function
import sys
import cgitb
import datetime
import decimal

cgitb.enable()

MESES = [[1, "enero"], [2, "febrero"], [3, "marzo"], [4, "abril"], [5, "mayo"], [6, "junio"],
         [7, "julio"], [8, "agosto"], [9, "setiembre"], [10, "octubre"], [11, "noviembre"],
         [12, "diciembre"]]

UNIDADES = ('', 'UN ', 'DOS ', 'TRES ', 'CUATRO ', 'CINCO ', 'SEIS ', 'SIETE ',
            'OCHO ', 'NUEVE ', 'DIEZ ', 'ONCE ', 'DOCE ', 'TRECE ', 'CATORCE ',
            'QUINCE ', 'DIECISEIS ', 'DIECISIETE ', 'DIECIOCHO ', 'DIECINUEVE ',
            'VEINTE ')
DECENAS = ('VENTI', 'TREINTA ', 'CUARENTA ', 'CINCUENTA ', 'SESENTA ', 'SETENTA ',
           'OCHENTA ', 'NOVENTA ', 'CIEN ')

CENTENAS = ('CIENTO ', 'DOSCIENTOS ', 'TRESCIENTOS ', 'CUATROCIENTOS ', 'QUINIENTOS ',
            'SEISCIENTOS ', 'SETECIENTOS ', 'OCHOCIENTOS ', 'NOVECIENTOS ')


def meses_ejercicio():
    return ["Oct", "Nov", "Dic", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set"]


def meses():
    return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", 
            "Setiembre", "Octubre", "Noviembre", "Diciembre"]


def meses_abrev():
    return ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"]


def a_palabras(number):
    """Convierte un número en representación alfabética"""
    converted = ''
    if not 0 < number < 999999999:
        return 'No es posible convertir el numero a letras'
    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]
    if millones:
        if millones == '001':
            converted += 'UN MILLON '
        elif int(millones) > 0:
            converted += '%sMILLONES ' % convertir_numero(millones)
    if miles:
        if miles == '001':
            converted += 'MIL '
        elif int(miles) > 0:
            converted += '%sMIL ' % convertir_numero(miles)
    if cientos:
        if cientos == '001':
            converted += 'UN '
        elif int(cientos) > 0:
            converted += '%s ' % convertir_numero(cientos)
    converted += 'PESOS'
    return converted.title()


def convertir_numero(num):
    """largo máximo 3 dígitos"""
    output = ''
    if num == '100':
        output = "CIEN "
    elif num[0] != '0':
        output = CENTENAS[int(num[0])-1]
    k = int(num[1:])
    if k <= 20:
        output += UNIDADES[k]
    else:
        if (k > 30) & (num[2] != '0'):
            output += '%sY %s' % (DECENAS[int(num[1])-2], UNIDADES[int(num[2])])
        else:
            output += '%s%s' % (DECENAS[int(num[1])-2], UNIDADES[int(num[2])])
    return output


def entero_pelado(num):
    """Devuelve enter sin comas ni puntos"""
    if isinstance(num, str):
        if "," in num:
            num = num.replace(",", "")
        if "." in num:
            num = float(num)
    return int(num)


def str_to_float(cadena):
    cadena = cadena.replace(" ", "")
    # cadena = cadena.replace("-","")
    cadena = cadena.replace ("$", "")
    if cadena == '' or cadena is None or cadena=="-":
        return 0.00
    if cadena[0] == '(':
        cadena = cadena.replace("(", "")
        cadena = cadena.replace(")", "")
        cadena = "-" + cadena
    if cadena[-3:-2] == '.':
        # entonces remover coma como separador de miles
        cadena = cadena.replace(",", "")
    elif cadena [-3:-2] == ',':
        # sacar punto como separador de miles
        cadena = cadena.replace(".","")
        # luego poner punto como separador decimal
        cadena = cadena.replace(",", ".")
    return float(cadena)


def decimal_pelado(num):
    """Devuelve decimal sin separador de miles"""
    if isinstance(num, str):
        if "," in num:
            num = num.replace(",", "")
    return float(num)


def ano_actual():
    """Devuelve año actual"""
    ahora = datetime.datetime.now()
    return ahora.year


def moneda(num):
    """transforma un número en una cadena con formato moneda"""
    if isinstance(num, decimal.Decimal):
        mon = str(num)
    else:
        mon = numero(num, 2, th_sep=True)
    mon = '$' + mon
    return mon


def substr_replace(cadena, reemplazo, posicion):
    """Reemplaza CADENA con REEMPLAZO en POSICION, sin alterar la longitud de la cadena"""
    cad = cadena[:posicion] + reemplazo + cadena[posicion + len(reemplazo):]
    return cad


def to_decimal(float_price):
    """convierte un flotante en decimal"""
    return decimal.Decimal('%.2f' % float_price)


def to_boolean(variable):
    if variable in ['False', 'false', 0, '0', None]:
        return False
    else:
        return True


def nstr(item):
    """Convierte a string, si es None queda cadena vacía"""
    # if isinstance(item, type(None)):
    if item is None:
        return ''
    return str(item)


def sql_a_fecha(fecha):
    """Convierte fecha en formato mysql a legible"""
    if isinstance(fecha, type(None)):
        return ""
    if isinstance(fecha, datetime.date) or isinstance(fecha, datetime.datetime):
        ano = str(fecha.year)
        mes = str(fecha.month)
        if len(mes) == 1:
            mes = "0" + mes
        dia = str(fecha.day)
        if len(dia) == 1:
            dia = "0" + dia
    else:
        ano = fecha[0:4]
        mes = fecha[5:7]
        dia = fecha[8:11]
    fecha2 = dia + "/" + mes + "/" + ano
    return fecha2


def iso_a_fecha(fecha):
    """Convierte fecha en formato iso a legible"""
    fecharr = fecha.split("-")
    return "%s/%s/%s" % (fecharr[2], fecharr[1], fecharr[0])


def fecha_a_sql(fecha):
    """Convierte fecha legible a fecha aceptable por mysql"""
    if isinstance(fecha, datetime.date) or (isinstance(fecha, datetime.datetime)):
        ano = str(fecha.year)
        mes = str(fecha.month)
        if len(mes) == 1:
            mes = "0" + mes
        dia = str(fecha.day)
        if len(dia) == 1:
            dia = "0" + dia
        fecha2 = ano + "-" + mes + "-" + dia
    elif isinstance(fecha, type(None)):
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
    if isinstance(num, str):
        num = float(num)
    elif isinstance(num, type(None)):
        num = 0
    elif isinstance(num, decimal.Decimal):
        num = float(num)
    places = max(0, places)
    tmp = "%.*f" % (places, num)
    point = tmp.find(".")
    integer = (point == -1) and tmp or tmp[:point]
    deci = (point != -1) and tmp[point:] or ""
    count = 0
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


def hoy_iso():
    """Devuelve el día de hoy en formato ISO"""
    return datetime.date.today().strftime("%Y-%m-%d")


def redondeo(cifra, digitos=0):
    """Rutina par redondeo de cifras decimales como para uso en contabilidad"""
    # Symmetric Arithmetic Rounding for decimal numbers
    if not isinstance(cifra, decimal.Decimal):
        cifra = decimal.Decimal(str(cifra))
    nume = decimal.Decimal("1")
    denomi = (decimal.Decimal('10') ** digitos)
    return cifra.quantize(nume / denomi, decimal.ROUND_HALF_UP)


def diff_years(date1, date2):
    """Calcula la diferencia en años entre 2 fechas en formato mysql"""
    # Devuelve en formato entero
    diff = date2 - date1
    diff_y = int((diff.days + diff.seconds/86400.0)/365.2425)
    return diff_y


def progreso(cuenta, total, estado=''):
    """barra de progreso"""
    largo = 50
    largo_lleno = int(round(largo * cuenta / float(total)))
    porcentaje = round(100.0 * cuenta / float(total), 1)
    barra = '=' * largo_lleno + '-' * (largo - largo_lleno)
    sys.stdout.write('[%s] %s%s ...%s\r' % (barra, porcentaje, '%', estado))
    sys.stdout.flush()


if __name__ == 'main':
    print("Es un módulo no ejecutable")
