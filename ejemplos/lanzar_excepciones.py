# Usando la instrucción raise
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")
    return a / b

try:
    resultado = dividir(10, 0)
except ZeroDivisionError as e:
    print(f"Error:{e}")

# Cuándo lanzar excepciones
def calcular_raiz_cuadrada(numero):
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return numero ** 0.5

def procesar_respuesta(respuesta):
    if respuesta.codigo == 200:
        return respuesta.datos
    elif respuesta.codigo == 404:
        return None
    else:
        raise RuntimeError(f"Código de respuesta no manejado:{respuesta.codigo}")
    
def retirar_dinero(cuenta, cantidad):
    if not cuenta.esta_activa:
        raise ValueError("La cuenta no está activa")

    if cantidad <= 0:
        raise ValueError("La cantidad debe ser positiva")

    if cantidad > cuenta.saldo:
        raise ValueError("Saldo insuficiente")

    cuenta.saldo -= cantidad
    return cuenta.saldo

# Tipos de excepciones comunes para lanzar
def establecer_edad(edad):
    if not isinstance(edad, int):
        raise TypeError("La edad debe ser un número entero")
    if edad < 0 or edad > 150:
        raise ValueError("La edad debe estar entre 0 y 150 años")
    return edad

def concatenar(texto, repeticiones):
    if not isinstance(texto, str):
        raise TypeError("El primer argumento debe ser una cadena de texto")
    if not isinstance(repeticiones, int):
        raise TypeError("El segundo argumento debe ser un número entero")
    return texto * repeticiones

def conectar_a_servidor():
    if not hay_conexion_internet():
        raise RuntimeError("No hay conexión a Internet")
    # Código para conectar al servidor

# Relanzando excepciones
def procesar_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError as e:
        print(f"Registrando error:{e}")
        raise  # Relanza la última excepción

def obtener_configuracion(archivo):
    try:
        with open(archivo, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigurationError(f"Archivo de configuración no encontrado:{archivo}") from e
    
# Creando excepciones personalizadas
class SaldoInsuficienteError(Exception):
    """Se lanza cuando se intenta retirar más dinero del disponible."""

    def __init__(self, saldo, cantidad):
        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo
        mensaje = f"No hay suficiente saldo. Saldo:{saldo}, Cantidad solicitada:{cantidad}"
        super().__init__(mensaje)

def retirar(cuenta, cantidad):
    if cantidad > cuenta.saldo:
        raise SaldoInsuficienteError(cuenta.saldo, cantidad)
    cuenta.saldo -= cantidad
    return cuenta.saldo

# Buenas prácticas al lanzar excepciones
# Poco útil
# raise ValueError("Fecha inválida")

# Mejor
# raise ValueError("La fecha '2023-13-45' no es válida. El formato debe ser YYYY-MM-DD")

# Demasiado genérico
# if not os.path.exists(ruta):
#    raise Exception("Problema con el archivo")

# Mejor
# if not os.path.exists(ruta):
#    raise FileNotFoundError(f"No se encontró el archivo:{ruta}")

# def procesar_datos(datos):
    # Validación al inicio
#    if datos is None:
#        raise ValueError("Los datos no pueden ser None")
#    if not isinstance(datos, list):
#        raise TypeError("Los datos deben ser una lista")
#    if len(datos) == 0:
#        raise ValueError("La lista de datos no puede estar vacía")

    # Procesamiento principal
#    resultado = []
#    for item in datos:

# def conectar_base_datos(host, puerto, usuario, contraseña):
#     """
#     Establece conexión con la base de datos.
#
#     Args:
#         host (str): Dirección del servidor
#         puerto (int): Puerto de conexión
#         usuario (str): Nombre de usuario
#         contraseña (str): Contraseña de acceso
#
#     Returns:
#         Conexión a la base de datos
#
#     Raises:
#         ConnectionError: Si no se puede establecer la conexión
#         AuthenticationError: Si las credenciales son incorrectas
#         TimeoutError: Si la conexión tarda demasiado tiempo
#     """
#     # Implementación

# Ejemplo práctico: Validación de entrada de usuario
def obtener_edad():
    while True:
        try:
            entrada = input("Introduce tu edad: ")

            if not entrada.strip():
                raise ValueError("La entrada no puede estar vacía")

            edad = int(entrada)

            if edad < 0:
                raise ValueError("La edad no puede ser negativa")

            if edad > 120:
                raise ValueError("La edad parece demasiado alta")

            return edad

        except ValueError as e:
            if str(e).startswith("invalid literal for int"):
                print("Por favor, introduce un número válido")
            else:
                print(f"Error:{e}")

# Uso
try:
    edad_usuario = obtener_edad()
    print(f"Tu edad es:{edad_usuario}")
except KeyboardInterrupt:
    print("\nOperación cancelada por el usuario")
    
