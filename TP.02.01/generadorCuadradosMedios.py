import matplotlib.pyplot as plt
import testsPseudoaleatorios as t

n = 2000 # Cantidad de numeros pseudoaleatorios
pseudos = []
semilla = input("Escriba la semilla: ")
tam1 = len(semilla)
num1 = int(semilla)
for i in range(0, n):
    num2 = pow(num1, 2)
    str2 = str(num2)
    tam2 = len(str2)
    inicio = int((tam2-tam1) / 2)
    fin = int(inicio+tam1)
    str3 = str2[inicio:fin]
    num1 = int(str3)
    str3 = ("0."+str3)
    numAleatorio = float(str3)
    pseudos.append(numAleatorio)
#print(pseudos)
plt.scatter(range(n), pseudos)
plt.title("Cuadrados Medios (Semilla = 1234567)")   
plt.xlabel("Iteraciones (n)")   
plt.ylabel("Valor Pseudoaleatorio")   
plt.show()

print("-----------------------------------------------------------------------------------------------------")
t.testKS(pseudos, 0.05)
print("-----------------------------------------------------------------------------------------------------")
t.testChiCuadrada(pseudos, 0.05)
print("-----------------------------------------------------------------------------------------------------")
t.testPoker(pseudos, 0.05)
print("-----------------------------------------------------------------------------------------------------")
t.testCorridas(pseudos, 0.05)