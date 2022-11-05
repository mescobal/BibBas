"""Librería para conectar con base de datos magik
version 0.11.22
Ver 1.12: ver_nombre: arreglado para lidiar con None y cadenas vacías
"""
import typing
from lib import datos


class Actividad(datos.Tabla):
    """Actividad = suactivi"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "suactivi", "lifunid", "magik")
        if ident is not None:
            self.ir_a(ident)


class AgrFuncionarios(datos.Tabla):
    """Agrupacion de funcionarios"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "licfunc1", "lifunid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Agrupamiento(datos.Tabla):
    """Categorías de agrupamiento de funcionarios"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "suagrfu1", "suagrfunco", "magik")
        if ident is not None:
            self.ir_a(ident)


class Cargos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "sucargo", "sucarcod", "magik")
        if ident is not None:
            self.ir_a(ident)


class CatClientes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "categori", "percatid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Contratos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "contrato", "percontid", "magik")
        if ident is not None:
            self.ir_a(ident)


class CtaCteMovimientos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "ccctact2", "ctctacod", "magik")
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


class Funcionarios(datos.Tabla):
    """Funcionarios de la empresa"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "licfunci", "lifunid", "magik")
        if ident is not None:
            self.ir_a(ident)

    def nombre(self) -> str:
        if self.registro["lifunid"]:
            pers = Personas(self.registro["perid"])
            nomb = pers.registro["perape1"].strip() + " " + pers.registro["perape2"].strip()
            nomb += ", " + pers.registro["pernom1"].strip() + " " + pers.registro["pernom2"].strip()
            return nomb.strip()


class Personas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "persona", "perid", "magik")
        if ident is not None:
            self.ir_a(ident)

    def ver_nombre(self, ident: typing.Optional[int]) -> str:
        """#{fila['perape1']} #{fila['perape2']}, #{fila['pernom1']} #{fila ['pernom2']}"""
        if ident is None:
            nombre = "Sin datos"
        else:
            try:
                numero = int(ident)
                self.ir_a(numero)
                nombre = self.registro["perape1"] + "," + self.registro["pernom1"]
            except ValueError:
                nombre = "Sin datos"
        return nombre

    def nombre_completo(self):
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


class Llamados(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "emllamad", "emonumid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Lugares(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "emlugar", "emlugid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Moviles(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "emmovil", "emmovid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Secciones(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "suseccio", "suseccod", "magik")
        if ident is not None:
            self.ir_a(ident)


class Telefonos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "domicil2", "domicid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Valores(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "valores", "perserid", "magik")
        if ident is not None:
            self.ir_a(ident)


class VinculoFuncional(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "pg", "suvinfun", "suvfuncod", "magik")
        if ident is not None:
            self.ir_a(ident)


def ver_nombre_completo(perid):
    pers = Personas(perid)
    if pers.registro is None:
        nombre = "Sin datos"
    else:
        nombre = "%s %s, %s %s" % (pers.registro["perape1"], pers.registro["perape2"],
                                   pers.registro["pernom1"], pers.registro["pernom2"])
    return nombre


def ver_telefono(perid):
    telefono = 'Sin datos'
    pers = Personas(perid)
    if pers.registro:
        tele = Telefonos()
        tele.filtro = "domicid = %s" % pers.registro["perdomref"]
        tele.filtrar()
        if tele.registro:
            telefono = tele.registro["domictel"]
    return telefono
