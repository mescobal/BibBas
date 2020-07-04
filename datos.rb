# frozen_string_literal: true

require 'active_record'
require 'sqlite3'
def conexion
  ActiveRecord::Base.establish_connection(
    adapter: 'sqlite3',
    database: './datos/emovil.db'
  )
end

# Categoria de clientes
class CatClientes < ActiveRecord::Base
  self.table_name = 'cat_clientes'
end

# Clientes
class Clientes < ActiveRecord::Base
  self.table_name = 'clientes'
end

# Llamadas telefonicas
class Llamadas < ActiveRecord::Base
  self.table_name = 'llamadas'
end

# Usuarios
class Usuarios < ActiveRecord::Base
  self.table_name = 'usuarios'
end

# Registro de logins
class Registro < ActiveRecord::Base
  self.table_name = 'registro'
end

def conexion_vehiculos
  ActiveRecord::Base.establish_connection(
    adapter: 'sqlite3',
    database: './data/vehiculos.db'
  )
end

# Indicadores
class Combustible < ActiveRecord::Base
  self.table_name = 'combustible'
end

# Comprobantes
class Comprobantes < ActiveRecord::Base
  self.table_name = 'comprobantes'
end

# Estados de traslados
class EstadosTraslados < ActiveRecord::Base
  self.table_name = 'estados_traslados'
end

# Estados de vehiculos
class EstadosVehiculos < ActiveRecord::Base
  self.table_name = 'estados_vehiculos'
end

# Mantenimiento
class Mantenimiento < ActiveRecord::Base
  self.table_name = 'mantenimiento'
end

# Tipo de combustible
class TipoCombustible < ActiveRecord::Base
  self.table_name = 'tipo_combustible'
end

# Tipo de mantenimiento
class TipoMantenimiento < ActiveRecord::Base
  self.table_name = 'tipo_mantenimiento'
end

# Tipo de traslado1
class TipoTraslado < ActiveRecord::Base
  self.table_name = 'tipo_traslado'
end

# Traslados
class Traslados < ActiveRecord::Base
  self.table_name = 'traslados'
end

# Trayectos
class Trayectos < ActiveRecord::Base
  self.table_name = 'trayectos'
end

# Vehiculos
class Vehiculos < ActiveRecord::Base
  self.table_name = 'vehiculos'
end

# Viajes
class Viajes < ActiveRecord::Base
  self.table_name = 'viajes'
end

# Variables de costos
class VariablesCostos < ActiveRecord::Base
  self.table_name = 'variables_costos'
end

# Productos traslados
class ProductosTraslados < ActiveRecord::Base
  self.table_name = 'productos_traslados'
end

# Variables de traslados
class VariablesTraslado < ActiveRecord::Base
  self.table_name = 'variables_traslado'
end

# ---------------- EMPLEADOS

# Categoria de empleados
class CatEmpleados < ActiveRecord::Base
  self.table_name = 'cat_empleados'
end

# Codigo Seguridad Social
class CodigoSS < ActiveRecord::Base
  self.table_name = 'codigoss'
end

# Cuenta de empleados
class CtaEmpleados < ActiveRecord::Base
  self.table_name = 'cat_empleados'
end

# det_liquidacion
class DetLiquidacion < ActiveRecord::Base
  self.table_name = 'det_liquidacion'
end

# Empleados
class Empleados < ActiveRecord::Base
  self.table_name = 'empleados'
end

# Legajo
class Legajo < ActiveRecord::Base
  self.table_name = 'legajo'
end

# Liquidacion
class Liquidacion < ActiveRecord::Base
  self.table_name = 'liquidacion'
end

# Salario
class Salario < ActiveRecord::Base
  self.table_name = 'salario'
end

# -------------- CONTABILIDAD

# Plan de Cuentas
class PlanDeCuentas < ActiveRecord::Base
  self.table_name = 'plancta'
end

# Tabla balancetes
class Balancetes < ActiveRecord::Base
  self.table_name = 'balancetes'
end

# Tabla ejercicios
class Ejercicios < ActiveRecord::Base
  self.table_name = 'ejercicios'
  self.primary_key = 'id'
end
conexion
