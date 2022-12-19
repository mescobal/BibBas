#!/usr/bin/env python3
"""Conjunto de rutinas para generar una pagina"""
import bottle
import base64
from lib import bulma
from lib import htm

APP_PAGI = bottle.Bottle()


class Pagina:
    """Clase para generar una pagina web"""
    def __init__(self, titulo: str, retorno: str = '', nivel=10):
        self.menu_lateral = ''
        self.pie = ''
        self.titulo = titulo
        self.retorno = retorno
        self.contenido = ''
        self.nivel = nivel
        self.saltear = False
        self.accion = ""
        self.form = ""

    def autorizar(self) -> bool:
        """Rutina para verificar nivel de acceso
        Niveles
         1 Admin, 2 Superusuario, 3 Director, 4 Gerente, 5 Encargado, 6 Adminstrativo
         7 Nurse, 8 Telefonista, 9 Resto del personal, 10 invitado/otros
         > 10 inhabilitado"""
        # Verificar si esta cookie NIVEL
        nivel_login_enc = bottle.request.get_cookie("nivel", secret=None)
        # Si ESTA NIVEL
        if nivel_login_enc is None:
            bottle.redirect("/pantalla_login")
        else:
            try:
                nivel_dec = base64.b64decode(nivel_login_enc)
                n_log = int(nivel_dec.decode("utf-8"))
                if n_log > self.nivel:
                    bottle.redirect(f"/no_autorizado?retorno={self.retorno}")
            except TypeError:
                bottle.redirect("/pantalla_login")
            except UnicodeDecodeError:
                bottle.redirect("/pantalla_login")
        return True

    def render(self) -> str:
        """Renderización de pagina"""
        # autorizacion.nivel(self.nivel, self.retorno)
        if self.saltear is False:
            self.autorizar()
        cadena = self.encabezado()
        cadena += "<body>\n"
        cadena += bulma.barra_navegacion()
        cadena += "<div class='columns'>"
        cadena += htm.div(self.menu_lateral, 'column is-narrow')
        cadena += "<div class='column'>"
        cadena += "<div class='card'>"
        cadena += f"<header class='card-header is-size-3'><p class='card-header-title'>{self.titulo}</p>"
        if self.retorno != '':
            cadena += bulma.boton_cerrar(self.retorno)
        cadena += "</header>\n"
        if self.accion != "":
            self.contenido += f"<form action='{self.accion}' method='post'>"
            self.contenido += self.form
            self.contenido += bulma.botones(self.retorno)
            self.contenido += "</form>"
        cadena += htm.div(self.contenido, 'card-content')
        cadena += '</div>'
        cadena += f"<footer class='card-footer'>{self.pie}</footer>"
        cadena += '</div>'
        cadena += '</div></body></html>'
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


@APP_PAGI.route("/no_disponible")
def no_disponible():
    """Pagina no disponible"""
    retorno = bottle.request.query.retorno
    if retorno is None or retorno == "":
        retorno = "/"
    pag = Pagina('Página no disponible', retorno)
    pag.contenido = htm.nota("La página a la que quiere acceder aún no está creada")
    return pag.render
