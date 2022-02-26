"""Rutinas que dependen den BULMA CSS
Ver 1.12 modifico input_check para manejar valores imprevistos
Ver 2.01 comienzo modificaciones para peewee: combobox
"""

import typing
from lib import dinero
from lib import htm

# Primer orden
from lib.htm import celda_encabezado


def boton(texto, accion, estilo='link'):
    """Boton con acción"""
    return "<a class='button is-%s' href='%s'>%s</a>" % (estilo, accion, texto)


# Pone un boton titulado TITULO con ICONO y ACCION
def boton_accion(titulo, accion, icono) -> str:
    return htm.enlace(accion, faicon(icono), titulo)


def etiqueta(texto):
    return "<label class='label'>%s</label>" % texto


def campo(texto, tipo=''):
    if tipo == 'H':
        str_tipo = 'field is-horizontal'
    elif tipo == 'G':
        str_tipo = 'field is-grouped'
    else:
        str_tipo = 'field'
    return htm.div(texto, str_tipo)


# Boton cancelar
def boton_cancelar(accion):
    cad = "<a href='#' title='Cancelar'><span class='icon'><i class='fas fa-window-close'"
    cad += " onClick=\"if(confirm('¿Desea cancelar?')) "
    cad += "window.location='%s" % accion
    cad += "';\"></i></span></a>"
    return cad


def control(texto):
    return htm.div(texto, 'control')


def cuerpo_campo(texto):
    return htm.div(texto, 'field-body')


def faicon(icono, color='grey'):
    return htm.span("<i class='%s'></i>" % icono, "icon has-text-%s" % color)


# Imprime un boton de volver
def boton_cerrar(retorno):
    cad = "<a class='button is-light is-small' href='%s'>" % retorno
    cad2 = "<i class='fas fa-window-close'></i>"
    cad += htm.span(cad2, 'icon is-small')
    cad += htm.span('Cerrar') + '</a>'
    return htm.div(cad, 'buttons is-right')


# Segundo orden
# Pone una imagen de eliminar cliqueable
def boton_detalles(accion):
    return boton_accion('Detalles', accion, 'fas fa-info')


# Pone una imagen de eliminar cliqueable
def boton_editar(accion):
    return boton_accion('Editar', accion, 'fas fa-edit')


# Pone una imagen de eliminar cliqueable, saca diálogo para confirmar
def boton_eliminar(accion):
    cad = "<a href='#' title='Eliminar'>"
    cad2 = "<i class='fas fa-trash-alt'"
    cad2 += " onClick=\"if(confirm('¿Desea eliminar este dato?')) "
    cad2 += "window.location='%s';\"></i>" % accion
    cad += htm.span(cad2, 'icon') + '</a>'
    return cad


# Pone un boton para ver un gráfico
def boton_grafica(accion):
    return boton_accion('Gráfica', accion, 'fas fa-chart-line')


# Boton con imagen de llamar x telefono
def boton_llamar(accion):
    return boton_accion('Llamada', accion, 'fas fa-phone')


def boton_seleccionar(accion):
    return boton_accion('Seleccionar', accion, 'fas fa-hand-pointer')


# Imprime boton de enviar formulario con texto = Aceptar
def botones(url):
    cad = etiqueta_campo('')
    cad += control("<button type='submit' class='button is-link'>Aceptar</button>")
    cad2 = "<button type='reset' class='button is-light'"
    cad2 += " onClick=\"window.location.href='%s'\">Cancelar</button>\n" % url
    cad += htm.div(cad2, 'control')
    return campo(cad, 'G')


# Imprime boton de enviar formulario con texto = Aceptar
def botones_formulario(texto_aceptar='Aceptar', url_cancelar=''):
    cad = etiqueta_campo('')
    cad += htm.div("<button type='submit' class='button is-link'>%s</button>\n" % texto_aceptar, 'control')
    cad2 = "<button type='reset' class='button is-light'"
    cad2 += " onClick=\"window.location.href='%s'\">Cancelar</button>\n" % url_cancelar
    cad += htm.div(cad2, 'control')
    return campo(cad, 'G')


# Combo box con opciones en un campo
def campo_combo(texto: str, listado, variable: str, defecto='') -> str:
    cad = etiqueta_campo(texto)
    cad += cuerpo_campo(control(htm.combo(listado, variable, defecto)))
    return campo(cad, 'H')


def etiqueta_campo(texto):
    return htm.div(etiqueta(texto), 'field-label')


