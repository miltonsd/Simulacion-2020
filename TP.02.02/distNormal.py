import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def normal(x, mu, sigma):
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  suma = 0.0
  aux = []
  for i in range(12):
    x = gcl.generaSemilla(x, a, c, m)
    r = x/m
    aux.append(r)
    suma += r
  nros.append(sigma * (suma - 6.0) + mu)  # Guarda la variable aleatoria generada
  return x  # Devuelve la ultima semilla x


nros = []  # Lista de las variables aleatorias
mu, sigma, x = 0, 1, 1234567
for i in range(2000):
  x = normal(x, mu, sigma)
print(nros)
print("-----------------------------------------------------------------------")
test.testKS(nros, 0.05)