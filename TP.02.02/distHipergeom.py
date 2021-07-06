import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def hipergeometrica(tn, ns, p, x):
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  aux = 0.0
  for i in range(ns):
    x = gcl.generaSemilla(x, a, c, m)
    r = x/m
    if r <= p:
      s = 1.0
      aux += 1.0
    else:
      s = 0.0
    p = (tn * p - s) / (tn - 1.0)
    tn = tn - 1.0
  nros.append(aux)  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x

nros = []  # Lista de las variables aleatorias
tn, ns, p, x = 100, 20, 0.6, 1234567  # poblacion, muestra, proporcion de poblacion, semilla
for i in range(2000):
  x = hipergeometrica(tn, ns, p, x)
print(nros)
print("-----------------------------------------------------------------------")
test.testChiCuadrada(nros, 0.05)