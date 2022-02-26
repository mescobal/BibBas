"""Funciones de tiempo
version 1.02
version 1.11: con type-hinting, fecha_a_local
version 2.01: agrego diccionario ejercicio_meses
"""

import datetime
import typing
from typing import List

# T I E M P O
MESES = {1: "enero", 2: "febrero", 3: "marzo", 4: "abril", 5: "mayo", 6: "junio",
         7: "julio", 8: "agosto", 9: "setiembre", 10: "octubre", 11: "noviembre",
         12: "diciembre"}


def meses_ejercicio() -> List:
    """Devuelve lista con meses de un ejercicio económico"""
    return ["Oct", "Nov", "Dic", "Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set"]


def ejercicio_meses() -> typing.Dict:
    """Diccionario con mes del ejercicio -> nombre de campo"""
    return {"m01": "OCTUBRE", "m02": "NOVIEMBRE", "m03": "DICIEMBRE", "m04": "ENERO",
            "m05": "FEBRERO", "m06": "MARZO", "m07": "ABRIL", "m08": "MAYO", "m09": "JUNIO",
            "m10": "JULIO", "m11": "AGOSTO", "m12": "SETIEMBRE"}


def meses() -> List:
    """Devuelve lista con meses del año"""
    return ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
            "Setiembre", "Octubre", "Noviembre", "Diciembre"]


def meses_abrev() -> List:
    """Devuelve lista con meses del año abreviados"""
    return ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"]


def dias_semana() -> List:
    """Devuelve lista de días de la semana empezando domingo"""
    return ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]


def inicio_de_mes(fecha_ver: datetime.date) -> datetime.date:
    """ Devuelve primer dia del mes """
    return fecha_ver.replace(day=1)
    # elif isinstance(fecha_ver, str):
    #    fec = str_to_fecha(fecha_ver)
    #    return fec.replace(day=1)


def fin_de_mes(fecha_ver: datetime.date) -> datetime.date:
    """Devuelve ultimo dia del mes"""
    # Arrimarse a fin de mes y agregar 4 días
    proximo = fecha_ver.replace(day=28) + datetime.timedelta(days=4)
    # restar el numero de dias en exceso al ultimo dia del mes
    return proximo - datetime.timedelta(days=proximo.day)


def utc_a_local(hora: datetime.datetime) -> datetime.datetime:
    """Desde hora UTC a local"""
    return hora.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)


def str_to_fecha(fecha_ver: str) -> datetime.date:
    """Devuelve anu fecha a partir de una cadena"""
    # Ver separador y separar matriz
    retorno = datetime.datetime(1, 1, 1)
    if "/" in fecha_ver:
        fec = fecha_ver.split("/")
        if len(fec[2]) == 2:
            retorno = datetime.datetime.strptime(fecha_ver, "%d/%m/%y")
        elif len(fec[2]) == 4:
            retorno = datetime.datetime.strptime(fecha_ver, "%d/%m/%Y")
        else:
            retorno = datetime.datetime(1, 1, 1)
    elif "-" in fecha_ver:
        fec = fecha_ver.split("-")
        if len(fec[0]) == 2:
            retorno = datetime.datetime.strptime(fecha_ver, "%y-%m-%d")
        elif len(fec[0]) == 4:
            retorno = datetime.datetime.strptime(fecha_ver, "%Y-%m-%d")
        else:
            retorno = datetime.datetime(1, 1, 1)
    return retorno


def ano_actual() -> int:
    """Devuelve año actual"""
    aactual = datetime.datetime.now()
    return aactual.year


def sql_a_fecha_local(fecha: str) -> str:
    """Convierte fecha en formato mysql a legible"""
    if isinstance(fecha, type(None)):
        return ""
    else:
        ano = fecha[0:4]
        mes = fecha[5:7]
        dia = fecha[8:11]
    return dia + "/" + mes + "/" + ano


def fecha_a_local(fecha: datetime.date) -> str:
    """Convierte fecha a formato local d/m/a"""
    intermedio = fecha_a_iso(fecha)
    return iso_a_fecha_local(intermedio)


