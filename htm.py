#!/usr/bin/env python3
# (c) CC Marcelo Escobal
# Version 0.7.6 arreglo min y max de fechas IMPORTANTE!
# Versión 0.11 visulizar datos, combo sin campo de BDD
"""Conjunto de rutinas para generar codigo html."""
import re
from lib import funciones

PRINCIPAL = "emovil.py"
IMG_LOGO = "logo.png"

# Formulario ================================================


def etiqueta_campo(texto: str) -> str:
    cadena = "<div class='field-label'>"
    cadena += "<label class='label'>%s</label>" % texto
    cadena += "</div>"
    return cadena


def campo(texto: str, tipo="") -> str:
    # H es horizontal, G es grupo
    if tipo == "H":
        str_tipo = "field is-horizontal"
    elif tipo == "G":
        str_tipo = "field is-grouped"
    else:
        str_tipo = "field"
    cadena = "<div class='%s'>%s" % (str_tipo, texto)
    cadena += "</div>\n"
    return cadena


def cuerpo_campo(texto: str) -> str:
    cadena = "<div class='field-body'>%s" % texto
    cadena += "</div>\n"
    return cadena


def control(texto: str) -> str:
    cadena = "<div class='control'>%s" % texto
    cadena += "</div>\n"
    return cadena


def entrada(tipo, texto, campo_bdd, valor):
    cadena = "<input class='input' type='%s' placeholder='%s' " % (tipo, texto)
    cadena += "name='%s' value='%s' id='%s'>" % (campo_bdd, valor, campo_bdd)
    return cadena


def input_password(texto: str, campo_bdd: str, valor: str) -> str:
    """Entrada de clave."""
    cadena = etiqueta_campo(texto)
    cadena += cuerpo_campo(control(entrada("password", texto, campo_bdd, valor)))
    return campo(cadena, "H")


def botones(url: str) -> str:
    """Imprime boton de enviar formulario con texto = Aceptar."""
    cadena = etiqueta_campo("")
    cadena += control("<button type='submit' class='button is-link'>Aceptar</button>")
    cadena += "<div class='control'>\n"
    cadena += "<button type='reset' class='button is-light'"
    cadena += " onClick=\"window.location.href='%s'\">Cancelar</button>\n" % url
    cadena += "</div>\n"
    return campo(cadena, "G")


def botones_formulario(texto_aceptar="Aceptar", url_cancelar="") -> str:
    """Imprime boton de enviar formulario con texto = Aceptar."""
    cadena = etiqueta_campo("")
    cadena += "<div class='control'>\n"
    cadena += "<button type='submit' class='button is-link'>" + texto_aceptar + "</button>\n"
    cadena += '</div>\n'
    cadena += "<div class='control'>\n"
    cadena += "<button type='reset' class='button is-light'"
    cadena += " onClick=\"window.location.href='%s'\">Cancelar</button>\n" % url_cancelar
    cadena += "</div>\n"
    return campo(cadena, "G")


def combo(listado, variable, defecto=''):
    """Combo box con listado como opciones y texto x defecto."""
    cadena = "<div class ='select'><select name='" + variable + "' id='" + variable + "'>\n"
    if defecto == '':
        cadena += "<option value='' selected='selected'>Sin datos</option>\n"
    for item in listado:
        if item == defecto:
            cadena += "<option selected='selected' value='" + item + "'>" + item + "</option>\n"
        else:
            cadena += "<option value='" + item + "'>" + item + "</option>\n"
    cadena += "</select></div>"
    return cadena


def campo_combo(texto, listado, variable, defecto=""):
    """Combo box con opciones en un campo"""
    cadena = etiqueta_campo(texto)
    cadena += cuerpo_campo(control(combo(listado, variable, defecto)))
    return campo(cadena, "H")


def fin_pagina() -> str:
    """Tags de finalizacion de una pagina."""
    return '</div></div></body></html>'


def fin_tabla() -> str:
    """Imprime tags de finalizacion de una tabla."""
    return '</tbody></table>'


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


