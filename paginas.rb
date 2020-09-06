get '/login_incorrecto' do
  cadena = Htm.encabezado_completo('Error', '/pantalla_login')
  mensaje = request.params['problema']
  cadena << Htm.nota("Hay un problema con su #{mensaje}")
  cadena << Htm.pie('/pantalla_login')
end

get '/duplicado' do
  retorno = reqest.params['retorno']
  cadena = Htm.encabezado_completo('Duplicado', retorno)
  cadena << Htm.nota('El registro que intenta insertar ya existe.')
  cadena << Htm.pie(retorno)
end

get '/no_disponible' do
  retorno = reqest.params['retorno']
  cadena = Htm.encabezado_completo('Página no disponible', retorno)
  cadena << Htm.nota('La página que quiere acceder se encuentra en construcción.')
  cadena << Htm.pie(retorno)
end

get '/error/claves/:retorno' do
  retorno = params['retorno']
  cadena = Htm.encabezado_completo('Error', retorno)
  cadena << Htm.nota('Las claves no coinciden.')
  cadena << Htm.pie(retorno)
end
