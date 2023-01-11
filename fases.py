
import os
import time
from os import remove
from personagem import*
from xp import xp_check
import interface_de_luta
from objetos import armas
from asyncio import sleep
from asyncore import write
from classe_narrador import*
from Inimigos import ini_lista
from load_save import load_save
from colorama import Fore, Style

"""um arquivo com os as fases do jogo no final de cada arquivo as informaçoes do player 
devem ser armazenadas para que possamos iniciar uma a proxima faze com seus status e itens"""

def Fase_1 (player):
  
    xp = 0
    
    os.system('cls')
    print(Fore.LIGHTWHITE_EX + """Bem vindo jovem guerreiro(a), O mundo foi dominado por um grande mal!!!\n\nGuerreiros foram escolhidos para combater o mal voce é mais um dentre muitos guerreiros.""" + Style.RESET_ALL)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    os.system('cls')
    loop = True
    while loop == True:
        print("<<<Escolha a sua arma>>>")
        print("\nARMA 1")
        print(armas.get_arma(1))
        print("\nARMA 2:")
        print(armas.get_arma(4))
        print("\nARMA 3:")
        print(armas.get_arma(7))
        print("\nDigite a arma que voce deseja pegar")
        try:
            seletor = int(input())
            loop = False
        except:
            os.system('cls')
            print("\n---------------->>>Valor invalido<<<-----------------\n")
            loop = True


    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    
    
    loop = 1
    while loop == 1:
        if seletor == 1:
            arma_escolhida = armas.get_arma(1)
            player = Personagem (player, 500, 250, arma_escolhida.ataque + 1, 0, 0, 10, 1, 0,armas.get_arma(1), 0)
            loop = 0
        elif seletor == 2:
            arma_escolhida = armas.get_arma(4)
            player = Personagem (player, 500, 250, arma_escolhida.ataque + 1, 0, 0, 10, 1, 0,armas.get_arma(4), 0)
            loop = 0
        elif seletor == 3:
            arma_escolhida = armas.get_arma(7)
            player = Personagem (player, 500, 600, 1, 0, arma_escolhida.inteligencia, 10, 1, 0,armas.get_arma(7), 0)
            loop = 0
        else:
            print("valor invalido")
    
    os.system('cls')
    
    print("         <<<Seus Status são>>>\n")
    print(player)
    print("         >>>'{}' Boa Sorte na sua jornada<<<".format(player.nome))
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    os.system('cls')
    #sons de florestas e passos
    Misha = NPC ("Misha", 250, 500, 25, 50, 100, 25, 5, 0) #NPC
    print(Fore.LIGHTYELLOW_EX + "Sua primeira Missão, matar uma Urso" + Style.RESET_ALL)
    print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
    inicio_decontagem = 4
    contador = 4
    pasta = 'Falas/Texto_.txt'
    p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
    os.system('cls')
    #som de algo quebrado
    
    print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
    inicio_decontagem = 5
    contador = 5
    pasta = 'Falas/Texto_.txt'
    p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
    os.system('cls')
    
    #som de lobos
    
    print(Fore.LIGHTRED_EX + "2 lobos apareceram" + Style.RESET_ALL)
    print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
    inicio_decontagem = 6
    contador = 6
    pasta = 'Falas/Texto_.txt'
    p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    os.system('cls')
    
    inimigo1 = ini_lista.pegar_um_inimigo(1)
    interface_l(inimigo1, player)
    print("sua vida é {}".format(player.vida))
    if(player.vida <= 0):
        print(Fore.RED + "\n\nG A M E__O V E R " + Style.RESET_ALL)
        sys.exit()
    else:
        player.xp += 10
        xp_check(player)
        print(Fore.GREEN + "voce ganhou 10xp" + Style.RESET_ALL)
        print("<<<voce subiu de nivel!!!>>>\nseu nivel agr é {}".format(player.LV))
        print("voce recebeu 5 pontos para colocar em um de seus status\n\nDigite 1 para Ataque\nDigite 2 para Defesa\nDigite 3 para inteligencia")
        seletor = int(input())
    
        if seletor == 1:
            player.ataque += 5
        elif seletor == 2:
            player.defesa += 5
        elif seletor == 3:
            player.inteligencia += 5
        
        print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
        inicio_decontagem = 7
        contador = 7
        pasta = 'Falas/Texto_.txt'
        p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
        os.system('cls')
        
        print(Fore.MAGENTA + "Misha: ..." + Style.RESET_ALL)
        print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
        inicio_decontagem = 8
        contador = 8
        pasta = 'Falas/Texto_.txt'
        p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
        
        print("seu HP foi restaurado para 750")
        player.vida = 750
        input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
        os.system('cls')
    
    print(Fore.CYAN + "<Voces se aproximan de uma caverna com marcas de garra>" + Style.RESET_ALL)
    print(Fore.MAGENTA + "\n\nMisha: " + Style.RESET_ALL)
    inicio_decontagem = 9
    contador = 9
    pasta = 'Falas/Texto_.txt'
    p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    os.system('cls')
    
    contador = 0
    loop = 1
    while loop == 1:
        print(Fore.RED + "\nVoce esta em uma area sem volta\n" + Style.RESET_ALL + "\nEscolha:\n1 para entrar na caverna\n2 para armar uma emboscada\n3 para olhar em volta\n4 para fugir")
        try:
            seletor = int(input())
        except:
            seletor = -1
        if seletor == 1:
            os.system('cls')
            print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
            inicio_decontagem = 10
            contador = 10
            pasta = 'Falas/Texto_.txt'
            p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
            input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
            os.system('cls')
            loop = 0
        elif seletor == 2:
            print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
            inicio_decontagem = 11
            contador = 11
            pasta = 'Falas/Texto_.txt'
            p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
            input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
            os.system('cls')
            loop = 0
        elif seletor == 3 and contador == 1:
            os.system('cls')
            print("\nNão ah mais nada para olhar")
            input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    
        elif seletor == 3 and contador == 0:
            os.system('cls')
            print("voce olha em volta...")
            print("""Voce encontra um uma tampa de barril, 'pode ser utilizada como escudo.
            \nvoce deseja equipar ela?\nDigite 1 para sim\nDigite 2 para não""") 
            try: 
                s = int(input())
            except: 
                print("Valor Invalido\n")
                s = -1
            if s == 1:
                print("Status do escudo\n")
                print(armas.get_arma(10))
                escudo_escolhido = armas.get_arma(10)
                player.defesa = escudo_escolhido.defesa
                contador = 1
            else:
                print("o escudo foi deixado no chão")
        elif seletor == 4:
            os.system('cls')
            print("se voce fugir, vc sera EXECUTADO por covardia, é preferivel morrer nas mãos do Urso")
            print("`-´ q mundo cruewwwwUwU")
    
    if seletor == 1:
        os.system('cls')
        print("Micha fica do lado de fora para cuidar de qualquer surpresa e tu entra para enfrentar o urso")
        input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
        inimigo2 = ini_lista.pegar_um_inimigo(2)
        interface_de_luta.interface_l(inimigo2, player)
    
    elif seletor == 2:
        os.system('cls')
        print("Vocês combinam uma armadilha e esperam até o urso sair da caverna para caçar\n")
        input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
        print(Fore.RED + "o Urso sai com fome da caverna\n" + Fore.MAGENTA + "Misha: nossa muito feio kkkkkkkkkkkk\n\n" + Fore.RED + "<o Urso tem cicatrises na cara e olhos vermelhos e pelo grisalhos, ele parece e cançado>\n" + Fore.MAGENTA +"Misha pula de cima de uma arvore proxima a caverna e finca a espada no urso!!!" + Style.RESET_ALL)
        input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
        inimigo2 = ini_lista.pegar_um_inimigo(2)
        ataque_surpresa = Misha.Causar_dano()
        ataque_surpresa = ataque_surpresa * 2
        
        inimigo2.vida = inimigo2.vida - ataque_surpresa
        print(Fore.MAGENTA + "sem espada Misha recua e deixa o resto para voce\nMisha: Divirta se!!!" + Style.RESET_ALL)
        input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
        os.system('cls')
        interface_de_luta.interface_l(inimigo2, player)
    
    if player.vida <= 0:
        print(Fore.RED + "G A M E__O V E R" + Style.RESET_ALL)
        print(Fore.MAGENTA + "Misha:  Você é a vergonha da proficiown `-´\n" + Style.RESET_ALL)
        sys.exit()
    else:
        player.xp += 20
        xp_check(player)
        print(Fore.GREEN + "voce ganhou 10xp" + Style.RESET_ALL)
        print("<<<voce subiu de nivel!!!>>>\nseu nivel agr é {}".format(player.LV))
        print("voce recebeu 5 pontos para colocar em um de seus status\n\nDigite 1 para Ataque\nDigite 2 para Defesa\nDigite 3 para inteligencia")
        seletor = int(input())
    
        if seletor == 1:
            player.ataque += 5
        elif seletor == 2:
            player.defesa += 5
        elif seletor == 3:
            player.inteligencia += 5
    
    
    print(Fore.MAGENTA + "Misha: " + Style.RESET_ALL)
    inicio_decontagem = 12
    contador = 12
    pasta = 'Falas/Texto_.txt'
    p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
    os.system('cls')
    print('\nVoces retornam da caçada e reportão o progresso\n')
    print("\nao relatar o seu progresso voce e Misha são chamados para, receberem sua recompença\nMisha recebe uma recompença e uma outra missão depois é mandanda para uma missao\n")
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    print(Fore.LIGHTBLACK_EX + "<{}> Bem vindo de volta Misha ja relatou todo o ocorrido, a sua proxima missão ja esta pronta\npor favor pegue sua recompensa".format(player.nome) + Style.RESET_ALL)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    print("<Escolha uma arma>")

    print(">\nItem 1:")
    print(armas.get_arma(3))
    print(">>\nItem 2:")
    print(armas.get_arma(6))
    print("\n>>>Item 3: ")
    print(armas.get_arma(9))
    loop = True
    while loop == True:
        try :
            seletor = int(input())
            loop = False
        except:
            print("VAlor invalido")
            loop = True

    if seletor == 1:
        player.item1 = armas.get_arma(3)
        x = player.item1
        player.ataque = x.ataque
    
    elif seletor == 2:
        player.item1 = armas.get_arma(6)
        x = player.item1
        player.ataque = x.ataque
    
    elif seletor == 3:
        player.item1 = armas.get_arma(9)
        x = player.item1
        player.ataque = x.inteligencia
    
    print(Fore.LIGHTBLACK_EX +  "A sua proxima missão sera ir a um castelo distante e executar um demonio que vem nos causando problemas a um tempo já\nQue a graça do nosso senhor esteja contigo." + Style.RESET_ALL)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n" + Style.RESET_ALL)
    print(player)
    
    
    #jogador = [player]
    x = player.item1 
    jogador_itens = (x.nome, x.ataque, x.inteligencia, x.tipo, x.descricao)
    
    jogador = (player.nome, player.vida, player.mana, player.ataque, player.defesa, player.inteligencia, player.sorte, player.LV, player.xp, x.nome, x.ataque, x.inteligencia, x.tipo, x.descricao)
    print(jogador[0:9])
    jogador = load_save(jogador, '1').salvar()
    print("fim da parte 1\n")