def input_texto(texto, campo_bdd, valor):
    """Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar"""
    cadena = etiqueta_campo(texto)
    cadena += cuerpo_campo(campo(control(entrada("text", texto, campo_bdd, valor))))
    return campo(cadena, "H")


def input_texto_1(texto, campo_bdd, valor):
    """Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar"""
    # cadena = "<div class='field is-grouped is-horizontal'>"
    cadena = "<div class='field is-horizontal is-grouped'>"
    cadena += etiqueta_campo(texto)
    cadena += cuerpo_campo(campo(control(entrada("text", texto, campo_bdd, valor))))
    return cadena


def input_texto_2(texto, campo_bdd, valor):
    """Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar"""
    cadena = etiqueta_campo(texto)
    cadena += cuerpo_campo(campo(control(entrada("text", texto, campo_bdd, valor))))
    cadena += "</div>"
    return cadena


def input_memo(texto: str, campo_bdd: str, valor: str) -> str:
    """Imprime una linea con una celda con texto y otra con un campo memo"""
    if valor is None:
        valor = ""
    cadena = etiqueta_campo(texto)
    ctrl = "<textarea class='textarea' name='%s' placeholder='%s'>%s</textarea>" % (campo_bdd, texto, valor)
    cadena += cuerpo_campo(campo(control(ctrl)))
    return campo(cadena, "H")


def input_combo(texto: str, campo_bdd: str, resultado, campos, valor) -> str:
    """Linea con celda con texto y otra con combobox."""
    cad_1 = etiqueta_campo(texto)
    cadena = "<div class='control'>\n"
    cadena += "<div class ='select'>\n<select name='%s' id='%s'>\n" % (campo_bdd, campo_bdd)
    if valor == '':
        cadena += "<option value='' selected='selected'>Sin datos</option>\n"
    for fil in resultado:
        cadena += "<option value='" + str(fil[campos[0]]) + "' "
        if str(fil[campos[0]]) == str(valor):
            cadena += "selected='selected'"
            # cadena += ' selected'
        cadena += '>' + str(fil[campos[1]]) + '</option>\n'
    cadena += "</select></div>\n</div>\n"
    cad_1 += cuerpo_campo(campo(cadena))
    return campo(cad_1, "H")


def input_combo_1(texto: str, campo_bdd: str, resultado, campos, valor) -> str:
    """Linea con celda con texto y otra con combobox. para poner lado a lado"""
    cadena = "<div class='field is-horizontal'>"
    cadena += etiqueta_campo(texto)
    cadena += "<div class='field-body'>"
    cadena += "<div class='field is-expanded'>\n"
    cadena += "<p class='control is-expanded'>\n"
    cadena += "<div class ='select is-fullwidth'>\n<select name='%s' id='%s'>\n" % (campo_bdd, campo_bdd)
    if valor == '':
        cadena += "<option value='' selected='selected'>Sin datos</option>\n"
    for fil in resultado:
        cadena += "<option value='" + str(fil[campos[0]]) + "' "
        if str(fil[campos[0]]) == str(valor):
            cadena += "selected='selected'"
            # cadena += ' selected'
        cadena += '>' + str(fil[campos[1]]) + '</option>\n'
    cadena += "</select></div>\n"
    cadena += "</p>\n</div>\n</div>\n"
    return cadena


def input_combo_2(texto: str, campo_bdd: str, resultado, campos, valor) -> str:
    """Linea con celda con texto y otra con combobox. para poner lado a lado"""
    cadena = "<div class='field-label is-normal'><label class='label'>%s</label></div>" % texto
    cadena += "<div class='field-body'>\n"
    cadena += "<div class='field is-expanded'>\n"
    cadena += "<p class='control is-expanded'>\n"
    cadena += "<div class ='select is-fullwidth'>\n<select name='%s' id='%s'>\n" % (campo_bdd, campo_bdd)
    if valor == '':
        cadena += "<option value='' selected='selected'>Sin datos</option>\n"
    for fil in resultado:
        cadena += "<option value='" + str(fil[campos[0]]) + "' "
        if str(fil[campos[0]]) == str(valor):
            cadena += "selected='selected'"
            # cadena += ' selected'
        cadena += '>' + str(fil[campos[1]]) + '</option>\n'
    cadena += "</select></div>\n"
    cadena += "</p>\n</div></div>\n"
    cadena += "</div>\n"
    return cadena


