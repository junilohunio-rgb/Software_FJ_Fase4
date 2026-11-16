from datetime import datetime
from entidades import Entidad
from excepciones import ReservaError, EstadoReservaError


class Reserva(Entidad):
    ESTADOS = ("Pendiente", "Confirmada", "Cancelada", "Procesada")

    def __init__(self, cliente, servicio, horas, **parametros):
        super().__init__()
        if cliente is None or servicio is None:
            raise ReservaError("La reserva requiere un cliente y un servicio.")
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ReservaError("Las horas deben ser mayores que cero.")
        servicio.validar_disponibilidad()
        servicio.validar_parametros(**parametros)
        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.parametros = parametros
        self.estado = "Pendiente"
        self.costo = None

    def confirmar(self):
        if self.estado != "Pendiente":
            raise EstadoReservaError("Solo se pueden confirmar reservas pendientes.")
        self.estado = "Confirmada"
        return self.estado

    def cancelar(self):
        if self.estado in ("Cancelada", "Procesada"):
            raise EstadoReservaError("No se puede cancelar una reserva cancelada o procesada.")
        self.estado = "Cancelada"
        return self.estado

    def procesar(self, impuesto=0.19, descuento=0):
        if self.estado != "Confirmada":
            raise EstadoReservaError("La reserva debe estar confirmada antes de procesarse.")
        try:
            self.costo = self.servicio.calcular_costo(
                self.horas, impuesto, descuento, **self.parametros
            )
        except TypeError as error:
            raise ReservaError("No fue posible calcular el costo de la reserva.") from error
        self.estado = "Procesada"
        return self.costo

    def describir(self):
        return (f"Reserva {self.id} | {self.cliente.nombre} | "
                f"{self.servicio.nombre} | {self.horas} horas | {self.estado}")
