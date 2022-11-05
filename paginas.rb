# frozen_string_literal: true

require_relative './bulma'
require_relative './htm'

# Clase para generar una pagina web
class Pagina
  attr_accessor :menu_lateral, :contenido, :pie, :retorno, :nivel_usuario

  def initialize(titulo, retorno = '')
    @menu_lateral = ''
    @pie = ''
    @titulo = titulo
    @retorno = retorno
  end

  def render
    cadena = encabezado
    cadena << "<body>\n"
    cadena << Bulma.barra_navegacion
    cadena << "<div class='columns'>"
    cadena << Htm.div(@menu_lateral, 'column is-narrow')
    cadena << "<div class='column'>"
    # cadena << "<div class='box'>"
    cadena << "<div class='card'>"
    cadena << "<header class='card-header is-size-3'><p class='card-header-title'>#{@titulo}</p>"
    cadena << Bulma.boton_cerrar(@retorno) unless @retorno.empty?
    cadena << '</header>'
    # cadena2 = Htm.encabezado(1, @titulo)
    # cadena2 << Bulma.boton_cerrar(retorno) unless @retorno.empty?
    # cadena << Htm.div(cadena2, 'block')
    cadena << Htm.div(@contenido, 'card-content')
    cadena << '</div>'
    # cadena << "<div class='box'>"
    cadena << "<footer class='card-footer'>#{@pie}</footer>"
    cadena << '</div>'
  end

  def encabezado
    cadena = +"<!DOCTYPE html>\n"
    cadena << "<html lang='es'>"
    cadena << "<head>\n"
    cadena << "<meta charset='utf-8' />\n"
    cadena << "<meta name='viewport' content='width=device-width, initial-scale=1'>\n"
    cadena << "<title>#{@titulo}</title>\n"
    cadena << "<link type='text/css' href='/css/bulma.css' rel='stylesheet' />"
    cadena << "<link href='/css/all.css' rel='stylesheet'>"
    cadena << "</head>\n"
  end
end
