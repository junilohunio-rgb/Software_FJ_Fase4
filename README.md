# Software FJ

Sistema de gestión de clientes, servicios y reservas desarrollado en Python, aplicando programación orientada a objetos. No utiliza bases de datos: los datos viven en listas y objetos durante la ejecución. Los eventos y errores se registran en `logs/software_fj.log`.

## Requisitos
- Python 3.10 o superior
- Visual Studio Code (recomendado)
- Extensión Python de Microsoft para VS Code

## Ejecución
Abre esta carpeta en VS Code. En la terminal integrada ejecuta:

```bash
python main.py
```

En Windows también puedes usar:

```powershell
py main.py
```

## Estructura
- `entidades.py`: clase abstracta Entidad.
- `clientes.py`: Cliente con propiedades encapsuladas y validaciones.
- `servicios.py`: clase abstracta Servicio y tres servicios derivados.
- `reservas.py`: creación, confirmación, cancelación y procesamiento.
- `excepciones.py`: excepciones personalizadas.
- `gestor.py`: listas internas y registro de eventos.
- `main.py`: demostración de 11 operaciones, exitosas y fallidas.
- `logs/software_fj.log`: archivo generado automáticamente.

## Conceptos POO aplicados
- Abstracción: `Entidad` y `Servicio` son clases abstractas.
- Herencia: Cliente y los servicios especializados heredan de sus clases base.
- Encapsulación: atributos privados/protegidos y propiedades de validación.
- Polimorfismo: cada servicio implementa `describir()` y `validar_parametros()`.
- Sobrecarga: `calcular_costo()` admite impuesto y descuento opcionales; el alquiler de equipos extiende el cálculo con cantidad.

## Git y GitHub
1. Crea un repositorio vacío en GitHub llamado `Software-FJ`.
2. Abre la terminal en la carpeta del proyecto.
3. Ejecuta:

```bash
git init
git add .
git commit -m "Primer avance: sistema Software FJ"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/Software-FJ.git
git push -u origin main
```

Reemplaza `TU-USUARIO` por tu nombre de usuario de GitHub.

Para subir cambios posteriores:

```bash
git add .
git commit -m "Actualización del sistema"
git push
```

## Nota académica
Python no implementa sobrecarga tradicional de métodos por firma como Java o C++. Este proyecto demuestra una variante idiomática mediante parámetros opcionales y sobrescritura en la clase `AlquilerEquipo`.
