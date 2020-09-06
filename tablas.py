#!/usr/bin env python3
"""Librería para manejo de tablas
Ver: 0.5-25"""

from lib import datos


class Balancetes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "balancetes", "id", "emovil")
        if ident is not None:
            self.ir_a(ident)


class CatClientes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "cat_clientes", "id", "clientes")
        if ident is not None:
            self.ir_a(ident)


class CatEmpleados(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "cat_empleados", "id", "empleados")
        if ident is not None:
            self.ir_a(ident)


class Clientes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "clientes", "id", "clientes")
        if ident is not None:
            self.ir_a(ident)


class Ejercicios(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "ejercicios", "id", "emovil")
        if ident is None:
            self.ir_a(ident)


class Empleados(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "empleados", "id", "empleados")
        if ident is not None:
            self.ir_a(ident)


class Empresas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "empresas", "emprid", "magik")
        if ident is not None:
            self.ir_a(ident)

    def ver_telefono(self):
        """Buscar telefono del registro actual"""
        domref = self.registro["emprdomref"]
        tele = Telefonos()
        tele.filtro = "domicid = %s" % domref
        tele.filtrar()
        if tele.encontrado:
            return tele.registro["domictel"]
        else:
            return "Desconocido"


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


class Indicadores(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "indicadores", "id", "indicadores")
        if ident is not None:
            self.ir_a(ident)


class Llamadas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "llamadas", "id", "clientes")
        if ident is not None:
            self.ir_a(ident)


class Localidades(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "localidades", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class Personas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "persona", "perid", "magik")
        if ident is not None:
            self.ir_a(ident)

    def ver_nombre(self, ident):
        """#{fila['perape1']} #{fila['perape2']}, #{fila['pernom1']} #{fila ['pernom2']}"""
        self.ir_a(ident)
        nombre = self.registro["perape1"] + " " + self.registro["perape2"] + "," + \
            self.registro["pernom1"] + " " + self.registro["pernom2"]
        return nombre

    def ver_telefono(self, ident):
        self.ir_a(ident)
        tele = Telefonos()
        tele.filtro = "domicid = %s" % self.registro["perdomref"]
        tele.filtrar()
        if tele.registro["domictel"]:
            telefono = tele.registro["domictel"]
        else:
            telefono = "Sin datos"
        return telefono


class PlanCuentas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "plancta", "id", "emovil")
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


class Telefonos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "domicil2", "domicid", "magik")
        if ident is not None:
            self.ir_a(ident)


class TiposProducto(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_producto", "id", "ventas")
        if ident is not None:
            self.ir_a(ident)


class TipoTraslado(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_traslado", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class TipoTrayecto(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "tipo_trayecto", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


class Traslados(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "traslados", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)


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
        datos.Tabla.__init__(self, "sq3", "viajes", "id", "vehiculos")
        if ident is not None:
            self.ir_a(ident)
