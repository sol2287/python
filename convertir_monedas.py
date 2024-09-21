import os
import sys

def clear():
    if os.name == "posix": 
        os.system("clear")
    elif os.name in ["ce", "nt", "dos"]:
        os.system("cls")

# Función principal de conversión de monedas
def convertir_monedas():
    # Tipos de cambio (pueden variar)
    tasa_peso_dolar = 0.055  # 1 peso = 0.055 dólares (Ejemplo)
    tasa_dolar_peso = 18.0   # 1 dólar = 18 pesos (Ejemplo)

    while True:
        clear()  # Limpiar pantalla al iniciar cada ciclo del menú
        print("Conversor de Monedas")
        print("1 = Pesos a Dólares")
        print("2 = Dólares a Pesos")
        print("3 = salir")

        opcion = input("Elija una opción (1 , 2 o 3): ").lower()

        if opcion == "1":
            try:
                pesos = float(input("Introduce la cantidad en pesos:\n"))
                dolares = pesos * tasa_peso_dolar
                print(f"{pesos} pesos son {dolares:.2f} dólares.")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
            input("Presiona Enter para regresar al menú principal...")
            clear()

        elif opcion == "2":
            try:
                dolares = float(input("Introduce la cantidad en dólares:\n"))
                pesos = dolares * tasa_dolar_peso
                print(f"{dolares} dólares son {pesos:.2f} pesos.")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
            input("Presiona Enter para regresar al menú principal...")
            clear()

        elif opcion == "3":
            print("Gracias por usar el conversor. ¡Hasta luego!")
            sys.exit()

        else:
            print("Opción no válida. Selecciona una opción correcta.")
            input("Presiona Enter para regresar al menú principal...")
            clear()

if __name__ == "__main__":
    convertir_monedas()