# frozen_string_literal: true

# Ver 1.09: inicio
# Ver 1.10: generar menu ahora funciona con texto para poder cambiar orden
# Ver 1.12: IMPORTANTE: arreglo combo box 1 y 2 para valores nulos

require 'yaml'
require_relative './funciones'
require_relative './htm'

# Librería para renderizar controles BULMA HTML
module Bulma
  # Primer orden
  # boton con acción
  def self.boton(texto, action, style = 'link')
    "<a class='button is-#{style}' href='#{action}'>#{texto}</a>"
  end

  # Pone un boton titulado TITULO con ICONO y ACCION
  def self.boton_accion(titulo, accion, icono)
    Htm.enlace(accion, faicon(icono), titulo)
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
    Htm.div(texto, str_tipo)
  end

  # Boton cancelar
  def self.boton_cancelar(accion)
    cadena = +''
    cadena << "<a href='#' title='Cancelar'><span class='icon'><i class='fas fa-window-close'"
    cadena << " onClick=\"if(confirm('¿Desea cancelar?')) "
    cadena << "window.location='#{accion}"
    cadena << "';\"></i></span></a>"
  end

  def self.control(texto)
    Htm.div(texto, 'control')
  end

  def self.cuerpo_campo(texto)
    Htm.div(texto, 'field-body')
  end

  def self.faicon(icono, color = 'grey')
    Htm.span("<i class='#{icono}'></i>", "icon has-text-#{color}")
  end

  # Imprime un boton de volver
  def self.boton_cerrar(retorno)
    cadena = +"<a class='button is-light is-small' href='#{retorno}'>"
    cadena2 = "<i class='fas fa-window-close'></i>"
    cadena << Htm.span(cadena2, 'icon is-small') << Htm.span('Cerrar') << '</a>'
    Htm.div(cadena, 'buttons is-right')
  end

  # Segundo orden
  # Pone una imagen de eliminar cliqueable
  def self.boton_detalles(accion)
    boton_accion('Detalles', accion, 'fas fa-info')
  end

  # Pone una imagen de eliminar cliqueable
  def self.boton_editar(accion)
    boton_accion('Editar', accion, 'fas fa-edit')
  end

  # Pone una imagen de eliminar cliqueable, saca diálogo para confirmar
  def self.boton_eliminar(accion)
    cadena = +''
    cadena << "<a href='#' title='Eliminar'>"
    cadena2 = +"<i class='fas fa-trash-alt'"
    cadena2 << " onClick=\"if(confirm('¿Desea eliminar este dato?')) "
    cadena2 << "window.location='#{accion}';\"></i>"
    # div(span(cadena2, 'icon has-text-danger'), 'icon-text')
    # cadena << Htm.span(cadena2, 'icon') << '</a>'
    cadena << Htm.span(cadena2, 'icon has-text-danger') << '</a>'
  end

  # Pone un boton para ver un gráfico
  def self.boton_grafica(accion)
    boton_accion('Gráfica', accion, 'fas fa-chart-line')
  end

  # Boton con imagen de llamar x telefono
  def self.boton_llamar(accion)
    boton_accion('Llamada', accion, 'fas fa-phone')
  end

  def self.boton_seleccionar(accion)
    boton_accion('Seleccionar', accion, 'fas fa-hand-pointer')
  end

  # Imprime boton de enviar formulario con texto = Aceptar
  def self.botones(url)
    cadena = +''
    cadena << etiqueta_campo('')
    cadena << control("<button type='submit' class='button is-link'>Aceptar</button>")
    cadena2 = +"<button type='reset' class='button is-light'"
    cadena2 << " onClick=\"window.location.href='#{url}'\">Cancelar</button>\n"
    cadena << Htm.div(cadena2, 'control')
    campo(cadena, 'G')
  end

  # Imprime boton de enviar formulario con texto = Aceptar
  def self.botones_formulario(texto_aceptar = 'Aceptar', url_cancelar = '')
    cadena = +''
    cadena << etiqueta_campo('')
    cadena << Htm.div("<button type='submit' class='button is-link'>#{texto_aceptar}</button>\n", 'control')
    cadena2 = +"<button type='reset' class='button is-light'"
    cadena2 << " onClick=\"window.location.href='#{url_cancelar}'\">Cancelar</button>\n"
    cadena << Htm.div(cadena2, 'control')
    campo(cadena, 'G')
  end

  # Combo box con opciones en un campo
  def self.campo_combo(texto, listado, variable, defecto = '')
    cadena = +''
    cadena << etiqueta_campo(texto)
    cadena << cuerpo_campo(control(Htm.combo(listado, variable, defecto)))
    campo(cadena, 'H')
  end

  def self.etiqueta_campo(texto)
    Htm.div(Htm.etiqueta(texto, 'label'), 'field-label')
  end

  # Imprime 2 celdas, una con texto y otra con un checkbox
  def self.input_check(texto, variable, valor)
    cadena = +''
    cadena << etiqueta_campo(texto)
    adicional = if valor.is_a? TrueClass
                  'checked'
                else
                  valor.to_i.positive? ? 'checked' : ''
                end
    chk = "<INPUT TYPE='checkbox' NAME='#{variable}' VALUE='1' #{adicional}>"
    cadena << cuerpo_campo(campo(control(chk)))
    campo(cadena, 'H')
  end

  # Checkbox en 2 columnas
  def self.input_check1(texto, variable, valor)
    cadena = +"<div class='field is-horizontal is-grouped'>"
    cadena << cuerpo_campo(input_check(texto, variable, valor))
  end

  # Checkbox en 2 columnas 2
  def self.input_check2(texto, variable, valor)
    cadena = +''
    cadena << cuerpo_campo(input_check(texto, variable, valor))
    cadena << '</div>'
  end

  # Linea con celda con texto y otra con combobox
  def self.input_combo(texto, campo_bdd, resultado, campos, valor)
    cad1 = +''
    cad1 << etiqueta_campo(texto)
    cadena = +"<div class='control'>\n"
    cadena << "<div class ='select'>\n<select name='#{campo_bdd}' id='#{campo_bdd}'>\n"
    cadena << "<option value='' selected='selected'>Sin datos</option>\n" if valor == '' || valor.nil?
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
  def self.input_combo1(texto, campo_bdd, resultado, campos, valor)
    cadena = +"<div class='field is-horizontal'>"
    cadena << etiqueta_campo(texto)
    cadena2 = +"<div class='field is-expanded'>\n"
    cadena2 << "<p class='control is-expanded'>\n"
    cadena2 << "<div class ='select is-fullwidth'>\n<select name='#{campo_bdd}' id='#{campo_bdd}'>\n"
    cadena2 << "<option value='' selected='selected'>Sin datos</option>\n" if valor == '' || valor.nil?
    resultado.each do |fil|
      cadena2 << "<option value='#{fil[campos[0]]}' "
      cadena2 << "selected='selected'" if fil[campos[0]].to_s == valor.to_s
      cadena2 << ">#{fil[campos[1]]}</option>\n"
    end
    cadena2 << "</select></div>\n</p>\n</div>\n"
    cadena << Htm.div(cadena2, 'field-body')
  end

  # Linea con celda con texto y otra con combobox. para poner lado a lado
  def self.input_combo2(texto, campo_bdd, resultado, campos, valor)
    cadena = +''
    cadena << etiqueta_campo(texto)
    cadena2 = +"<div class='field is-expanded'>\n"
    cadena2 << "<p class='control is-expanded'>\n"
    cadena2 << "<div class ='select is-fullwidth'>\n<select name='#{campo_bdd}' id='#{campo_bdd}'>\n"
    cadena2 << "<option value='' selected='selected'>Sin datos</option>\n" if valor == '' || valor.nil?
    resultado.each do |fil|
      cadena2 << "<option value='#{fil[campos[0]]}' "
      cadena2 << "selected='selected'" if fil[campos[0]].to_s == valor.to_s
      cadena2 << ">#{fil[campos[1]]}</option>\n"
    end
    cadena2 << "</select></div>\n</p>\n</div>"
    cadena << Htm.div(cadena2, 'field-body')
    cadena << "</div>\n"
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

  # Crea celdas contiguas con texto y campo de texto
  def self.input_fecha(texto, campo_bdd, valor)
    cadena = +''
    cadena << etiqueta_campo(texto)
    entrada = +"<input class='input' type='date' placeholder='dd/mm/aaaa' "
    entrada << "min='1920-01-01' max='2120-12-31' "
    entrada << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>\n"
    cadena << cuerpo_campo(campo(control(entrada)))
    campo(cadena, 'H')
  end

  # Crea celdas contiguas con texto y campo de texto
  def self.input_fecha1(texto, campo_bdd, valor)
    cadena = +"<div class='field is-horizontal'>"
    cadena << etiqueta_campo(texto)
    cadena2 = +"<div class='field is-expanded'>\n"
    cadena2 << "<p class='control is-expanded'>\n"
    cadena2 << "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    cadena2 << "min='1920-01-01' max='2120-12-31' "
    cadena2 << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>\n"
    cadena2 << "</p>\n</div>\n"
    cadena << Htm.div(cadena2, 'field-body')
  end

  def self.input_fecha2(texto, campo_bdd, valor)
    cadena = +''
    cadena << Htm.div(Htm.etiqueta(texto, 'label'), 'field-label is-normal')
    cadena2 = +"<div class='field is-expanded'>\n"
    cadena2 << "<p class='control is-expanded'>\n"
    cadena2 << "<input class='input' type='date' placeholder='dd/mm/aaaa' "
    cadena2 << "min='1920-01-01' max='2120-12-31' "
    cadena2 << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>\n"
    cadena2 << "</p>\n</div>"
    cadena << Htm.div(cadena2, 'field-body')
    cadena << "</div>\n"
  end

  def self.input_hora(texto, campo_bdd, valor)
    cadena = +''
    cadena << etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(Htm.entrada('time', texto, campo_bdd, valor))))
    campo(cadena, 'H')
  end

  # Imprime una linea con una celda con texto y otra con un campo memo
  def self.input_memo(texto, campo_bdd, valor)
    valor = '' if valor.nil?
    cadena = +''
    cadena << etiqueta_campo(texto)
    ctrl = "<textarea class='textarea' name='#{campo_bdd}' placeholder='#{texto}'>#{valor}</textarea>"
    cadena << cuerpo_campo(campo(control(ctrl)))
    campo(cadena, 'H')
  end

  # Imprime un campo de ingreso de valor numerico
  def self.input_numero(texto, campo_bdd, valor, decimales = 2)
    valor = '0' if (valor.is_a? String) && valor.empty?
    num = numero(valor, decimales)
    cadena = +''
    cadena << etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(Htm.entrada('number', texto, campo_bdd, num))))
    campo(cadena, 'H')
  end

  def self.input_numero1(texto, campo_bdd, valor, decimales = 2)
    cadena = +"<div class='field is-horizontal is-grouped'>"
    cadena << input_numero(texto, campo_bdd, valor, decimales)
  end

  def self.input_numero2(texto, campo_bdd, valor, decimales = 2)
    cadena = +''
    cadena << input_numero(texto, campo_bdd, valor, decimales)
    cadena << '</div>'
  end

  def self.input_password(texto, campo_bdd, valor)
    cadena = +''
    cadena << etiqueta_campo(texto)
    cadena << cuerpo_campo(control(Htm.entrada('password', texto, campo_bdd, valor)))
    campo(cadena, 'H')
  end

  # arreglo es un DICCIONARIO con texto y valor del item
  def self.input_radio(texto, variable, arreglo, valor)
    radio = +''
    arreglo.each do |llave, dato|
      chkd = dato == valor ? 'checked' : ''
      radio << Htm.etiqueta("<input type='radio' name='#{variable}' value='#{dato}' #{chkd}> #{llave}", 'radio')
    end
    cadena = +''
    cadena << etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(radio)))
    campo(cadena, 'H')
  end

  # Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
  def self.input_texto(texto, campo_bdd, valor)
    cadena = +''
    cadena << etiqueta_campo(texto)
    cadena << cuerpo_campo(campo(control(Htm.entrada('text', texto, campo_bdd, valor))))
    campo(cadena, 'H')
  end

  # Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
  def self.input_texto1(texto, campo_bdd, valor)
    cadena = +"<div class='field is-horizontal is-grouped'>"
    cadena << input_texto(texto, campo_bdd, valor)
  end

  # Imprime celda con un texto y campo para llenarlo, el ancho se puede determinar
  def self.input_texto2(texto, campo_bdd, valor)
    cadena = +''
    cadena << input_texto(texto, campo_bdd, valor)
    cadena << '</div>'
  end

  def self.nav_bar(enlace, icono, texto)
    cadena = +"<a class='navbar-item' href='#{enlace}'>"
    cadena << faicon(icono) << Htm.span(texto) << '</a>'
  end

  # PIE de pagina
  def self.pie(txt_enlace)
    cadena = +"<footer class='footer'>\n"
    cadena << Htm.div(boton('Volver', txt_enlace), 'content has-text-centered')
    cadena << "</footer>\n"
    cadena << Htm.fin_pagina
  end

  def self.rango_fechas(fini = nil, ffin = nil, accion)
    cadena = +''
    cadena << Htm.form_edicion('Seleccionar fechas', accion)
    cadena << input_fecha1('Inicio', 'fini', fini)
    cadena << input_fecha2('Fin', 'ffin', ffin)
    cadena << Htm.div("<input class='button is-link' type='submit' value='Buscar'>", 'control')
    cadena << Htm.form_edicion_fin
  end

  def self.script_file
    cadena = +''
    cadena << "const fileInput = document.querySelector('#fileupld input[type=file]');"
    cadena << 'fileInput.onchange = () => {'
    cadena << 'if (fileInput.files.length > 0) {'
    cadena << "const fileName = document.querySelector('#fileupld .file-name');"
    cadena << 'fileName.textContent = fileInput.files[0].name;'
    cadena << "}\n}\n"
    Htm.script(cadena)
  end

  # Nivel terciario
  def self.barra_navegacion
    cadena = +"<nav class='navbar' role='navigation' aria-label='main navigation'>"
    cadena << "<div class='navbar-brand'><a class='navbar-item' href='/'>"
    cadena << "<img src='/img/#{IMG_LOGO}'></a>"
    cadena << "<a role='button' class='navbar-burger' aria-label='menu' aria-expanded='false' "
    cadena << "data-target='navbarBasicExample'>"
    cadena << "<span aria-hidden='true'></span><span aria-hidden='true'></span><span aria-hidden='true'></span>"
    cadena << '</a></div>'
    cadena << "<div id='navbarBasicExample' class='navbar-menu'><div class='navbar-start'>"
    cadena << nav_bar('/', 'fas fa-home', 'Inicio')
    cadena << nav_bar('/recepcion', 'fas fa-headset', 'Recepción')
    cadena << nav_bar('/administracion', 'fas fa-dollar-sign', 'Administración')
    cadena << nav_bar('/vehiculos', 'fas fa-ambulance', 'Vehículos')
    cadena << nav_bar('/direccion', 'fas fa-cogs', 'Dirección')
    cadena << nav_bar('/direccion_tecnica', 'fas fa-user-md', 'Dir.Técnica')
    cadena << nav_bar('/sistema', 'fas fa-desktop', 'Sistema')
    cadena << '</div>'
    cadena << "<div class='navbar-end'><div class='navbar-item'><div class='buttons'>"
    cadena << "<a class='button is-warning' href='/logout'>#{faicon('fas fa-sign-out-alt')}<strong>Salir</strong></a>"
    cadena << '</div></div></div></div></nav>'
  end

  def self.file_upload(destino, retorno)
    cadena = +''
    cadena << "<form action='#{destino}' method='post' enctype='multipart/form-data'>"
    cadena << "<div id='fileupld' class='file has-name'>"
    cadena << "<label class='file-label'>"
    cadena << "<input class='file-input' type='file' name='file'>"
    cadena2 = Htm.span("<i class='fas fa-upload'></i>", 'file-icon')
    cadena2 << Htm.span('Seleccione un archivo...', 'file-label')
    cadena <<  Htm.span(cadena2, 'file-cta')
    cadena << Htm.span('...', 'file-name')
    cadena << '</label>'
    cadena << botones(retorno)
    cadena << '</div></form>'
    cadena << script_file
  end

  def self.generar_menu(etiqueta, items, activo = nil)
    if activo.is_a? String
      num_activo = nil
      items.each do |indice, item|
        num_activo = indice if activo.upcase == item[2].upcase
      end
    else
      num_activo = activo
    end
    cadena = +"<aside class='menu'>"
    cadena << "<p class='menu-label'>#{etiqueta}</p>"
    cadena << "<ul class='menu-list'>"
    items.each do |indice, item|
      cadena << if indice == num_activo
                  "<li><a class='is-active' href='#{item[0]}'>#{faicon(item[1], 'white')}#{item[2]}</a></li>"
                else
                  "<li><a href='#{item[0]}'>#{faicon(item[1])} #{item[2]}</a></li>"
                end
    end
    cadena << '</ul></aside>'
  end
end
