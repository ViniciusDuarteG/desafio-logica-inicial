import random

experiencia_player = int(0) 
sexo_do_heroi=str(input("Defina o genero do heroi:\nM - Masculino\nF - Feminino\n")).strip().upper()
if sexo_do_heroi == "M":
    nome_do_heroi = str(input("Defina o nome do herói:\n"))
elif sexo_do_heroi =="F":
    nome_do_heroi = str(input("Defina o nome da heroina:\n"))

nivel_do_heroi = int(1)
vida_do_heroi = int(100)
xp_total = 0 
xp = 0

decisao = 1

dano = 0

def FimDoJogo():
    global sexo_do_heroi, xp_total, nivel_do_heroi

    if xp_total <= 1000:
        nivel_do_heroi = str("1 - Ferro")
    elif xp_total > 1001 and xp_total <= 2000:
        nivel_do_heroi = str("2 - Bronze")
    elif xp_total > 2001 and xp_total <= 5000:
        nivel_do_heroi = str("3 - Prata")
    elif xp_total > 5001 and xp_total <= 7000:
        nivel_do_heroi = str("4 - Ouro")
    elif xp_total > 7001 and xp_total <= 8000:
        nivel_do_heroi = str("5 - Platina")
    elif xp_total > 8001 and xp_total <= 9000:
        nivel_do_heroi = str("6 - Ascendente")
    elif xp_total > 9001 and xp_total <= 10000:
        nivel_do_heroi = str("7 - Imortal")
    elif xp_total <= 1001:
        nivel_do_heroi = str("8 - Radiante")
    
    if sexo_do_heroi == "M":
        print("O {} recebeu {} de XP e chegou ao nível {}".format(nome_do_heroi, xp_total, nivel_do_heroi))
    elif sexo_do_heroi == "F":
        print("A {} recebeu {} de XP e chegou ao nível {}".format(nome_do_heroi, xp_total, nivel_do_heroi))


def bauDeXP():
    global xp
    global nivel_do_heroi
    global xp_total

    print("Você encontrou um bau de XP!")
    print("Você recebeu 250 de XP.")
    xp = xp + 250
    print("Seu XP é de: ",xp)
    if xp == 1000:
        nivel_do_heroi = nivel_do_heroi + 1
        xp_total = xp_total + xp 
        xp = 0
        print("Parabens pelo novo nível! Agora seu nivel é {0}".format(nivel_do_heroi))


def Combate():
    global dano, vida_do_heroi

    print("Você encontrou uma armadilha!")
    print("Ela é acionada e você recebeu...")
    dano=random.randint(1,10)
    print(dano," de dano")
    vida_do_heroi = vida_do_heroi - dano
    print("Sua vida é de ", vida_do_heroi)

while decisao != 0:
    decisao = int(input("Escolha para onde você quer ir: \n1- Direita\n2- Esquerda\n0-Encerrar o jogo\n\n"))
    if decisao == 1: 
        print("Você entrou em uma sala.")
        print("As portas se abrem e você encontrou um...")
        acao = random.randint(1,2)
        if acao  == 1:
           Combate()
        elif acao  == 2:
           bauDeXP()
        
    elif decisao == 2:
        print("Você entrou em uma sala.")
        print("As portas se abrem e você encontrou um...")
        acao = random.randint(1,2)
        if acao  == 1:
           Combate()
        elif acao  == 2:
           bauDeXP()
        
    if vida_do_heroi <= 0:
        break
    

print("Fim de jogo!")
FimDoJogo()

