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
print("------------------------------------------------------------")
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

print("------------------------------------------------------------")
print("Você gostaria de [1] Perder Peso ou [2] Ganhar Peso ?")
objetivo = int(input("Resposta: "))
while objetivo != 1 and objetivo != 2:
    print("||||||||||||||||||||||||||||||||||")
    print("Erro de Digitação!")
    print("Você gostaria de [1] Perder Peso ou [2] Ganhar Peso ?")
    objetivo = int(input("Resposta: "))

if objetivo == 1:
    print("Como gostaria de definir seu Déficit Calórico?")
    print("[1] Déficit Leve")
    print("[2] Déficit Moderado")
    print("[3] Déficit Agressivo")
    deficit = int(input("Resposta: "))
    if deficit == 1:
        print("------------------------------------------------------------")
        print("Ótima Escolha! O Déficit Leve é ideal para quem busca uma perda lenta e sustentável de peso.")
        print("Escolha a porcentagem do Déficit, entre 5 a 10%")
        porcentagem = float(input("Resposta: "))
        calculo_porcentagem = porcentagem/100
        deficit_leve = calculo_tmt - (calculo_porcentagem*calculo_tmt)
        print("------------------------------------------------------------")
        print(f"{nome}, você irá precisar consumir {deficit_leve:.2f} Calórias para Perder Peso.")
        print("------------------------------------------------------------")
    elif deficit == 2:
        print("------------------------------------------------------------")
        print("Ótima Escolha! O Déficit Moderado é ideal para as pessoas que desejam emagrecer com segurança e certa velocidade.")
        print("Escolha a porcentagem do Déficit, entre 10 a 20%")
        porcentagem = float(input("Resposta: "))
        calculo_porcentagem = porcentagem/100
        deficit_moderado = calculo_tmt - (calculo_porcentagem*calculo_tmt)
        print("------------------------------------------------------------")
        print(f"{nome}, você irá precisar consumir {deficit_moderado:.2f} Calórias para Perder Peso.")
        print("------------------------------------------------------------")
    elif deficit == 3:
        print("------------------------------------------------------------")
        print("O Déficit Agressivo, é usado em casos específicos, como preparação de atletas ou sob supervisão médica.")
        print("Escolha a porcentagem do Déficit, entre 20 a 30%")
        porcentagem = float(input("Resposta: "))
        calculo_porcentagem = porcentagem/100
        deficit_agressivo = calculo_tmt - (calculo_porcentagem*calculo_tmt)
        print("------------------------------------------------------------")
        print(f"{nome}, você irá precisar consumir {deficit_agressivo:.2f} Calórias para Perder Peso.")
        print("------------------------------------------------------------")
if objetivo == 2:
    print("Como gostaria de definir seu Ganho de Peso?")
    print("[1] Superávit Leve")
    print("[2] Superávit Moderado")
    print("[3] Superávit Agressivo")
    superavit = int(input("Resposta: "))
    if superavit == 1:
        print("------------------------------------------------------------")
        print("Ótima Escolha! O Superávit Leve é ideal para quem busca ganho de peso gradual, com menor acúmulo de gordura.")
        print("Escolha a porcentagem do Superávit, entre 5 a 10%")
        porcentagem = float(input("Resposta: "))
        calculo_porcentagem = porcentagem/100
        superavit_leve = calculo_tmt + (calculo_porcentagem*calculo_tmt)
        print("------------------------------------------------------------")
        print(f"{nome}, você irá precisar consumir {superavit_leve:.2f} Calórias para Ganhar Peso.")
        print("------------------------------------------------------------")
    if superavit == 2:
        print("------------------------------------------------------------")
        print("Ótima Escolha! O Superávit Moderado é ideal para a maioria das pessoas que desejam ganhar peso ou aumentar a massa muscular.")
        print("Escolha a porcentagem do Superávit, entre 10 a 20%")
        porcentagem = float(input("Resposta: "))
        calculo_porcentagem = porcentagem/100
        superavit_moderado = calculo_tmt + (calculo_porcentagem*calculo_tmt)
        print("------------------------------------------------------------")
        print(f"{nome}, você irá precisar consumir {superavit_moderado:.2f} Calórias para Ganhar Peso.")
        print("------------------------------------------------------------")
    if superavit == 3:
        print("------------------------------------------------------------")
        print("Usado em casos específicos, como pessoas com metabolismo extremamente acelerado ou dificuldades extremas de ganho de pes")
        print("Escolha a porcentagem do Superávit, entre 20 a 30%")
        porcentagem = float(input("Resposta: "))
        calculo_porcentagem = porcentagem/100
        superavit_agressivo = calculo_tmt + (calculo_porcentagem*calculo_tmt)
        print("------------------------------------------------------------")
        print(f"{nome}, você irá precisar consumir {superavit_agressivo:.2f} Calórias para Ganhar Peso.")
        print("------------------------------------------------------------")

































































# QUANTIDADE DE MACRO NUTRIENTES!