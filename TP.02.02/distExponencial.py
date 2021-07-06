import math
import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def exponencial(esperanza, x):
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  x = gcl.generaSemilla(x, a, c, m)
  r = x/m
  nros.append(- esperanza * (math.log(r)))  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x

nros = []  # Lista de las variables aleatorias
esperanza, x = 0.9, 1234567
for i in range(2000):
  x = exponencial(esperanza, x)
print(nros)
print("-----------------------------------------------------------------------")
test.testKS(nros, 0.05)