def input_fecha(texto: str, campo_bdd: str, valor) -> str:
    """Crea celdas contiguas con texto y campo de texto."""
    cadena = etiqueta_campo(texto)
    entra = "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    entra += "min='1920-01-01' max='2120-12-31' "
    # pattern = "(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d"
    # entrada += "name='%s' value='%s' id='%s' pattern='%s'>" % (campo_bdd, valor, campo_bdd, pattern)
    entra += "name='%s' value='%s' id='%s'>\n" % (campo_bdd, valor, campo_bdd)
    cadena += cuerpo_campo(campo(control(entra)))

    return campo(cadena, "H")


def input_hora(texto, campo_bdd, valor):
    cadena = etiqueta_campo(texto)
    cadena += cuerpo_campo(campo(control(entrada("time", texto, campo_bdd, valor))))
    return campo(cadena, "H")


def input_numero(texto, campo_bdd, valor, decimales=2):
    """Imprime un campo de ingreso de valor numerico"""
    if isinstance(valor, str):
        if valor == "":
            valor = "0"
    numero = funciones.numero(valor, decimales)
    cadena = etiqueta_campo(texto)
    if decimales is None:
        escalon = 0
    else:
        escalon = "0." + "1".rjust(decimales, "0")
    inp_num = "<input class='input' type='number' placeholder='%s' step='%s' " % (texto, escalon)
    inp_num += "name='%s' value='%s' id='%s'>" % (campo_bdd, numero, campo_bdd)
    cadena += cuerpo_campo(campo(control(inp_num)))
    return campo(cadena, "H")


def input_entero(texto, campo_bdd, valor, minimo=None, maximo=None):
    """Imprime un campo de ingreso de valor numerico"""
    if not isinstance(texto, str):
        tex = str(texto)
    else:
        tex = texto
    if isinstance(valor, str):
        if valor == "":
            valor = "0"
    numero = funciones.numero(valor)
    cdn_2 = etiqueta_campo(tex)
    cadena = "<div class='control'>"
    cadena += "<input class='input' type='number' "
    if minimo is not None:
        minimo = str(int(minimo))
        cadena += "min=%s " % minimo
    if maximo is not None:
        maximo = str(int(maximo))
        cadena += "max=%s " % maximo
    cadena += "name='%s' value='%s' id='%s' step='1'>" % (campo_bdd, numero, campo_bdd)
    cadena += "</div>"
    cdn_3 = cdn_2 + cuerpo_campo(cadena)
    return campo(cdn_3, "H")


def input_check(texto, variable, valor):
    """Imprime 2 celdas, una con texto y otra con un checkbox"""
    adicional = ""
    if (valor is None) or (valor == "") or (valor == "None"):
        val = 0
    elif isinstance(valor, int):
        val = valor
    else:
        val = int(valor)
    if val > 0:
        adicional = "checked"
    cadena = etiqueta_campo(texto)
    # cadena = "<div class='field'><label class='checkbox'>"
    # cadena += "<INPUT TYPE='checkbox' NAME='" + variable + "' VALUE='1' " + adicional + ">%s" % texto
    # cadena += "</label></div>"
    chk = "<INPUT TYPE='checkbox' NAME='" + variable + "' VALUE='1' " + adicional + ">"
    cadena += cuerpo_campo(campo(control(chk)))
    return campo(cadena, "H")


