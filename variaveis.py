nome = "Carla Martins"
empresa = "FATEC"
qtd_funcionarios = 500
mediaMensalidade = 856.50

print(nome, " trabalha na empresa ", empresa)
print(" a mesma possui ", qtd_funcionarios, "funcionários. ")
print(" Cuja média da mensalidade é de ", mediaMensalidade)

#----------------------------------------------------------------#

nome = input("Digite o nome do funcionário: ")    # não precisa colocar o str
empresa = input("Digite a empresa: ")
qtd_funcionarios = int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome, " trabalha na empresa ", empresa)
print(" a mesma possui ", qtd_funcionarios, "funcionários. ")
print(" Cuja média da mensalidade é de ", mediaMensalidade)
print("========== Verifique os tipos de dados abaixo ==========")
print("O tipo de dado da variavel [nome] é: ", type(nome))
print("O tipo de dado da variavel [empresa] é: ", type(empresa))
print("O tipo de dado da variavel [qtd_funcionarios] é: ", type(qtd_funcionarios))
print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))

#-----------------------------------------------------------------------------------#

responsavel = input("Digite o nome do responsavel: ")
funcionário = input("Digite o nome do funcionário: ")
evento = input("Digite o nome do evento: ")
gastos = float(input("Digite o valor dos gastos: "))

print("Declaro para o senhor", funcionário, "que o senhor", responsavel, "esteve presente no evento", evento, "e gastou o valor de R$", gastos, "com a entrada")




