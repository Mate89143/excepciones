def dividir_numeros():
    try:
        # Solicitar al usuario que introduzca dos números
        numero1 = input("Introduce el primer número: ")
        numero2 = input("Introduce el segundo número: ")

        # Convertir las entradas a números enteros
        numero1 = int(numero1)
        numero2 = int(numero2)

        # Realizar la división del primer número entre el segundo
        resultado = numero1 / numero2

        # Mostrar el resultado
        print(f"El resultado de la división es: {resultado}")

        # Devolver el resultado
        return resultado

    except ValueError:
        print("Error: Debes introducir un número válido")

    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")

    finally:
        print("Operación finalizada")


# Llamada a la función
dividir_numeros()