def iso_a_fecha_local(fecha: str) -> str:
    """Convierte fecha en formato iso a legible"""
    fecharr = fecha.split("-")
    return "%s/%s/%s" % (fecharr[2], fecharr[1], fecharr[0])


def fecha_a_sql(fecha: datetime.date):
    """Devuelve fecha en format ISO"""
    return fecha_a_iso(fecha)


def iso_a_datetime(fecha: str) -> datetime.datetime:
    """convierte fecha ISO a datetime de python"""
    arrfecha = fecha.split("-")
    return datetime.datetime(int(arrfecha[0]), int(arrfecha[1]), int(arrfecha[2]))


def str_to_date(strfecha) -> datetime.date:
    """Cadena a fecha"""
    fecha_retorno = datetime.datetime(1, 1, 1)
    if isinstance(strfecha, datetime.date) or isinstance(strfecha, datetime.datetime):
        return strfecha
    if not isinstance(strfecha, str):
        return datetime.datetime(1, 1, 1)
    if "/" in strfecha:
        fec = strfecha.split('/')
        if len(fec[2]) == 2:
            fecha_retorno = datetime.datetime.strptime(strfecha, "%d/%m/%y")
        elif len(fec[2]) == 4:
            fecha_retorno = datetime.datetime.strptime(strfecha, "%d/%m/%Y")
        else:
            fecha_retorno = datetime.datetime(1, 1, 1)
    if "-" in strfecha:
        fec = strfecha.split('-')
        if len(fec[0]) == 4:
            fecha_retorno = datetime.datetime.strptime(strfecha, "%Y-%m-%d")
        else:
            fecha_retorno = datetime.datetime(1, 1, 1)
    return fecha_retorno


def fecha_a_iso(fecha: datetime.date) -> str:
    """Convierte fecha legible a fecha aceptable por sql"""
    if isinstance(fecha, datetime.date) or (isinstance(fecha, datetime.datetime)):
        ano = str(fecha.year)
        mes = str(fecha.month)
        if len(mes) == 1:
            mes = "0" + mes
        dia = str(fecha.day)
        if len(dia) == 1:
            dia = "0" + dia
        fecha2 = ano + "-" + mes + "-" + dia
    else:
        fecha2 = None
    return fecha2


def hoy() -> datetime.date:
    return datetime.date.today()


def hoy_local() -> str:
    """Devuelve el día de hoy en formato estándard"""
    return datetime.date.today().strftime("%d/%m/%y")


def hoy_iso() -> str:
    """Devuelve el día de hoy en formato ISO"""
    return datetime.date.today().strftime("%Y-%m-%d")


def ahora() -> str:
    """Devuelve la hora de hoy en formato HH:MM"""
    return datetime.datetime.now().strftime("%H:%M")


def date_a_datetime(fecha: datetime.date) -> datetime.datetime:
    """Convierte date a datetime para poder operar"""
    return datetime.datetime(fecha.year, fecha.month, fecha.day)


def timestamp() -> str:
    """Devuelve el TS actual en formato ISO"""
    estampa = datetime.datetime.now()
    return estampa.isoformat().replace("T", " ")


def ts_a_fecha(ts: str) -> datetime.datetime:
    """Devuelve la fecha correspondiente a timestamp"""
    return datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S.%f")


def hms(tiempoestampa):
    """Devuelve dmahms"""
    if isinstance(tiempoestampa, datetime.datetime):
        resultado = tiempoestampa.strftime("%d/%m/%Y %H:%M:%S")
    else:
        resultado = ""
    return resultado


def sumar_anos(fecha, anos):
    """devuelve una fecha sumando años, si llega a ser 19 de febrero
    lo pasa a 1 de marzo"""
    try:
        return fecha.replace(year=fecha.year + anos)
    except ValueError:
        return fecha + (datetime.date(fecha.year + anos, 1, 1) - datetime.date(fecha.year, 1, 1))


def diff_years(date1, date2):
    """Calcula la diferencia en años entre 2 fechas en formato mysql"""
    # Devuelve en formato entero
    diff = date2 - date1
    diff_y = int((diff.days + diff.seconds/86400.0)/365.2425)
    return diff_y