# Imprime 2 celdas, una con texto y otra con un checkbox
def input_check(texto: str, variable: str, val: str) -> str:
    cad = etiqueta_campo(texto)
    if val == "" or val is None:
        val = "0"
    try:
        int_val = int(val)
    except ValueError:
        int_val = 0
    if int_val > 0:
        adicional = 'checked'
    else:
        adicional = ''
    chk = "<INPUT TYPE='checkbox' NAME='%s' VALUE='1' %s>" % (variable, adicional)
    cad += cuerpo_campo(campo(control(chk)))
    return campo(cad, 'H')


# Checkbox en 2 columnas
def input_check1(texto: str, variable: str, val: str) -> str:
    cad = "<div class='field is-horizontal is-grouped'>"
    cad += cuerpo_campo(input_check(texto, variable, val))
    return cad


# Checkbox en 2 columnas 2
def input_check2(texto: str, variable: str, val: str) -> str:
    cad = cuerpo_campo(input_check(texto, variable, val))
    cad += '</div>'
    return cad


def combo(campo_bdd: str, resultado, campos: typing.List[str], val) -> str:
    cad = "<select name='%s' id='%s'>\n" % (campo_bdd, campo_bdd)
    if val == '':
        cad += "<option value='' selected='selected'>Sin datos</option>\n"
    for fil in resultado:
        # cad += "<option value='%s' " % fil[campos[0]]
        cad += "<option value='%s' " % getattr(fil, campos[0])
        if str(getattr(fil, campos[0])) == str(val):
            cad += "selected='selected'"
        # cad += ">%s</option>\n" % fil[campos[1]]
        cad += ">%s</option>\n" % getattr(fil, campos[1])
    cad += "</select>\n"
    return cad


# Linea con celda con texto y otra con combobox
def input_combo(texto: str, campo_bdd: str, resultado, campos: typing.List[str], val) -> str:
    cad1 = etiqueta_campo(texto)
    cad = "<div class='control'>\n"
    cad += "<div class ='select'>\n"
    cad += combo(campo_bdd, resultado, campos, val)
    cad += "</div>\n</div>\n"
    cad1 += cuerpo_campo(campo(cad))
    return campo(cad1, 'H')


# Linea con celda con texto y otra con combobox. para poner lado a lado
def input_combo1(texto, campo_bdd, resultado, campos, val):
    cad = "<div class='field is-horizontal'>"
    cad += etiqueta_campo(texto)
    cad2 = "<div class='field is-expanded'>\n"
    cad2 += "<p class='control is-expanded'>\n"
    cad2 += "<div class ='select is-fullwidth'>\n"
    cad2 += combo(campo_bdd, resultado, campos, val)
    cad2 += "</div>\n</p>\n</div>\n"
    cad += htm.div(cad2, 'field-body')
    return cad


# Linea con celda con texto y otra con combobox. para poner lado a lado
def input_combo2(texto, campo_bdd, resultado, campos, val):
    cad = etiqueta_campo(texto)
    cad2 = "<div class='field is-expanded'>\n"
    cad2 += "<p class='control is-expanded'>\n"
    cad2 += "<div class ='select is-fullwidth'>\n"
    cad2 += combo(campo_bdd, resultado, campos, val)
    cad2 += "</div>\n</p>\n</div>"
    cad += htm.div(cad2, 'field-body')
    cad += "</div>\n"
    return cad


# Imprime un campo de ingreso de valor numerico
def input_entero(texto: str, campo_bdd: str, val, minimo=None) -> str:
    tex = str(texto)
    if isinstance(val, str) and (val == ""):
        val = '0'
    numero = dinero.numero(val)
    cdn2 = etiqueta_campo(tex)
    cad = "<div class='control'>"
    cad += "<input class='input' type='number' "
    if minimo is not None:
        minimo = str(int(minimo))
        cad += "min=%s " % minimo
    cad += "name='%s' value='%s' id='%s' step='1'>" % (campo_bdd, numero, campo_bdd)
    cad += '</div>'
    cdn3 = cdn2 + cuerpo_campo(cad)
    return campo(cdn3, 'H')


# Crea celdas contiguas con texto y campo de texto
def input_fecha(texto: str, campo_bdd: str, val):
    cad = etiqueta_campo(texto)
    entrada = "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    entrada += "min='1920-01-01' max='2120-12-31' "
    entrada += "name='%s' value='%s' id='%s'>\n" % (campo_bdd, val, campo_bdd)
    cad += cuerpo_campo(campo(control(entrada)))
    return campo(cad, 'H')


