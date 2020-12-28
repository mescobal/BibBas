# frozen_string_literal: true

# Version 0.11.07
# Ver 0.12: campo_combo
# Conjunto de rutinas para generar codigo html

require_relative './funciones'

IMG_LOGO = 'logo.png'

# genera HTML
module Htm
  # Formulario ================================================
  def self.etiqueta_campo(texto)
    cadena = +"<div class='field-label'>"
    cadena << "<label class='label'>#{texto}</label></div>"
  end

  def self.campo(texto, tipo = '')
    str_tipo = case tipo
               when 'H'
                 'field is-horizontal'
               when 'G'
                 'field is-grouped'
               else
                 'field'
               end
    "<div class='#{str_tipo}'>#{texto}</div>\n"
  end

  def self.cuerpo_campo(texto)
    "<div class='field-body'>#{texto}</div>\n"
  end

  def self.control(texto)
    "<div class='control'>#{texto}</div>\n"
  end

  def self.entrada(tipo, texto, campo_bdd, valor)
    cadena = +"<input class='input' type='#{tipo}' placeholder='#{texto}' "
    cadena << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>"
  end

  # Entrada de clave
  def self.input_password(texto, campo_bdd, valor)
    cadena = etiqueta_campo(texto)
    cadena << cuerpo_campo(control(entrada('password', texto, campo_bdd, valor)))
    campo(cadena, 'H')
  end

  # Imprime boton de enviar formulario con texto = Aceptar
  def self.botones(url)
    cadena = etiqueta_campo('')
    cadena << control("<button type='submit' class='button is-link'>Aceptar</button>")
    cadena << "<div class='control'>\n"
    cadena << "<button type='reset' class='button is-light'"
    cadena << " onClick=\"window.location.href='#{url}'\">Cancelar</button>\n</div>\n"
    campo(cadena, 'G')
  end

  # Combo box con listado como opciones y texto x defecto
  def self.combo(listado, variable, defecto = '')
    cadena = +"<div class ='select'><select name='#{variable}' id='#{variable}'>\n"
    cadena << "<option value='' selected='selected'>Sin datos</option>\n" if defecto == ''
    listado.each do |item|
      cadena << if item == defecto
                  "<option selected='selected' value='#{item}'>#{item}</option>\n"
                else
                  "<option value='#{item}'>#{item}</option>\n"
                end
    end
    cadena << '</select></div>'
  end

  # Imprime boton de enviar formulario con texto = Aceptar
  def self.botones_formulario(texto_aceptar = 'Aceptar', url_cancelar = '')
    cadena = etiqueta_campo('')
    cadena << "<div class='control'>\n"
    cadena << "<button type='submit' class='button is-link'>#{texto_aceptar}</button>\n"
    cadena << "</div>\n"
    cadena << "<div class='control'>\n"
    cadena << "<button type='reset' class='button is-light'"
    cadena << " onClick=\"window.location.href='#{url_cancelar}'\">Cancelar</button>\n"
    cadena << "</div>\n"
    campo(cadena, 'G')
  end

  # Combo box con opciones en un campo
  def self.campo_combo(texto, listado, variable, defecto = '')
    cadena = etiqueta_campo(texto)
    cadena += cuerpo_campo(control(combo(listado, variable, defecto)))
    campo(cadena, 'H')
  end

  # Tags de finalizacion de una pagina."""
  def self.fin_pagina
    '</div></div></body></html>'
  end

  # Imprime tags de finalizacion de una tabla
  def self.fin_tabla
    '</tbody></table>'
  end

  # Pone un formulario de edicion, encabezado
  def self.form_edicion(texto, accion)
    cadena = +"<h2 class='subtitle'>#{texto}</h2>"
    cadena << "<form action='#{accion}' method='post'>"
  end

  # Finalización de form de edición
  def self.form_edicion_fin
    '</form>'
  end

  # Imprime encabezado de pagina web SIN cookie.
  def inicio
    cadena = 'Content-Type: text/html; charset=utf-8\n\n'
    cadena << '<!DOCTYPE html>'
    cadena << "<html lang='es'>"
  end

  # Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
  def self.input_texto(texto, campo_bdd, valor)
    cadena = etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(entrada('text', texto, campo_bdd, valor))))
    campo(cadena, 'H')
  end

  # Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
  def self.input_texto_1(texto, campo_bdd, valor)
    cadena = "<div class='field is-horizontal is-grouped'>"
    cadena << etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(entrada('text', texto, campo_bdd, valor))))
  end

  # Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
  def input_texto_2(texto, campo_bdd, valor)
    cadena = etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(entrada('text', texto, campo_bdd, valor))))
    cadena << '</div>'
  end

  # Imprime una linea con una celda con texto y otra con un campo memo
  def self.input_memo(texto, campo_bdd, valor)
    valor = '' if valor.nil?
    cadena = etiqueta_campo(texto)
    ctrl = "<textarea class='textarea' name='#{campo_bdd}' placeholder='#{texto}'>#{valor}</textarea>"
    cadena << cuerpo_campo(campo(control(ctrl)))
    campo(cadena, 'H')
  end

  # Linea con celda con texto y otra con combobox
  def self.input_combo(texto, campo_bdd, resultado, campos, valor)
    cad1 = etiqueta_campo(texto)
    cadena = +"<div class='control'>\n"
    cadena << "<div class ='select'>\n<select name='#{campo_bdd}' id='#{campo_bdd}'>\n"
    cadena << "<option value='' selected='selected'>Sin datos</option>\n" if valor == ''
    resultado.each do |fil|
      cadena << "<option value='#{fil[campos[0]]}' "
      cadena << "selected='selected'" if fil[campos[0]].to_s == valor.to_s
      cadena << ">#{fil[campos[1]]}</option>\n"
    end
    cadena << "</select></div>\n</div>\n"
    cad1 << cuerpo_campo(campo(cadena))
    campo(cad1, 'H')
  end

  # Linea con celda con texto y otra con combobox. para poner lado a lado
  def self.input_combo_1(texto, campo_bdd, resultado, campos, valor)
    cadena = +"<div class='field is-horizontal'>"
    cadena << etiqueta_campo(texto)
    cadena << "<div class='field-body'>"
    cadena << "<div class='field is-expanded'>\n"
    cadena << "<p class='control is-expanded'>\n"
    cadena << "<div class ='select is-fullwidth'>\n<select name='#{campo_bdd}' id='#{campo_bdd}'>\n"
    cadena << "<option value='' selected='selected'>Sin datos</option>\n" if valor == ''
    resultado.each do |fil|
      cadena << "<option value='#{fil[campos[0]]}' "
      cadena << "selected='selected'" if fil[campos[0]].to_s == valor.to_s
      cadena << ">#{fil[campos[1]]}</option>\n"
    end
    cadena << "</select></div>\n"
    cadena << "</p>\n</div>\n</div>\n"
  end

  # Linea con celda con texto y otra con combobox. para poner lado a lado
  def self.input_combo_2(texto, campo_bdd, resultado, campos, valor)
    cadena = +"<div class='field-label is-normal'><label class='label'>#{texto}</label></div>"
    cadena << "<div class='field-body'>\n"
    cadena << "<div class='field is-expanded'>\n"
    cadena << "<p class='control is-expanded'>\n"
    cadena << "<div class ='select is-fullwidth'>\n<select name='#{campo_bdd}' id='#{campo_bdd}'>\n"
    cadena << "<option value='' selected='selected'>Sin datos</option>\n" if valor == ''
    resultado.each do |fil|
      cadena << "<option value='#{fil[campos[0]]}' "
      cadena << "selected='selected'" if fil[campos[0]].to_s == valor.to_s
      cadena << ">#{fil[campos[1]]}</option>\n"
    end
    cadena << "</select></div>\n"
    cadena << "</p>\n</div></div>\n"
    cadena << "</div>\n"
  end

  # Crea celdas contiguas con texto y campo de texto
  def self.input_fecha(texto, campo_bdd, valor)
    cadena = etiqueta_campo(texto)
    entrada = +"<input class='input' type='date' placeholder='dd/mm/aaaa' "
    entrada << "min='1920-01-01' max='2120-12-31' "
    entrada << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>\n"
    cadena << cuerpo_campo(campo(control(entrada)))
    campo(cadena, 'H')
  end

  # Crea celdas contiguas con texto y campo de texto
  def self.input_fecha_1(texto, campo_bdd, valor)
    cadena = +"<div class='field is-horizontal'>"
    cadena << etiqueta_campo(texto)
    cadena << "<div class='field-body'>"
    cadena << "<div class='field is-expanded'>\n"
    cadena << "<p class='control is-expanded'>\n"
    cadena << "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    cadena << "min='1920-01-01' max='2120-12-31' "
    cadena << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>\n"
    cadena << "</p>\n</div>\n</div>\n"
  end

  def self.input_fecha_2(texto, campo_bdd, valor)
    cadena = +"<div class='field-label is-normal'><label class='label'>#{texto}</label></div>"
    cadena << "<div class='field-body'>\n"
    cadena << "<div class='field is-expanded'>\n"
    cadena << "<p class='control is-expanded'>\n"
    cadena << "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    cadena << "min='1920-01-01' max='2120-12-31' "
    cadena << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>\n"
    cadena << "</p>\n</div></div>\n"
    cadena << "</div>\n"
  end

  # def input_hora(texto, campo_bdd, valor)
  #     cadena = etiqueta_campo(texto)
  #     cadena << cuerpo_campo(campo(control(entrada("time", texto, campo_bdd, valor))))
  #     return campo(cadena, "H")
  # end

  # Imprime un campo de ingreso de valor numerico
  def self.input_numero(texto, campo_bdd, valor, decimales = 2)
    valor = '0' if (valor.is_a? String) && valor.empty?
    num = numero(valor, decimales)
    cadena = etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(entrada('number', texto, campo_bdd, num))))
    campo(cadena, 'H')
  end

  # Imprime un campo de ingreso de valor numerico
  def self.input_entero(texto, campo_bdd, valor, minimo = nil, maximo = nil)
    tex = texto.to_s
    valor = '0' if (valor.is_a? String) && valor.empty?
    numero = numero(valor)
    cdn2 = etiqueta_campo(tex)
    cadena = +"<div class='control'>"
    cadena << "<input class='input' type='number' "
    unless minimo.nil?
      minimo = minimo.to_i.to_s
      cadena << "min=#{minimo} "
    end
    unless maximo.nil?
      maximo = maximo.to_i.to_s
      cadena << "max=#{maximo} "
    end
    cadena << "name='#{campo_bdd}' value='#{numero}' id='#{campo_bdd}' step='1'>"
    cadena << '</div>'
    cdn3 = cdn2 + cuerpo_campo(cadena)
    campo(cdn3, 'H')
  end

  # Imprime 2 celdas, una con texto y otra con un checkbox
  def self.input_check(texto, variable, valor)
    cadena = etiqueta_campo(texto)
    adicional = valor.to_i.positive? ? 'checked' : ''
    chk = "<INPUT TYPE='checkbox' NAME='#{variable}' VALUE='1' #{adicional}>"
    cadena << cuerpo_campo(campo(control(chk)))
    campo(cadena, 'H')
  end

  # Checkbox en 2 columnas
  def self.input_check_1(texto, variable, valor)
    cadena = +"<div class='field is-horizontal is-grouped'>"
    cadena << cuerpo_campo(input_check(texto, variable, valor))
  end

  # Checkbox en 2 columnas 2
  def self.input_check_2(texto, variable, valor)
    # cadena = +"<div class='field is-horizontal is-grouped'>"
    cadena = +''
    cadena << cuerpo_campo(input_check(texto, variable, valor))
    cadena << '</div>'
  end

  # arreglo es un DICCIONARIO con texto y valor del item
  def self.input_radio(texto, variable, arreglo, valor)
    radio = +''
    arreglo.each do |llave, dato|
      radio << "<label class='radio'>"
      chkd = dato == valor ? 'checked' : ''
      radio << "<input type='radio' name='#{variable}' value='#{dato}' #{chkd}> "
      radio << llave.to_s
      radio << ' </label>   '
    end
    cadena = etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(radio)))
    campo(cadena, 'H')
  end

  # Imprime una linea con 2 celdas: una con un texto y otra con un dato
  def self.linea_dato(texto, dato)
    "<tr><td>#{texto}</td><td>#{dato}</td></tr>"
  end
  #
  # # Imprime una celda con un número formateado con 2 decimales
  # def linea_numero(texto, decimales=2)
  #   celda(funciones.numero(texto, decimales), 'right')
  # end
  #
  # # Impide que funcione la tecla enter en una pagina
  # def script_noenter
  #     return """<script type='text/javascript'>
  #     function stopRKey(evt) {
  #     var evt = (evt) ? evt : ((event) ? event : null);
  #     var node = (evt.target) ? evt.target : ((evt.srcElement) ? evt.srcElement : null);
  #     if ((evt.keyCode == 13) && (node.type=='text'))  {return false;}
  #     }
  #     document.onkeypress = stopRKey;
  #     </script>';"""
  # end
  #
  # # Combo box para seleccionar año - 10 antes del actual"""
  # def seleccionar_ano(defecto='')
  #     ano_actual = funciones.ano_actual
  #     if defecto == ''
  #         seleccionado = ano_actual.to_s
  #     else
  #         seleccionado = defecto.to_s
  #     end
  #     cadena = "<select name='ano'>"
  #     for contador in range(ano_actual, ano_actual-10, -1)
  #         if contador.to_s == seleccionado
  #             cadena << "<option selected value='#{contador}'>#{contador}</option>"
  #         else
  #             cadena "<option value='#{contador}'>#{contador}</option>"
  #         end
  #     end
  #     cadena << '</select>'
  # end
  # ========================================
  # Con devolución de cadena

  # Imprime un encabezado con nivel
  def self.encabezado(nivel, texto)
    niveles = ['', ' is-4', ' is-5', ' is-6']
    cadena = +"<h#{nivel} class='title#{niveles[nivel - 1]}"
    cadena << "'>#{texto}</h#{nivel}>"
  end

  # Imprime encabezado con logo y boton de retorno
  def self.encabezado_completo(titulo, referencia)
    cadena = +"<!DOCTYPE html>\n"
    cadena << "<html lang='es'>"
    cadena << "<head>\n"
    cadena << "<meta charset='utf-8' />\n"
    cadena << "<title>#{titulo}</title>\n"
    cadena << "<link type='text/css' href='/css/bulma.css' rel='stylesheet' />"
    cadena << "</head>\n"
    cadena << "<body>\n"
    cadena << "<div class='section'><div class='container'>\n"
    cadena << "<div class='box'>\n"
    cadena << "<img src='/img/#{IMG_LOGO}' align='right'>"
    cadena << encabezado(1, titulo)
    cadena << retroceso(referencia)
    cadena << "</div>\n"
  end

  # Carga script
  # def load_script(tipo="text/javascript", src='', charset="utf-8")
  #   cadena = '<script type="{0}" src="{1}" charset="{2}"></script>'
  #   return cadena.format(tipo, src, charset)
  # end
  #
  # ========================================
  # Conversión de tags HTML
  # ========================================
  # BOTONES ===========================

  # Pone un boton titulado TITULO con ICONO y ACCION
  def self.boton_accion(titulo, accion, icono)
    cadena = +"<a href='#{accion}' title='#{titulo}'>"
    cadena << "<img src='/img/#{icono}.png' width='24' height='24' border='0'></a>"
  end

  # Pone un boton con imagen ambulancia
  def boton_ambulancia(accion)
    cadena = "<a href='#{accion}' title='Asignar viaje'>"
    cadena << "<img src='/img/ambulancia_chico.png' width='24' height='24' border='0'></a>"
  end

  # Boton cancelar
  def boton_cancelar(accion)
    cadena = "<a href='#' title='Cancelar'>"
    cadena << "<img src='/img/cancelar.png' width='24' height='24' border='0' "
    cadena << "onClick=\"if(confirm('¿Desea cancelar?')) "
    cadena << "window.location='#{accion}"
    cadena << "';\"></a>\n"
  end

  # Pone una imagen de eliminar cliqueable, saca diálogo para confirmar
  def self.boton_eliminar(accion)
    cadena = +"<a href='#' title='Eliminar registro'>"
    cadena << "<img src='/img/eliminar.png' width='24' height='24' border='0' "
    cadena << "onClick=\"if(confirm('¿Desea borrar este registro?'))"
    cadena << "window.location='#{accion}"
    cadena << "';\"></a>\n"
  end

  # Pone un boton para acción con privilegio
  def boton_llave(accion)
    cadena = "<a href='#{accion}' title='Acción con privilegio'>"
    cadena << "<img src='/img/llave.png' width='24' height='24' border='0'></a>"
  end

  # pone un boton con una ACCION
  def boton_imprimir(accion)
    cadena = "<a href='#{accion}' title='Imprimir'>"
    cadena << "<img src='/img/printer32.png' width='24' height='24' border='0'></a>"
  end

  # pone un boton con una ACCION
  def boton_actualizar(accion)
    cadena = "<a href='#{accion}' title='Actualizar'>"
    cadena << "<img src='/img/actualizar.png' width='24' height='24' border='0'></a>"
  end

  # Pone un boton para ver un gráfico
  def self.boton_grafica(accion)
    enlace(accion, img('/img/chart.png', 24, 24, 0), 'Gráfica')
  end

  # ========================================================

  # Pone una celda del menu
  def self.celda_menu(texto, enl, icono, ayuda = '')
    # 1
    cadena = +"<div class='tile is-child is-info box'>\n"
    cadena << "<a href='#{enl}'>"
    cadena << "<p class='title' align='center'>#{texto}</p></a>\n"
    cadena << "<a href='#{enl}'>"
    cadena << "<div class='level'><div class='level-item has-text-centered'>\n"
    cadena << "<figure class='image is-96x96'>\n"
    cadena << "<img src='/img/#{icono}'>\n"
    cadena << "</figure>\n"
    cadena << "</div>\n</div>\n"
    cadena << "</a>\n"
    # 2
    cadena << "<div class='content'>\n"
    cadena << ayuda
    # cierra 2
    cadena << "</div>\n"
    # Cierra 1
    cadena << '</div>'
  end

  # Pone imagen con caracteristicas predeterminadas
  def imagen(imag)
    "<img src='/img/#{imag}' width='64' height='64' border='0'>"
  end

  # A partir de un array arma el encabezado de una tabla
  def self.encabezado_tabla(arr)
    cadena = +"<table class='table is-hoverable'><thead><tr>\n"
    arr.each do |lin|
      cadena << celda_encabezado(lin)
    end
    cadena << "</tr>\n</thead>\n<tbody>\n"
  end

  # Imprime un campo oculto
  def self.campo_oculto(variable, dato)
    "<input type='hidden' name='#{variable}' value='#{dato}'>"
  end

  # Termina el formulario
  def self.fin_formulario
    '</form>'
  end
  # Imprime un navegador al pie de una tabla
  # def navegador(este_archivo, pagina_actual, total_paginas)
  #     nav = ''
  #     union = '?'
  #     union = '&' if este_archivo.include?("?")
  #     pagina_actual = pagina_actual.to_i unless pagina_actual.is_a? Integer
  #     total_paginas = total_paginas.to_i unless total_paginas.is_a? Integer
  #     (1..total_paginas + 1).each do |num|
  #         if num == pagina_actual
  #             nav << " #{pagina_actual} "
  #         else
  #             nav << " <a href='#{este_archivo}#{union}pagina="
  #             nav << "#{num}'>#{num}</a> "
  #         end
  #     end
  #     # enlaces a primero - anterior - posterior - ultimo
  #     if pagina_actual > 1
  #         pag = pagina_actual - 1
  #         prev = " <a href='" + este_archivo + union + "pagina="
  #         prev << str(pag) + "'>[<-]</a> "
  #         prim = " <a href='" + este_archivo + union + "pagina=1'>[<<]</a> "
  #     else
  #         prev = " "
  #         prim = " "
  #     end
  #     if pagina_actual < total_paginas
  #         pag = pagina_actual + 1
  #         sig = " <a href='" + este_archivo + union + "pagina=" + str(pag) + "'>[->]</a> "
  #         ult = " <a href='" + este_archivo + union + "pagina="
  #         ult << "#{total_paginas + 1}'>[>>]</a> "
  #     else
  #         sig = ' '
  #         ult = ' '
  #     end
  #     print("<center class='barra'>" + prim + prev + nav + sig + ult + "</center>")
  # end
  # ===============================================================================

  # Pone una imagen de eliminar cliqueable
  def self.boton_detalles(accion)
    enlace(accion, img('/img/detalles.png', 24, 24, 0), 'Detalles')
  end

  # Pone una imagen de eliminar cliqueable
  def boton_visto(accion)
    enlace(accion, img('/img/ver.png', 24, 24, 0), 'Visto')
  end

  # Pone una imagen de eliminar cliqueable
  def boton_no_visto(accion)
    enlace(accion, img('/img/no_ver.png', 24, 24, 0), 'No visto')
  end

  # Pone una imagen de eliminar cliqueable
  def self.boton_editar(accion)
    enlace(accion, img('/img/editar.png', 24, 24, 0), 'Editar')
  end

  # Imprime una celda con un valor monetario adentro
  def celda_moneda(texto)
    celda(funciones.moneda(texto), 'right')
  end

  # Imprime una tabla con texto pequeno
  def self.nota(texto)
    table(fila(celda(span(texto, 'nota'))))
  end

  # Imprime un texto blanco
  def self.texto_barra(texto)
    "<div class='texto_barra'>#{texto}</div>"
  end

  # Boton con imagen de seleccion de persona
  def boton_seleccionar(accion)
    cadena = "<a href='#{accion}' title='Seleccionar'>"
    cadena << "<img src='/img/seleccionar.png' width='24' height='24' border='0'></a>"
  end

  # Boton con imagen de llamar x telefono
  def self.boton_llamar(accion)
    cadena = +"<a href='#{accion}' title='Llamadas'>"
    cadena << "<img src='/img/telefono_chico.png' width='24' height='24' border='0'></a>"
  end

  # PIE de pagina
  def self.pie(txt_enlace)
    cadena = +"<footer class='footer'>\n"
    cadena << "<div class='content has-text-centered'>\n"
    cadena << boton('Volver', txt_enlace)
    cadena << "</div>\n</footer>\n"
    cadena << fin_pagina
  end

  # Imprime un boton de volver
  def self.retroceso(referencia)
    # cadena = "<a class='button is-link' style='float: right' href='"
    "<a class='button is-link' href='#{referencia}'>Volver</a>"
  end

  # def input_decimal(texto, campo, valor)
  #   valor = '' if valor.nil?
  #   puts "<tr><td>#{texto}</td>"
  #   puts "<td><input id='#{campo}' type='number' step='0.01' value='#{valor}' name='#{campo}'>"
  #   puts '</td></tr>'
  # end
  # ===========================================================================
  # TAGS HTML
  # ===========================================================================

  # Tag HTML
  def self.enlace(enl, texto, titulo = '')
    if titulo.empty?
      "<a href='#{enl}'>#{texto}</a>"
    else
      "<a href='#{enl}' title='#{titulo}'>#{texto}</a>"
    end
  end

  # Devuelve un boton - texto con estilo CSS
  def self.boton(texto, referencia, clase = 'link')
    "<a class='button is-#{clase}' href='#{referencia}'>#{texto}</a>"
  end

  # boton con acción
  def button(texto, action, style = 'link')
    "<a class='button is-#{style}' href='#{action}'>#{texto}</a>"
  end

  # Tag html
  def self.img(src, width = 0, height = 0, border = 0)
    cadena = +"<img src='#{src}' "
    cadena << " width='#{width}' " if width != 0
    cadena << " height='#{height}' " if height != 0
    cadena << " border='#{border}'>"
  end

  # Tag html
  def self.label(texto)
    "<label class='label'>#{texto}</label>"
  end

  # Tag html
  def script(texto, typ = '', src = '')
    typ = "type='#{typ}'" if typ != ''
    src = "src='#{src}'" if src != ''
    "<script #{typ} #{src}>\n#{texto}\n</script>"
  end

  # Html tag
  def self.span(contenido, clase = '')
    cadena = +'<span '
    cadena << " class='#{clase}'" if clase != ''
    cadena << ">#{contenido}</span>"
  end

  # Tag HTML
  def self.table(content, width = '', clase = '')
    cadena = +'<table'
    cadena << " width='#{width}' " if width != ''
    cadena << " class='#{clase}'" if clase != ''
    cadena << ">#{content}</table>"
  end

  # Devuelve una celda en una tabla
  def self.celda(texto = '', align = 'left', rowspan = 1, colspan = 1)
    "<td align='#{align}' rowspan='#{rowspan}' colspan='#{colspan}'>#{texto}</td>"
  end

  # Tag html
  def self.celda_encabezado(texto)
    "<th>#{texto}</th>"
  end

  # Tag html
  def self.fila(texto = '')
    "<tr>#{texto}</tr>"
  end

  # limpia tags html de un texto
  # def limpiar_html(texto)
  #   # limpio = re.compile('<.*?>')
  #   mensaje = re.sub("<.*?>", '', texto)
  #   mensaje = mensaje.replace("&nbsp;", "")
  #   mensaje = mensaje.replace("&aacute;", "á")
  #   mensaje = mensaje.replace("&eacute;", "é")
  #   mensaje = mensaje.replace("&iacute;", "í")
  #   mensaje = mensaje.replace("&oacute;", "ó")
  #   mensaje = mensaje.replace("&aacute;", "ú")
  #   mensaje = mensaje.replace("&ntilde;", "ñ")
  # end

  def self.boton_play(accion)
    enlace(accion, img('/img/play.png', 24, 24, 0), 'No visto')
  end

  def self.boton_stop(accion)
    enlace(accion, img('/img/stop.png', 24, 24, 0), 'No visto')
  end
end
