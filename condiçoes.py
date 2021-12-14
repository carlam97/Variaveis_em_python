nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
prioridade="NÃO"
if idade>=65:
    prioridade="SIM"
print("O(A) paciente", nome, "possui atendimento prioritário? ", prioridade)
print()
#------------------------------------------------------------------------#

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
if idade>=65:
    print("O(A) paciente", nome, "POSSUI atendimento prioritário")
else:
     print("O(A) paciente", nome, "NÃO possui atendimento prioritário")
print()
#----------------------------------------------------------------------#

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca=input("Suspeita de doença infecto-contagiosa?").upper()  #upper transforma a resposta em letras maiusculas
if idade>=65 and doenca == "SIM":
    print("O(A) paciente", nome, "POSSUI atendimento prioritário e deve ser direcionado(a) para a sala reservada")
elif idade>=65 and doenca == "NAO":
    print("O(A) paciente", nome, "POSSUI atendimento prioritário, mas pode aguardar na sala comum")
elif idade<65 and doenca == "SIM":
     print("O(A) paciente", nome, "NÃO possui atendimento prioritario, mas deve ser direcionado(a) para a sala reservada")
elif idade<65 and doenca == "NAO":
    print("O(A) paciente", nome, "NÃO possui atendimento prioritario e pode aguardar na sala comum")
else:
    print("Responda a suspeita de doença infecto-contagiosa com 'sim' ou 'nao'")

#-----------------------------------------------------------------------#