# Crea celdas contiguas con texto y campo de texto
def input_fecha1(texto, campo_bdd, val):
    cad = "<div class='field is-horizontal'>"
    cad += etiqueta_campo(texto)
    cad2 = "<div class='field is-expanded'>\n"
    cad2 += "<p class='control is-expanded'>\n"
    cad2 += "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    cad2 += "min='1920-01-01' max='2120-12-31' "
    cad2 += "name='%s' value='%s' id='%s'>\n" % (campo_bdd, val, campo_bdd)
    cad2 += "</p>\n</div>\n"
    cad += htm.div(cad2, 'field-body')
    return cad


def input_fecha2(texto, campo_bdd, val):
    cad = htm.div(etiqueta(texto), 'field-label is-normal')
    cad2 = "<div class='field is-expanded'>\n"
    cad2 += "<p class='control is-expanded'>\n"
    cad2 += "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    cad2 += "min='1920-01-01' max='2120-12-31' "
    cad2 += "name='%s' value='%s' id='%s'>\n" % (campo_bdd, val, campo_bdd)
    cad2 += "</p>\n</div>"
    cad += htm.div(cad2, 'field-body')
    cad += "</div>\n"
    return cad


def input_hora(texto, campo_bdd, val):
    cad = etiqueta_campo(texto)
    cad += cuerpo_campo(campo(control(htm.entrada('time', texto, campo_bdd, val))))
    return campo(cad, 'H')


# Imprime una linea con una celda con texto y otra con un campo memo
def input_memo(texto, campo_bdd, val):
    if val is None:
        val = ''
    cad = etiqueta_campo(texto)
    ctrl = "<textarea class='textarea' name='%s' placeholder='%s'>%s</textarea>" % (campo_bdd, texto, val)
    cad += cuerpo_campo(campo(control(ctrl)))
    return campo(cad, 'H')


# Imprime un campo de ingreso de valor numerico
def input_numero(texto, campo_bdd, val, decimales=2):
    if isinstance(val, str) and (val == ''):
        val = '0'
    num = dinero.numero(val, decimales)
    cad = etiqueta_campo(texto)
    cad += cuerpo_campo(campo(control(htm.entrada('number', texto, campo_bdd, num))))
    return campo(cad, 'H')


def input_password(texto, campo_bdd, val):
    cad = etiqueta_campo(texto)
    cad += cuerpo_campo(control(htm.entrada('password', texto, campo_bdd, val)))
    return campo(cad, 'H')


# arreglo es un DICCIONARIO con texto y valor del item
def input_radio(texto: str, variable: str, arreglo: typing.Dict[str, int], val: str) -> str:
    radio = ''
    for llave in arreglo:
        radio += "<label class='radio'>"
        if arreglo[llave] == val:
            chkd = 'checked'
        else:
            chkd = ''
        radio += "<input type='radio' name='%s' value='%s' %s> " % (variable, arreglo[llave], chkd)
        radio += str(llave)
        radio += ' </label>   '
    cad = etiqueta_campo(texto)
    cad += cuerpo_campo(campo(control(radio)))
    return campo(cad, 'H')


# Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
def input_texto(texto: str, campo_bdd: str, val: str) -> str:
    cad = etiqueta_campo(texto)
    cad += cuerpo_campo(campo(control(htm.entrada('text', texto, campo_bdd, val))))
    return campo(cad, 'H')


# Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
def input_texto1(texto, campo_bdd, val):
    cad = "<div class='field is-horizontal is-grouped'>"
    cad += input_texto(texto, campo_bdd, val)
    return cad


# Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
def input_texto2(texto: str, campo_bdd: str, val: str) -> str:
    cad = input_texto(texto, campo_bdd, val)
    cad += '</div>'
    return cad


def nav_bar(enlace, icono, texto):
    cad = "<a class='navbar-item' href='%s'>" % enlace
    cad += faicon(icono)
    cad += htm.span(texto)
    cad += '</a>'
    return cad


def rango_fechas(fini=None, ffin=None, accion=''):
    cad = htm.form_edicion('Seleccionar fechas', accion)
    cad += input_fecha1('Inicio', 'fini', fini)
    cad += input_fecha2('Fin', 'ffin', ffin)
    cad += htm.div("<input class='button is-link' type='submit' value='Buscar'>", 'control')
    cad += htm.form_edicion_fin()
    return cad


def script_file():
    cad = "const fileInput = document.querySelector('#fileupld input[type=file]');"
    cad += 'fileInput.onchange = () => {'
    cad += 'if (fileInput.files.length > 0) {'
    cad += "const fileName = document.querySelector('#fileupld .file-name');"
    cad += 'fileName.textContent = fileInput.files[0].name;'
    cad += "}\n}\n"
    return htm.script(cad)


