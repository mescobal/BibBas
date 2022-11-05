#!/usr/bin/env python3
"""Conjunto de rutinas para generar una pagina"""
import bottle
from lib import bulma
from lib import htm

APP_PAGI = bottle.Bottle()


class Pagina:
    """Clase para generar una pagina web"""
    def __init__(self, titulo: str, retorno: str = ''):
        self.menu_lateral = ''
        self.pie = ''
        self.titulo = titulo
        self.retorno = retorno
        self.contenido = ''

    def render(self) -> str:
        """Renderización de pagina"""
        cadena = self.encabezado()
        cadena += "<body>\n"
        cadena += bulma.barra_navegacion()
        cadena += "<div class='columns'>"
        cadena += htm.div(self.menu_lateral, 'column is-narrow')
        cadena += "<div class='column'>"
        cadena += "<div class='card'>"
        cadena += "<header class='card-header is-size-3'><p class='card-header-title'>%s</p>" % self.titulo
        if self.retorno != '':
            cadena += bulma.boton_cerrar(self.retorno)
        cadena += '</header>'
        cadena += htm.div(self.contenido, 'card-content')
        cadena += '</div>'
        cadena += "<footer class='card-footer'>%s</footer>" % self.pie
        cadena += '</div>'
        return cadena

    def encabezado(self):
        """Encabezado de pagina"""
        cadena = "<!DOCTYPE html>\n"
        cadena += "<html lang='es'>"
        cadena += "<head>\n"
        cadena += "<meta charset='utf-8' />\n"
        cadena += "<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
        cadena += "<title>%s</title>\n" % self.titulo
        cadena += "<link type='text/css' href='/css/bulma.css' rel='stylesheet' />"
        cadena += "<link href='/css/all.css' rel='stylesheet'>"
        cadena += "</head>\n"
        return cadena


def error_generico(mensaje, retorno):
    """Error genérico"""
    pag = Pagina("Error", retorno)
    pag.contenido = htm.nota(mensaje)
    return pag.render


def faltan_datos(retorno):
    """Error por falta de datos"""
    htm.inicio()
    htm.nota('Faltan datos para completar la operación solicitada')
    print(htm.button('Volver', retorno))


def no_coinciden(retorno):
    """Error por falta de coincidencia"""
    htm.inicio()
    htm.nota("Las claves no coinciden, no se realizó el cambio.")
    print(htm.button('Volver', retorno))


@APP_PAGI.route("/no_disponible")
def no_disponible():
    """Pagina no disponible"""
    retorno = bottle.request.query.retorno
    if retorno is None or retorno == "":
        retorno = "/"
    pag = Pagina('Página no disponible', retorno)
    pag.contenido = htm.nota("La página a la que quiere acceder aún no está creada")
    return pag.render
