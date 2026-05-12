# Excepciones

### Autor
Mateo Úsuga Álvarez

## Descripción del proyecto

Este proyecto fue desarrollado con Python y tiene como objetivo comprender e implementar el manejo de excepciones mediante estructuras "try", "except", "else", "finally" y "raise".

A través de diferentes ejemplos prácticos y un reto final, se trabajó la captura de errores comunes durante la ejecución de programas, mejorando la robustez y estabilidad del código.

## Objetivos

- Comprender qué son las excepciones en Python.
- Implementar estructuras "try-except".
- Identificar excepciones comunes.
- Utilizar correctamente "else" y "finally".
- Lanzar excepciones personalizadas usando "raise".
- Desarrollar programas más seguros y organizados.
- Mejorar la validación de datos ingresados por el usuario.

## ¿Qué es una excepción?

Las excepciones son errores que ocurren durante la ejecución de un programa.

Cuando Python encuentra un error, normalmente detiene la ejecución y muestra un mensaje indicando el problema ocurrido.

El manejo de excepciones permite controlar esos errores para evitar que el programa falle inesperadamente.

Esto se realiza utilizando estructuras como:

- try
- except
- else
- finally

## Explicación del manejo de excepciones implementado

Durante el desarrollo de la actividad se implementaron diferentes técnicas de manejo de errores.

### Uso de try y except

Se utilizó try para ejecutar código que podría generar errores y except para capturar excepciones específicas.

Ejemplo:

![evidencia template](/images/Ejemplo%20try-except.png)

### Uso de finally

El bloque finally se ejecuta siempre, exista o no una excepción.

Ejemplo:

![evidencia template](/images/Ejemplo%20finally.png)

### Uso de raise

También se trabajó el lanzamiento manual de excepciones utilizando raise.

Ejemplo:

![evidencia template](/images/Ejemplo%20raise.png)

### Excepciones trabajadas

Durante los ejercicios se implementaron y analizaron las siguientes excepciones:

- ValueError: Valor inválido.
- ZeroDivisionError: División entre cero.
- TypeError: Tipos incompatibles.
- IndexError: Indice fuera de rango.
- KeyError: Clave inexistente.
- FileNotFoundError: Archivo no encontrado.
- PermissionError: Falta de permisos.
- AttributeError: Atributo inexistente.
- NameError: Variable no definida.
- ImportError: Error al importar.
- ModuleNotFoundError: Modulo inexistente.

## Diferencia entre except, else y finally

### except

El bloque "except" se utiliza para capturar y manejar errores que ocurren dentro del bloque "try".

Cuando ocurre una excepción, Python detiene la ejecución normal del programa y ejecuta el código que se encuentra dentro del "except" correspondiente.

Su función principal es evitar que el programa termine abruptamente y permitir mostrar mensajes de error más claros o tomar acciones correctivas.

### else

El bloque "else" se ejecuta únicamente cuando el bloque "try" finaliza correctamente y no ocurre ninguna excepción.

Se utiliza para separar el código que depende del éxito de la operación principal, haciendo que el programa sea más organizado y fácil de entender.

### finally

El bloque "finally" se ejecuta siempre, independientemente de si ocurrió una excepción o no.

Generalmente se utiliza para realizar tareas de limpieza, como cerrar archivos, liberar recursos o mostrar mensajes finales del proceso.

## Capturas de ejecución

### Try Except

![evidencia template](/images/Try-except.png)

En esta sección se trabajó el manejo básico de excepciones utilizando bloques "try" y "except".

Primero se realizó una división entre números para controlar el error de división entre cero. 

Luego se capturaron excepciones específicas como "ValueError" y "ZeroDivisionError" al solicitar datos al usuario.

También se trabajó la lectura de archivos inexistentes utilizando "FileNotFoundError", mostrando cómo acceder a la información del error y crear automáticamente un nuevo archivo.