# Nivel terciario
def barra_navegacion():
    cad = "<nav class='navbar' role='navigation' aria-label='main navigation'>"
    cad += "<div class='navbar-brand'><a class='navbar-item' href='/'>"
    cad += "<img src='/img/logo.png'></a>"
    cad += "<a role='button' class='navbar-burger' aria-label='menu' aria-expanded='false' "
    cad += "data-target='navbarBasicExample'>"
    cad += "<span aria-hidden='true'></span><span aria-hidden='true'></span><span aria-hidden='true'></span>"
    cad += '</a></div>'
    cad += "<div id='navbarBasicExample' class='navbar-menu'><div class='navbar-start'>"
    cad += nav_bar('/', 'fas fa-home', 'Inicio')
    cad += nav_bar('/recepcion', 'fas fa-headset', 'Recepción')
    cad += nav_bar('/administracion', 'fas fa-dollar-sign', 'Administración')
    cad += nav_bar('/vehiculos', 'fas fa-ambulance', 'Vehículos')
    cad += nav_bar('/direccion', 'fas fa-cogs', 'Dirección')
    cad += nav_bar('/direccion_tecnica', 'fas fa-user-md', 'Dir.Técnica')
    cad += nav_bar('/sistema', 'fas fa-desktop', 'Sistema')
    cad += '</div>'
    cad += "<div class='navbar-end'><div class='navbar-item'><div class='buttons'>"
    cad += "<a class='button is-warning' href='/logout'>%s<strong>Salir</strong></a>" % faicon('fas fa-sign-out-alt')
    cad += '</div></div></div></div></nav>'
    return cad


def file_upload(destino, retorno):
    cad = "<form action='%s' method='post' enctype='multipart/form-data'>" % destino
    # cad += "<div id='fileupld' class='file has-name'>"
    # cad += "<label class='file-label'>"
    # cad += "<input class='file-input' type='file' name='file'>"
    # cad += "<span class='file-cta'>"
    # cad += htm.span("<i class='fas fa-upload'></i>", 'file-icon')
    # cad += '</span>'
    # cad += htm.span('Seleccione un archivo...', 'file-label')
    # cad += '</span>'
    # cad += htm.span('...', 'file-name')
    # cad += '</label>'
    # cad += botones(retorno)
    # cad += '</div></form>'
    # cad += script_file()
    cad += "<div id = 'file-js-example' class ='file has-name'>"
    cad += "<label class ='file-label'>"
    cad += "<input class ='file-input' type='file' name='archivo'>"
    cad += "<span class ='file-cta'>"
    cad += htm.span("<i class ='fas fa-upload'></i>", "file-icon")
    cad += htm.span("Elija un archivo...", "file-label")
    cad += "</span>"
    cad += htm.span("No se subió ningún archivo", "file-name")
    cad += "</label>"
    cad += "</div>"
    cad += botones(retorno)
    cad += "</form>"
    cad += "<script>"
    cad += "const fileInput = document.querySelector('#file-js-example input[type=file]');"
    cad += "fileInput.onchange = () => {"
    cad += "if (fileInput.files.length > 0)"
    cad += "{"
    cad += "const fileName = document.querySelector('#file-js-example .file-name');"
    cad += "fileName.textContent = fileInput.files[0].name;"
    cad += "}"
    cad += "}"
    cad += "</script>"
    return cad


def generar_menu(eti: str, items: dict, activo=None) -> str:
    if isinstance(activo, str):
        num_activo = None
        for llave in items.keys():
            if activo.upper() == items[llave][2].upper():
                num_activo = llave
    else:
        num_activo = activo
    cad = "<aside class='menu'>"
    cad += "<p class='menu-label'>%s</p>" % eti
    cad += "<ul class='menu-list'>"
    for indice, item in items.items():
        if indice == num_activo:
            cad += "<li><a class='is-active' href='%s'>%s %s</a></li>" % (item[0], faicon(item[1], 'white'), item[2])
        else:
            cad += "<li><a href='%s'>%s %s</a></li>" % (item[0], faicon(item[1]), item[2])
    cad += '</ul></aside>'
    return cad


def encabezado(nivel, texto) -> str:
    """Imprime un encabezado con nivel"""
    niveles = ["", " is-4", " is-5", " is-6"]
    cadena = "<h" + str(nivel) + " class='title" + niveles[nivel-1]
    cadena += "'>" + texto + "</h" + str(nivel) + ">"
    return cadena


def celda_menu(texto, enl, icono, ayuda="") -> str:
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


def encabezado_tabla(arr):
    """A partir de un array arma el encabezado de una tabla"""
    cad = "<div class='table-container'>"
    cad += "<table class='table is-hoverable'><thead><tr>\n"
    for lin in arr:
        cad += celda_encabezado(lin)
    cad += '</tr>\n</thead>\n<tbody>\n'
    return cad
