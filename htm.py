#!/usr/bin/env python3
# (c) CC Marcelo Escobal
# Version 5.30
"""Conjunto de rutinas para generar codigo html."""
from __future__ import print_function
import http.cookies
import os
import re

from lib import funciones

PRINCIPAL = "emovil.py"
IMG_LOGO = "logo.png"

# ========================================
# Navegación


def redirigir(url):
    """Redirige usando javascript a otra pagina"""
    texto = 'window.location = "' + url + '";'
    return script(texto, "text/javascript")


def ir_a_pagina(pagina):
    """Manda navegador a una url."""
    cadena = inicio()
    cadena += "<html>\n<body>\n"
    cadena += "<form id='autolog' action='%s' method='post'>\n</form>" % pagina
    cadena += "<script language='JavaScript' type: 'text/javascript'>\n"
    cadena += "document.getElementById('autolog').submit();"
    cadena += "</script>\n"
    return cadena


# Con impresión
def input_password(texto, campo, valor, ancho=60):
    """Entrada de clave."""
    cadena = "<div class='field'>"
    cadena += "<label class='label'>%s</label>" % texto
    cadena += "<div class='control has-icons-left'>"
    cadena += "<input class='input' type='password' placeholder='%s' name='%s'" % (texto, campo)
    cadena += " value='%s'  id='%s' size='%s'>" % (valor, campo, ancho)
    cadena += "<span class='icon is-small is-left'>"
    cadena += "<i class='fas fa-lock'></i></span>"
    cadena += '</div></div>'
    return cadena


def titulares(titulo, subtitulo=''):
    """Encabezado nivel 1."""
    cadena = "<div id='main'>\n"
    cadena += "<div class='header'><h1>%s</h1>\n" % titulo
    if subtitulo != '':
        cadena += "<h2>%s</h2>\n" % subtitulo
    cadena += '</div>'
    return cadena


def botones(url):
    """Imprime boton de enviar formulario con texto = Aceptar."""
    cadena = "<div class='field is-grouped'>\n"
    cadena += "<div class='control'>\n"
    cadena += "<button type='submit' class='button is-link'>Aceptar</button>\n"
    cadena += '</div>\n'
    cadena += "<div class='control'>\n"
    cadena += "<button type='reset' class='button is-light'"
    cadena += " onClick=\"window.location.href='%s'\">Cancelar</button>\n" % url
    cadena += "</div>\n</div>\n"
    return cadena


def botones_formulario(texto_aceptar="Aceptar", url_cancelar=""):
    """Imprime boton de enviar formulario con texto = Aceptar."""
    cadena = "<div class='field is-grouped'>\n"
    cadena += "<div class='control'>\n"
    cadena += "<button type='submit' class='button is-link'>" + texto_aceptar + "</button>\n"
    cadena += '</div>\n'
    cadena += "<div class='control'>\n"
    cadena += "<button type='reset' class='button is-light'"
    cadena += " onClick=\"window.location.href='%s'\">Cancelar</button>\n" % url_cancelar
    cadena += "</div>\n</div>\n"
    return cadena


def combo(listado, variable, defecto):
    """Combo box con listado como opciones y texto x defecto."""
    cadena = "<div class ='select'><select name='" + variable + "' id='" + variable + "' >\n"
    for item in listado:
        if item == defecto:
            cadena += "<option selected='selected' value='" + item + "'>" + item + "</option>\n"
        else:
            cadena += "<option value='" + item + "'>" + item + "</option>\n"
    cadena += "</select></div>"
    return cadena


def estilo(cascade="/css/bulma.css"):
    """Imprime un link a hoja de estilo con una predeterminada."""
    return '<link type="text/css" href="' + cascade + '" rel="stylesheet" />'


def fin_pagina():
    """Tags de finalizacion de una pagina."""
    return '</div></div></body></html>'


def fin_tabla():
    """Imprime tags de finalizacion de una tabla."""
    return '</tbody></table>'


def form_edicion(texto, accion):
    """Pone un formulario de edicion, encabezado."""
    cadena = "<h2 class='subtitle'>%s</h2>" % texto
    cadena += "<form action='%s' method='post'>" % accion
    return cadena


