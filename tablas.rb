#!/usr/bin env python3
"""Librería para manejo de tablas
Ver: 0.6.27 : elimino magik y lo saco aparte
"""

import datetime
from lib import datos


class Actividades(datos.Tabla):
    """Actividad del empleado"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "suactivi", "lifunid", "indicadores")
        if ident is not None:
            self.ir_a(ident)


class Balancetes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "balancetes", "id", "contabilidad")
        if ident is not None:
            self.ir_a(ident)


class CatEmpleados(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "cat_empleados", "id", "empleados")
        if ident is not None:
            self.ir_a(ident)


class Claves(datos.Tabla):
    """Clave 1 2 3"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "claves", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class Clientes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "clientes", "id", "clientes")
        if ident is not None:
            self.ir_a(ident)


class CV(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "cv", "id", "empleados")
        if ident is not None:
            self.ir_a(ident)


class Ejercicios(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "ejercicios", "id", "contabilidad")
        if ident is None:
            self.ir_a(ident)


class Empleados(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "empleados", "id", "empleados")
        if ident is not None:
            self.ir_a(ident)


class EstadosVehiculos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "estados_vehiculos", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class EvolIndicadores(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "evol_indicadores", "id", "indicadores")
        if ident is not None:
            self.ir_a(ident)


class Formacion(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "formacion", "id", "empleados")
        if ident is not None:
            self.ir_a(ident)


class Indicadores(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "indicadores", "id", "indicadores")
        if ident is not None:
            self.ir_a(ident)


class Llamadas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "llamadas", "id", "recepcion")
        if ident is not None:
            self.ir_a(ident)


class Llamados(datos.Tabla):
    """Llamados clave 1, 2 y 3"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "llamados", "id", "recepcion")
        if ident is not None:
            self.ir_a(ident)


class Locales(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "locales", "id", "sistema")
        if ident is not None:
            self.ir_a(ident)


class Localidades(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "localidades", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class Mantenimiento(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "mantenimiento", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class PersonalTurno(datos.Tabla):
    def __init__(self,  ident=None):
        datos.Tabla.__init__(self,  "sq3", "personal_turno",  "id",  "recepcion")
        if ident is not None:
            self.ir_a(ident)


class PlanCuentas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "plancta", "id", "contabilidad")
        if ident is not None:
            self.ir_a(ident)


class Productos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "productos", "id", "ventas")
        if ident is not None:
            self.ir_a(ident)


class Proveedores(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "proveedores", "id", "proveedores")
        if ident is not None:
            self.ir_a(ident)


class ProvMantenimiento(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "prov_mantenimiento", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class Puntos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "puntos", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class Tareas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tareas", "id", "tareas")
        if ident is not None:
            self.ir_a(ident)


class TipoLlamado(datos.Tabla):
    """Area protegida, socio, etc"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_llamado", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class TiposMantenimiento(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_mantenimiento", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class TiposProducto(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_producto", "id", "ventas")
        if ident is not None:
            self.ir_a(ident)


class TipoTraslado(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_traslado", "id", "recepcion")
        if ident is not None:
            self.ir_a(ident)


class TipoTrayecto(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_trayecto", "id", "recepcion")
        if ident is not None:
            self.ir_a(ident)


class Traslados(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "traslados", "id", "recepcion")
        if ident is not None:
            self.ir_a(ident)


class Turnos(datos.Tabla):
    """0 a 6, 6 a 12, etc"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "turnos", "id", "sistema")
        if ident is not None:
            self.ir_a(ident)

    @staticmethod
    def turno_actual():
        ahora = datetime.datetime.now()
        hora = ahora.strftime("%H:%M:%S")
        valor = None
        if "00:00:00" <= hora < "06:00:00":
            valor = 1
        elif "06:00:00" <= hora < "12:00:00":
            valor = 2
        elif "12:00:00" <= hora < "18:00:00":
            valor = 3
        elif "18:00:00" <= hora <= "24:59:59":
            valor = 4
        return valor


class Usuarios(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "usuarios", "id", "usuarios")
        if ident is not None:
            self.ir_a(ident)


class Vehiculos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "vehiculos", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class Ventas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "ventas", "id", "ventas")
        if ident is not None:
            self.ir_a(ident)


class Viajes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "viajes", "id", "recepcion")
        if ident is not None:
            self.ir_a(ident)