Además, se combinaron múltiples excepciones en un mismo bloque "except" y se implementó un ejemplo práctico de validación de edad usando ciclos y control de errores.

Finalmente, se mostraron buenas prácticas para escribir bloques "try" más organizados y específicos.

### Tipos comunes

![evidencia template](/images/Tipos-comunes.png)

En esta parte se probaron diferentes excepciones comunes de Python para comprender cuándo ocurren y cómo manejarlas correctamente.

Se trabajaron errores relacionados con:

- Operaciones matemáticas ("ZeroDivisionError", "OverflowError").
- Tipos de datos ("TypeError", "ValueError").
- Índices y claves ("IndexError", "KeyError").
- Archivos ("FileNotFoundError", "PermissionError").
- Atributos y variables ("AttributeError", "NameError").
- Importaciones ("ImportError", "ModuleNotFoundError").

También se utilizó "Exception" para capturar errores generales e identificar el tipo exacto de excepción generada.

Finalmente, se realizaron ejemplos con la librería "requests" para manejar errores de conexión, tiempo de espera y errores HTTP.

### Else Finally

![evidencia template](/images/Else-finally.png)

En esta sección se trabajó el uso de las cláusulas "else" y "finally" junto al manejo de excepciones.

Se utilizó "else" para ejecutar código únicamente cuando no ocurría ningún error, por ejemplo al realizar divisiones o leer archivos correctamente.

Con "finally" se realizaron tareas que deben ejecutarse siempre, como cerrar archivos y mostrar mensajes finales del proceso.

También se trabajaron ejemplos prácticos relacionados con conexiones a bases de datos, restauración de estados y registro de finalización de tareas.

Además, se explicó el orden de ejecución entre "try", "except", "else" y "finally", así como el comportamiento de "return" dentro de estos bloques.

### Lanzar excepciones

![evidencia template](/images/Lanzar-excepciones.png)

En esta parte se aprendió a generar excepciones manualmente usando la instrucción "raise".

Se validaron datos antes de realizar operaciones, evitando errores futuros y mostrando mensajes personalizados.

Se implementaron ejemplos como:

- Validación de división entre cero.
- Validación de números negativos.
- Validación de tipos de datos.
- Verificación de conexión a internet.
- Validación de saldo bancario.

También se trabajó el relanzamiento de excepciones y la creación de excepciones personalizadas mediante clases heredadas de "Exception".

Finalmente, se aplicaron buenas prácticas para escribir mensajes de error más claros, específicos y útiles para el usuario.

## Desarrollo del reto

![evidencia template](/images/Reto.png)

Se desarrolló una función llamada dividir_numeros() capaz de:

- Solicitar dos números al usuario.
- Convertir los valores ingresados a enteros.
- Realizar una división.
- Manejar errores de conversión y división.
- Mostrar mensajes personalizados.
- Ejecutar un bloque finally.

La función implementada utiliza un bloque try para ejecutar las operaciones principales.

Primero solicita dos números usando input().

Luego convierte ambos datos a tipo entero utilizando int().

Posteriormente realiza la división entre los números ingresados.

Se implementaron dos excepciones específicas:

- ValueError: cuando el usuario introduce texto u otro valor inválido.
- ZeroDivisionError: cuando el segundo número es cero.

## Reflexión personal

El manejo de excepciones es una parte fundamental del desarrollo de software porque permite crear aplicaciones más seguras y estables.

Además, ayudan a mostrar mensajes claros al usuario y facilitan la depuración del código.

Durante esta actividad comprendí la importancia de validar correctamente los datos ingresados y capturar errores específicos en lugar de usar excepciones genéricas.

También aprendí cómo utilizar "raise" para generar excepciones personalizadas y mejorar el control de errores dentro de una aplicación.

Entonces, considero que el manejo adecuado de excepciones mejora considerablemente la calidad del software y permite desarrollar programas más profesionales y confiables.