def form_edicion_fin():
    """Finalización de form de edición."""
    return '</form>'


def formulario(accion):
    """Imprime el encabezado de un formulario."""
    print("<form action='%s' method='POST'>" % accion)


def inicio():
    """Imprime encabezado de pagina web SIN cookie."""
    cadena = 'Content-Type: text/html; charset=utf-8\n\n'
    cadena += "<!DOCTYPE html>"
    cadena += "<html lang='es'>"
    return cadena


def input_combo(texto, campo, resultado, campos, valor):
    """Linea con celda con texto y otra con combobox."""
    cadena = "<div class='field'>\n"
    cadena += "<label class='label'>%s</label>" % texto
    cadena += "<div class='control'>\n"
    cadena += "<div class ='select'>\n<select name='%s' id='%s'>\n" % (campo, campo)
    if valor == '':
        cadena += '<option value="" selected="selected">Sin datos</option>\n'
    for fil in resultado:
        cadena += '<option value="' + str(fil[campos[0]]) + '" '
        if str(fil[campos[0]]) == str(valor):
            cadena += 'selected="selected"'
        cadena += '>' + str(fil[campos[1]]) + '</option>\n'
    cadena += "</select></div>\n</div>\n</div>\n"
    return cadena


def input_fecha(texto, campo, valor):
    """Crea celdas contiguas con texto y campo de texto."""
    # fecha = funciones.sql_a_fecha(valor)
    cadena = "<div class='field'>\n"
    cadena += "<label class='label'>%s</label>\n" % texto
    cadena += "<div class='control'>\n"
    cadena += "<input class='input' type='date' placeholder='%s' " % texto
    cadena += "name='%s' value='%s' id='%s'>\n" % (campo, valor, campo)
    cadena += "</div>\n</div>\n"
    return cadena


def input_hora(texto, campo, valor):
    cadena = "<div class='field'>\n"
    cadena += "<label class='label'>%s</label>\n" % texto
    cadena += "<div class='control'>\n"
    cadena += "<input class='input' type='time' placeholder='%s' " % texto
    cadena += "name='%s' value='%s' id='%s'>\n" % (campo, str(valor), campo)
    cadena += "</div>\n</div>\n"
    return cadena


def input_numero(texto, campo, valor, decimales=2):
    """Imprime un campo de ingreso de valor numerico"""
    if not isinstance(texto, str):
        tex = str(texto)
    else:
        tex = texto
    if isinstance(valor, str):
        if valor == "":
            valor = "0"
    numero = funciones.numero(valor, decimales)
    cadena = "<div class='field'>"
    cadena += "<label class='label'>%s</label>" % tex
    cadena += "<div class='control'>"
    cadena += "<input class='input' type='number' placeholder='%s' " % tex
    cadena += "name='%s' value='%s' id='%s'>" % (campo, numero, campo)
    cadena += "</div></div>"
    return cadena


def input_entero(texto, campo, valor, minimo=None, maximo=None):
    """Imprime un campo de ingreso de valor numerico"""
    if not isinstance(texto, str):
        tex = str(texto)
    else:
        tex = texto
    if isinstance(valor, str):
        if valor == "":
            valor = "0"
    numero = funciones.numero(valor)
    cadena = "<div class='field'>"
    cadena += "<label class='label'>%s</label>" % tex
    cadena += "<div class='control'>"
    cadena += "<input class='input' type='number' "
    if minimo is not None:
        minimo = str(int(minimo))
        cadena += "min=%s " % minimo
    if maximo is not None:
        maximo = str(int(maximo))
        cadena += "max=%s " % maximo
    cadena += "name='%s' value='%s' id='%s'>" % (campo, numero, campo)
    cadena += "</div></div>"
    return cadena


def linea_numero(texto, decimales=2):
    """Imprime una celda con un número formateado con 2 decimales"""
    print(celda(funciones.numero(texto, decimales), "right"))


def script_noenter():
    """Impide que funcione la tecla enter en una pagina"""
    print("""<script type="text/javascript">
    function stopRKey(evt) {
    var evt = (evt) ? evt : ((event) ? event : null);
    var node = (evt.target) ? evt.target : ((evt.srcElement) ? evt.srcElement : null);
    if ((evt.keyCode == 13) && (node.type=="text"))  {return false;}
    }
    document.onkeypress = stopRKey;
    </script>';""")