def input_check_1(texto: str, variable: str, valor) -> str:
    cadena = "<div class='field is-horizontal is-grouped'>"
    adicional = ""
    if valor is None or valor == "":
        val = 0
    elif isinstance(valor, int):
        val = valor
    else:
        val = int(valor)
    if val > 0:
        adicional = "checked"
    cadena += etiqueta_campo(texto)
    chk = "<INPUT TYPE='checkbox' NAME='" + variable + "' VALUE='1' " + adicional + ">"
    cadena += cuerpo_campo(campo(control(chk)))
    return cadena


def input_check_2(texto: str, variable: str, valor) -> str:
    adicional = ""
    if valor is None or valor == "":
        val = 0
    elif isinstance(valor, int):
        val = valor
    else:
        val = int(valor)
    if val > 0:
        adicional = "checked"
    cadena = etiqueta_campo(texto)
    chk = "<INPUT TYPE='checkbox' NAME='" + variable + "' VALUE='1' " + adicional + ">"
    cadena += cuerpo_campo(campo(control(chk)))
    cadena += "</div>"
    return cadena


def input_radio(texto, variable, arreglo, valor):
    # arreglo es un DICCIONARIO con texto y valor del item
    radio = ""
    for llave in arreglo:
        radio += "<label class='radio'>"
        chkd = ""
        if arreglo[llave] == valor:
            chkd = "checked"
        radio += "<input type='radio' name='%s' value='%s' %s> " % (variable, arreglo[llave], chkd)

        radio += llave
        radio += " </label>   "
    cadena = etiqueta_campo(texto)
    cadena += cuerpo_campo(campo(control(radio)))
    return campo(cadena, "H")


def linea_dato(texto: str, dato) -> str:
    """Imprime una linea con 2 celdas: una con un texto y otra con un dato"""
    return "<tr><td>%s</td><td>%s</td></tr>" % (texto, str(dato))


def linea_numero(texto, dato, decimales=2):
    """Imprime una celda con un número formateado con 2 decimales"""
    return "<tr><td>%s</td><td align='right'>%s</td></tr>" % (texto, funciones.numero(dato, decimales))


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
    cadena = "<!DOCTYPE html>\n"
    cadena += "<html lang='es'>"
    cadena += "<head>\n"
    cadena += "<meta charset='utf-8' />\n"
    cadena += "<title>%s</title>\n" % titulo
    cadena += "<link type='text/css' href='/css/bulma.css' rel='stylesheet' />"
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

# BOTONES ===========================

def boton_accion(titulo, accion, icono):
    """Pone un boton titulado TITULO con ICONO y ACCION"""
    cadena = "<a href='%s' title='%s'>" % (accion, titulo)
    cadena += "<img src='/img/%s.png' width='24' height='24' border='0'></a>" % icono
    return cadena


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
    return enlace(accion, img('/img/chart.png', 24, 24, 0), 'Gráfica')


def boton_play(accion: str) -> str:
    return enlace(accion, img("/img/play.png", 24, 24, 0), "No visto")


def boton_stop(accion: str) -> str:
    return enlace(accion, img("/img/stop.png", 24, 24, 0), "No visto")


def boton_texto(texto: str,  accion: str, detalle='') -> str:
    return enlace(accion, texto, detalle)
# ========================================================


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
    cadena = '<table class="table is-hoverable"><thead><tr>\n'
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


def celda_moneda(texto):
    """Imprime una celda con un valor monetario adentro"""
    return celda(funciones.moneda(texto), "right")


def nota(texto):
    """Imprime una tabla con texto pequeno"""
    return table(fila(celda(span(texto, "nota"))))


def texto_barra(texto: str) -> str:
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


def boton(texto, referencia, clase="link"):
    """Devuelve un boton - texto con estilo CSS"""
    return "<a class='button is-" + clase + "' " + "href='" + referencia + "'>" + texto + "</a>"


def button(texto, action, style='link'):
    """boton con acción"""
    cadena = "<a class='button is-%s' href='%s'> " % (style, action)
    cadena += texto
    cadena += "</a>"
    return cadena


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


def limpiar_html(texto: str) -> str:
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
