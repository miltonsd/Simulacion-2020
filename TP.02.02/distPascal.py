import math
import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def pascal(k, q, x):
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  tr = 1.0
  qr = math.log(q)
  for i in range(k):
    x = gcl.generaSemilla(x, a, c, m)
    r = x/m
    tr = tr * r
  nx = math.log(tr)/qr
  nros.append(math.floor(nx))  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x

nros = []  # Lista de las variables aleatorias
k, q, x = 6, 0.48, 1234567  # exitos, probabilidad de fracaso, semilla
for i in range(2000):
  x = pascal(k, q, x)
print(nros)
print("-----------------------------------------------------------------------")
test.testChiCuadrada(nros, 0.05)