def seleccionar_ano(defecto=""):
    """Combo box para seleccionar año - 10 antes del actual"""
    ano_actual = funciones.ano_actual()
    if defecto == "":
        seleccionado = str(ano_actual)
    else:
        seleccionado = str(defecto)
    print("<select name='ano'>")
    for contador in range(ano_actual, ano_actual-10, -1):
        if str(contador) == seleccionado:
            print("<option selected value='" + str(contador) + "'>" + str(contador) + "</option>")
        else:
            print("<option value='" + str(contador) + "'>" + str(contador) + "</option>")
    print("</select>")

# ========================================
# Con devolución de cadena


def encabezado(nivel, texto):
    """Imprime un encabezado con nivel"""
    niveles = ["", " is-4", " is-5", " is-6"]
    cadena = "<h" + str(nivel) + " class='title" + niveles[nivel-1]
    cadena += "'>" + texto + "</h" + str(nivel) + ">"
    return cadena


def encabezado_completo(titulo, referencia):
    """ Imprime encabezado con logo y boton de retorno"""
    cadena = "<head>\n"
    cadena += "<meta charset='utf-8' />\n"
    cadena += "<title>%s</title>\n" % titulo
    cadena += estilo()
    cadena += "</head>\n"
    cadena += '<body>\n'
    cadena += "<div class='section'><div class='container'>\n"
    cadena += "<div class='box'>\n"
    cadena += "<img src='/img/%s' align='right'>" % IMG_LOGO
    # cadena += "</div>\n"
    cadena += encabezado(1, titulo)
    cadena += retroceso(referencia)
    cadena += "</div>\n"
    return cadena


def load_script(tipo="text/javascript", src='', charset="utf-8"):
    """Carga script"""
    cadena = '<script type="{0}" src="{1}" charset="{2}"></script>'
    return cadena.format(tipo, src, charset)


# ========================================
# Conversión de tags HTML
# ========================================

def boton_ambulancia(accion):
    """Pone un boton con imagen ambulancia"""
    cadena = "<a href='%s' title='Asignar viaje'>" % accion
    cadena += "<img src='/img/ambulancia_chico.png' width='24' height='24' border='0'></a>"
    return cadena


# Boton cancelar
def boton_cancelar(accion):
    cadena = "<a href='#' title='Cancelar'>"
    cadena += "<img src='/img/cancelar.png' width='24' height='24' border='0' "
    cadena += "onClick=\"if(confirm('¿Desea cancelar?')) "
    cadena += "window.location='" + accion
    cadena += "';" + '"' + "></a>\n"
    return cadena


def boton_eliminar(accion):
    """Pone una imagen de eliminar cliqueable, saca diálogo para confirmar"""
    cadena = "<a href='#' title='Eliminar registro'>"
    cadena += "<img src='/img/eliminar.png' width='24' height='24' border='0' "
    cadena += "onClick=\"if(confirm('¿Desea borrar este registro?'))"
    cadena += "window.location='" + accion
    cadena += "';" + '\"' + "></a>\n"
    return cadena


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


def boton_grafica(accion):
    """Pone un boton para ver un gráfico"""
    return enlace(accion, img('/img/chart.png', 24, 24, 0), 'G ráfica')


def celda_menu(texto, enl, icono, ayuda=""):
    """Pone una celda del menu"""
    # 1
    cadena = "<div class='tile is-child is-info box'>\n"
    cadena += "<a href='%s'>" % enl
    cadena += "<p class='title' align='center'>%s</p></a>\n" % texto
    cadena += "<a href='%s'>" % enl
    cadena += "<div class='level'><div class='level-item has-text-centered'>\n"
    cadena += "<figure class='image is-96x96'>\n"
    cadena += "<img src='/img/%s'>\n" % icono
    cadena += '</figure>\n'
    cadena += '</div>\n</div>\n'
    cadena += '</a>\n'
    # 2
    cadena += "<div class='content'>\n"
    cadena += ayuda
    # cierra 2
    cadena += '</div>\n'
    # Cierra 1
    cadena += '</div>'
    return cadena


