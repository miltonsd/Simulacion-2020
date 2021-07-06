import numpy as np
import math
import random
import matplotlib.pyplot as plt

#Parametros Entrada
limite = 100
cantDelayedMaximo = 1000
numeroEventos = 2
tasaArribo = 1.0
tasaPartida = 0.5
nClientes = 3
# Listas Promedios
promClientesSistema = []
promClientesCola = []
promEsperasSistema = []
promEsperasCola = []
promUsoServidor = []
promProbNClientes = []
tiempoTotal = []

def inicio():
  global time
  global servidor
  global cantCola
  global tiempoUltimoEvento
  global cantDelayed
  global totalDelays
  global areaQ
  global areaServidor
  global tiempoArribo
  global tiempoProximoEvento
  global plotClientesSistema
  global plotClientesCola
  global plotEsperasSistema
  global plotEsperasCola
  global plotUsoServidor
  global plotProbNClientes
  time = 0.0
  servidor = "D"
  cantCola = 0
  tiempoUltimoEvento = 0.0
  cantDelayed = 0
  totalDelays = 0.0
  areaQ = 0.0
  areaServidor = 0.0
  tiempoArribo = [0.0 for i in range(limite+1)]
  tiempoProximoEvento = [0.0, 0.0, 0.0]
  tiempoProximoEvento[1] = time + expo(tasaArribo)
  tiempoProximoEvento[2] = 1.0e+30
  plotClientesSistema = []
  plotClientesCola = []
  plotEsperasSistema = []
  plotEsperasCola = []
  plotUsoServidor = []
  plotProbNClientes = []

def timing():
  global time
  global tipoEventoProximo
  tiempoMinimoProximoEvento = 1.0e+29
  tipoEventoProximo = 0
  for i in range(1,numeroEventos+1):
    if (tiempoProximoEvento[i] < tiempoMinimoProximoEvento):
      tiempoMinimoProximoEvento = tiempoProximoEvento[i]
      tipoEventoProximo = i
  if (tipoEventoProximo == 0):
    print("Error. No hay próximo evento")
    exit()
  time = tiempoMinimoProximoEvento

def arribo():
  global servidor
  global cantCola
  global cantDelayed
  global totalDelays
  tiempoProximoEvento[1] = time + expo(tasaArribo)
  if (servidor == "O"):
    cantCola += 1
    if (cantCola > limite):
      print("Cola llena papa")
      exit()
    tiempoArribo[cantCola] = time
  else:
    delay = 0.0
    totalDelays += delay
    cantDelayed += 1
    servidor = "O"
    tiempoProximoEvento[2] = time + expo(tasaPartida)

def partida():
  global servidor
  global cantCola
  global cantDelayed
  global totalDelays
  if (cantCola == 0):
    servidor = "D"
    tiempoProximoEvento[2] = 1.0e+30
  else:
    cantCola -= 1
    delay = time -tiempoArribo[1]
    totalDelays += delay
    cantDelayed += 1
    tiempoProximoEvento[2] = time + expo(tasaPartida)
    for i in range(1,cantCola+1):
      tiempoArribo[i] = tiempoArribo[i+1]

def prints():
  print("Promedio de clientes en el sistema: ", round(L,4))
  print("Promedio de clientes en cola: ", round(Lq,4))
  print("Tiempo promedio espera en sistema: ", round(W,4), " minutos")
  print("Tiempo promedio espera en cola: ", round(Wq,4), " minutos")
  print("Utilizacion del Servidor: ", round(ro,4), "(", round(ro*100,4), "%)")
  print("Probabilidad de ",nClientes," clientes en cola: ", round(p,4), "(", round(p*100,4), "%)")

def actualizar_tiempos():
  global tiempoUltimoEvento
  global areaQ
  global areaServidor
  tiempoDesdeUltimoEvento = time - tiempoUltimoEvento
  tiempoUltimoEvento = time
  areaQ += cantCola * tiempoDesdeUltimoEvento
  if servidor == "O":
    serv = 1
  else:
    serv = 0
  areaServidor += serv * tiempoDesdeUltimoEvento

def expo(tasa):
  u = random.uniform(0,1)
  numero = -tasa * math.log(u)
  return numero

for n in range(10):
  inicio()
  while (cantDelayed < cantDelayedMaximo):
    timing()
    actualizar_tiempos()
    if (tipoEventoProximo == 1):
      arribo()
    elif (tipoEventoProximo == 2):
      partida()
    ro = areaServidor/time
    Wq = totalDelays/cantDelayed
    W = Wq + tasaPartida
    Lq = areaQ/time 
    L = tasaArribo * W
    p = math.pow(ro,nClientes) * (1-ro)
    plotClientesSistema.append(L)
    plotClientesCola.append(Lq)
    plotEsperasSistema.append(W)
    plotEsperasCola.append(Wq)
    plotUsoServidor.append(ro)
    plotProbNClientes.append(p)
  prints()
  promClientesSistema.append(L)
  promClientesCola.append(Lq)
  promEsperasSistema.append(W)
  promEsperasCola.append(Wq)
  promUsoServidor.append(ro)
  promProbNClientes.append(p)
  tiempoTotal.append(round(time,4))
  plt.figure(1)
  plt.title("Clientes en Sistema (tArribo= "+str(tasaArribo)+", tServicio= "+str(tasaPartida)+")")
  plt.plot(plotClientesSistema)
  plt.figure(2)
  plt.title("Clientes en cola (tArribo= "+str(tasaArribo)+", tServicio= "+str(tasaPartida)+")")
  plt.plot(plotClientesCola)
  plt.figure(3)
  plt.title("Tiempo promedio en Sistema (tArribo= "+str(tasaArribo)+", tServicio= "+str(tasaPartida)+")")
  plt.plot(plotEsperasSistema)
  plt.figure(4)
  plt.title("Tiempo promedio en Cola (tArribo= "+str(tasaArribo)+", tServicio= "+str(tasaPartida)+")")
  plt.plot(plotEsperasCola)
  plt.figure(5)
  plt.title("Utilización del Servidor (tArribo= "+str(tasaArribo)+", tServicio= "+str(tasaPartida)+")")
  plt.plot(plotUsoServidor)
  plt.figure(6)
  plt.title("Probabilidad de encontrar "+str(nClientes)+" clientes (tArribo= "+str(tasaArribo)+", tServicio= "+str(tasaPartida)+")")
  plt.plot(plotProbNClientes)
print("-------------------  RESULTADOS  -------------------")
print("Promedio de Clientes en Sistema: ",round(np.mean(promClientesSistema),4))
print("Promedio de Clientes en Cola: ",round(np.mean(promClientesCola),4))
print("Tiempo promedio esperas en sistema: ", round(np.mean(promEsperasSistema),4), " minutos")
print("Tiempo promedio esperas en cola: ", round(np.mean(promEsperasCola),4), " minutos")
print("Utilizacion del Servidor: ", round(np.mean(promUsoServidor),4), "(", round(np.mean(promUsoServidor)*100,4), "%)")
print("Probabilidad de ",nClientes," clientes en cola: ", round(np.mean(promProbNClientes),4), "(", round(np.mean(promProbNClientes)*100,4), "%)")
plt.show()