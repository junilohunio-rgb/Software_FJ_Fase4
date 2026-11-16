from abc import ABC, abstractmethod
from datetime import datetime
from uuid import uuid4


class Entidad(ABC):
    """Clase abstracta para las entidades del sistema."""

    def __init__(self):
        self._id = str(uuid4())[:8]
        self._fecha_creacion = datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def fecha_creacion(self):
        return self._fecha_creacion

    @abstractmethod
    def describir(self):
        pass
