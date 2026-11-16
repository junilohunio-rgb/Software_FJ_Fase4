from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError, ServicioNoDisponibleError


class Servicio(ABC):
    def __init__(self, nombre, tarifa_hora, disponible=True):
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise DatosInvalidosError("El nombre del servicio no es válido.")
        if not isinstance(tarifa_hora, (int, float)) or tarifa_hora <= 0:
            raise DatosInvalidosError("La tarifa debe ser un número mayor que cero.")
        self._nombre = nombre.strip()
        self._tarifa_hora = float(tarifa_hora)
        self._disponible = bool(disponible)

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valor):
        self._disponible = bool(valor)

    def validar_disponibilidad(self):
        if not self._disponible:
            raise ServicioNoDisponibleError(f"El servicio '{self.nombre}' no está disponible.")

    # Sobrecarga simulada en Python mediante parámetros opcionales.
    def calcular_costo(self, horas, impuesto=0.19, descuento=0, **kwargs):
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatosInvalidosError("La duración debe ser mayor que cero.")
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatosInvalidosError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self._tarifa_hora * horas
        return round(subtotal * (1 - descuento) * (1 + impuesto), 2)

    @abstractmethod
    def validar_parametros(self, **kwargs):
        pass

    @abstractmethod
    def describir(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, nombre, tarifa_hora, capacidad, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un entero positivo.")
        self.capacidad = capacidad

    def validar_parametros(self, **kwargs):
        personas = kwargs.get("personas")
        if personas is None:
            raise DatosInvalidosError("Falta indicar la cantidad de personas.")
        if not isinstance(personas, int) or not 1 <= personas <= self.capacidad:
            raise DatosInvalidosError(f"La sala admite entre 1 y {self.capacidad} personas.")

    def describir(self):
        return f"Sala: {self.nombre} | Capacidad: {self.capacidad} personas"


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, tarifa_hora, unidades, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if not isinstance(unidades, int) or unidades <= 0:
            raise DatosInvalidosError("Las unidades deben ser un entero positivo.")
        self.unidades = unidades

    def validar_parametros(self, **kwargs):
        cantidad = kwargs.get("cantidad")
        if cantidad is None:
            raise DatosInvalidosError("Falta indicar la cantidad de equipos.")
        if not isinstance(cantidad, int) or not 1 <= cantidad <= self.unidades:
            raise DatosInvalidosError(f"Solo hay {self.unidades} unidades disponibles.")

    def calcular_costo(self, horas, impuesto=0.19, descuento=0, cantidad=1):
        self.validar_parametros(cantidad=cantidad)
        return super().calcular_costo(horas, impuesto, descuento) * cantidad

    def describir(self):
        return f"Equipo: {self.nombre} | Unidades disponibles: {self.unidades}"


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, tarifa_hora, especialidad, disponible=True):
        super().__init__(nombre, tarifa_hora, disponible)
        if not isinstance(especialidad, str) or len(especialidad.strip()) < 3:
            raise DatosInvalidosError("Debe indicar una especialidad válida.")
        self.especialidad = especialidad.strip()

    def validar_parametros(self, **kwargs):
        tema = kwargs.get("tema")
        if not isinstance(tema, str) or len(tema.strip()) < 3:
            raise DatosInvalidosError("Debe indicar un tema de asesoría válido.")

    def describir(self):
        return f"Asesoría: {self.nombre} | Especialidad: {self.especialidad}"
