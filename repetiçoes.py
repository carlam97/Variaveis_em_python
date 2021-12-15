numero = int(input("Digite um numero: "))
while numero<100:
    print(" " + str(numero))
    numero=numero+1
print("Laço encerrado.... ")
print()

#---------------------------------------------------------------------#

resposta = "SIM"
while resposta == "SIM":
    nivel=input("Digite o nível de acesso: ").upper()
    if nivel=="ADM" or nivel=="USR":
        genero=input("Digite o seu genero: ").upper()
        if nivel=="ADM":
            if genero=="FEMININO":
                print("Olá administradora")
            else:
                print("Olá administrador")
        else:
            if genero=="FEMININO":
                print("Olá usuária")
            else:
                print("Olá usuario")
    elif nivel=="GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    resposta=input("Digite SIM para continuar: ").upper()
print()

#-------------------------------------------------------------------#

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca=input("Suspeita de doença infecto-contagiosa?").upper()

while doenca != "SIM" and doenca != "NAO":
    print("Digite SIM ou NAO")
    doenca=input("Suspeita de doença infecto-contagiosa?").upper()
    
if doenca == "SIM":
    print("Encaminhe o paciente para a sala AMARELA")
elif doenca == "NAO":
    print("Encaminhe o paciente para a sala BRANCA")
else:
    print("Responda a suspeita de doença com 'sim' ou 'nao'")

if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o genero do(a) paciente: ").upper()
    if genero == "FEMININO" and idade>10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioriidade")
    else:
        print("Paciente SEM prioridade")