import matplotlib.pyplot as plt
import testsPseudoaleatorios as t

x, a, c, m, n = 1234567, 1093, 18257, 3594325, 2000 # Semilla, multiplicador, incrementador, modulo, numeros pseudoaleatorios
pseudos = [round(x/m, 5)] # distribucion uniforme (0,1)
plt.title('Generador Congruencial Lineal (Semilla '+str(x)+')')
for i in range(n-1):
  x = (a*x + c) % m
  pseudos.insert(i+1, round(x/m, 5))
#print(pseudos)
plt.scatter(range(n), pseudos)
plt.xlabel('Iteraciones (n)')
plt.ylabel('Valor Pseudoaleatorio')
plt.show()

print("-----------------------------------------------------------------------------------------------------")
t.testKS(pseudos, 0.05)
print("-----------------------------------------------------------------------------------------------------")
t.testChiCuadrada(pseudos, 0.05)
print("-----------------------------------------------------------------------------------------------------")
t.testPoker(pseudos, 0.05)
print("-----------------------------------------------------------------------------------------------------")
t.testCorridas(pseudos, 0.05)
