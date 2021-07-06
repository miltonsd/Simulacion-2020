import numpy as np
import matplotlib.pyplot as plt


def frecuenciaR(nro, valores):
    freqAbs = 0
    for n in valores:
        if n == nro:
            freqAbs+= 1
    freqRel= freqAbs/len(valores)
    return freqRel


# Datos de la ruleta
frecuencia= 1/37
esperanza= np.arange(0, 37).mean()
desvio= np.arange(0, 37).std()
varianza= np.arange(0, 37).var()

# Numeros generados aleatoriamente
np.random.seed(1)
m= 50  # Numero de tiradas [10, 50, 200, 1000, 5000, 10000, 25000, 35000, 50000]
datos= np.random.randint(0, 37, m)

#nroEvaluar= int(input("Ingrese numero para evaluar: "))
nroEvaluar= 12

# Listas que guardan los datos de las m tiradas
frecuencias= []
medias= []
desvios= []
varianzas= []

for n in range(0, m):
    lista= datos[:n+1]
    frecuencias.insert(n, frecuenciaR(nroEvaluar, lista))
    medias.insert(n, lista.mean())
    desvios.insert(n, lista.std())
    varianzas.insert(n, lista.var())
print(frecuencias)

# Grafico
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[9, 6.75])

axs[0, 0].set_title('Frecuencia Relativa (fr)')
axs[0, 0].set(xlabel='Tiradas', ylabel='Frecuencia Relativa (fr)')
axs[0, 0].set_ylim(bottom=0, top=max(np.amax(frecuencias), frecuencia)+0.05)
axs[0, 0].plot(range(1, m+1), frecuencias, color='r', label='fr con respecto a las tiradas')
axs[0, 0].axhline(y=frecuencia, color='b', linestyle='-', label='fr esperada')

axs[0, 1].set_title('Valor Promedio (vp)')
axs[0, 1].set(xlabel='Tiradas', ylabel='Valor Promedio (vp)')
axs[0, 1].set_ylim(bottom=0, top=max(np.amax(medias), esperanza)+1)
axs[0, 1].plot(range(1, m+1), medias, color='r', label='vp de las tiradas')
axs[0, 1].axhline(y=esperanza, color='b', linestyle='-', label='vp esperado')

axs[1, 0].set_title('Valor del Desvío (vd)')
axs[1, 0].set(xlabel='Tiradas', ylabel='Valor del Desvío (vd)')
axs[1, 0].set_ylim(bottom=0, top=max(np.amax(desvios), desvio)+1)
axs[1, 0].plot(range(1, m+1), desvios, color='r', label='vd en las tiradas')
axs[1, 0].axhline(y=desvio, color='b', linestyle='-', label='vd eesperado')

axs[1, 1].set_title('Valor de la Varianza (vv)')
axs[1, 1].set(xlabel='Tiradas', ylabel='Valor de la Varianza (vv)')
axs[1, 1].set_ylim(bottom=0, top=max(np.amax(varianzas), varianza)+10)
axs[1, 1].plot(range(1, m+1), varianzas, color='r', label='varianza en las tiradas')
axs[1, 1].axhline(y=varianza, color='b', linestyle='-', label='varianza esperada')

for ax in axs.flat:
    ax.legend()
    ax.set_xlim(left=0, right=m)

plt.show()
