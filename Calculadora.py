print("")
print("Bem-Vindo! Vamos Começar...")
nome = input("Digite seu Nome: ")
print("Qual seu Sexo? [1] Homem | [2] Mulher")
sexo = int(input("Resposta: "))
while sexo != 1 and sexo != 2:
    print("||||||||||||||||||||||||||||||||||")
    print("Erro de Digitação!")
    print("Qual seu Sexo? [1] Homem | [2] Mulher")
    sexo = int(input("Resposta: "))

if sexo == 1: 
    idade = int(input("Digite sua Idade: "))
    peso = float(input("Digite seu Peso em kilogramas: "))
    altura = float(input("Digite sua Altura em Centímetros: "))
    calculo_tmb = (88.362 + (13.397*peso) + (4.799*altura)) - (5.677*idade)
    print("-------------------------------------------------------")
    print(f"{nome}, sua Taxa de Metabolismo Basal é de {calculo_tmb:.2f} Calórias.")

elif sexo == 2:
    idade = int(input("Digite sua Idade: "))
    peso = float(input("Digite seu Peso em kilogramas: "))
    altura = float(input("Digite sua Altura em Centímetros: "))
    calculo_tmb = (447.593 + (9.247*peso) + (3.098*altura)) - (4.330*idade)
    print("-------------------------------------------------------")
    print(f"{nome}, sua Taxa de Metabolismo Basal é de {calculo_tmb:.2f} Calórias.")


   