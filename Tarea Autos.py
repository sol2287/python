import os

# Clase Padre
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")


# Clase Hija para Autos
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas,color):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.color= color

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de Puertas: {self.numero_puertas}")
        print(f"color : {self.color}")

# Clase Hija para Camiones
class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Capacidad de Carga: {self.capacidad_carga} toneladas")
def limpiar_consola():
    # 'cls' para Windows y 'clear' para otros sistemas
    os.system('cls' if os.name == 'nt' else 'clear')


# Función para ingresar los datos de un Auto
def ingresar_auto():
    limpiar_consola()
    print("\n--- Ingresar Datos del Auto ---")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = input("Año: ")
    numero_puertas = int(input("Número de Puertas: "))
    color =input("color: ")
    auto = Auto(marca, modelo, año, numero_puertas,color)
    print("\nInformación del Auto Ingresado:")
    auto.mostrar_info()
    input("\nPresione Enter para volver al menú principal...")


# Función para ingresar los datos de un Camion
def ingresar_camion():
    limpiar_consola()
    print("\n--- Ingresar Datos del Camion ---")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = input("Año: ")
    capacidad_carga = float(input("Capacidad de Carga (en toneladas): "))
    camion = Camion(marca, modelo, año, capacidad_carga)
    print("\nInformación del Camion Ingresado:")
    camion.mostrar_info()
    input("\nPresione Enter para volver al menú principal...")


# Función para mostrar el menú principal
def menu_principal():
    while True:
        limpiar_consola()
        print("--- Menú Principal ---")
        print("1. Ingresar un Auto")
        print("2. Ingresar un Camion")
        print("3. Salir")
        opcion = input("Seleccione una opción (1, 2 o 3): ")

        if opcion == "1":
            ingresar_auto()
        elif opcion == "2":
            ingresar_camion()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
            input("Presione Enter para continuar...")

# Ejecución del programa
menu_principal()