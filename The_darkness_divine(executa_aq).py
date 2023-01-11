import os
import fases
import pygame
from time import sleep
from classe_narrador import*

opcao = 's'
while opcao == 's':
    os.system('cls')
    pygame.init()
    pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
    pygame.mixer.music.load('Efeitos sonoros/introducao/sinos.mp3')
    pygame.mixer.music.play(-1)
    print(Fore.GREEN +'''  
                                                        CAVINJHOMO GAMES APRESENTA...
    ''' + Style.RESET_ALL)
    sleep(3)
    os.system('cls')

    print(Fore.RED +'''
                                                        ****************************
                                                        *                          *
                                                        *   THE DARKNESS DIVINE    *
                                                        *                          *
                                                        ****************************

    ''' + Style.RESET_ALL)
    sleep(3)
    print("Voce deseja pular a introdução?\nDigite 1 para não\nDigite 2 para sim")
    try: 
        seletor = int(input())
        os.system('cls')
    except:
        seletor = 2

    if seletor == 1:
        
        pygame.init()
        pygame.mixer.music.set_volume(0.10)#controlar o volume do meu audio
        pygame.mixer.music.load('Efeitos sonoros/introducao/terror.mp3')
        pygame.mixer.music.play(-1)
        inicio_decontagem = 0
        contador = 2
        pasta = 'Falas/Texto_.txt'
        p1 = Narrador.narrando(pasta,contador,inicio_decontagem)
        player_name = str(input("\nDIGITE O SEU NOME >>> "))
        tamanho_do_nome = len(player_name)
        player_name = player_name[0].upper() + player_name[1 : tamanho_do_nome]
        os.system('cls')

        pygame.init()
        pygame.mixer.music.set_volume(0.10)#controlar o volume do meu audio
        pygame.mixer.music.load('Efeitos sonoros/musica principal.mp3')
        pygame.mixer.music.play(-1)
        fases.Fase_1(player_name)

        pygame.init()
        pygame.mixer.music.set_volume(0.10)#controlar o volume do meu audio
        pygame.mixer.music.load('Efeitos sonoros/batalhafinal.mp3')
        pygame.mixer.music.play()
        fases.Fase_2()
        
        pygame.init()
        pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
        pygame.mixer.music.load('Efeitos sonoros/a-sinister-power-rising-epic-dark-gothic.mp3')
        pygame.mixer.music.play(-1)
        
        os.system('cls')
        print(Fore.GREEN +'''  
        DIREÇÃO DE SOM: CARLOS EDUARDO 
                            & KEVIN
                            
        DIREÇÃO DE ARTE: CARLOS EDUARDO
        
        HISTÓRIA DO GAME: CARLOS EDUARDO
                        JONATHAN
                        KEVIN
                        MOISÉS MONTEIRO
                        
        
        ''' + Style.RESET_ALL)
        sleep(7)
        os.system('cls')
        
        print('''
            FIM???
            
        ''')
        sys.exit()
        
    if seletor == 2:
        loop = True
        while loop == True:
            player_name = str(input("\nDIGITE O SEU NOME >>> "))
            try:
                tamanho_do_nome = len(player_name)
                player_name = player_name[0].upper() + player_name[1 : tamanho_do_nome]
                loop = False
            except:
                print("<<<Valor Invalido>>>\n")
                loop = True
        os.system('cls')
        pygame.init()
        pygame.mixer.music.set_volume(0.10)#controlar o volume do meu audio
        pygame.mixer.music.load('Efeitos sonoros/musica principal.mp3')
        pygame.mixer.music.play(-1)
        fases.Fase_1(player_name)

        pygame.init()
        pygame.mixer.music.set_volume(0.10)#controlar o volume do meu audio
        pygame.mixer.music.load('Efeitos sonoros/batalhafinal.mp3')
        pygame.mixer.music.play()
        fases.Fase_2()

        pygame.init()
        pygame.mixer.music.set_volume(0.30)#controlar o volume do meu audio
        pygame.mixer.music.load('Efeitos sonoros/a-sinister-power-rising-epic-dark-gothic.mp3')
        pygame.mixer.music.play(-1)

        os.system('cls')
        print(Fore.GREEN +'''  
        DIREÇÃO DE SOM: CARLOS EDUARDO 
                            & KEVIN

        DIREÇÃO DE ARTE: CARLOS EDUARDO

        HISTÓRIA DO GAME: CARLOS EDUARDO
                        JONATHAN
                        KEVIN
                        MOISÉS MONTEIRO


        ''' + Style.RESET_ALL)
        sleep(7)
        os.system('cls')

        print('''
            FIM???

        ''')
        sys.exit()