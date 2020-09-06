#!/usr/bin/env ruby
# Clase para manejar HTML
# Version: 0.5.13
require_relative 'funciones'

# Conjunto de rutinas para generar codigo html."""
module Htm
  extend self

  LOGO = 'logo.png'.freeze
  # # ========================================
  # # Navegacion

  # def redirigir(url):
  #     """Redirige usando javascript a otra pagina"""
  #     texto = 'window.location = "' + url + '";'
  #     return script(texto, "text/javascript")

  # def ir_a_pagina(pagina):
  #     """Manda navegador a una url."""
  #     cadena = inicio()
  #     cadena += "<html>\n<body>\n"
  #     cadena += "<form id='autolog' action='%s' method='post'>\n</form>" % (pagina)
  #     cadena += "<script language='JavaScript' type: 'text/javascript'>\n"
  #     cadena += "document.getElementById('autolog').submit();"
  #     cadena += "</script>\n"

  # def autorizacion():
  #     """Incluido por compatibilidad con librería en Ruby"""
  #     # TODO hay que reescribir todo
  #     # cgi = cgimodulo('html5')
  #     # sesion = cgisession(cgi)
  #     # if sesion['nivel'] == None:
  #     #    nivel_usuario = 100
  #     # else:
  #     #    nivel_usuario = int(sesion['nivel'])
  #     # if nivel >= nivel_usuario:
  #     #    autorizacion = True
  #     # else:
  #     #    autorizacion = False
  #     # if sesion['nivel'] == None:
  #     #    inicio
  #     #    redirigir('login.py')
  #     # elif autorizacion != True:
  #     #    Paginas.no_autorizado('login.py')
  #     # autorizacion
  #     print("No implementado en python, solo en Ruby")

  # # Con impresión
  def self.input_password(texto, campo, valor, ancho = 60)
    # Entrada de clave
    cadena = "<div class='field'>"
    cadena << "<label class='label'>#{texto}</label>"
    cadena << "<div class='control has-icons-left'>"
    cadena << "<input class='input' type='password' placeholder='#{texto}' name='#{campo}'"
    cadena << " value='#{valor}'  id='#{campo}' size='#{ancho}'>"
    cadena << "<span class='icon is-small is-left'>"
    cadena << "<i class='fas fa-lock'></i></span>"
    cadena << '</div></div>'
  end
  # def titulares(titulo, subtitulo=''):
  #     """Encabezado nivel 1."""
  #     cadena = "<div id='main'>\n"
  #     cadena += "<div class='header'><h1>%s</h1>\n" % (titulo)
  #     if subtitulo != '':
  #         cadena += "<h2>%s</h2>\n" % (subtitulo)
  #     cadena += '</div>'
  #     return cadena

  # Imprime boton de enviar formulario con texto = Aceptar.
  def self.botones(url)
    cadena = "<div class='field is-grouped'>\n"
    cadena << "<div class='control'>\n"
    cadena << "<button type='submit' class='button is-link'>Aceptar</button>\n"
    cadena << "</div>\n"
    cadena << "<div class='control'>\n"
    cadena << "<button type='reset' class='button is-light'"
    cadena << " onClick=\"window.location.href='#{url}'\">Cancelar</button>\n"
    cadena << "</div>\n</div>\n"
  end

  # def botones_formulario(texto_aceptar="Aceptar", url_cancelar=""):
  #     """Imprime boton de enviar formulario con texto = Aceptar."""
  #     cadena = "<div class='field is-grouped'>\n"
  #     cadena += "<div class='control'>\n"
  #     cadena += "<button type='submit' class='button is-link'>" + texto_aceptar + "</button>\n"
  #     cadena += '</div>\n'
  #     cadena += "<div class='control'>\n"
  #     cadena += "<button type='reset' class='button is-light'"
  #     cadena += " onClick=\"window.location.href='%s'\">Cancelar</button>\n" % (url_cancelar)
  #     cadena += "</div>\n</div>\n"
  #     return cadena

  # def combo(listado, variable, defecto):
  #     """Combo box con listado como opciones y texto x defecto."""
  #     cadena = "<div class ='select'><select name='" + variable + "' id='" + variable + "' >\n"
  #     for item in listado:
  #         if item == defecto:
  #             cadena += "<option selected='selected' value='" + item + "'>" + item + "</option>\n"
  #         else:
  #             cadena += "<option value='" + item + "'>" + item + "</option>\n"
  #     cadena += "</select></div>"
  #     return cadena

  # Imprime un link a hoja de estilo con una predeterminada
  def self.estilo(cascade = '/css/bulma.css')
    "<link type='text/css' href='#{cascade}' rel='stylesheet'>"
  end

  def self.fin_pagina
    # Tags de finalizacion de una pagina
    '</div></div></body></html>'
  end

  # Imprime tags de finalizacion de una tabla
  def fin_tabla
    '</tbody></table>'
  end

  # Pone un formulario de edicion, encabezado.
  def form_edicion(texto, accion)
    cadena = "<h2 class='subtitle'>#{texto}</h2>"
    cadena << "<form action='#{accion}' method='post'>"
  end

  # Finalización de form de edición
  def form_edicion_fin
    '</form>'
  end

  # def formulario(accion):
  #     """Imprime el encabezado de un formulario."""
  #     print("<form action='%s' method='POST'>" % (accion))

  # def inicio():
  #     """Imprime encabezado de pagina web SIN cookie."""
  #     cadena = 'Content-Type: text/html; charset=utf-8\n\n'
  #     cadena += "<!DOCTYPE html>"
  #     cadena += "<html lang='es'>"
  #     return cadena

  # Linea con celda con texto y otra con combobox
  def self.input_combo(texto, campo, resultado, campos, valor)
    cadena = "<div class='field'>\n"
    cadena << "<label class='label'>#{texto}</label>"
    cadena << "<div class ='select'><select name='#{campo}' id='#{campo}'>"
    cadena << "<option value='' selected='selected'>Sin datos</option>\n" if valor == ''
    resultado.each do |fil|
      cadena << "<option value='#{fil[campos[0]]}'"
      cadena << "selected='selected'" if fil[campos[0]].to_s == valor.to_s
      cadena << ">#{fil[campos[1]]}</option>\n"
    end
    cadena << "</select></div>\n</div>\n"
  end

  # Crea celdas contiguas con texto y campo de texto.
  def self.input_fecha(texto, campo, valor)
    cadena = "<div class='field'>\n"
    cadena << "<label class='label'>#{texto}</label>\n"
    cadena << "<div class='control'>\n"
    cadena << "<input class='input' type='date' placeholder='#{texto}' "
    cadena << "name='#{campo}' value='#{valor}' id='#{campo}'>\n"
    cadena << "</div>\n</div>\n"
  end

  def self.input_hora(texto, campo, valor)
    cadena = "<div class='field'>\n"
    cadena << "<label class='label'>#{texto}</label>\n"
    cadena << "<div class='control'>\n"
    cadena << "<input class='input' type='time' placeholder='#{texto}' "
    cadena << "name='#{campo}' value='#{valor}' id='#{campo}'>\n"
    cadena << "</div>\n</div>\n"
  end
  # def input_fecha2(texto, campo, valor):
  #     """Crea celdas para form con 2 fechas"""
  #     cadena = "<tr>"
  #     cadena += celda(texto)
  #     cadena += "<td>"
  #     cadena += '<input type="text" name="' + campo + '" id="f_date_b2" value="'
  #     cadena += funciones.sql_a_fecha(valor) + '"/>'
  #     cadena += '<BUTTON TYPE="reset" ID="f_trigger_b2">...</button>'
  #     cadena += '</TD></TR>'
  #     return cadena

  # Imprime un campo de ingreso de valor numerico
  def self.input_numero(texto, campo, valor, decimales = 2)
    tex = texto.to_s
    valor = '0' if (valor.is_a? String) && valor.empty?
    numero = Funciones.numero_ss(valor, decimales)
    cadena = "<div class='field'>\n<label class='label'>#{tex}</label>\n"
    cadena << "<div class='control'>"
    cadena << "<input class='input' type='number' placeholder='#{tex}' "
    cadena << "name='#{campo}' value='#{numero}' id='#{campo}'></div></div>"
  end

  # Imprime un campo de ingreso de valor numerico
  def self.input_entero(texto, campo, valor, minimo = nil, maximo = nil)
    if !texto.instance_of?(String)
      tex = texto.to_s
    else
      tex = texto
    end
    if valor.instance_of?(String)
      valor = '0' if valor == ''
    end
    numero = Funciones.numero(valor)
    cadena = "<div class='field'>"
    cadena << "<label class='label'>#{tex}</label>"
    cadena << "<div class='control'>"
    cadena << "<input class='input' type='number' "
    unless minimo.nil?
      minimo = minimo.to_i
      cadena << "min=#{minimo} "
    end
    unless maximo.nil?
      maximo = maximo.to_i
      cadena << "max=#{maximo} "
    end
    cadena << "name='#{campo}' value='#{numero}' id='#{campo}'>"
    cadena << '</div></div>'
  end

  # def linea_numero(texto, decimales=2):
  #     """Imprime una celda con un número formateado con 2 decimales"""
  #     print(celda(funciones.numero(texto, decimales), "right"))

  # def script_noenter():
  #     """Impide que funcione la tecla enter en una pagina"""
  #     print("""<script type="text/javascript">
  #     function stopRKey(evt) {
  #     var evt = (evt) ? evt : ((event) ? event : null);
  #     var node = (evt.target) ? evt.target : ((evt.srcElement) ? evt.srcElement : null);
  #     if ((evt.keyCode == 13) && (node.type=="text"))  {return false;}
  #     }
  #     document.onkeypress = stopRKey;
  #     </script>';""")

  # def seleccionar_ano(defecto=""):
  #     """Combo box para seleccionar año - 10 antes del actual"""
  #     ano_actual = funciones.ano_actual()
  #     if defecto == "":
  #         seleccionado = str(ano_actual)
  #     else:
  #         seleccionado = str(defecto)
  #     print("<select name='ano'>")
  #     for contador in range(ano_actual, ano_actual-10, -1):
  #         if str(contador) == seleccionado:
  #           print("<option selected value='" + str(contador) + "'>" + str(contador) + "</option>")
  #         else:
  #             print("<option value='" + str(contador) + "'>" + str(contador) + "</option>")
  #     print("</select>")

  # # ========================================
  # # Con devolución de cadena

  # def encabezado(titulo, texto, referencia):
  #     """Imprime un encabezado"""
  #     cadena = encabezado_1(titulo)
  #     cadena = cadena + '<a class="retroceso" href="' + referencia + '">' + \
  #         texto + '</a>'
  #     return cadena

  # encabezado completo para una pagina
  def self.encabezado_completo(titulo, referencia)
    # Imprime encabezado con logo y boton de retorno
    cadena = "<head>\n<meta charset='utf-8' />\n"
    cadena << "<title>#{titulo}</title>\n"
    cadena << estilo
    cadena << "</head>\n<body>\n"
    cadena << "<div class='section'><div class='container'>\n<div class='box'>\n"
    cadena << "<img src='/img/#{LOGO}' align='right'>"
    cadena << Htm.encabezado(1, titulo)
    cadena << Htm.retroceso(referencia)
    cadena << "</div>\n"
  end

  # def load_script(tipo="text/javascript", src='', charset="utf-8"):
  #     """Carga script"""
  #     cadena = '<script type="{0}" src="{1}" charset="{2}"></script>'
  #     return cadena.format(tipo, src, charset)

  # # ========================================
  # # Conversión de tags HTML
  # # ========================================

  # pone una celda del menu
  def self.celda_menu(texto, enl, icono, ayuda = '')
    # 1
    cadena = "<div class='title is-child is-info box'>\n"
    cadena << "<a href='#{enl}'><p class='title' align='center'>#{texto}</p></a>\n"
    cadena << "<a href='#{enl}'><div class='level'><div class='level-item has-text-centered'>\n"
    cadena << "<figure class='image is-96x96'><img src='/img/#{icono}'></figure>\n"
    cadena << "</div>\n</div>\n</a>\n"
    # 2
    cadena << "<div class='content is-small has-text-centered'>\n"
    cadena << ayuda
    cadena << "</div>\n</div>\n"
  end

  # def imagen(imag):
  #     """Pone imagen con caracteristicas predeterminadas"""
  #     return '<img src="./img/%s" width="64" height="64" border="0">' % imag

  # A partir de un array arma el encabezado de una tabla
  def self.encabezado_tabla(arr)
    cadena = "<table class='table'><thead><tr>\n"
    arr.each do |lin|
      cadena << Htm.celda_encabezado(lin)
    end
    cadena << "</tr>\n</thead>\n<tbody>\n"
  end

  # Imprime un campo oculto
  def self.campo_oculto(variable, dato)
    "<input type='hidden' name='#{variable}' value='#{dato}'>"
  end

  # def fin_formulario():
  #     """Termina el formulario"""
  #     return '</form>'

  # def input_input(tipo, nombre, valor=''):
  #     """Imprime un campo tipo INPUT"""
  #     print('<input type="' + tipo + '" name="' + nombre + '" value="' + valor + '"></input>')

  # Imprime 2 celdas, una con texto y otra con un checkbox
  def self.input_check(texto, variable, valor)
    adicional = ''
    cadena = ''
    val = if valor.nil?
            0
          else
            valor.to_i
          end
    adicional = 'checked' if val.positive?
    cadena << "<div class='field'>"
    cadena << "<label class='checkbox'>"
    # cadena << "<div class='control'>"
    cadena << "<input type='checkbox' "
    cadena << "name='#{variable}' value='#{val}' #{adicional}>"
    cadena << " #{texto}</label>"
    # cadena << "</div>\n</div>\n"
    cadena << "</div>\n"
  end
  # def fila_alterna(i):
  #     """Genera colores alternos para filas de una tabla"""
  #     if (i % 2) == 0:
  #         print("<tr>")
  #     else:
  #         print("<tr class='odd'>")

  # def fila_lista():
  #     """Genera fila para listado de datos"""
  #     print("<tr class='fila_datos'>")

  # def imagen_menu(imag, enl, texto):
  #     """Imprime una celda con una imagen, enlace y texto"""
  #     print('<td align="center"><a href="' + enl + '"><img src="./img/' + imag +
  #           '" align="top" border="0"></a></br>' + texto + '</td>')
  #     # imag  + '" width="64" height="64" align="top" border="0"></a></br>' +

  # def duplicado(pag):
  #     """Genera html de error por existencia de duplicado"""
  #     texto = 'Ya existe un dato igual al que usted intenta agregar.'
  #     texto = texto + ' Verifique el dato e inténtelo nuevamente'
  #     nota(texto)
  #     print(button('Volver', pag))

  # def navegador(este_archivo, pagina_actual, total_paginas):
  #     """Imprime un navegador al pie de una tabla"""
  #     nav = ""
  #     union = "?"
  #     if "?" in este_archivo:
  #         union = "&"
  #     if not isinstance(pagina_actual, int):
  #         pagina_actual = int(pagina_actual)
  #     if not isinstance(total_paginas, int):
  #         total_paginas = int(total_paginas)
  #     for num in range(1, total_paginas + 1):
  #         if num == pagina_actual:
  #             nav += " " + str(pagina_actual) + " "
  #         else:
  #             nav += " <a href='" + este_archivo + union + "pagina="
  #             nav += str(num) + "'>" + str(num) + "</a> "
  #     # enlaces a primero - anterior - posterior - ultimo
  #     if pagina_actual > 1:
  #         pag = pagina_actual - 1
  #         prev = " <a href='" + este_archivo + union + "pagina="
  #         prev += str(pag) + "'>[<-]</a> "
  #         prim = " <a href='" + este_archivo + union + "pagina=1'>[<<]</a> "
  #     else:
  #         prev = " "
  #         prim = " "
  #     if pagina_actual < total_paginas:
  #         pag = pagina_actual + 1
  #         sig = " <a href='" + este_archivo + union + "pagina=" + str(pag) + "'>[->]</a> "
  #         ult = " <a href='" + este_archivo + union + "pagina="
  #         ult += str(total_paginas + 1) + "'>[>>]</a> "
  #     else:
  #         sig = " "
  #         ult = " "
  #     print("<center class='barra'>" + prim + prev + nav + sig + ult + "</center>")

  # def script_fecha():
  #     """Imprime en una pagina web un javascript para manejo de fechas"""
  #     texto = """Calendar.setup({
  #         inputField     :    'f_date_b',
  #         ifFormat       :    '%d/%m/%Y',
  #         showsTime      :    false,
  #         button         :    'f_trigger_b',
  #         step           :    1
  #         });"""
  #     return script(texto, "text/javascript")

  # def script_fecha2():
  #     """Genera segundo script de fecha"""
  #     texto2 = """Calendar.setup({
  #         inputField     :    'f_date_b2',
  #         ifFormat       :    '%d/%m/%Y',
  #         showsTime      :    false,
  #         button         :    'f_trigger_b2',
  #         step           :    1
  #         });"""
  #     return script(texto2, "text/javascript")

  # # ===============================================================================

  # def boton_confirmar(texto, leyenda, accion):
  #     """Pone un boton con un TEXTO que saca diálogo para confirmar"""
  #     action = "if(confirm(\"{0}\")) window.location=\"{1}\";".format(leyenda, accion)
  #     cadena = "<input type='button' value='" + texto + "' "
  #     cadena = cadena + "onClick='" + action + "' "
  #     cadena = cadena + "/>"
  #     print(cadena)

  # Pone una imagen de eliminar cliqueable, saca diálogo para confirmar
  def self.boton_eliminar(accion)
    cadena = "<a href='#' title='Eliminar registro'>"
    cadena << "<img src='/img/eliminar.png' width='24' height='24' border='0' "
    cadena << "onClick=\"if(confirm('¿Desea borrar este registro?')) "
    cadena << "window.location='" + accion
    cadena << "';" + '"' + "></a>\n"
  end

  # Pone un boton para acción con privilegio
  def self.boton_llave(accion)
    cadena = "<a href='#{accion}' title='Acción con privilegio'>"
    cadena + "<img src='/img/llave.png' width='24' height='24' border='0'></a>"
  end

  # pone un boton con una ACCION
  def boton_imprimir(accion)
    cadena = "<a href='" + accion + "' title='Imprimir'>"
    cadena << "<img src='./img/printer32.png' width='24' height='24' border='0'></a>"
  end

  # def boton_actualizar(accion):
  #     """pone un boton con una ACCION"""
  #     cadena = "<a href='" + accion + "' title='Actualizar'>"
  #     cadena += "<img src='./img/actualizar.png' width='24' height='24' border='0'></a>"
  #     return cadena



  # Pone una imagen de ver-detalle cliqueable
  def self.boton_detalles(accion)
    enlace(accion, img('/img/detalles.png', 24, 24, 0), 'Detalles')
  end

  # Pone una imagen de ver
  def self.boton_visto(accion)
    enlace(accion, img('/img/ver.png', 24, 24, 0), 'Visto')
  end

  # Pone una imagen de no-ver
  def self.boton_no_visto(accion)
    enlace(accion, img('/img/no_ver.png', 24, 24, 0), 'No visto')
  end

  # Pone una imagen de editar cliqueable
  def self.boton_editar(accion)
    enlace(accion, img('/img/editar.png', 24, 24, 0), 'Editar')
  end

  # Pone un boton para ver un gráfico
  def self.boton_grafica(accion)
    enlace(accion, img('/img/chart.png', 24, 24, 0), 'Gráfica')
  end

  # Boton con imagen de seleccion de persona
  def self.boton_seleccionar(accion)
    cadena = "<a href='#{accion}' title='Seleccionar'>"
    cadena << "<img src='/img/seleccionar.png' width='24' height='24' border='0'></a>"
  end

  # Boton cancelar
  def self.boton_cancelar(accion)
    cadena = "<a href='#' title='Cancelar'>"
    cadena << "<img src='/img/cancelar.png' width='24' height='24' border='0' "
    cadena << "onClick=\"if(confirm('¿Desea cancelar?')) "
    cadena << "window.location='" + accion
    cadena << "';" + '"' + "></a>\n"
  end

  # Boton con imagen de llamar x telefono
  def self.boton_llamar(accion)
    cadena = "<a href='#{accion}' title='Llamadas'>"
    cadena << "<img src='/img/telefono_chico.png' width='24' height='24' border='0'></a>"
  end

  def self.boton_ambulancia(accion)
    cadena = "<a href='#{accion}' title='Asignar viaje'>"
    cadena << "<img src='/img/ambulancia_chico.png' width='24' height='24' border='0'></a>"
  end

  # def fila_resaltada():
  #     """Fila sobreiluminada"""
  #     print("<tr class='fila_datos'>")

  # def fila_datos(texto, datos):
  #     """Imprime una hilera con 2 celdas: una de texto y otra de datos"""
  #     datos = str(datos)
  #     print(fila(celda(texto) + celda(datos)))

  # Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
  def self.input_texto(texto, campo, valor, ancho = 60)
    cadena = "<div class='field'>"
    cadena << "<label class='label'>#{texto}</label>"
    cadena << "<div class='control'>"
    cadena << "<input class='input' type='text' placeholder='#{texto}' name='#{campo}' "
    cadena << "value='#{valor}' id='#{campo}' size='#{ancho}'>"
    cadena << '</div></div>'
  end

  # def input_disabled(texto, campo, valor, ancho=60):
  #     """Imprime celda con texto y texto, muestra un campo no modificable"""
  #     print(fila(celda(texto + celda(text(campo, valor, ancho, disabled=True)))))

  # def input_label(texto1, texto2):
  #     """Imprime 2 celdas adyacentes en 1 fila ambas con texto"""
  #     print(fila(celda(texto1) + celda(texto2)))

  # Imprime una linea con una celda con texto y otra con un campo memo
  def self.input_memo(texto, campo, valor)
    valor = '' if valor.nil?
    cadena = "<div class='field'>"
    cadena << "<label class='label'>#{texto}</label>"
    cadena << "<div class='control'>"
    cadena << "<textarea class='textarea' type='text' placeholder='#{texto}' name='#{campo}' "
    cadena << "id='#{campo}' rows='10' cols='100'>#{valor}</textarea>"
    cadena << '</div></div>'
  end
  # def leer_cookie():
  #     """Lee una cookie presente en la sesion"""
  #     coo = Cookie.SimpleCookie(os.environ.get("HTTP_COOKIE", ""))
  #     return coo

  # def linea_moneda(texto):
  #     """Imprime una celda con un valor monetario adentro"""
  #     print(celda(funciones.moneda(texto), "right"))

  # def celda_moneda(texto):
  #     """Imprime una celda con un valor monetario adentro"""
  #     print(celda(funciones.moneda(texto), "right"))

  # Imprime una tabla con texto pequeno
  def self.nota(texto)
    "<div class='notification'>#{texto}</div>"
  end

  # Imprime un texto blanco
  def self.texto_barra(texto)
    "<div class='notification'>#{texto}</div>"
  end

  def self.pie(txt_enlace)
    # PIE de pagina
    cadena = "<footer class='footer'>\n"
    cadena << "<div class='content has-text-centered'>\n"
    cadena << boton('Volver', txt_enlace)
    cadena << "</div>\n</footer>\n"
    cadena << fin_pagina
  end

  # retroceso a pagina anterior
  def self.retroceso(referencia)
    "<a class='button is-link' href='#{referencia}'>Volver</a>"
  end

  # # def input_fechahora(texto, campo_fecha, campo_hora, valor_fecha, valor_hora)
  # #   valor_fecha = '' if valor_fecha.nil?
  # #   valor_hora = '' if valor_hora.nil?
  #    puts <tr><td>#{texto}</td>
  # puts <td>Fecha:<input id='#{campo_fecha}' type='date' value='#{valor_fecha}
  # name='#{campo_fecha}'>"
  # puts " - Hora:<input id='#{campo_hora}' type='time' value='#{valor_hora}'
  # name='#{campo_hora}'></td></tr>"
  # # end

  # # def input_decimal(texto, campo, valor)
  # #   valor = '' if valor.nil?
  # #   puts "<tr><td>#{texto}</td>"
  # #   puts "<td><input id='#{campo}' type='number' step='0.01' value='#{valor}' name='#{campo}'>"
  # #   puts '</td></tr>'
  # # end

  # #===========================================================================
  # # TAGS HTML
  # # ===========================================================================

  # Tag HTML
  def self.enlace(enl, texto, titulo = '')
    cadena = "<a href='#{enl}'"
    cadena << " title='#{titulo}'" unless titulo == ''
    cadena << ">#{texto}</a>"
  end
  # def negrita(texto):
  #     """Tag html"""
  #     cadena = "<b>{0}</b>"
  #     return cadena.format(texto)

  # def body(contenido):
  #     """HTML TAG"""
  #     cadena = "<body>" + contenido + "</body>"
  #     return cadena

  def self.boton(texto, referencia, clase = 'link')
    # Devuelve un boton - texto con estilo CSS
    "<a class='button is-#{clase}' href='#{referencia}'>#{texto}</a>"
  end
  # def button(texto, action, style='link'):
  #     """boton con acción"""
  #     # cadena = "<input type='button' value='" + texto + "' "
  #     # cadena = cadena + "onClick=\"parent.location='" + action + "'\" "
  #     # if style != "":
  #     #     cadena = cadena + " style='" + style + "'"
  #     # cadena = cadena + "/>"
  #     cadena = "<a class='button is-%s' href='%s'> " % (style, action)
  #     cadena += texto
  #     cadena += "</a>"
  #     return cadena

  # def caption(texto):
  #     """Tag html"""
  #     cadena = "<caption>{0}</caption>"
  #     return cadena.format(texto)

  # def div(texto, clase=""):
  #     """tag html"""
  #     cadena = "<div "
  #     if clase != "":
  #         cadena = cadena + "class='" + clase + "'>"
  #     else:
  #         cadena = cadena + ">"
  #     return cadena + texto + "</div>"

  # diferentes encabezados
  def self.encabezado(num = 1, texto)
    clases = ['title', 'title is-4', 'title is-5', 'title is-6']
    clase = clases[num - 1]
    "<h#{num} class='#{clase}'>#{texto}</h#{num}>"
  end

  # def head(contenido):
  #     """Encabezado de pagina web"""
  #     return '<head>' + contenido + '</head>'

  # def hidden(campo, valor):
  #     """Tag Html"""
  #     return "<input type='hidden' name='%s' value='%s'>" % (campo, valor)

  # def linea_horizontal():
  #     """Tag html"""
  #     return '<hr />'

  # Tag HTML
  def img(src, width = 0, height = 0, border = 0)
    cadena = "<img src='#{src}' "
    cadena << " width='#{width}' " unless width.zero?
    cadena << " height='#{height}' " unless height.zero?
    cadena << " border='#{border}'>"
  end

  # def linea(texto):
  #     """Tag html"""
  #     cadena = "<li>{0}</li>"
  #     return cadena.format(texto)

  # def parrafo(texto):
  #     """Tag html"""
  #     cadena = "<p>{0}</p>"
  #     return cadena.format(texto)

  # def script(texto, typ="", src=""):
  #     """Tag html"""
  #     if typ != "":
  #         typ = "type='" + str(typ) + "'"
  #     if src != "":
  #         src = "src='" + str(src) + "'"
  #     return "<script " + typ + " " + src + ">\n" + texto + "\n</script>"

  # def span(contenido, clase=''):
  #     """Html tag"""
  #     cadena = "<span "
  #     if clase != '':
  #         cadena = cadena + " class='" + clase + "'"
  #     cadena = cadena + ">{0}</span>"
  #     return cadena.format(contenido)

  # def submit(valor="Enviar", style=""):
  #     """Tag HTML"""
  #     cadena = "<input type='submit' value='" + valor + "'"
  #     if style != "":
  #         cadena = cadena + "style='" + style + "'"
  #     cadena = cadena + ">"
  #     return cadena

  # def table(content, width='', clase=''):
  #     """Tag HTML"""
  #     cadena = "<table"
  #     if width != '':
  #         cadena = cadena + " width='" + width + "' "
  #     if clase != '':
  #         cadena = cadena + " class='" + clase + "'"
  #     cadena = cadena + ">" + content + "</table>"
  #     return cadena

  # Devuelve una celda en una tabla
  def self.celda(texto = '', align = 'left', rowspan = 1, colspan = 1)
    "<td align='#{align}' rowspan='#{rowspan}' colspan='#{colspan}'>#{texto}</td>"
  end
  # def text(field, value, size=40, disabled=False):
  #     """Html tag"""
  #     dis = ""
  #     if disabled:
  #         dis = "disabled"
  #     cadena = "<input {0} type='text' name='{1}' value='{2}' size='{3}'/>"
  #     return cadena.format(dis, field, value, size)

  # def tfoot(texto):
  #     """Tag html"""
  #     cadena = "<tfoot>{0}</tfoot>"
  #     return cadena.format(texto)

  # Tag html"""
  def self.celda_encabezado(texto)
    "<th>#{texto}</th>"
  end

  # def title(texto):
  #     """Tag html"""
  #     cadena = "<title>{0}</title>"
  #     return cadena.format(texto)

  # Tag HTML
  def fila(texto = '')
    "<tr>#{texto}</tr>"
  end
  # def lista(texto):
  #     """Tag html"""
  #     cadena = "<ul>{0}</ul>"
  #     return cadena.format(texto)

  # def limpiar_html(texto):
  #     # limpio = re.compile('<.*?>')
  #     mensaje = re.sub("<.*?>", '', texto)
  #     mensaje = mensaje.replace("&nbsp;", "")
  #     mensaje = mensaje.replace("&aacute;", "á")
  #     mensaje = mensaje.replace("&eacute;", "é")
  #     mensaje = mensaje.replace("&iacute;", "í")
  #     mensaje = mensaje.replace("&oacute;", "ó")
  #     mensaje = mensaje.replace("&aacute;", "ú")
  #     mensaje = mensaje.replace("&ntilde;", "ñ")
  #     return mensaje
end
