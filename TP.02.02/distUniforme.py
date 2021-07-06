import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def uniforme(a, b, x):
  va, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  x = gcl.generaSemilla(x, va, c, m)
  r = x/m
  nros.append(a + (b - a) * r)  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x

nros = []  # Lista de las variables aleatorias
a, b, x = 20, 25, 1234567
for i in range(2000):
  x = uniforme(a, b, x)
print(nros)
print("-----------------------------------------------------------------------")
test.testKS(nros, 0.05)