repeat=True
i=0
while repeat==True:
    nombre= input("Escribe Nombre: ")
    hoursDay= int(input("Horas trabajadas (por dia): "))
    DaysWeek= int(input("Dias trabajados (por semana): "))
    salary= int(input("Sueldo por hora: "))

    salaryWeek=DaysWeek*hoursDay*salary
    print(f'Sueldo por semana: {salaryWeek}$')
    salaryMonth=salaryWeek*4
    print(f'Sueldo por mes: {salaryMonth}$')

    if salaryMonth <=10000:
        print(f"{nombre} es obrero tipo A")
    elif salaryMonth < 10000 & salaryMonth >=15000:
        print(f"{nombre} es obrero tipo B")
    else:
        print(f"{nombre}no tiene categoria")

    i=i+1


    repeat=input("Desea agregar otra captura?")
    if repeat=="si":
        repeat=True
    elif repeat=="no":
        repeat=False


print(f"Se ingresaron {i}")