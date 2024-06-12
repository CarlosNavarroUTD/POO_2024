n=[0]
i=1
for numero in range(1,25):
    if numero % 2 == 0:
        n.insert(i,numero)
        num= n[i] + n[i-1] + n[i-2] 
        i=i+1
        if num == 60:
            print(n[i-3])