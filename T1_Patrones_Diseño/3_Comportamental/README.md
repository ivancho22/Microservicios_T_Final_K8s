## Escenario 3
Estás desarrollando una aplicación de chat grupal. Los usuarios pueden enviarse mensajes
entre sí dentro de una sala de chat. Sin embargo, gestionar las interacciones directas entre
cada usuario haría que cada uno deba conocer y comunicarse con todos los demás, lo que
resulta en una alta dependencia entre objetos.

## Problema
Sin un mediador, cada usuario tendría que mantener referencias directas a todos los demás,
lo que genera un sistema difícil de escalar y mantener. Si agregas o eliminas usuarios, debes
actualizar muchas relaciones.

## Beneficios esperados de la solución:
- Facilita el mantenimiento: Agregar o eliminar usuarios no debe requerir modificar los
demás.

- Mejor organización: La lógica de comunicación debe estar centralizada, no dispersa
en muchos objetos.

- Reduce la complejidad: Evitar una red enmarañada de interacciones punto a punto.

## Solución
### Tipo de patrón
Patrón comportamental.

Esto es porque los patrones comportamentales se centran en cómo los objetos interactúan y se comunican entre sí.


### Patrón Mediador
El patrón Mediador actúa como un intermediario permite centralizar la comunicación entre los componentes, en este caso los usuarios, en lugar de que cada objeto Usuario se comunique directamente con todos los demás, evitando un alta acoplamiento, ya que no necesitan interactuar entre sí directamente.

El patrón Mediador es la mejor elección porque:

- Centraliza la comunicación entre usuarios mediante un objeto intermediario (Sala de chat).
- Reduce la dependencia entre los objetos, permitiendo agregar/eliminar usuarios sin afectar a los demás.
- Mejora el mantenimiento, porque las reglas de comunicación residen en el mediador, evitando la dispersión del código.
- Reduce la complejidad, porque evita crear una red de interacciones entre cada uno de los objetos.
