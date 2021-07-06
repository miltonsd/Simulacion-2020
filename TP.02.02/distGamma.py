import math
import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def gamma(k, alfa, x):
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  tr = 1.0
  for i in range(k):
    x = gcl.generaSemilla(x, a, c, m)
    r = x/m
    tr = tr * r
  nros.append(- math.log(tr)/alfa)  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x

nros = []  # Lista de las variables aleatorias
k, alfa, x = 3, 1.62, 1234567
for i in range(2000):
  x = gamma(k, alfa, x)
print(nros)
print("-----------------------------------------------------------------------")
test.testKS(nros, 0.05)