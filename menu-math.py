def sumar():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print(f"Resultado: {a + b}")

def restar():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    print(f"Resultado: {a - b}")

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    main()