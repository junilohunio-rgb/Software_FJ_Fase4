import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):
    def __init__(self, nombre, documento, correo, telefono):
        super().__init__()
        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatosInvalidosError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        if not str(valor).isdigit() or len(str(valor)) < 6:
            raise DatosInvalidosError("El documento debe contener al menos 6 dígitos.")
        self._documento = str(valor)

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", valor):
            raise DatosInvalidosError("El correo electrónico no tiene un formato válido.")
        self._correo = valor.lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        limpio = re.sub(r"\D", "", str(valor))
        if len(limpio) < 7 or len(limpio) > 15:
            raise DatosInvalidosError("El teléfono debe tener entre 7 y 15 dígitos.")
        self._telefono = limpio

    def describir(self):
        return f"Cliente {self.nombre} | Documento: {self.documento} | Correo: {self.correo}"

    def __str__(self):
        return self.describir()
