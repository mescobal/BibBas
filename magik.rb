"""Librería para conectar con base de datos magik
version 0.6.27
"""
from lib import datos


class AgrFuncionarios(datos.Tabla):
    """Agrupacion de funcionarios"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "licfunc1", "lifunid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Agrupamiento(datos.Tabla):
    """Categorías de agrupamiento de funcionarios"""
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "suagrfu1", "suagrfunco", "magik")
        if ident is not None:
            self.ir_a(ident)


class Cargos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "sucargo", "sucarcod", "magik")
        if ident is not None:
            self.ir_a(ident)


class CatClientes(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "categori", "percatid", "magik")
        if ident is not None:
            self.ir_a(ident)


class Contratos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "contrato", "percontid", "magik")
        if ident is not None:
            self.ir_a(ident)


class CtaCteMovimientos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "ccctact2", "ctctacod", "magik")
        if ident is not None:
            self.ir_a(ident)


class CuentaCorriente(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "ccctacte", "ccctacod", "magik")
        if ident is not None:
            self.ir_a(ident)


class Empresas(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "empresas", "emprid", "magik")
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
        datos.Tabla.__init__(self, "sq3", "licfunci", "lifunid", "magik")
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
        datos.Tabla.__init__(self, "sq3", "persona", "perid", "magik")
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


class Secciones(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "suseccio", "suseccod", "magik")
        if ident is not None:
            self.ir_a(ident)


class Telefonos(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "domicil2", "domicid", "magik")
        if ident is not None:
            self.ir_a(ident)


class VinculoFuncional(datos.Tabla):
    def __init__(self, ident=None):
        datos.Tabla.__init__(self, "sq3", "suvinfun", "suvfuncod", "magik")
        if ident is not None:
            self.ir_a(ident)

