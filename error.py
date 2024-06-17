class Error(Exception):
    """Clase Base de Excepciones"""

    pass


class DimensionError(Error):

    def __init__(self, mensaje: str, dimension: int, maximo: int) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        if self.mensaje != None and self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            ret = f"{self.mensaje}"
            if self.dimension != None:
                ret += f" valor ingresado: {self.dimension}."
            if self.maximo != None:
                ret += f" Máximo {self.maximo} permitido"
            return ret
