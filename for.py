for numero in range(1, int(input("Digite um numero para determinar o fim: ")),1):
    print(" " + str(numero))
print()

#----------------------------------------------------------------------------------#

tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabauada do numero", tabuada)
for i in range(0,11,1):
    print(str(tabuada) + "x" + str(i) + " = " + str((tabuada*i)))