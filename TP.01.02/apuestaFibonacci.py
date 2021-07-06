import numpy as np
import matplotlib.pyplot as plt


# Datos Apuesta Fibonacci
cajaInicial= 10000 # Caja limitada
c= 5 # Numero de corridas
fr= 18/37 # Frecuencia relativa de que salga Par

# Generacion de la serie de Fibonacci con Apuesta= $200
fibo= []
n1= 0
n2= 1
for i in range (40):
  fibo.insert(i, 200*n2)
  nro= n1 + n2
  n1= n2
  n2= nro

# Apuesta Fibonacci: Par - Caja Limitada
fig, axs = plt.subplots(nrows=1, ncols=2, constrained_layout=True, figsize=[10, 5])
valMin= []
valMax= []
for i in range(0, c):
  caja= cajaInicial
  n= 0 # Tiradas
  f= 0 # Posicion en la serie de Fibonacci
  flujoCaja= [caja]
  frecuencias= [0]
  freqAbs= 0
  while (caja > 0) and (n < 300):
    n+= 1
    np.random.seed()
    datos= np.random.randint(0, 37)
    if (datos % 2) == 0:
      caja+= fibo[f]
      freqAbs+= 1
      if f >= 2:
        f-= 2
      else:
        f= 0
    else:
      caja-= fibo[f]
      f+= 1
    flujoCaja.insert(n, caja)
    frecuencias.insert(n, freqAbs/n)
  valMin.append(np.amin(flujoCaja))
  valMax.append(np.amax(flujoCaja))
  axs[0].plot(frecuencias)
  axs[1].plot(flujoCaja)
axs[0].axhline(y=fr, color='r', linestyle='-')
axs[0].set_title('Apuesta Fibonacci - Números Pares')
axs[0].set(xlabel='Tiradas (n)', ylabel='Frecuencia Relativa')
axs[0].set_ylim(bottom=0, top=1.02)
axs[1].axhline(y=cajaInicial, color='r', linestyle='-')
axs[1].set_title('Apuesta Fibonacci - Números Pares')
axs[1].set(xlabel='Tiradas (n)', ylabel='Flujo de Caja')
axs[1].set_ylim(bottom=np.amin(valMin)-1000, top=max(np.amax(valMax), cajaInicial)+1000)
plt.show()

# Apuesta Fibonacci: Par - Caja Ilimitada
fig, axs = plt.subplots(nrows=1, ncols=2, constrained_layout=True, figsize=[10, 5])
valMin= []
valMax= []
for i in range(0, c):
  ganancia= 0
  n= 0 # Tiradas
  f= 0 # Posicion en la serie de Fibonacci
  flujoGanancias= [0]
  frecuencias= [0]
  freqAbs= 0
  while (n < 300):
    n+= 1
    np.random.seed()
    datos= np.random.randint(0, 37)
    if (datos % 2) == 0:
      ganancia+= fibo[f]
      freqAbs+= 1
      if f >= 2:
        f-= 2
      else:
        f= 0
    else:
      ganancia-= fibo[f]
      f+= 1
    flujoGanancias.insert(n, ganancia)
    frecuencias.insert(n, freqAbs/n)
  valMin.append(np.amin(flujoGanancias))
  valMax.append(np.amax(flujoGanancias))
  axs[0].plot(frecuencias)
  axs[1].plot(flujoGanancias)    
axs[0].axhline(y=fr, color='r', linestyle='-')
axs[0].set_title('Caja Ilimitada - Apuesta Par')
axs[0].set(xlabel='Tiradas (n)', ylabel='Frecuencia Relativa')
axs[0].set_ylim(bottom=0, top=1.02)
axs[1].axhline(y=0, color='r', linestyle='-')
axs[1].set_title('Caja Ilimitada - Apuesta Par')
axs[1].set(xlabel='Tiradas (n)', ylabel='Flujo de Caja')
axs[1].set_ylim(bottom=min(np.amin(valMin), 0)-1000, top=max(np.amax(valMax), 0)+1000)
plt.show()