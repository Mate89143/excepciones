# La cláusula else
try:
    numero = int(input("Introduce un número: "))
    resultado = 100 / numero
except ValueError:
    print("Debes introducir un número válido.")
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
else:
    print(f"El resultado es:{resultado}")
    # Este código solo se ejecuta si no hubo excepciones

# Casos de uso prácticos para else
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
    contenido = ""
else:
    print("Archivo leído correctamente.")
    archivo.close()  # Solo cerramos si se abrió con éxito

# try:
#     datos = obtener_datos_de_api()
#     validar_formato(datos)
# except ConexionError:
#     print("No se pudo conectar con el servidor.")
# except FormatoInvalidoError:
#     print("Los datos recibidos tienen un formato incorrecto.")
# else:
#     # Solo procesamos si obtuvimos y validamos los datos correctamente
#     resultados = procesar_datos(datos)
#     guardar_resultados(resultados)

# La cláusula finally
try:
    archivo = open("registro.txt", "w")
    archivo.write("Operación iniciada\n")
    # Código que podría generar una excepción
    resultado = 10 / int(input("Introduce un número: "))
    archivo.write(f"Resultado:{resultado}\n")
except ZeroDivisionError:
    archivo.write("Error: División por cero\n")
except ValueError:
    archivo.write("Error: Valor no válido\n")
finally:
    archivo.write("Operación finalizada\n")
    archivo.close()  # El archivo se cierra siempre
    print("Proceso completado")

# Casos de uso prácticos para finally
# conexion = None
# try:
#     conexion = conectar_a_base_de_datos()
#     datos = conexion.ejecutar_consulta("SELECT * FROM usuarios")
#     procesar_datos(datos)
# except ConexionError:
#     print("Error al conectar con la base de datos")
# except ConsultaError:
#     print("Error al ejecutar la consulta")
# finally:
#     if conexion:
#         conexion.cerrar()  # La conexión se cierra siempre

# modo_original = sistema.obtener_modo()
# try:
#    sistema.cambiar_modo("mantenimiento")
#    realizar_actualizacion()
# except ActualizacionError:
#    print("La actualización falló")
# finally:
#    sistema.cambiar_modo(modo_original)  # Restauramos el modo original

# try:
#    registrar_inicio("tarea_diaria")
#    ejecutar_tarea_diaria()
# except Exception as e:
#    registrar_error("tarea_diaria", str(e))
# finally:
#    registrar_finalizacion("tarea_diaria")  # Siempre registramos que terminó

# Combinando else y finally
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe, se creará uno nuevo.")
    archivo = open("datos.txt", "w")
    archivo.write("Archivo creado automáticamente")
else:
    print(f"Contenido leído:{contenido}")
    # Este código solo se ejecuta si no hubo excepciones
finally:
    print("Operación de archivo completada.")
    archivo.close()  # El archivo se cierra siempre, se haya abierto para leer o escribir

# Orden de ejecución
def demostrar_orden():
    try:
        print("1. Ejecutando bloque try")
        # Descomentar para generar una excepción:
        # x = 1 / 0
    except ZeroDivisionError:
        print("2. Ejecutando bloque except")
    else:
        print("3. Ejecutando bloque else")
    finally:
        print("4. Ejecutando bloque finally")

    print("5. Continuando después del bloque try")

demostrar_orden()

# Consideraciones importantes
def dividir(a, b):
    try:
        resultado = a / b
        return resultado  # Este return no se ejecuta inmediatamente
    except ZeroDivisionError:
        print("Error: División por cero")
        return None  # Este return tampoco se ejecuta inmediatamente
    finally:
        print("División finalizada")  # Esto se ejecuta antes de cualquier return
        # Ahora sí se devuelve el valor correspondiente

print(dividir(10, 2))  # Imprime "División finalizada" y luego 5.0
print(dividir(10, 0))  # Imprime "Error: División por cero", "División finalizada" y luego None

try:
    1 / 0  # Genera ZeroDivisionError
except ZeroDivisionError:
    print("Capturada división por cero")
    # La excepción ha sido manejada
finally:
    # Si descomentas la siguiente línea, el ZeroDivisionError original se perderá
    # y será reemplazado por este ValueError
    # int("abc")  # Genera ValueError
    print("Bloque finally ejecutado")