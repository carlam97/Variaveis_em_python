nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca=input("Suspeita de doença infecto-contagiosa?").upper()
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca == "SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doenca == "NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else: 
        print("Responda a suspeita de doença com 'sim' ou 'nao'")
else:
    print("Paciente SEM prioridade")
    if doenca == "SIM":
        print("Encaminhe o paciente para a sala AMARELA")
    elif doenca == "NAO":
        print("Encaminhe o paciente para a sala BRANCA")
    else: 
        print("Responda a suspeita de doença com 'sim' ou 'nao'")
print()

#-------------------------------------------------------------------#

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
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




