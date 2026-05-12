try:
    numero1 = 10
    numero2 = 0
    resultado = numero1 / numero2
    print(f"El resultado es:{resultado}")
except:
    print("¡Ups! No se puede dividir entre cero.")

# Capturando excepciones específicas
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
    print(f"100 dividido por{numero} es{resultado}")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes introducir un número válido.")

# Accediendo a la información de la excepción
try:
    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError as error:
    print(f"Error:{error}")
    print("Creando un archivo nuevo...")
    with open("archivo_inexistente.txt", "w") as archivo:
        archivo.write("Este es un archivo nuevo")

# Combinando múltiples excepciones
try:
    # Intentamos abrir y leer un archivo
    archivo = open("datos.txt", "r")
    valor = int(archivo.readline().strip())
    resultado = 100 / valor
except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    print(f"Ocurrió un error:{type(e).__name__}")
    print(f"Descripción:{e}")

# Uso práctico en aplicaciones reales
def obtener_edad():
    while True:
        try:
            edad = int(input("¿Cuál es tu edad? "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                continue
            return edad
        except ValueError:
            print("Por favor, introduce un número entero.")

# Uso de la función
edad_usuario = obtener_edad()
print(f"Tu edad es:{edad_usuario}")

# Buenas prácticas
# Mal ejemplo: bloque try demasiado grande
# try:
#     archivo = open("datos.txt", "r")
#     contenido = archivo.read()
#     numeros = [int(x) for x in contenido.split()]
#     resultado = sum(numeros) / len(numeros)
#     print(f"El promedio es:{resultado}")
#     archivo.close()
# except:
#     print("Ocurrió un error")
#
# # Buen ejemplo: bloques try específicos
# try:
#     archivo = open("datos.txt", "r")
# except FileNotFoundError:
#     print("El archivo 'datos.txt' no existe")
#     return
#
# try:
#     contenido = archivo.read()
#     numeros = [int(x) for x in contenido.split()]
# except ValueError:
#     print("El archivo contiene datos que no son números")
#     archivo.close()
#     return
#
# try:
#     resultado = sum(numeros) / len(numeros)
#     print(f"El promedio es:{resultado}")
# except ZeroDivisionError:
#     print("El archivo está vacío, no se puede calcular el promedio")
#
# archivo.close()