# (c) CC Marcelo Escobal
# Version 0.7.6 arreglo min y max de fechas IMPORTANTE!
# Versión 0.11 visulizar datos, combo sin campo de BDD
# Version 0.12: campo_combo
# Versión 1.03 fontawesome
# Version 1.07 file_upload
# Ver 1.09: separo Bulma de Htm
# Ver 2.06: elimino funciones no usadas

"""Conjunto de rutinas para generar codigo html."""
from lib import dinero


# Primer orden
def div(contenido: str, clase='') -> str:
    cad = '<div '
    if clase != '':
        cad += f"class='{clase}'"
    cad += f">{contenido}</div>\n"
    return cad


def entrada(tipo: str, texto: str, campo: str, val) -> str:
    """Entrada con placeholder"""
    cad = f"<input class='input' type='{tipo}' placeholder='{texto}' "
    cad += f"name='{campo}' value='{val}' id='{campo}'>"
    return cad


def combo(listado, variable, defecto='') -> str:
    """Combo box con listado como opciones y texto x defecto."""
    cad = f"<div class ='select'><select name='{variable}' id='{variable}'>\n"
    if defecto == '':
        cad += "<option value='' selected='selected'>Sin datos</option>\n"
    for item in listado:
        if item == defecto:
            cad += f"<option selected='selected' value='{item}'>{item}</option>\n"
        else:
            cad += f"<option value='{item}'>{item}</option>\n"
    cad += "</select></div>"
    return cad


def fin_pagina() -> str:
    """Tags de finalizacion de una pagina."""
    return '</div></div></body></html>'


def form_edicion(texto: str, accion: str) -> str:
    """Pone un formulario de edicion, encabezado."""
    cadena = f"<h2 class='subtitle'>{texto}</h2>"
    cadena += f"<form action='{accion}' method='post'>"
    return cadena


def form_edicion_fin() -> str:
    """Finalización de form de edición."""
    return '</form>'


def inicio() -> str:
    """Imprime encabezado de pagina web SIN cookie."""
    cadena = 'Content-Type: text/html; charset=utf-8\n\n'
    cadena += "<!DOCTYPE html>"
    cadena += "<html lang='es'>"
    return cadena


def linea_dato(texto: str, dato, alineacion: str = "left") -> str:
    """Imprime una linea con 2 celdas: una con un texto y otra con un dato"""
    return f"<tr><td>{texto}</td><td align='{alineacion}'>{str(dato)}</td></tr>\n"


def fin_tabla() -> str:
    """Imprime tags de finalizacion de una tabla."""
    return "</tbody>\n</table>\n</div>\n"


def campo_oculto(variable, dato):
    """Imprime un campo oculto"""
    return f"<input type='hidden' name='{variable}' value='{dato}'>"


def fin_formulario():
    """Termina el formulario"""
    return '</form>'


def nota(texto):
    """Imprime una tabla con texto pequeno"""
    return table(fila(celda(span(texto, "nota"))))


def texto_barra(texto: str) -> str:
    """Imprime un texto blanco"""
    return div(texto, 'texto_barra')


def enlace(enl: str, texto: str, titulo='') -> str:
    """Tag html"""
    return f"<a href='{enl}' title='{titulo}'>{texto}</a>"


def img(src, width=0, height=0, border=0):
    """Tag html"""
    cadena = f"<img src='{src}' "
    if width != 0:
        cadena += f" width='{width}' "
    if height != 0:
        cadena += f" height='{height}' "
    cadena += f" border='{border}'>"
    return cadena


def script(texto, typ="", src=""):
    """Tag html"""
    if typ != "":
        typ = f"type='{typ}'"
    if src != "":
        src = f"src='{src}'"
    return f"<script {typ} {src}>\n{texto}\n</script>"


def span(contenido, clase=''):
    """Html tag"""
    cadena = "<span "
    if clase != '':
        cadena += f" class='{clase}'"
    cadena = cadena + ">{0}</span>"
    return cadena.format(contenido)


def table(content, width='', clase=''):
    """Tag HTML"""
    cadena = "<table"
    if width != '':
        cadena = cadena + " width='" + width + "' "
    if clase != '':
        cadena = cadena + " class='" + clase + "'"
    cadena = cadena + ">" + content + "</table>"
    return cadena


def celda(texto="", align='left', rowspan=1, colspan=1):
    """Devuelve una celda en una tabla."""
    cadena = f"<td align='{align}' rowspan='{rowspan}' colspan='{colspan}'>{texto}</td>"
    return cadena


def celda_encabezado(texto: str) -> str:
    """Tag html"""
    cadena = "<th>{0}</th>"
    return cadena.format(texto)


def fila(texto: str = "") -> str:
    return f"<tr>{texto}</tr>\n"


def boton_play(accion: str) -> str:
    """imagen enlace"""
    return enlace(accion, img("/img/play.png", 24, 24, 0), "No visto")


def boton_stop(accion: str) -> str:
    """imagen enlace"""
    return enlace(accion, img("/img/stop.png", 24, 24, 0), "No visto")


def linea_numero(texto, dato, decimales=2):
    """Imprime una celda con un número formateado con 2 decimales"""
    return f"<tr><td>{texto}</td><td align='right'>{dinero.numero(dato, decimales)}</td></tr>"


def boton_llave(accion):
    """Pone un boton para acción con privilegio"""
    cadena = f"<a href='{accion}' title='Acción con privilegio'>"
    cadena += "<img src='/img/llave.png' width='24' height='24' border='0'></a>"
    return cadena


def boton_imprimir(accion):
    """pone un boton con una ACCION"""
    cadena = "<a href='" + accion + "' title='Imprimir'>"
    cadena += "<img src='/img/printer32.png' width='24' height='24' border='0'></a>"
    return cadena


def boton_actualizar(accion):
    """pone un boton con una ACCION"""
    cadena = "<a href='" + accion + "' title='Actualizar'>"
    cadena += "<img src='/img/actualizar.png' width='24' height='24' border='0'></a>"
    return cadena


def boton_texto(texto: str, accion: str, detalle='') -> str:
    """Enlace bulma"""
    return enlace(accion, texto, detalle)
# ========================================================


def boton_detalles(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/detalles.png", 24, 24, 0), "Detalles")


def boton_editar(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/editar.png", 24, 24, 0), 'Editar')


def boton_seleccionar(accion):
    """Boton con imagen de seleccion de persona"""
    cadena = f"<a href='{accion}' title='Seleccionar'>"
    cadena += "<img src='/img/seleccionar.png' width='24' height='24' border='0'></a>"
    return cadena


def boton_llamar(accion):
    """Boton con imagen de llamar x telefono"""
    cadena = f"<a href='{accion}' title='Llamadas'>"
    cadena += "<img src='/img/telefono_chico.png' width='24' height='24' border='0'></a>"
    return cadena
