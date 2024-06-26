#tablas=[1,10]

for tablas in range (1,11):
    print(f"Tabla del {tablas}")
    for num2 in range(1,11):
        resultado=tablas*num2
        print(f"{tablas} x {num2} = {resultado}")
        