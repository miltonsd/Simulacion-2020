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
m= 10000  # Numero de tiradas
c= 10  # Numero de corridas
nroEvaluar= 12  # Numero para evaluar su frecuencia relativa

# Listas que guardan los datos de las "c" corridas de m tiradas
frecuencias= [[0 for x in range(m)] for y in range(c)]
medias= [[0 for x in range(m)] for y in range(c)]
desvios= [[0 for x in range(m)] for y in range(c)]
varianzas= [[0 for x in range(m)] for y in range(c)]

for i in range(0, c):
    datos= np.random.randint(0, 37, m)
    print(datos)
    for n in range(0, m):
        lista= datos[:n+1]
        frecuencias[i][n]= frecuenciaR(nroEvaluar, lista)
        medias[i][n]= lista.mean()
        desvios[i][n]= lista.std()
        varianzas[i][n]= lista.var()

# Grafico de las corridas
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[8, 6])

axs[0, 0].set_title('Frecuencia Relativa (fr)')
axs[0, 0].set(xlabel='Tiradas', ylabel='Frecuencia Relativa (fr)')
axs[0, 0].set_ylim(bottom=0, top=max(np.amax(frecuencias), frecuencia)+0.05)
for i in range(0, c):
    axs[0, 0].plot(range(1, m+1), frecuencias[i], label=str(i+1)+' corridas')
axs[0, 0].axhline(y=frecuencia, color='b', linestyle='-', label='fre')

axs[0, 1].set_title('Valor Promedio (vp)')
axs[0, 1].set(xlabel='Tiradas', ylabel='Valor Promedio (vp)')
axs[0, 1].set_ylim(bottom=0, top=max(np.amax(medias), esperanza)+1)
for i in range(0, c):
    axs[0, 1].plot(range(1, m+1), medias[i], label=str(i+1)+' corridas')
axs[0, 1].axhline(y=esperanza, color='b', linestyle='-', label='vpe')

axs[1, 0].set_title('Valor del Desvío (vd)')
axs[1, 0].set(xlabel='Tiradas', ylabel='Valor del Desvío (vd)')
axs[1, 0].set_ylim(bottom=0, top=max(np.amax(desvios), desvio)+1)
for i in range(0, c):
    axs[1, 0].plot(range(1, m+1), desvios[i], label=str(i+1)+' corridas')
axs[1, 0].axhline(y=desvio, color='b', linestyle='-', label='vde')

axs[1, 1].set_title('Valor de la Varianza (vve)')
axs[1, 1].set(xlabel='Tiradas', ylabel='Valor de la Varianza (vv)')
axs[1, 1].set_ylim(bottom=0, top=max(np.amax(varianzas), varianza)+10)
for i in range(0, c):
    axs[1, 1].plot(range(1, m+1), varianzas[i], label=str(i+1)+' corridas')
axs[1, 1].axhline(y=varianza, color='b', linestyle='-', label='vve')

for ax in axs.flat:
    ax.legend()
    ax.set_xlim(left=0, right=m)

plt.show()

# Listas que guardan los calculos generales de las corridas
freqGral= []
mediaGral= []
desvioGral= []
varianzaGral= []

for n in range(0, c):
    freqGral.insert(n, np.asarray(frecuencias[n]).mean())
    mediaGral.insert(n, np.asarray(medias[n]).mean())
    desvioGral.insert(n, np.asarray(desvios[n]).mean())
    varianzaGral.insert(n, np.asarray(varianzas[n]).mean())

# Graficas de los promedios
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[8, 6])

axs[0, 0].set_title('Frecuencia Relativa (fr)')
axs[0, 0].set(xlabel='Corridas', ylabel='Frecuencia Relativa (fr)')
axs[0, 0].set_ylim(bottom=0, top=max(np.amax(freqGral), frecuencia)+0.05)
axs[0, 0].plot(range(1, c+1), freqGral, color='r', label='fr promedio')
axs[0, 0].axhline(y=frecuencia, color='b', linestyle='-', label='fre')

axs[0, 1].set_title('Valor Promedio (vp)')
axs[0, 1].set(xlabel='Corridas', ylabel='Valor Promedio (vp)')
axs[0, 1].set_ylim(bottom=0, top=max(np.amax(mediaGral), esperanza)+1)
axs[0, 1].plot(range(1, c+1), mediaGral, color='r', label='vp promedio')
axs[0, 1].axhline(y=esperanza, color='b', linestyle='-', label='vpe')

axs[1, 0].set_title('Valor del Desvío (vd)')
axs[1, 0].set(xlabel='Corridas', ylabel='Valor del Desvío (vd)')
axs[1, 0].set_ylim(bottom=0, top=max(np.amax(desvioGral), desvio)+1)
axs[1, 0].plot(range(1, c+1), desvioGral, color='r', label='vd promedio')
axs[1, 0].axhline(y=desvio, color='b', linestyle='-', label='vde')

axs[1, 1].set_title('Valor de la Varianza (vve)')
axs[1, 1].set(xlabel='Corridas', ylabel='Valor de la Varianza (vv)')
axs[1, 1].set_ylim(bottom=0, top=max(np.amax(varianzaGral), varianza)+10)
axs[1, 1].plot(range(1, c+1), varianzaGral, color='r', label='vv promedio')
axs[1, 1].axhline(y=varianza, color='b', linestyle='-', label='vve')

for ax in axs.flat:
    ax.legend()
    ax.set_xlim(left=0, right=c)

plt.show()
