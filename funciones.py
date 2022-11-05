"""Funciones generales
 Ver 0.10.28.
 Ver 2.01: agrego cargar datos  (x peewee), valor de checkbox
 """

import sys
import decimal


def entero_pelado(num):
    """Devuelve entero sin comas ni puntos"""
    if isinstance(num, str):
        if "," in num:
            num = num.replace(",", "")
        if "." in num:
            num = float(num)
    return int(num)


def str_to_float(cadena: str) -> float:
    cadena = cadena.replace(" ", "")
    # cadena = cadena.replace("-","")
    cadena = cadena.replace("$", "")
    if cadena == '' or cadena is None or cadena == "-":
        return 0.00
    if cadena[0] == '(':
        cadena = cadena.replace("(", "")
        cadena = cadena.replace(")", "")
        cadena = "-" + cadena
    if cadena[-3:-2] == '.':
        # entonces remover coma como separador de miles
        cadena = cadena.replace(",", "")
    elif cadena[-3:-2] == ',':
        # sacar punto como separador de miles
        cadena = cadena.replace(".", "")
        # luego poner punto como separador decimal
        cadena = cadena.replace(",", ".")
    return float(cadena)


def decimal_pelado(num: str) -> float:
    """Devuelve decimal sin separador de miles"""
    if "," in num:
        num = num.replace(",", "")
    return float(num)


def substr_replace(cadena, reemplazo, posicion):
    """Reemplaza CADENA con REEMPLAZO en POSICION, sin alterar la longitud de la cadena"""
    cad = cadena[:posicion] + reemplazo + cadena[posicion + len(reemplazo):]
    return cad


def to_decimal(float_price):
    """convierte un flotante en decimal"""
    return decimal.Decimal('%.2f' % float_price)


def to_boolean(variable) -> bool:
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


def progreso(cuenta, total, estado=''):
    """barra de progreso"""
    largo = 50
    largo_lleno = int(round(largo * cuenta / float(total)))
    porcentaje = round(100.0 * cuenta / float(total), 1)
    barra = '=' * largo_lleno + '-' * (largo - largo_lleno)
    sys.stdout.write('[%s] %s%s ...%s\r' % (barra, porcentaje, '%', estado))
    sys.stdout.flush()


def cargar_datos(formulario, registro, indice):
    """carga datos a la tabla a partir de un formulario web (bottle)"""
    for clave, valor in formulario.items():
        if clave == indice:
            continue
        # Si no lo hago así, no registra UNICODE
        setattr(registro, clave, getattr(formulario, clave))


def valor_checkbox(parametro):
    try:
        retorno = int(parametro)
    except ValueError:
        retorno = None
    return retorno


def entero(valor: str) -> int:
    """ devuelve entero, para evitar error al convertir INT"""
    try:
        retorno = int(float(valor))
    except ValueError:
        retorno = 0
    return retorno
