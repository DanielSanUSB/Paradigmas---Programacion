a = 0
b = 0
c = 0

while True:

    print("\nCalculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    menu = int(input("Seleccione una opcion: "))

    if menu == 1:
        print("Suma")
        a = int(input("Ingrese primer valor: "))
        b = int(input("Ingrese segundo valor: "))
        c = a + b
        print("Resultado:", c)

    elif menu == 2:
        print("Resta")
        a = int(input("Ingrese primer valor: "))
        b = int(input("Ingrese segundo valor: "))
        c = a - b
        print("Resultado:", c)

    elif menu == 3:
        print("Multiplicacion")
        a = int(input("Ingrese primer valor: "))
        b = int(input("Ingrese segundo valor: "))
        c = a * b
        print("Resultado:", c)

    elif menu == 4:
        print("Division")
        a = int(input("Ingrese primer valor: "))
        b = int(input("Ingrese segundo valor: "))
        c = a / b
        print("Resultado:", c)

    elif menu == 5:
        print("Saliendo...")
        break

    else:
        print("Opcion invalida")