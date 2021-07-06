import math
import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def binomial(n, p, x):
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  aux = 0.0
  for i in range(n):
    x = gcl.generaSemilla(x, a, c, m)
    r = x/m
    if r <= p:
      aux += 1.0
  nros.append(aux)  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x

nros = []  # Lista de las variables aleatorias
n, p, x = 40, 0.4, 1234567  # ensayos, probabilidad de exito, semilla
for i in range(2000):
  x = binomial(n, p, x)
print(nros)
print("-----------------------------------------------------------------------")
test.testChiCuadrada(nros, 0.05)