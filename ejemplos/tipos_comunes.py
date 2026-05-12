# Excepciones relacionadas con operaciones matemáticas
try:
    resultado = 5 / 0
except ZeroDivisionError:
    print("No es posible dividir entre cero")

try:
    resultado = 10.0 ** 1000000  # Intentar calcular 10 elevado a un millón
except OverflowError:
    print("El número es demasiado grande para ser representado")

# Excepciones relacionadas con tipos de datos
try:
    resultado = "42" + 10  # Intentar sumar un string y un entero
except TypeError:
    print("No se pueden sumar tipos diferentes")

try:
    numero = int("abc")  # Intentar convertir una cadena no numérica a entero
except ValueError:
    print("La cadena no representa un número válido")

# Excepciones relacionadas con índices y claves
try:
    lista = [1, 2, 3]
    elemento = lista[10]  # Intentar acceder a un índice que no existe
except IndexError:
    print("El índice está fuera del rango de la lista")

try:
    diccionario = {"nombre": "Ana", "edad": 25}
    valor = diccionario["telefono"]  # Intentar acceder a una clave inexistente
except KeyError:
    print("La clave 'telefono' no existe en el diccionario")

# Excepciones relacionadas con archivos
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe")

try:
    with open("/etc/passwd", "w") as archivo:  # Intentar escribir en un archivo protegido
        archivo.write("datos")
except PermissionError:
    print("No tienes permisos para modificar este archivo")

# Excepciones relacionadas con atributos y nombres
try:
    texto = "Hola"
    longitud = texto.size  # El método correcto sería len(texto) o texto.__len__()
except AttributeError:
    print("El objeto string no tiene el atributo 'size'")

try:
    print(variable_no_definida)  # Intentar usar una variable que no existe
except NameError:
    print("La variable no está definida")

# Excepciones relacionadas con importaciones
try:
    import biblioteca_inexistente
except ImportError:
    print("No se pudo importar el módulo")

try:
    import modulo_que_no_existe
except ModuleNotFoundError:
    print("El módulo no existe")

# Jerarquía de excepciones
try:
    # Código que podría generar diferentes tipos de excepciones
    resultado = int("abc") / 0
except Exception as e:
    print(f"Se produjo un error:{type(e).__name__}")
    print(f"Descripción:{e}")

# Identificando el tipo de excepción
try:
    # Código que podría fallar
    resultado = eval(input("Introduce una expresión: "))
except Exception as e:
    print(f"Error de tipo:{type(e).__name__}")
    print(f"Descripción:{e}")

# Excepciones en bibliotecas externas
import requests

try:
    respuesta = requests.get("https://api.ejemplo.com/datos", timeout=1)
    respuesta.raise_for_status()  # Lanza una excepción si el código de estado HTTP es un error
except requests.exceptions.ConnectionError:
    print("No se pudo conectar al servidor")
except requests.exceptions.Timeout:
    print("La solicitud excedió el tiempo de espera")
except requests.exceptions.HTTPError as e:
    print(f"Error HTTP:{e}")