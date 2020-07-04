#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103

"""Conjunto de rutinas para generar una pagina"""
import bottle
import os
import http.cookies
from lib import htm

APP_PAGI = bottle.Bottle()


class Pagina:
    """Clase para generar una pagina web"""
    def __init__(self, titulo, nivel=20, fecha=0, tipo='comun'):
        # tipos: comun, boleta, informe, recibo
        self.tipo = tipo
        self.sesion = http.cookies.SimpleCookie(os.environ.get('HTTP_COOKIE', ""))
        self.fecha = fecha
        self.titulo = titulo
        self.filas_por_pagina = 20
        self.nivel = nivel
        htm.inicio()
        self.pagina_segun_autorizacion()

    @staticmethod
    def texto_script():
        """Autosubmit"""
        texto = "<!--\n"
        texto += "document.getElementById('autolog').submit();\n"
        texto += "//-->\n"
        return texto

    def procesando_entrada(self, url):
        """PRocesando entrada"""
        print("<p>Procesando entrada</p>")
        print("<form id='autolog' action='" + url + "' method='post'>")
        print("<script language='JavaScript' type='text/javascript'>")
        self.texto_script()
        print("</script>")

    def pagina_segun_autorizacion(self):
        """Página según autorización"""
        accion = self.autorizacion(self.nivel)
        if accion == 'noautorizado':
            print("<META HTTP-EQUIV='Refresh' CONTENT='0;URL=no_autorizado.html'>")
        elif accion == 'autorizado':
            self.encabezado()
        elif accion == "faltan datos":
            print("<META HTTP-EQUIV='Refresh' CONTENT='0;URL=login.py'>")
        else:
            print("<META HTTP-EQUIV='Refresh' CONTENT='0;URL=login.py'>")

    @staticmethod
    def estilo():
        """Hoja de estilo"""
        return "<link rel='stylesheet'  href='./css/bulma.css'>"

    def script_fecha(self):
        """Pone un script con la fecha"""
        print("<style type='text/css'>")
        print('@import url(./js/calendar-win2k-1.css);</style>')
        self.javascript('./js/calendar.js')
        self.javascript('./js/lang/calendar-es.js')
        self.javascript('./js/calendar-setup.js')

    @staticmethod
    def javascript(src):
        """Tag html"""
        return "<script type='text/javascript' src='" + src + "' charset='utf-8'"

    def tipo_comun(self):
        """Encabezado 1"""
        print("<header><h1>%s</h1></header>" % self.titulo)

    def encabezado(self):
        """Encabezado"""
        print('<head>')
        print("<meta charset='utf-8' />")
        print("<title>%s</title>" % self.titulo)
        print("<script type='text/javascript' src='emovil.js' charset='utf-8'>")
        if self.fecha >= 1:
            self.script_fecha()
        print('</script>')
        print("<link rel='stylesheet' href='./css/bulma.css'>")
        print('</head>')
        print("<body>")
        print("<div class='container'><img align='right' src='./img/LogoUNEM.png'>")
        print("<div class='box'><h1 class='title'>%s</h1></div>" % self.titulo)

    @staticmethod
    def fin():
        """Finalización de página"""
        # if self.fecha > 0:
        #    self.script_fecha1()
        # if self.fecha > 1:
        #    self.script_fecha2()
        return '</div></div></body>'

    def autorizacion(self, niv):
        """Autorización según nivel"""
        # 20: cualquiera 10: empleado 5: recepcion 4: secretario
        # 3: contador / gerente 2: Dueno 1: SysAdmin
        # if not self.sesion.has_key("nivel"):
        autorizacion = 'login'
        if 'nivel' in self.sesion:
            if self.sesion['nivel'] is not None:
                nivel_sesion = int(self.sesion['nivel'].value)
                if nivel_sesion > niv:
                    autorizacion = "noautorizado"
                else:
                    autorizacion = "autorizado"
        else:
            autorizacion = "faltan datos"
        return autorizacion


def error_generico(mensaje, retorno):
    """Error genérico"""
    cadena = htm.encabezado_completo("Error", retorno)
    cadena += htm.nota(mensaje)
    cadena += htm.pie(retorno)
    return cadena


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
