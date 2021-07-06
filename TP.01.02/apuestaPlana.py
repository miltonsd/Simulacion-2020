import numpy as np
import matplotlib.pyplot as plt

# Datos Apuesta Plana
cajainicial = 10000 
apuesta = 200 # Apuesta Constante
c = 5 #Cantidad de corridas

# Apuesta Plana y Impares
for i in range(0, c):
    
    caja = 10000
    n = 0 #Tiradas
    flujocaja= []
    flujocaja.insert(n, caja)

    while (caja > 0) and (n<300) :
        np.random.seed()
        datos= np.random.randint(0, 37)
        if ((datos % 2) == 0):
            caja = (caja-apuesta)
            n=n+1
            flujocaja.insert(n, caja)
        elif ((datos % 2) != 0):
            caja = (caja+apuesta)
            n=n+1
            flujocaja.insert(n, caja)

    print(caja)
    print(n)
    plt.plot(flujocaja)




plt.axhline(y=cajainicial, color='r', linestyle='-', label='Caja Inicial')
plt.title("Apuesta Plana - Numeros Impares")   
plt.xlabel("Tiradas (n)")   
plt.ylabel("Flujo de Caja")   
plt.show()

# Apuesta Plana y al numero 4
for i in range(0, c):
    
    caja = 10000
    n = 0 #Tiradas
    flujocaja= []
    flujocaja.insert(n, caja)
    frecabs = 0
    frecrel = 0

    while (caja > 0) and (n<300) :
        np.random.seed()
        datos= np.random.randint(0, 37)
        if (datos != 4):
            caja = (caja-apuesta)
            n=n+1
            flujocaja.insert(n, caja)
        elif (datos == 4):
            caja = (caja+(apuesta*36))
            frecabs = frecabs + 1
            n=n+1
            flujocaja.insert(n, caja)

    frecrel=frecabs/n
    print(frecabs)
    print(frecrel)
    print(caja)
    print(n)
    plt.plot(flujocaja)


plt.axhline(y=cajainicial, color='r', linestyle='-', label='Caja Inicial')
plt.title("Apuesta Plana - Apuesta Sencilla (x=4)")   
plt.xlabel("Tiradas (n)")   
plt.ylabel("Flujo de Caja")   
plt.show()

# Apuesta Plana y a la 2da docena
for i in range(0, c):
    
    caja = 10000
    n = 0 #Tiradas
    flujocaja= []
    flujocaja.insert(n, caja)
    frecabs = 0
    frecrel = 0

    while (caja > 0) and (n<300) :
        np.random.seed()
        datos= np.random.randint(0, 37)
        if (datos < 13) or (datos > 24):
            caja = (caja-apuesta)
            n=n+1
            flujocaja.insert(n, caja)
        elif (datos >= 13) and (datos <= 24):
            caja = (caja+(apuesta*3))
            frecabs = frecabs + 1
            n=n+1
            flujocaja.insert(n, caja)

    frecrel=frecabs/n
    print(frecabs)
    print(frecrel)
    print(caja)
    print(n)
    plt.plot(flujocaja)


plt.axhline(y=cajainicial, color='r', linestyle='-', label='Caja Inicial')
plt.title("Apuesta Plana - Apuesta por docena")   
plt.xlabel("Tiradas (n)")   
plt.ylabel("Flujo de Caja")   
plt.show()

# Apuesta Plana y Caja ilimitada
for i in range(0, c):
    
    caja = 10000
    n = 0 #Tiradas
    flujocaja= []
    flujocaja.insert(n, caja)
    frecabs = 0
    frecrel = 0

    while n < 2000 :
        np.random.seed()
        datos= np.random.randint(0, 37)
        if ((datos % 2) == 0):
            caja = (caja-apuesta)
            n=n+1
            flujocaja.insert(n, caja)
        elif ((datos % 2) != 0):
            caja = (caja+apuesta)
            n=n+1
            flujocaja.insert(n, caja)

    frecrel=frecabs/n
    print(frecabs)
    print(frecrel)
    print(caja)
    print(n)
    plt.plot(flujocaja)


plt.axhline(y=cajainicial, color='r', linestyle='-', label='Caja Inicial')
plt.title("Caja ilimitada - Apuesta Impar")   
plt.xlabel("Tiradas (n)")   
plt.ylabel("Flujo de Caja")   
plt.show()
