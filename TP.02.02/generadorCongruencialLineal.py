import matplotlib.pyplot as plt

def generar(nros):
  #x, a, c, m, n = 1234567, 1093, 18257, 3594325, 2000 # Semilla, multiplicador, incrementador, modulo, numeros pseudoaleatorios
  x, a, c, m = 1234567, 1093, 18257, 3594325 # Semilla, multiplicador, incrementador, modulo, numeros pseudoaleatorios
  pseudos = [round(x/m, 5)] # distribucion uniforme (0,1)
  plt.title('Generador Congruencial Lineal (Semilla '+str(x)+')')
  for i in range(nros-1):
    x = (a*x + c) % m
    pseudos.insert(i+1, round(x/m, 5))
  return pseudos

def generaSemilla(x, a, c, m):
  x = (a*x + c) % m
  return x

if __name__ == '__main__':
  pseudos = generar()
  plt.scatter(range(len(pseudos)), pseudos)
  plt.xlabel('Iteraciones (n)')
  plt.ylabel('Valor Pseudoaleatorio')
  plt.show()