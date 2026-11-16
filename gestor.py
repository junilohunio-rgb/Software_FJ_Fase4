import logging
from pathlib import Path
from clientes import Cliente
from reservas import Reserva
from excepciones import SoftwareFJError


RUTA_LOG = Path(__file__).parent / "logs" / "software_fj.log"
RUTA_LOG.parent.mkdir(exist_ok=True)
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8",
    force=True
)


class GestorSoftwareFJ:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            raise SoftwareFJError("El objeto recibido no es un cliente.")
        if any(c.documento == cliente.documento for c in self.clientes):
            raise SoftwareFJError("Ya existe un cliente con ese documento.")
        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.documento)
        return cliente

    def registrar_servicio(self, servicio):
        self.servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.nombre)
        return servicio

    def crear_reserva(self, cliente, servicio, horas, **parametros):
        reserva = Reserva(cliente, servicio, horas, **parametros)
        self.reservas.append(reserva)
        logging.info("Reserva creada: %s", reserva.id)
        return reserva

    def listar_clientes(self):
        return [str(c) for c in self.clientes]

    def listar_servicios(self):
        return [s.describir() for s in self.servicios]

    def listar_reservas(self):
        return [r.describir() for r in self.reservas]
