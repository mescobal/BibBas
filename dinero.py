"""Módulo para manejo de variables ligadas a dinero"""

import decimal
import typing

UNIDADES = ('', 'UN ', 'DOS ', 'TRES ', 'CUATRO ', 'CINCO ', 'SEIS ', 'SIETE ',
            'OCHO ', 'NUEVE ', 'DIEZ ', 'ONCE ', 'DOCE ', 'TRECE ', 'CATORCE ',
            'QUINCE ', 'DIECISEIS ', 'DIECISIETE ', 'DIECIOCHO ',
            'DIECINUEVE ', 'VEINTE ')
DECENAS = ('VENTI', 'TREINTA ', 'CUARENTA ', 'CINCUENTA ', 'SESENTA ',
           'SETENTA ', 'OCHENTA ', 'NOVENTA ', 'CIEN ')

CENTENAS = ('CIENTO ', 'DOSCIENTOS ', 'TRESCIENTOS ', 'CUATROCIENTOS ',
            'QUINIENTOS ', 'SEISCIENTOS ', 'SETECIENTOS ', 'OCHOCIENTOS ',
            'NOVECIENTOS ')


def a_palabras(number) -> str:
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


def convertir_numero(num) -> str:
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
            output += '%sY %s' % (DECENAS[int(num[1])-2],
                                  UNIDADES[int(num[2])])
        else:
            output += '%s%s' % (DECENAS[int(num[1])-2], UNIDADES[int(num[2])])
    return output


def moneda(num: typing.Union[float, decimal.Decimal, int]) -> str:
    """transforma un número en una cadena con formato moneda"""
    if num is None:
        num = 0
    return "$ " + "{:,.2f}".format(num).replace(",", "X").replace(".", ",").replace("X", ".")


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


def redondeo(cifra, digitos=0):
    """Rutina par redondeo de cifras decimales como para uso en contabilidad"""
    # Symmetric Arithmetic Rounding for decimal numbers
    if not isinstance(cifra, decimal.Decimal):
        cifra = decimal.Decimal(str(cifra))
    nume = decimal.Decimal("1")
    denomi = decimal.Decimal('10') ** digitos
    return cifra.quantize(nume / denomi, decimal.ROUND_HALF_UP)
