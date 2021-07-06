import random
import matplotlib.pyplot as plt
import testsPseudoaleatorios as t

semilla = 1234567
n = 2000
pseudos = []
random.seed(semilla)
for i in range(n):
  pseudos.append(random.random())
plt.title('Generador Random Python (Semilla '+str(semilla)+')')
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