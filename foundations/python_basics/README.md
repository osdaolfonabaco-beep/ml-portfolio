Robustez y Manejo de Errores
area_circulo_pro.py

- Análisis de Flujo: ¿Cuál es la ventaja clave de tener la función 'obtener_radio_valido()' separada de 'main()'?
reflexion: 
La ventaja es el principio de responsabilidad única. Cada función hace una sola cosa bien. 'obtener_radio_valido' se encarga solo de la interacción con el usuario, mientras que 'main' orquesta el flujo del programa. Esto hace el código más fácil de probar y modificar.

- Lógica del Loop: ¿Qué pasa si el usuario ingresa un valor correcto en el primer intento?
Reflexion:
La función usa un 'return' para salir inmediatamente y devolver el valor. El 'return' es como un "atajo" que rompe el loop 'while' y sale de la función al mismo tiempo.

- Manejo de Errores: ¿Se puede distinguir si el error vino de 'float()' o de nuestro 'raise'?
Reflexion : 
Técnicamente no directamente, porque ambos son del mismo tipo ('ValueError').pero si podemos hacerlo indirectamente mirando el mensaje de error ('str(e)'). El error de 'float()' dice "could not convert string to float", y nuestro error dice "El radio no puede ser negativo".
