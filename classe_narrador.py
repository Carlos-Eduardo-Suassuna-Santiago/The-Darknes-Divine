import pyttsx3
import sys,time,os
from colorama import Fore, Style

"""Classe que contem A narradora da biblioteca pyttsx3, ela lé um arquivo txt em alguem idioma"""

class Narrador: #narra o texto
    
    def narrando(pasta,contador,inicio_decontagem):
        #contador = 0
        #pasta = 'Falas/Texto.txt'
        while inicio_decontagem <= contador:
            nx = pasta.replace('_',str(inicio_decontagem))
            #print(nx) VERIFICAR POSICAO DO ARQUIVO
            f1 = open(nx, 'r', encoding='utf8')
            texto = f1.read()
    
            print(Fore.YELLOW + texto + Style.RESET_ALL)#printar o texto contido na variavel
            speaker = pyttsx3.init()#variavel que vai iniciar a biblioteca
            voices = speaker.getProperty("voices")#variavel que vai aguardar as variaveis de voz
            speaker.setProperty("voice", voices[0].id)#sentando a voz que vai ser usada e o idioma
            rate = speaker.getProperty("rate")
            speaker.setProperty("rate", rate+10)#definindo a velocidade que a voz vai ler o texto rate+2000 rapidão
            speaker.say(texto)#ler o texto da variavel
            speaker.runAndWait()          
            inicio_decontagem= inicio_decontagem+1
