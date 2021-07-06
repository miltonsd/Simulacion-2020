import numpy as np
import scipy.stats as sp
import math

def testKS(datos, alfa):
  print("Prueba de Frecuencias - Prueba de Kolmogorov-Smirnov")
  datos = np.sort(datos)
  n = np.size(datos)
  d1 = []
  d2 = []
  for i in range(n):
    aux = (i+1)/n
    d1.insert(i, round(aux-datos[i], 4))
    d2.insert(i, round(datos[i]-(i/n), 4))
  d = max(np.amax(d1), np.amax(d2))
  valorCritico = sp.ksone.ppf(1-alfa/2, n)
  print("El valor estadístico es D = "+str(d))
  print("El valor estadístico de la tabla (con nivel de significancia α = "+str(alfa)+") es Dα = "+str(valorCritico))
  if valorCritico >= d:
    print("Aceptación de Ho: NO hay suficiente evidencia para rechazar la hipotesis (D < Dα)")
  else:
    print("Rechazo de Ho: HAY suficiente evidencia para rechazar la hipotesis (D > Dα)")

def testChiCuadrada(datos, alfa):
  print("Prueba de Frecuencias - Prueba Chi-Cuadrada")
  n = np.size(datos)
  m = 10 # nro de Intervalos, cada uno de longitud 0.1
  esperados  = [n/m, n/m, n/m, n/m, n/m, n/m, n/m, n/m, n/m, n/m]
  observados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for i in range(n):
    if datos[i] <= 0.1:
      observados[0]+= 1
    elif datos[i] <= 0.2:
      observados[1]+= 1
    elif datos[i] <= 0.3:
      observados[2]+= 1
    elif datos[i] <= 0.4:
      observados[3]+= 1
    elif datos[i] <= 0.5:
      observados[4]+= 1
    elif datos[i] <= 0.6:
      observados[5]+= 1
    elif datos[i] <= 0.7:
      observados[6]+= 1
    elif datos[i] <= 0.8:
      observados[7]+= 1
    elif datos[i] <= 0.9:
      observados[8]+= 1
    elif datos[i] <= 1.0:
      observados[9]+= 1
  f = []
  for i in range(m):
    f.insert(i, pow(observados[i]-esperados[i], 2)/esperados[i])
  estadistico = np.sum(f)
  valorCritico = sp.chi2.ppf(1-alfa, m-1)
  print("El valor estadístico es X² = "+str(estadistico))
  print("El valor estadístico de la tabla (con nivel de significancia α = "+str(alfa)+") es X²α = "+str(valorCritico))
  if valorCritico >= estadistico:
    print("Aceptación de Ho: NO hay suficiente evidencia para rechazar la hipotesis (X² < X²α)")
  else:
    print("Rechazo de Ho: HAY suficiente evidencia para rechazar la hipotesis (X² > X²α)")

def testPoker(datos, alfa):
  print("Prueba de Póker")
  n = np.size(datos)
  freqEsp = [n*0.3024, n*0.504, n*0.108, n*0.072, n*0.009, n*0.0045, n*0.0001]
  freqObs = [0, 0, 0, 0, 0, 0, 0]
  for i in range(n):
    lista = []
    for j in str(format(datos[i], '.5f'))[1:]:
      if j.isdigit():
        lista.append(j)
    u, veces = np.unique(lista, return_counts=True)
    if np.amax(veces) == 5:   # [6]: Quintilla
      freqObs[6]+= 1
    elif np.amax(veces) == 4: # [5]: Poker
      freqObs[5]+= 1
    elif np.amax(veces) == 3:
      if np.size(veces) == 2: # [4]: Full
        freqObs[4]+= 1
      else:                   # [3]: Tercia
        freqObs[3]+= 1
    elif np.amax(veces) == 2:
      if np.size(veces) == 3: # [2]: Dos Pares
        freqObs[2]+= 1
      else:                   # [1]: Un Par
        freqObs[1]+= 1
    else:                     # [0]: Diferentes
      freqObs[0]+= 1
  fe = []
  fo = []
  j = -1
  for i in range(np.size(freqEsp)):
    if freqEsp[i] >= 5:
      fe.append(freqEsp[i])
      fo.append(freqObs[i])
      j+= 1
    else:
      fe[j]+= freqEsp[i]
      fo[j]+= freqObs[i]
  f = []
  m = np.size(fe) # nro de intervalos
  for i in range(m):
    f.insert(i, pow((fe[i]-fo[i]), 2)/fe[i])
  estadistico = np.sum(f)
  valorCritico = sp.chi.ppf(1-alfa, m-1)
  print("El valor estadístico es X² = "+str(estadistico))
  print("El valor estadístico de la tabla (con nivel de significancia α = "+str(alfa)+") es X²α = "+str(valorCritico))
  if valorCritico >= estadistico:
    print("Aceptación de Ho: NO hay suficiente evidencia para rechazar la hipotesis (X² < X²α)")
  else:
    print("Rechazo de Ho: HAY suficiente evidencia para rechazar la hipotesis (X² > X²α)")

def testCorridas(datos, alfa):
  print("Prueba de corridas - Arriba y abajo de la media para numeros uniformes")
  n = np.size(datos)
  signos = []
  media = np.mean(datos)
  x1, x2 = 0, 0
  for i in range(0, n):
    if datos[i] > media:
      signos.append('+')
      x1 += 1
    if datos[i] < media:
      signos.append('-')
      x2 += 1
#  print(signos)
  corridas = 1
  for i in range(0, len(signos)-1):
    if signos[i] != signos[i+1]:
      corridas += 1
  mediaC = ((2*x1*x2)/(x1+x2))+1
  varianzaC = ((2*x1*x2)*(2*x1*x2-n))/(pow(n,2)*(n-1))
  desvio = math.sqrt(varianzaC) 
  print(f"Datos de la prueba: Media = {mediaC} - Varianza = {varianzaC} - Corridas = {corridas}")   
  z = abs((corridas - mediaC) / desvio)
  print(f"El Valor estadistico de prueba es Z = {z}")
  Ztabla = round(sp.norm.ppf(1-alfa/2), 3)
  print(f"El Valor estadistico de la tabla (con nivel de significacia α = {alfa}) es Zα = {Ztabla}")
  if  z < Ztabla:
      print("Aceptación de Ho: La hipotesis no puede ser rechazada  (Z < Zα)")
  if  z > Ztabla:
      print("Rechazo de Ho: La secuencia de números NO es independiente y por lo tanto la secuencia NO es aleatoria. (Z > Zα)")