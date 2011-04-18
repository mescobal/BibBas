#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Conjunto de rutinas para generar codigo html"""
import funciones
import Cookie
import os
# ========================================
# Con impresión
def botones(url):
    """Imprime boton de enviar formulario con texto = Aceptar"""
    print(table(tr(td(submit("Aceptar", 'height: 40px; width: 150px'), align="center") +
     td(button("Cancelar", url , 'height: 40px; width: 150px'), align="center")), '100%', clase='tform'))
def encabezado_recibo(titulo):
    """Encabezado para recibo de sueldos"""
    inicio()
    title(titulo)
    estilo("recibo.css")
    print('</head><body>')
    h1(titulo)
def encabezado_informe(titulo):
    """Imprime un encabezado, pero haciendo referencia a una hoja de estilo para informes"""
    inicio()
    title(titulo)
    estilo("greyscale.css")
    print '</head><body>'
    h1(titulo)
def estilo(cascade = "geinedpy.css"):
    """Imprime un link a hoja de estilo con una predeterminada"""
    print('<link type="text/css" href="'+cascade+'" rel="stylesheet" />')
def fin():
    """Tags de finalizacion de una pagina"""
    print '</div></body></html>'
def form_edicion(texto, accion):
    """Pone un formulario de edicion, encabezado"""
    print("<div align='center'><form action='" + accion + "' method='post'><table class='tform'><caption>" + texto + "</caption><tr>")
    # print("<form action='" + accion + "' method='post'><table><caption>" + texto + "</caption><tr>")
def form_edicion_fin():
    """Finalización de form de edición"""
    print '</tr></table></form></div>'
    # print '</tr></table></form>'
def formulario(accion):
    """Imprime el encabezado de un formulario"""
    print("<div align='center'><form action='" + accion + "' method='POST'>")
def inicio():
    """Imprime encabezado de pagina web SIN cookie"""
    print 'Content-Type: text/html; charset=utf-8'
    print ""
def input_combo(texto, campo, resultado, campos, valor):
    """Linea con celda con texto y otra con combobox"""
    print("<tr>")
    print(td(texto))
    print("<td>")
    print("<select name='%s' id='%s'>" % (campo, campo))
    for fil in resultado:
        print('<option value="' + str(fil[campos[0]]) + '" '),
        if str(fil[campos[0]]) == str(valor):
            print('selected="selected"'),
        print('>' + fil[campos[1]] + '</option>')
    print '</select></td></tr>'
def input_fecha(texto, campo, valor):
    """Crea celdas contiguas con texto y campo de texto"""
    print '<tr>'
    print(td(texto))
    print '<td>'
    print '<input type="text" name="' + campo + '" id="f_date_b" value="' \
    + funciones.mysql_a_fecha(valor) + '">'
    print '<BUTTON TYPE="reset" ID="f_trigger_b">...</button>'
    print '</TD></TR>'
def input_fecha2(texto, campo, valor):
    """Crea celdas para form con 2 fechas"""
    print("<tr>")
    print(td(texto))
    print("<td>")
    print('<input type="text" name="' + campo + '" id="f_date_b2" value="' \
    + funciones.mysql_a_fecha(valor) + '"/>')
    print('<BUTTON TYPE="reset" ID="f_trigger_b2">...</button>')
    print('</TD></TR>')
def input_numero(texto, campo, valor, decimales=2):
    """Imprime un campo de ingreso de valor numerico"""
    if not type(texto) is str:
        tex = str(texto)
    else:
        tex = texto
    if type(valor) is str:
        if valor == "":
            valor = "0"
    print(tr(td(tex) + td('<input type="text" style="text-align:right" name="' + 
        campo + '" value="' + funciones.numero(valor, decimales) + '">')))
def linea_numero(texto, decimales=2):
    """Imprime una celda con un número formateado con 2 decimales"""
    print(td(funciones.numero(texto, decimales), "right"))
def script_noenter():
    """Impide que funcione la tecla enter en una pagina"""
    print """<script type="text/javascript">
    function stopRKey(evt) {
    var evt = (evt) ? evt : ((event) ? event : null);
    var node = (evt.target) ? evt.target : ((evt.srcElement) ? evt.srcElement : null);
    if ((evt.keyCode == 13) && (node.type=="text"))  {return false;}
    }
    document.onkeypress = stopRKey;
    </script>';"""
# ========================================
# Con devolución de cadena
def encabezado(titulo, texto, referencia ):
    """Imprime un encabezado"""
    cadena = h1(titulo)
    cadena = cadena + '<a class="retroceso" href="' + referencia + '">' + texto + '</a>'
    return cadena
def load_script(tipo="text/javascript", src='', charset="utf-8"):
    """Carga script"""
    cadena = '<script type="{0}" src="{1}" charset="{2}"></script>'
    return cadena.format(tipo, src, charset)
def redirigir(url):
    """Redirige usando javascript a otra pagina"""
    texto = 'window.location = "' + url + '";'
    return script(texto, "text/javascript")
    
# ========================================
# Conversión de tags HTML
# ========================================


