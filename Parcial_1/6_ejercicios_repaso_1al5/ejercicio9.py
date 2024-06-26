def solicitar_numeros():
    while True:
        numero = int(input("Ingrese un número (o ingrese 111 para salir): "))
        if numero == 111:
            print("Saliendo del programa...")
            break
        else:
            print(f"El número ingresado es: {numero}")

solicitar_numeros()