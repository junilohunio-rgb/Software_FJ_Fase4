class SoftwareFJError(Exception):
    """Excepción base del sistema."""


class DatosInvalidosError(SoftwareFJError):
    pass


class ServicioNoDisponibleError(SoftwareFJError):
    pass


class ReservaError(SoftwareFJError):
    pass


class EstadoReservaError(SoftwareFJError):
    pass