def fin_tabla():
    """Imprime tags de finalizacion de una tabla"""
    print '</tbody></table>'
def boton_eliminar(accion):
    """Pone una imagen de eliminar cliqueable, saca diálogo para confirmar"""
    print("<a href='#' title='Eliminar registro'><img src='./img/eliminar.png' width='24' height='24' border='0' \
        onClick=\"if(confirm('¿Desea borrar este registro?')) window.location='" + accion + "';\"></a>")
def boton_imprimir(accion):
    """pone un boton con una ACCION"""
    print("<a href='" + accion + "' title='Imprimir'><img src='./img/printer32.png' width='24' height='24' border='0'></a>")
def celda_menu(texto, enlace, icono):
    """Pone una celda del menu"""
    t = td(
        a(enlace,
            img("./img/" + icono) +
            '<p class="texto_icono">' +
            texto + '</p>'),
        "center")
    return t
def imagen(imag):
    """Pone imagen con caracteristicas predeterminadas"""
    print('<img src="./img/%s" width="64" height="64" border="0">' % imag)
def encabezado_tabla(arr):
    """A partir de un array arma el encabezado de una tabla"""
    #print '<table width="100%"><thead><tr>'
    print('<table class="tabla_datos"><thead><tr>')
    for lin in arr:
        print(th(lin))
    print '</tr></thead><tbody>'
def campo_oculto(variable, dato):
    """Imprime un campo oculto"""
    print "<input type='hidden' name='%s' value='%s'>" % (variable, dato)
def fin_formulario():
    """Termina el formulario"""
    print '</form></div>'
def input_input(tipo, nombre, valor=''):
    """Imprime un campo tipo INPUT"""
    print('<input type="'+ tipo + '" name="' + nombre + '" value="'+ valor + '"></input>')
def input_check(texto, variable, valor):
    """Imprime 2 celdas, una con texto y otra con un checkbox"""
    adicional = ""
    if type(valor) is type(None):
        val = 0
    elif type(valor) is int:
        val = valor
    else:
        val = int(valor)
    if val > 0:
        adicional = "checked"
    print '<TR>'
    print(td(texto))
    print(td("<INPUT TYPE='checkbox' NAME='" + variable + "' VALUE='1' " + adicional + ">"))
    print("</tr>")
def fila_alterna(i):
    """Genera colores alternos para filas de una tabla"""
    if (i % 2) == 0:
        print "<tr>"
    else:
        print "<tr class='odd'>"
def imagen_menu(imag, enlace, texto):
    """Imprime una celda con una imagen, enlace y texto"""
    print '<td align="center"><a href="' + enlace + '"><img src="./img/' +\
    imag  + '" align="top" border="0"></a></br>' + \
    texto + '</td>'
    #imag  + '" width="64" height="64" align="top" border="0"></a></br>' + 
def duplicado(pag):
    """Genera html de error por existencia de duplicado"""
    texto = 'Ya existe un dato igual al que usted intenta agregar.'
    texto = texto + ' Verifique el dato e inténtelo nuevamente'
    nota(texto)
    print button('Volver', pag)
def navegador(este_archivo, pagina_actual, total_paginas):
    """Imprime un navegador al pie de una tabla"""
    nav = ""
    union = "?"
    if "?" in este_archivo:
        union = "&"
    if type(pagina_actual) != "int":
        pagina_actual = int(pagina_actual)
    if type(total_paginas) != "int":
        total_paginas = int(total_paginas)
    for n in range(1, total_paginas + 1):
        if n == pagina_actual:
            nav = nav + " " + str(pagina_actual) + " "
        else:
            nav = nav + " <a href='" + este_archivo + union + "pagina="+ str(n) + "'>" + str(n) + "</a> "
    #enlaces a primero - anterior - posterior - ultimo
    if pagina_actual > 1:
        pag = pagina_actual -1
        prev = " <a href='" + este_archivo + union + "pagina=" + str(pag) + "'>[<-]</a> "
        prim = " <a href='" + este_archivo + union + "pagina=1'>[<<]</a> "
    else:
        prev = " "
        prim = " "
    if pagina_actual < total_paginas:
        pag = pagina_actual + 1
        sig = " <a href='" + este_archivo + union + "pagina=" + str(pag) + "'>[->]</a> "
        ult = " <a href='" + este_archivo + union + "pagina=" + str(total_paginas + 1) + "'>[>>]</a> "
    else:
        sig = " "
        ult = " "
    print("<center class='barra'>" + prim + prev + nav + sig + ult + "</center>")
def script_fecha():
    """Imprime en una pagina web un javascript para manejo de fechas"""
    texto = """Calendar.setup({
        inputField     :    'f_date_b',
        ifFormat       :    '%d/%m/%Y',
        showsTime      :    false,
        button         :    'f_trigger_b',
        step           :    1
        });"""
    return(script(texto, "text/javascript"))
def script_fecha2():
    """Genera segundo script de fecha"""
    texto2 = """Calendar.setup({
        inputField     :    'f_date_b2',
        ifFormat       :    '%d/%m/%Y',
        showsTime      :    false,
        button         :    'f_trigger_b2',
        step           :    1
        });"""
    return(script(texto2, "text/javascript"))
    
