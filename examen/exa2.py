# Índice de Masa Corporal (IMC)
opcion = ""
while opcion != "NO":
    print("Vamos a calcular tu IMC")

    try:
        peso = float(input("Por favor, introduce tu peso en kilogramos: "))
        estatura = float(input("Por favor, introduce tu estatura en metros: "))

        print(f"Tu peso es: {peso} kg")
        print(f"Tu estatura es: {estatura} m")

        imc = peso / (estatura ** 2)
        print(f"Tu IMC es: {imc:.2f}")

        if imc < 18.5:
            print("Composición corporal: Peso inferior al normal")
        elif 18.5 <= imc < 25:
            print("Composición corporal: Normal")
        elif 25 <= imc < 30:
            print("Composición corporal: Peso superior al normal")
        else:
            print("Composición corporal: Obesidad")
    except ValueError:
        print("Entrada no válida. Por favor, introduce números para el peso y la estatura.")

    opcion = input("¿Quieres calcular otro IMC? [SI/NO]: ").strip().upper()
