"""Funciones generales
 Ver 0.10.28.
 Ver 2.01: agrego cargar datos  (x peewee), valor de checkbox
 Ver 2.10: soluciono perid "Sin datos" para nombre_cliente
 TODO: sacar nombre_cliente para otro lado.
 """

import sys
import decimal
from modelos import db_magik


def entero_pelado(num):
    """Devuelve entero sin comas ni puntos"""
    if isinstance(num, str):
        if "," in num:
            num = num.replace(",", "")
        if "." in num:
            num = float(num)
    return int(num)


def str_to_float(cadena: str) -> float:
    """Convierte cadena a flotante"""
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
    if num is None:
        num = 0
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
        retorno = 0
    return retorno


def entero(valor: str) -> int:
    """ devuelve entero, para evitar error al convertir INT"""
    if valor == "":
        return 0
    if valor is None:
        return 0
    try:
        retorno = int(float(valor))
    except ValueError:
        retorno = 0
    return retorno


def nombre_cliente(tipo: int, ident: int) -> str:
    if tipo == 1:
        if ident == 1117:
            nombre = 'CAMCEL'
        else:
            empr = db_magik.Empresas.get_or_none(ident)
            nombre = empr.emprdes if empr else "Sin datos"
    elif tipo == 2:
        cont = db_magik.Contratos.get_or_none(ident)
        if cont:
            pers = db_magik.Personas.get_or_none(cont.perid)
            nombre = pers.nombre() if pers else "Sin datos"
        else:
            nombre = "Sin datos"
    elif tipo == 3:
        pers = db_magik.Personas.get_or_none(ident)
        nombre = pers.nombre() if pers else "Sin datos"
    elif tipo == 4:
        nombre = "Solicitado por UNEM"
    else:
        nombre = "Sin datos"
    return nombre