def imagen(imag):
    """Pone imagen con caracteristicas predeterminadas"""
    return '<img src="/img/%s" width="64" height="64" border="0">' % imag


def encabezado_tabla(arr):
    """A partir de un array arma el encabezado de una tabla"""
    cadena = '<table class="table"><thead><tr>\n'
    for lin in arr:
        cadena += celda_encabezado(lin)
    cadena += '</tr>\n</thead>\n<tbody>\n'
    return cadena


def campo_oculto(variable, dato):
    """Imprime un campo oculto"""
    return "<input type='hidden' name='%s' value='%s'>" % (variable, dato)


def fin_formulario():
    """Termina el formulario"""
    return '</form>'


def input_input(tipo, nombre, valor=''):
    """Imprime un campo tipo INPUT"""
    print('<input type="' + tipo + '" name="' + nombre + '" value="' + valor + '"></input>')


def input_check(texto, variable, valor):
    """Imprime 2 celdas, una con texto y otra con un checkbox"""
    adicional = ""
    if valor is None or valor == "":
        val = 0
    elif isinstance(valor, int):
        val = valor
    else:
        val = int(valor)
    if val > 0:
        adicional = "checked"
    cadena = '<TR>'
    cadena += celda(texto)
    cadena += celda("<INPUT TYPE='checkbox' NAME='" + variable + "' VALUE='1' " + adicional + ">")
    cadena += "</tr>"
    return cadena


def fila_alterna(i):
    """Genera colores alternos para filas de una tabla"""
    if (i % 2) == 0:
        print("<tr>")
    else:
        print("<tr class='odd'>")


def fila_lista():
    """Genera fila para listado de datos"""
    print("<tr class='fila_datos'>")


def imagen_menu(imag, enl, texto):
    """Imprime una celda con una imagen, enlace y texto"""
    print('<td align="center"><a href="' + enl + '"><img src="/img/' + imag +
          '" align="top" border="0"></a></br>' + texto + '</td>')
    # imag  + '" width="64" height="64" align="top" border="0"></a></br>' +


def duplicado(pag):
    """Genera html de error por existencia de duplicado"""
    texto = 'Ya existe un dato igual al que usted intenta agregar.'
    texto = texto + ' Verifique el dato e inténtelo nuevamente'
    nota(texto)
    print(button('Volver', pag))


def navegador(este_archivo, pagina_actual, total_paginas):
    """Imprime un navegador al pie de una tabla"""
    nav = ""
    union = "?"
    if "?" in este_archivo:
        union = "&"
    if not isinstance(pagina_actual, int):
        pagina_actual = int(pagina_actual)
    if not isinstance(total_paginas, int):
        total_paginas = int(total_paginas)
    for num in range(1, total_paginas + 1):
        if num == pagina_actual:
            nav += " " + str(pagina_actual) + " "
        else:
            nav += " <a href='" + este_archivo + union + "pagina="
            nav += str(num) + "'>" + str(num) + "</a> "
    # enlaces a primero - anterior - posterior - ultimo
    if pagina_actual > 1:
        pag = pagina_actual - 1
        prev = " <a href='" + este_archivo + union + "pagina="
        prev += str(pag) + "'>[<-]</a> "
        prim = " <a href='" + este_archivo + union + "pagina=1'>[<<]</a> "
    else:
        prev = " "
        prim = " "
    if pagina_actual < total_paginas:
        pag = pagina_actual + 1
        sig = " <a href='" + este_archivo + union + "pagina=" + str(pag) + "'>[->]</a> "
        ult = " <a href='" + este_archivo + union + "pagina="
        ult += str(total_paginas + 1) + "'>[>>]</a> "
    else:
        sig = " "
        ult = " "
    print("<center class='barra'>" + prim + prev + nav + sig + ult + "</center>")

# ===============================================================================


