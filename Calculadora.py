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
    print("------------------------------------------------------------")
    print(f"{nome}, sua Taxa de Metabolismo Basal é de {calculo_tmb:.2f} Calórias.")

elif sexo == 2:
    idade = int(input("Digite sua Idade: "))
    peso = float(input("Digite seu Peso em kilogramas: "))
    altura = float(input("Digite sua Altura em Centímetros: "))
    calculo_tmb = (447.593 + (9.247*peso) + (3.098*altura)) - (4.330*idade)
    print("------------------------------------------------------------")
    print(f"{nome}, sua Taxa de Metabolismo Basal é de {calculo_tmb:.2f} Calórias.")

print("------------------------------------------------------------")
print("Qual seu nível de Atividade Físca?")
print("[1] Sedentário (Nenhuma atividade física)")
print("[2] Levemente Ativo (Atividades leves, como caminhadas ocasionais)")  
print("[3] Moderadamente ativo (Exercício moderado 3-5 dias por semana)")
print("[4] Muito ativo (Exercício intenso 6-7 dias por semana)") 
print("[5] Extremamente ativo (Atividade física muito intensa, trabalho físico pesado)") 
nivel = int(input("Resposta: "))
while nivel != 1 and nivel != 2 and nivel != 3 and nivel != 4 and nivel != 5:
    print("||||||||||||||||||||||||||||||||||")
    print("Erro de Digitação!")
    print("Qual seu nível de Atividade Físca?")
    print("[1] Sedentário (Nenhuma atividade física)")
    print("[2] Levemente Ativo (Atividades leves, como caminhadas ocasionais)")  
    print("[3] Moderadamente ativo (Exercício moderado 3-5 dias por semana)")
    print("[4] Muito ativo (Exercício intenso 6-7 dias por semana)") 
    print("[5] Extremamente ativo (Atividade física muito intensa, trabalho físico pesado)") 
    nivel = int(input("Resposta: "))
    print("------------------------------------------------------------")


if nivel == 1:
    calculo_tmt = calculo_tmb * 1.2 
    print(f"{nome}, sua Taxa de Metabolismo Total é de {calculo_tmt:.2f} calórias.")
elif nivel == 2:
    calculo_tmt = calculo_tmb * 1.375 
    print(f"{nome}, sua Taxa de Metabolismo Total é de {calculo_tmt:.2f} calórias.")
elif nivel == 3:
    calculo_tmt = calculo_tmb * 1.55 
    print(f"{nome}, sua Taxa de Metabolismo Total é de {calculo_tmt:.2f} calórias.")
elif nivel == 4:
    calculo_tmt = calculo_tmb * 1.725
    print(f"{nome}, sua Taxa de Metabolismo Total é de {calculo_tmt:.2f} calórias.")
elif nivel == 5:
    calculo_tmt = calculo_tmb * 1.9 
    print(f"{nome}, sua Taxa de Metabolismo Total é de {calculo_tmt:.2f} calórias.")