# ===============================================================================    

def boton_confirmar(texto, leyenda, accion):
    """Pone un boton con un TEXTO que saca diálogo para confirmar"""
    action = "if(confirm(\"{0}\")) window.location=\"{1}\";".format(leyenda, accion)
    cadena = "<input type='button' value='" + texto + "' "
    cadena = cadena + "onClick='" + action + "' "
    cadena = cadena + "/>"   
    print cadena
def boton_detalles(accion):
    """Pone una imagen de eliminar cliqueable"""
    print(a(accion, img("./img/ver.png", 24, 24, 0), "Detalles"))
def boton_editar(accion):
    """Pone una imagen de eliminar cliqueable"""
    print(a(accion, img("./img/editar.png", 24, 24, 0),'Editar'))
def fila_datos(texto, datos):
    """Imprime una hilera con 2 celdas: una de texto y otra de datos"""
    datos = str(datos)
    print (tr(td(texto) + td(datos)))
def input_texto(texto, campo, valor, ancho=60):
    """Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar"""
    print(tr(td(texto) + td(text(campo, valor, ancho))))
def input_disabled(texto, campo, valor, ancho=60):
    """Imprime celda con texto y texto, muestra un campo no modificable"""
    print(tr(td(texto + td(text(campo, valor, ancho, disabled=True)))))
def input_label(texto1, texto2):
    """Imprime 2 celdas adyacentes en 1 fila ambas con texto"""
    print(tr(td(texto1) + td(texto2)))
def input_memo(texto, campo, valor):
    """Imprime una linea con una celda con texto y otra con un campo memo"""
    if type(valor) == type(None):
        valor = ""
    print(tr(td(texto) + td(textarea(valor, campo))))
def leer_cookie():
    """Lee una cookie presente en la sesion"""
    coo = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE",""))
    return coo
def linea_moneda(texto):
    """Imprime una celda con un valor monetario adentro"""
    print(td(funciones.moneda(texto), "right"))
def nota(texto):
    """Imprime una tabla con texto pequeno"""
    print(table(tr(td(span(texto, "nota")))))
def texto_barra(texto):
    """Imprime un texto blanco"""
    return "<div class='texto_barra'>" + texto + "</div>"
# ===============================================================================

    
def a(enlace, texto, titulo=''):
    """Tag html"""
    cadena = "<a href='{0}'>{1}</a>"
    if titulo != "":
        cadena = "<a href='{0}' title='" + titulo + "'>{1}</a>"
    return cadena.format(str(enlace), str(texto))
def b(texto):
    """Tag html"""
    cadena = "<b>{0}</b>"
    return cadena.format(texto)
def body(contenido):
    cadena = "<body>" + contenido + "</body>"
    return cadena
def boton(texto, referencia):
    """Devuelve un boton - texto con estilo CSS"""
    return '<a class="boton" href="' + referencia + '">' + texto + '</a>'
def button(texto, action, style=""):
    """Tag html"""
    cadena = "<input type='button' value='" + texto + "' "
    cadena = cadena + "onClick=\"parent.location='" + action + "'\" "
    if style != "":
        cadena = cadena + " style='" + style + "'"
    cadena = cadena + "/>"   
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
def h1(texto):
    """Tag HTML"""
    cadena = "<h1>{0}</h1>"
    return cadena.format(texto)
def h2(texto):
    """Tag html"""
    cadena = "<h2>{0}</h2>"
    return cadena.format(texto)
def h3(texto):
    """Tag html"""
    cadena = "<h3>{0}</h3>"
    return cadena.format(texto)
def head(contenido):
    """Encabezado de pagina web"""
    return '<head>' + contenido + '</head>'
def hidden(campo, valor):
    """Tag Html"""
    return "<input type='hidden' name='%s' value='%s'>" % (campo, valor)
def hr():
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
def li(texto):
    """Tag html"""
    cadena = "<li>{0}</li>"
    return cadena.format(texto)
def p(texto):
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
def td(texto="", align='left', rowspan=1, colspan=1):
    """Tag html"""
    cadena = "<td align='" + align + "' rowspan='" + str(rowspan) + \
        "' colspan='" + str(colspan) + "'>" + str(texto) + "</td>"
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
    r = str(rows)
    c = str(cols)
    cadena = "<textarea name='" + field + "' rows='" + r + "' cols='" + c + "'>" + value + "</textarea>"
    return cadena
def tfoot(texto):
    """Tag html"""
    cadena = "<tfoot>{0}</tfoot>"
    return cadena.format(texto)
def th(texto):
    """Tag html"""
    cadena = "<th>{0}</th>"
    return cadena.format(texto)
def title(texto):
    """Tag html"""
    cadena = "<title>{0}</title>"
    return cadena.format(texto)
def tr(texto):
    """Tag html"""
    cadena = "<tr>{0}</tr>"
    return cadena.format(texto)
def ul(texto):
    """Tag html"""
    cadena = "<ul>{0}</ul>"
    return cadena.format(texto)

if __name__ == 'main':
    print "Es un módulo no ejecutable"
