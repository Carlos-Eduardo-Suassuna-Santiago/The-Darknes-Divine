import os
from ast import Global
from random import randrange
from colorama import Fore, Style

#from zmq import XPUB
from objetos import Itens, armas
from combate import Inimigo_ataque, fisicos
from Inimigos import Inimigo, lista_inimigos, ini_lista

#item = armas.get_arma(1)
#print(item)

def interface_l(inimigo, personagem): #interface de combate recebe o inimigo e o player
    global XP
    XP = 0
    print(Fore.LIGHTRED_EX + '{}'.format(inimigo) + Style.RESET_ALL)
    loop_de_teste = True
    while loop_de_teste == True:

        if personagem.vida <= 0:
            print("VOCE MORREU")
            break

        print(Fore.GREEN + "\n\nSua Vida é: {}".format(personagem.vida) + Style.RESET_ALL )
        print(Fore.LIGHTRED_EX + "A Vida do {} è: {}\n\n".format(inimigo.nome, inimigo.vida) + Style.RESET_ALL)

        if inimigo.vida <= 0:
                print("o {} morreu".format(inimigo.nome))
                loop_de_teste = False
                break
        print('-------------------------\n       Voce Deseja\n-------------------------\nDigite 1 para ATACAR\nDigite 2 para Usar SKILL\nDigite 3 para ler STATUS')
        try: 
            seletor = int(input(">>> "))
        except:
            seletor = -1
            os.system('cls')

        if seletor == 1:
            os.system('cls')
            ataque = personagem.Causar_dano()
            inimigo.vida = inimigo.vida - ataque
            ataque = Inimigo_ataque.ataque_do_inimigo(inimigo, personagem)
            personagem.vida = personagem.vida - ataque

                
            
        elif seletor == 2:
            os.system('cls')
            if(personagem.LV >= 1 ):
                print(Fore.LIGHTWHITE_EX + "Digite 1 para usar a skill 'Corte'. Custo de Mana: 20" + Style.RESET_ALL)
                print(Fore.LIGHTWHITE_EX + "Digite 2 para usar a skill 'Tiro Concentrado'. Custo de Mana: 40" + Style.RESET_ALL)
                print(Fore.RED + "Digite 3 para usar 'Bola de fogo'. Custo de Mana: 100" + Style.RESET_ALL)
                
            if(personagem.LV >= 5):
                print(Fore.BLUE + "Digite 4 para usar 'Caixão de gelo'. Custo de Mana: 5000" + Style.RESET_ALL)
                print(Fore.LIGHTGREEN_EX+ "Digite 5 para usar 'Cura'. Custo de Mana: 50" + Style.RESET_ALL)
                print(Fore.CYAN + "Digite 6 para restaurar mana " +  Style.RESET_ALL)
            try:
                seletor = int(input(">>> "))
            except:
                seletor = -1
                os.system('cls')

            if seletor == 1:
                personagem.corte(inimigo, personagem.item1)
                if inimigo.vida <= 0:
                    print(Fore.LIGHTRED_EX + "A Vida do {} è: {}\n\n".format(inimigo.nome, inimigo.vida) + Style.RESET_ALL)
                    break
                else:
                    ataque = Inimigo_ataque.ataque_do_inimigo(inimigo, personagem)
                    personagem.vida = personagem.vida - ataque

            
            elif seletor == 2:
                personagem.tiro_concentrado(inimigo, personagem.item1)
                if inimigo.vida <= 0:
                    print(Fore.LIGHTRED_EX + "A Vida do {} è: {}\n\n".format(inimigo.nome, inimigo.vida) + Style.RESET_ALL)
                    break
                else:
                    ataque = Inimigo_ataque.ataque_do_inimigo(inimigo, personagem)
                    personagem.vida = personagem.vida - ataque

            elif seletor == 3:
                personagem.bola_fogo(inimigo, personagem.item1)
                if inimigo.vida <= 0:
                    print(Fore.LIGHTRED_EX + "A Vida do {} è: {}\n\n".format(inimigo.nome, inimigo.vida) + Style.RESET_ALL)
                    break
                else:
                    ataque = Inimigo_ataque.ataque_do_inimigo(inimigo, personagem)
                    personagem.vida = personagem.vida - ataque


            elif seletor == 4:
                personagem.Caixao_De_gelo(inimigo, personagem.item1)
                if inimigo.vida <= 0:
                    print(Fore.LIGHTRED_EX + "A Vida do {} è: {}\n\n".format(inimigo.nome, inimigo.vida) + Style.RESET_ALL)
                    break
                else:
                    ataque = Inimigo_ataque.ataque_do_inimigo(inimigo, personagem)
                    personagem.vida = personagem.vida - ataque

            elif seletor == 5:
                cura = personagem.Cura()
                print(Fore.LIGHTBLUE_EX + "voce se cura em {}".format(cura) + Style.RESET_ALL)
                input("\n\n>>>Digite qualquer coisa para continuar")
                personagem.vida = personagem.vida + cura
                if inimigo.vida <= 0:
                    print(Fore.LIGHTRED_EX + "A Vida do {} è: {}\n\n".format(inimigo.nome, inimigo.vida) + Style.RESET_ALL)
                    break
                else:
                    ataque = Inimigo_ataque.ataque_do_inimigo(inimigo, personagem)
                    personagem.vida = personagem.vida - ataque

            elif seletor == 6:
                personagem.Restaurar_Mana(personagem.item1)
                print(Fore.LIGHTBLUE_EX + "sua mana agora é {}".format(personagem.mana) + Style.RESET_ALL)
                if inimigo.vida <= 0:
                    print(Fore.LIGHTRED_EX + "A Vida do {} è: {}\n\n".format(inimigo.nome, inimigo.vida) + Style.RESET_ALL)
                    break
                else:
                    ataque = Inimigo_ataque.ataque_do_inimigo(inimigo, personagem)
                    personagem.vida = personagem.vida - ataque
            else: print("<<<valor digitado invalido>>>".upper())


        elif seletor == 3: # slide : uml ,poilmorfismo, herança, interface,  oq cd um fez ,
            os.system('cls')
            print(personagem,"\nItem 1", personagem.item1)
        else: 
            print("<<<valor digitado invalido>>>".upper())

            #loop_de_teste = Falso