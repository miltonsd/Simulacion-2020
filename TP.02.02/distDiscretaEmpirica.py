import generadorCongruencialLineal as gcl
import testsPseudoaleatorios as test

def empirica(x):
  pj = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]  
  a, c, m = 1093, 18257, 3594325 # multiplicador, incrementador, modulo
  x = gcl.generaSemilla(x, a, c, m)
  r = x/m
  for i in range(10):
    p1 = round(sum(pj[:i]),3)
    p2 = round(sum(pj[:i+1]),3)
    if (p1 < r) and (r <= p2):
      nros[i] += 1.0
      break
  return x  # Devuelve la ultima semilla x

nros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
x = 1234567 # Semilla
for i in range(1000):
  x = empirica(x)
print(nros)
print("-----------------------------------------------------------------------")
test.testChiCuadrada(nros, 0.05)