## Escenario 1
Imagina que estás desarrollando una aplicación para una compañía automotriz que permite
a los clientes personalizar y ordenar un automóvil. Un objeto Automóvil puede tener muchas
configuraciones opcionales: tipo de motor, color, llantas, sistema de sonido, interiores, techo
solar, navegación GPS, etc.

## Problema
Crear un objeto Automóvil con múltiples configuraciones puede llevar a constructores con
muchos parámetros (el infame "constructor telescópico") o a múltiples constructores
sobrecargados, lo que dificulta el mantenimiento y legibilidad del código.

## Beneficios esperados de la solución:
- Legibilidad y claridad: Facilitar la creación de objetos complejos con muchos
parámetros sin necesidad de múltiples constructores o valores por defecto.

- Inmutabilidad: Una vez creado el objeto, sus propiedades no se pueden modificar si
el constructor lo define como inmutable.

- Flexibilidad: Poder omitir atributos opcionales sin necesidad de crear subclases o
múltiples constructores.

- Separación de construcción y representación: Separar la lógica de construcción del
objeto en sí, facilitando modificaciones futuras.

## Solución
### Tipo de patrón
Patrón Creacional.

Esto es porque los patrones creacionales proporcionan mecanismos de creación de objetos que incrementan la flexibilidad y la reutilización del código existente


### Patrón Builder
Se eligió el patrón de diseño Builder porque permite construir objetos complejos, como un automóvil en este caso con múltiples configuraciones opcionales, de manera clara, flexible y mantenible. En este contexto, crear un objeto Automovil puede implicar una gran cantidad de parámetros (motor, color, llantas, interiores, sonido, techo solar, GPS, etc.), lo que haría que usar un constructor tradicional resulte poco legible y difícil de mantener.

Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. Este patrón permite separar la lógica de construcción de la representación del objeto, de manera que podamos reutilizar el mismo proceso de construcción para crear diferentes variantes del producto.

El patrón Builder es la mejor elección porque:

- Se puede reutilizar el mismo Builder para crear un automóvil básico, de lujo o personalizado.
- Permite agregar u omitir fácilmente atributos opcionales sin necesidad de crear múltiples subclases o constructores sobrecargados.
- Aumenta la inmutabilidad del objeto final, ya que se construye en un solo paso y luego no se modifica.

