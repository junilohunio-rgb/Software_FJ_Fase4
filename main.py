import logging
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from gestor import GestorSoftwareFJ
from excepciones import SoftwareFJError


def ejecutar_operacion(numero, descripcion, funcion):
    """Aísla cada operación: un error no detiene las siguientes."""
    print(f"\\nOPERACIÓN {numero}: {descripcion}")
    try:
        resultado = funcion()
    except Exception as error:
        logging.exception("Operación %s fallida: %s", numero, descripcion)
        print(f"ERROR CONTROLADO: {error}")
    else:
        print(f"RESULTADO: {resultado}")
    finally:
        print("Fin de la operación.")


def main():
    sistema = GestorSoftwareFJ()

    # Objetos de servicios creados para las demostraciones.
    sala = ReservaSala("Sala Ejecutiva", 50000, 20)
    equipo = AlquilerEquipo("Proyector", 25000, 5)
    asesoria = AsesoriaEspecializada("Consultoría Python", 80000, "Desarrollo de software")

    clientes_creados = {}

    def cliente_valido():
        c = Cliente("Laura Gómez", "10203040", "laura@email.com", "3001234567")
        sistema.registrar_cliente(c)
        clientes_creados["laura"] = c
        return c.describir()

    def cliente_invalido():
        return Cliente("Li", "123", "correo-mal", "12")

    def cliente_duplicado():
        c = Cliente("Laura Gómez", "10203040", "laura2@email.com", "3001234567")
        sistema.registrar_cliente(c)
        return "Cliente duplicado registrado"

    def registrar_servicios():
        for s in (sala, equipo, asesoria):
            sistema.registrar_servicio(s)
        return sistema.listar_servicios()

    def servicio_invalido():
        return ReservaSala("Sala pequeña", -100, 10)

    def reserva_exitosa():
        r = sistema.crear_reserva(clientes_creados["laura"], sala, 2, personas=8)
        r.confirmar()
        costo = r.procesar(descuento=0.10)
        return f"{r.describir()} | Costo final: ${costo:,.2f}"

    def reserva_sin_parametros():
        return sistema.crear_reserva(clientes_creados["laura"], sala, 2)

    def equipo_excede_unidades():
        return sistema.crear_reserva(clientes_creados["laura"], equipo, 3, cantidad=9)

    def servicio_no_disponible():
        asesoria.disponible = False
        return sistema.crear_reserva(
            clientes_creados["laura"], asesoria, 1, tema="Automatización"
        )

    def cancelacion_correcta():
        r = sistema.crear_reserva(clientes_creados["laura"], equipo, 1, cantidad=1)
        r.cancelar()
        return r.describir()

    def procesamiento_incorrecto():
        r = sistema.crear_reserva(clientes_creados["laura"], sala, 1, personas=4)
        return r.procesar()

    operaciones = [
        ("Registro válido de cliente", cliente_valido),
        ("Registro inválido de cliente", cliente_invalido),
        ("Intento de registrar cliente duplicado", cliente_duplicado),
        ("Registro de tres servicios especializados", registrar_servicios),
        ("Creación de servicio con tarifa inválida", servicio_invalido),
        ("Reserva confirmada y procesada correctamente", reserva_exitosa),
        ("Reserva de sala sin parámetro obligatorio", reserva_sin_parametros),
        ("Alquiler de más equipos de los disponibles", equipo_excede_unidades),
        ("Reserva de un servicio no disponible", servicio_no_disponible),
        ("Cancelación correcta de una reserva", cancelacion_correcta),
        ("Intento de procesar reserva sin confirmar", procesamiento_incorrecto),
    ]

    for numero, (descripcion, funcion) in enumerate(operaciones, start=1):
        ejecutar_operacion(numero, descripcion, funcion)

    print("\\nRESUMEN FINAL")
    print(f"Clientes registrados: {len(sistema.clientes)}")
    print(f"Servicios registrados: {len(sistema.servicios)}")
    print(f"Reservas creadas: {len(sistema.reservas)}")
    print(f"Archivo de eventos y errores: {sistema.__class__.__module__} / logs/software_fj.log")
    print("El programa terminó sin detenerse por los errores controlados.")


if __name__ == "__main__":
    main()