def Fase_2 ():
    os.system('cls')
    """#aqui é carregado os statos da faze 1, pode-se alteralos aqui para quebrar o jogo ou testar """
    x = []
    x = load_save(x, 1).carregar()
    arma = int(x[10])
    nome = str(x[0])
    vida = 5000
    mana = int(x[2])
    ataque = int(x[3])
    defesa = int(x[4])
    inteligencia = int(x[5])
    sorte = int(x[6])
    LV = 5
    xp = 30
    
    
    if arma == 200:
        print("<<<arco lendario>>>")
        pl = armas.get_arma(3)
    elif arma == 125:
        print("<<<espada lendaria>>>")
        pl = armas.get_arma(6)
    else:
        pl = armas.get_arma(9)
    playerf = Personagem (nome, vida, mana, pl.ataque, defesa, pl.inteligencia, sorte, LV, xp, pl, 0)
    playerf.LV = 5
    #print(playerf)
    
    
    print(Fore.YELLOW + "Voce se aproxima do castelo\né posivel sentir um frio na barriga" + Style.RESET_ALL)
    print(Fore.YELLOW + "voce entra no castelo, e se pergunta o que o trouce até aqui?\nvoce poderia estar fazendo qualquer outra coisa, mais voce esta aqui" + Style.RESET_ALL)
    print(Fore.YELLOW + "voce se perde nos pensamentos, de como voce queria estar em qualquer lugar menos aqui e não percebe que\nvoce ja esta esta na sala so chefe." + Style.RESET_ALL)
    input("\n\n---------------->>>Aperte enter para continuar<<<----------------\n")
    os.system('cls')
    print(Fore.YELLOW + 'Demonio do Castelo: Vai ficar parado ai até quando?\nDemonio do Castelo: Criatura inutil-se voce não vai atacar eu vou!!' + Style.RESET_ALL)
    print("\npreparece a batalha vai começar\n\n------------------->>>novas magias foram adicionadas<<<-------------------")
    inimigo = ini_lista.pegar_um_inimigo(7)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    os.system('cls')
    interface_de_luta.interface_l(inimigo, playerf)
    
    if playerf.vida <= 0:
        print(Fore.RED + "G A M E__O V E R" + Style.RESET_ALL)
        sys.exit()
    else:
        print(Fore.GREEN + "A Ameaça foi E-l-i-m-i-n-a-d-a\n" + Style.RESET_ALL)
        input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    print(Fore.GREEN + "{}: que batalha dificil eu me pergunto que tipo e missao a Misha esta tendo...\nEu vou voltar e reportar o meu progresso".format(playerf.nome) + Style.RESET_ALL)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")
    print(Fore.LIGHTYELLOW_EX + "A historia de {} termina por aqui\n\n\nO-B-R-I-G-A-D-O__P-O-R__J-O-G-A-R". format(playerf.nome) + Style.RESET_ALL)
    input("\n---------------->>>Aperte enter para continuar<<<----------------\n")