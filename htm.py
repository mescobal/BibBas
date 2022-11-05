# (c) CC Marcelo Escobal
# Version 0.7.6 arreglo min y max de fechas IMPORTANTE!
# Versión 0.11 visulizar datos, combo sin campo de BDD
# Version 0.12: campo_combo
# Versión 1.03 fontawesome
# Version 1.07 file_upload
# Ver 1.09: separo Bulma de Htm

"""Conjunto de rutinas para generar codigo html."""
from lib import dinero


# Primer orden
def div(contenido: str, clase='') -> str:
    cad = '<div '
    if clase != '':
        cad += " class='%s'" % clase
    cad += ">%s</div>\n" % contenido
    return cad


def entrada(tipo: str, texto: str, campo_bdd: str, val) -> str:
    """Entrada con placeholder"""
    cad = "<input class='input' type='%s' placeholder='%s' " % (tipo, texto)
    cad += "name='%s' value='%s' id='%s'>" % (campo_bdd, val, campo_bdd)
    return cad


def combo(listado, variable, defecto='') -> str:
    """Combo box con listado como opciones y texto x defecto."""
    cad = "<div class ='select'><select name='" + variable + "' id='" + variable + "'>\n"
    if defecto == '':
        cad += "<option value='' selected='selected'>Sin datos</option>\n"
    for item in listado:
        if item == defecto:
            cad += "<option selected='selected' value='" + item + "'>" + item + "</option>\n"
        else:
            cad += "<option value='" + item + "'>" + item + "</option>\n"
    cad += "</select></div>"
    return cad


def fin_pagina() -> str:
    """Tags de finalizacion de una pagina."""
    return '</div></div></body></html>'


def form_edicion(texto: str, accion: str) -> str:
    """Pone un formulario de edicion, encabezado."""
    cadena = "<h2 class='subtitle'>%s</h2>" % texto
    cadena += "<form action='%s' method='post'>" % accion
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
    return "<tr><td align='%s'>%s</td><td>%s</td></tr>" % (alineacion, texto, str(dato))


def imagen(imag):
    """Pone imagen con caracteristicas predeterminadas"""
    return '<img src="/img/%s" width="64" height="64" border="0">' % imag


def fin_tabla() -> str:
    """Imprime tags de finalizacion de una tabla."""
    return "</tbody></table>\n</div>"


def campo_oculto(variable, dato):
    """Imprime un campo oculto"""
    return "<input type='hidden' name='%s' value='%s'>" % (variable, dato)


def fin_formulario():
    """Termina el formulario"""
    return '</form>'


def boton_visto(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/ver.png", 24, 24, 0), "Visto")


def boton_no_visto(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/no_ver.png", 24, 24, 0), "No visto")


def celda_moneda(texto):
    """Imprime una celda con un valor monetario adentro"""
    return celda(dinero.moneda(texto), "right")


def nota(texto):
    """Imprime una tabla con texto pequeno"""
    return table(fila(celda(span(texto, "nota"))))


def texto_barra(texto: str) -> str:
    """Imprime un texto blanco"""
    return div(texto, 'texto_barra')


def enlace(enl: str, texto: str, titulo='') -> str:
    """Tag html"""
    return "<a href='%s' title='%s'>%s</a>" % (enl, titulo, texto)


def img(src, width=0, height=0, border=0):
    """Tag html"""
    cadena = "<img src='" + src + "' "
    if width != 0:
        cadena = cadena + " width='" + str(width) + "' "
    if height != 0:
        cadena = cadena + " height='" + str(height) + "' "
    cadena = cadena + " border='" + str(border) + "'>"
    return cadena


def script(texto, typ="", src=""):
    """Tag html"""
    if typ != "":
        typ = "type='" + str(typ) + "'"
    if src != "":
        src = "src='" + str(src) + "'"
    return "<script " + typ + " " + src + ">\n" + texto + "\n</script>"


def span(contenido, clase=''):
    """Html tag"""
    cadena = "<span "
    if clase != '':
        cadena = cadena + " class='" + clase + "'"
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
    cadena = "<td align='%s' rowspan='%s' colspan='%s'>%s</td>" % (str(align),
                                                                   str(rowspan),
                                                                   str(colspan),
                                                                   str(texto))
    return cadena


def celda_encabezado(texto: str) -> str:
    """Tag html"""
    cadena = "<th>{0}</th>"
    return cadena.format(texto)


def fila(texto="") -> str:
    """Tag html"""
    cadena = "<tr>{0}</tr>"
    return cadena.format(texto)


def boton_play(accion: str) -> str:
    """imagen enlace"""
    return enlace(accion, img("/img/play.png", 24, 24, 0), "No visto")


def boton_stop(accion: str) -> str:
    """imagen enlace"""
    return enlace(accion, img("/img/stop.png", 24, 24, 0), "No visto")


# =================================
def linea_numero(texto, dato, decimales=2):
    """Imprime una celda con un número formateado con 2 decimales"""
    return "<tr><td>%s</td><td align='right'>%s</td></tr>" % (texto, dinero.numero(dato, decimales))


def boton_llave(accion):
    """Pone un boton para acción con privilegio"""
    cadena = "<a href='%s' title='Acción con privilegio'>" % accion
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
    cadena = "<a href='%s' title='Seleccionar'>" % accion
    cadena += "<img src='/img/seleccionar.png' width='24' height='24' border='0'></a>"
    return cadena


def boton_llamar(accion):
    """Boton con imagen de llamar x telefono"""
    cadena = "<a href='%s' title='Llamadas'>" % accion
    cadena += "<img src='/img/telefono_chico.png' width='24' height='24' border='0'></a>"
    return cadena


def pie(txt_enlace):
    """ PIE de pagina"""
    cadena = "<footer class='footer'>\n"
    cadena += "<div class='content has-text-centered'>\n"
    cadena += boton("Volver", txt_enlace)
    cadena += "</div>\n</footer>\n"
    cadena += fin_pagina()
    return cadena


def retroceso(referencia):
    """Imprime un boton de volver"""
    # cadena = "<a class='button is-link' style='float: right' href='"
    cadena = "<a class='button is-link' href='"
    cadena += referencia + "'>Volver</a>"
    return cadena


# ===========================================================================
# TAGS HTML
# ===========================================================================

def boton(texto, referencia, clase="link"):
    """Devuelve un boton - texto con estilo CSS"""
    return "<a class='button is-" + clase + "' " + "href='" + referencia + "'>" + texto + "</a>"


def button(texto, action, style='link'):
    """boton con acción"""
    cadena = "<a class='button is-%s' href='%s'> " % (style, action)
    cadena += texto
    cadena += "</a>"
    return cadena


def label(texto: str) -> str:
    """Tag HTML"""
    return "<label class='label'>%s</label>" % texto
