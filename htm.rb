# frozen_string_literal: true

# Ver 0.12: campo_combo
# Ver 1.01: fontawesome, cadenas NO frozen
# Ver 1.07: file upload
# Ver 1.09: separo BULMA de HTM

# Conjunto de rutinas para generar codigo html

require_relative './funciones'

IMG_LOGO = 'logo.png'

# genera HTML
module Htm
  # Primer orden
  def self.div(contenido, clase = '')
    cadena = +'<div '
    cadena << " class='#{clase}'" if clase != ''
    cadena << ">#{contenido}</div>\n"
  end

  def self.etiqueta(contenido, clase = '')
    cadena = +'<label '
    cadena << " class='#{clase}'" if clase != ''
    cadena << ">#{contenido}</label>"
  end

  def self.entrada(tipo, texto, campo_bdd, valor)
    cadena = +"<input class='input' type='#{tipo}' placeholder='#{texto}' "
    cadena << "step='any' " if tipo == 'number'
    cadena << "name='#{campo_bdd}' value='#{valor}' id='#{campo_bdd}'>"
  end

  def self.lista(texto)
    "<li>#{texto}</li>"
  # Segundo orden

  # Combo box con listado como opciones y texto x defecto
  def self.combo(listado, variable, defecto = '')
    cadena = +"<select name='#{variable}' id='#{variable}'>\n"
    cadena << "<option value='' selected='selected'>Sin datos</option>\n" if defecto == ''
    listado.each do |item|
      cadena << if item == defecto
                  "<option selected='selected' value='#{item}'>#{item}</option>\n"
                else
                  "<option value='#{item}'>#{item}</option>\n"
                end
    end
    cadena << '</select>'
    div(cadena, 'select')
  end

  # Tags de finalizacion de una pagina.
  def self.fin_pagina
    '</div></div></body></html>'
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

  # Imprime una linea con 2 celdas: una con un texto y otra con un dato
  def self.linea_dato(texto, dato, alineacion = 'left')
    "<tr><td>#{texto}</td><td align='#{alineacion}'>#{dato}</td></tr>"
  end
  #
  # # Imprime una celda con un número formateado con 2 decimales
  # def linea_numero(texto, decimales=2)
  #   celda(funciones.numero(texto, decimales), 'right')
  # end
  #
  # Con devolución de cadena

  # Imprime un encabezado con nivel
  def self.encabezado(nivel, texto)
    niveles = ['', ' is-4', ' is-5', ' is-6']
    cadena = +"<h#{nivel} class='title#{niveles[nivel - 1]}"
    cadena << "'>#{texto}</h#{nivel}>"
  end

  # ========================================================
  # A partir de un array arma el encabezado de una tabla
  def self.encabezado_tabla(arr)
    cadena = +"<div class='table-container'>"
    cadena << "<table class='table is-hoverable'><thead><tr>\n"
    arr.each do |lin|
      cadena << celda_encabezado(lin)
    end
    cadena << "</tr>\n</thead>\n<tbody>\n"
  end

  # Imprime tags de finalizacion de una tabla
  def self.fin_tabla
    "</tbody>\n</table>\n</div>"
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
  def self.boton_visto(accion)
    enlace(accion, img('/img/ver.png', 24, 24, 0), 'Visto')
  end

  # Pone una imagen de eliminar cliqueable
  def self.boton_no_visto(accion)
    enlace(accion, img('/img/no_ver.png', 24, 24, 0), 'No visto')
  end

  # Imprime una celda con un valor monetario adentro
  def self.celda_moneda(texto)
    celda(moneda(texto), 'right')
  end

  # Imprime una tabla con texto pequeno
  def self.nota(texto)
    table(fila(celda(span(texto, 'nota'))))
  end

  # Imprime un texto blanco
  def self.texto_barra(texto)
    div(texto, 'texto_barra')
  end

  # def input_decimal(texto, campo, valor)
  #   valor = '' if valor.nil?
  #   puts "<tr><td>#{texto}</td>"
  #   puts "<td><input id='#{campo}' type='number' step='0.01' value='#{valor}' name='#{campo}'>"
  #   puts '</td></tr>'
  # end
  # Tag HTML

  def self.enlace(enl, texto, titulo = '')
    if titulo.empty?
      "<a href='#{enl}'>#{texto}</a>"
    else
      "<a href='#{enl}' title='#{titulo}'>#{texto}</a>"
    end
  end

  # Tag html
  def self.img(src, width = 0, height = 0, border = 0)
    cadena = +"<img src='#{src}' "
    cadena << " width='#{width}' " if width != 0
    cadena << " height='#{height}' " if height != 0
    cadena << " border='#{border}'>"
  end

  # Tag html
  def self.script(texto, typ = '', src = '')
    typ = "type='#{typ}'" if typ != ''
    src = "src='#{src}'" if src != ''
    "<script #{typ} #{src}>\n#{texto}\n</script>"
  end

  # Html tag
  def self.span(contenido, clase = '')
    cadena = +'<span'
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
  def self.celda(texto, align = 'left', rowspan = 1, colspan = 1)
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

  def self.boton_play(accion)
    enlace(accion, img('/img/play.png', 24, 24, 0), 'No visto')
  end

  def self.boton_stop(accion)
    enlace(accion, img('/img/stop.png', 24, 24, 0), 'No visto')
  end
end
