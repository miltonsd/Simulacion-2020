import math
import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def poisson(p, x):
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  aux = 0.0
  b = math.exp(-p)
  tr = 1.0
  while tr >= b:
    x = gcl.generaSemilla(x, a, c, m)
    r = x/m
    tr = tr * r
    if tr >= b:
      aux += 1.0
  nros.append(aux)  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x

nros = []  # Lista de las variables aleatorias
p, x = 6, 1234567  # parametro lambda, semilla
for i in range(1000):
  x = poisson(p, x)
print(nros)
print("-----------------------------------------------------------------------")
test.testChiCuadrada(nros, 0.05)