def boton_confirmar(texto, leyenda, accion):
    """Pone un boton con un TEXTO que saca diálogo para confirmar"""
    action = "if(confirm(\"{0}\")) window.location=\"{1}\";".format(leyenda, accion)
    cadena = "<input type='button' value='" + texto + "' "
    cadena = cadena + "onClick='" + action + "' "
    cadena = cadena + "/>"
    print(cadena)


def boton_detalles(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/detalles.png", 24, 24, 0), "Detalles")


def boton_visto(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/ver.png", 24, 24, 0), "Visto")


def boton_no_visto(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/no_ver.png", 24, 24, 0), "No visto")


def boton_editar(accion):
    """Pone una imagen de eliminar cliqueable"""
    return enlace(accion, img("/img/editar.png", 24, 24, 0), 'Editar')


def fila_resaltada():
    """Fila sobreiluminada"""
    print("<tr class='fila_datos'>")


def fila_datos(texto, datos):
    """Imprime una hilera con 2 celdas: una de texto y otra de datos"""
    datos = str(datos)
    print(fila(celda(texto) + celda(datos)))


def input_texto(texto, campo, valor, ancho=60):
    """Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar"""
    cadena = "<div class='field'>\n"
    cadena += "<label class='label'>%s</label>" % texto
    cadena += "<div class='control'>\n"
    cadena_2 = "<input class='input' type='text' placeholder='%s' name='%s' "
    cadena_2 += "value='%s' id='%s' size='%s'>"
    cadena += cadena_2 % (texto, campo, valor, campo, ancho)
    cadena += "</div>\n</div>\n"
    return cadena


def input_disabled(texto, campo, valor, ancho=60):
    """Imprime celda con texto y texto, muestra un campo no modificable"""
    print(fila(celda(texto + celda(text(campo, valor, ancho, disabled=True)))))


def input_label(texto1, texto2):
    """Imprime 2 celdas adyacentes en 1 fila ambas con texto"""
    print(fila(celda(texto1) + celda(texto2)))


def input_memo(texto, campo, valor):
    """Imprime una linea con una celda con texto y otra con un campo memo"""
    if valor is None:
        valor = ""
    return fila(celda(texto) + celda(textarea(valor, campo)))


def leer_cookie():
    """Lee una cookie presente en la sesion"""
    coo = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
    return coo


def linea_moneda(texto):
    """Imprime una celda con un valor monetario adentro"""
    print(celda(funciones.moneda(texto), "right"))


def celda_moneda(texto):
    """Imprime una celda con un valor monetario adentro"""
    print(celda(funciones.moneda(texto), "right"))


def nota(texto):
    """Imprime una tabla con texto pequeno"""
    return table(fila(celda(span(texto, "nota"))))


def texto_barra(texto):
    """Imprime un texto blanco"""
    return "<div class='texto_barra'>" + texto + "</div>"


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

# def input_fechahora(texto, campo_fecha, campo_hora, valor_fecha, valor_hora)
#   valor_fecha = '' if valor_fecha.nil?
#   valor_hora = '' if valor_hora.nil?
#   puts "<tr><td>#{texto}</td>"
#   "<td>Fecha:<input id='#{campo_fecha}' type='date' value='#{valor_fecha}' name='#{campo_fecha}'>"
#   puts " - Hora:<input id='#{campo_hora}' type='time' value='#{valor_hora}'
# name='#{campo_hora}'></td></tr>"
# end

# def input_decimal(texto, campo, valor)
#   valor = '' if valor.nil?
#   puts "<tr><td>#{texto}</td>"
#   puts "<td><input id='#{campo}' type='number' step='0.01' value='#{valor}' name='#{campo}'>"
#   puts '</td></tr>'
# end

# ===========================================================================
# TAGS HTML
# ===========================================================================


def enlace(enl, texto, titulo=''):
    """Tag html"""
    cadena = "<a href='{0}'>{1}</a>"
    if titulo != "":
        cadena = "<a href='{0}' title='" + titulo + "'>{1}</a>"
    return cadena.format(str(enl), str(texto))


def negrita(texto):
    """Tag html"""
    cadena = "<b>{0}</b>"
    return cadena.format(texto)


def body(contenido):
    """HTML TAG"""
    cadena = "<body>" + contenido + "</body>"
    return cadena


def boton(texto, referencia, clase="link"):
    """Devuelve un boton - texto con estilo CSS"""
    return "<a class='button is-" + clase + "' " + "href='" + referencia + "'>" + texto + "</a>"


def button(texto, action, style='link'):
    """boton con acción"""
    # cadena = "<input type='button' value='" + texto + "' "
    # cadena = cadena + "onClick=\"parent.location='" + action + "'\" "
    # if style != "":
    #     cadena = cadena + " style='" + style + "'"
    # cadena = cadena + "/>"
    cadena = "<a class='button is-%s' href='%s'> " % (style, action)
    cadena += texto
    cadena += "</a>"
    return cadena


def caption(texto):
    """Tag html"""
    cadena = "<caption>{0}</caption>"
    return cadena.format(texto)


def div(texto, clase=""):
    """tag html"""
    cadena = "<div "
    if clase != "":
        cadena = cadena + "class='" + clase + "'>"
    else:
        cadena = cadena + ">"
    return cadena + texto + "</div>"


def head(contenido):
    """Encabezado de pagina web"""
    return '<head>' + contenido + '</head>'


def hidden(campo, valor):
    """Tag Html"""
    return "<input type='hidden' name='%s' value='%s'>" % (campo, valor)


def linea_horizontal():
    """Tag html"""
    return '<hr />'


def img(src, width=0, height=0, border=0):
    """Tag html"""
    cadena = "<img src='" + src + "' "
    if width != 0:
        cadena = cadena + " width='" + str(width) + "' "
    if height != 0:
        cadena = cadena + " height='" + str(height) + "' "
    cadena = cadena + " border='" + str(border) + "'>"
    return cadena


def linea(texto):
    """Tag html"""
    cadena = "<li>{0}</li>"
    return cadena.format(texto)


def parrafo(texto):
    """Tag html"""
    cadena = "<p>{0}</p>"
    return cadena.format(texto)


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


def submit(valor="Enviar", style=""):
    """Tag HTML"""
    cadena = "<input type='submit' value='" + valor + "'"
    if style != "":
        cadena = cadena + "style='" + style + "'"
    cadena = cadena + ">"
    return cadena


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


def text(field, value, size=40, disabled=False):
    """Html tag"""
    dis = ""
    if disabled:
        dis = "disabled"
    cadena = "<input {0} type='text' name='{1}' value='{2}' size='{3}'/>"
    return cadena.format(dis, field, value, size)


def textarea(value, field, rows=10, cols=100):
    """Html tag"""
    r_fila = str(rows)
    c_columna = str(cols)
    cadena = "<textarea name='" + field + "' rows='" + r_fila + "' cols='"
    cadena += c_columna + "'>" + value + "</textarea>"
    return cadena


def tfoot(texto):
    """Tag html"""
    cadena = "<tfoot>{0}</tfoot>"
    return cadena.format(texto)


def celda_encabezado(texto):
    """Tag html"""
    cadena = "<th>{0}</th>"
    return cadena.format(texto)


def title(texto):
    """Tag html"""
    cadena = "<title>{0}</title>"
    return cadena.format(texto)


def fila(texto=""):
    """Tag html"""
    cadena = "<tr>{0}</tr>"
    return cadena.format(texto)


def lista(texto):
    """Tag html"""
    cadena = "<ul>{0}</ul>"
    return cadena.format(texto)


def limpiar_html(texto):
    """limpia tags html de un texto"""
    # limpio = re.compile('<.*?>')
    mensaje = re.sub("<.*?>", '', texto)
    mensaje = mensaje.replace("&nbsp;", "")
    mensaje = mensaje.replace("&aacute;", "á")
    mensaje = mensaje.replace("&eacute;", "é")
    mensaje = mensaje.replace("&iacute;", "í")
    mensaje = mensaje.replace("&oacute;", "ó")
    mensaje = mensaje.replace("&aacute;", "ú")
    mensaje = mensaje.replace("&ntilde;", "ñ")
    return mensaje


def boton_play(accion):
    return enlace(accion, img("/img/play.png", 24, 24, 0), "No visto")


def boton_stop(accion):
    return enlace(accion, img("/img/stop.png", 24, 24, 0), "No visto")
