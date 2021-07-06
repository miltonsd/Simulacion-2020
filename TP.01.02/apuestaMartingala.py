import numpy as np
import matplotlib.pyplot as plt


# Datos Apuesta Martingala
cajaInicial= 10000 # Caja limitada
c= 5 # Numero de corridas
fr= 18/37 # Frecuencia relativa de que salga Negro

# Lista de numeros de la ruleta de color Negro
negro= [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

# Apuesta Martingala: Negro - Caja Limitada - Apuesta Base = $200
fig, axs = plt.subplots(nrows=1, ncols=2, constrained_layout=True, figsize=[10, 5])
valMin= []
valMax= []
for i in range(0, c):
  caja= cajaInicial
  n= 0 # Tiradas
  apuesta= 200
  flujoCaja= [caja]
  frecuencias= [0]
  freqAbs= 0
  while (caja > 0) and (n < 300):
    n+= 1
    np.random.seed()
    datos= np.random.randint(0, 37)
    if datos in negro:
      caja+= apuesta
      apuesta= 200
      freqAbs+= 1
    else:
      caja-= apuesta
      apuesta*= 2
    flujoCaja.insert(n, caja)
    frecuencias.insert(n, freqAbs/n)
  valMin.append(np.amin(flujoCaja))
  valMax.append(np.amax(flujoCaja))
  axs[0].plot(frecuencias)
  axs[1].plot(flujoCaja)
axs[0].axhline(y=fr, color='r', linestyle='-')
axs[0].set_title('Apuesta Martingala - Negro')
axs[0].set(xlabel='Tiradas (n)', ylabel='Frecuencia Relativa')
axs[0].set_ylim(bottom=0, top=1.02)
axs[1].axhline(y=cajaInicial, color='r', linestyle='-')
axs[1].set_title('Apuesta Martingala - Negro')
axs[1].set(xlabel='Tiradas (n)', ylabel='Flujo de Caja')
axs[1].set_ylim(bottom=np.amin(valMin)-1000, top=max(np.amax(valMax), cajaInicial)+1000)
plt.show()

# Apuesta Martingala: Negro - Caja Ilimitada - Apuesta Base = $200
fig, axs = plt.subplots(nrows=1, ncols=2, constrained_layout=True, figsize=[10, 5])
valMin= []
valMax= []
for i in range(0, c):
  ganancia= 0
  n= 0 # Tiradas
  apuesta= 200 
  flujoGanancias= [ganancia]
  frecuencias= [0]
  freqAbs= 0
  while (n < 300):
    n+= 1
    np.random.seed()
    datos= np.random.randint(0, 37)
    if datos in negro:
      ganancia+= apuesta
      apuesta= 200
      freqAbs+= 1
    else:
      ganancia-= apuesta
      apuesta*= 2
    flujoGanancias.insert(n, ganancia)
    frecuencias.insert(n, freqAbs/n)
  valMin.append(np.amin(flujoGanancias))
  valMax.append(np.amax(flujoGanancias))
  axs[0].plot(frecuencias)
  axs[1].plot(flujoGanancias)    
axs[0].axhline(y=fr, color='r', linestyle='-')
axs[0].set_title('Apuesta Martingala - Negro')
axs[0].set(xlabel='Tiradas (n)', ylabel='Apuesta Martingala - Negro')
axs[0].set_ylim(bottom=0, top=1.02)
axs[1].axhline(y=0, color='r', linestyle='-')
axs[1].set_title('Apuesta Martingala - Negro')
axs[1].set(xlabel='Tiradas (n)', ylabel='Flujo de Caja')
axs[1].set_ylim(bottom=min(np.amin(valMin), 0)-1000, top=max(np.amax(valMax), 0)+1000)
plt.show()