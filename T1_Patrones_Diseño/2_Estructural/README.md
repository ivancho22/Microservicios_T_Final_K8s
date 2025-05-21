## Escenario 2
Estás desarrollando una aplicación que gestiona la visualización de notificaciones 
en diferentes plataformas (por ejemplo: escritorio, móvil, web). Las notificaciones pueden
ser de distintos tipos (mensaje, alerta, advertencia, confirmación) y cada tipo puede 
mostrarse de distintas formas según la plataforma. 

## Problema
Si usas herencia tradicional, tendrías que crear clases como: 
-	 NotificacionMensajeWeb, NotificacionAlertaWeb, NotificacionMensajeMovil, NotificacionAlertaMovil, etc. 

Esto lleva rápidamente a una explosión combinatoria de subclases difíciles de mantener. 

## Beneficios esperados de la solución:
-	Separación de responsabilidades: Separar la lógica de la notificación del medio por el que se presenta. 

-	Escalabilidad: Poder agregar nuevas plataformas o tipos de notificación sin modificar el resto del sistema. 

-	Reducción de clases: Evitar la multiplicación de clases para cada combinación. 

-	Flexibilidad en tiempo de ejecución: Poder cambiar la plataforma dinámicamente si es necesario.

## Solución
### Tipo de patrón
Patrón estructural.

Esto es porque los patrones estructurales permiten ensamblar objetos y clases en estructuras más grandes,
a la vez que se mantiene la flexibilidad y eficiencia de estas estructuras. [Fuente](https://refactoring.guru/es/design-patterns/structural-patterns)


### Patrón Bridge
El patrón Bridge permite dividir una clase grande, o un grupo de clases relacionadas, en dos jerarquías separadas (abstracción e implementación).
Éstas jerarquías pueden desarrollarse independientemente la una de la otra. [Fuente](https://refactoring.guru/es/design-patterns/bridge)

El patrón Bridge es la mejor elección porque:

- Desacopla una abstracción, en nuestro caso las notificaciones, de su implementación (plataformas).
- Separación de responsabilidades, puesto que, la lógica de notificación se separa del canal de entrega.
- Escalabilidad, debido a que se pueden agregar más plataformas y tipos de notificación sin modificar el código existente (cumpliendo el principio SOLID de open/closed).
- Reducción de clases gracias a separación de jerarquías.