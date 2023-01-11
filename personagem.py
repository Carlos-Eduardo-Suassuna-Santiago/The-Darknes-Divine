import os
import abc
import sys
import random
#from Classes.Inimigos import Inimigo
import xp
from objetos import armas
from Inimigos import ini_lista
from texto import texto_devagar
from colorama import Fore, Style
from interface_de_luta import interface_l
from combate import Magicos, Suporte, fisicos


class Status(abc.ABC):

    def __init__ (self, vida, mana, ataque, defesa, inteligencia, sorte, LV, xp):
        self.vida = vida
        self.mana = mana
        self.ataque = ataque
        self.defesa = defesa
        self.inteligencia = inteligencia 
        self.sorte = sorte
        self.LV = LV 
        self.xp = xp

    @abc.abstractmethod
    def receber_dano(self, dano):
        self.vida = self.vida - dano
        if self.vida <= 0:
            print("FIM DE JOGO")
            return sys.exit()
        else:
            return print(self.vida)

    @abc.abstractmethod
    def Causar_dano(self):
        return self.ataque + 10


class Personagem(Status, fisicos, Suporte, Magicos):

    def __init__ (self, nome, vida, mana, ataque, defesa, inteligencia, sorte, LV, xp, item1, item2):
        super().__init__(vida, mana, ataque, defesa, inteligencia, sorte, LV, xp)
        self.nome = nome
        self.item1 = item1
        self.item2 = item2

    def Causar_dano(self):
        return self.ataque + 10

    def receber_dano(self, dano): 
        self.vida = self.vida - dano
        if self.vida <= 0:
            print("FIM DE JOGO")
            return sys.exit()
        else:
            return print(self.vida)

    
    def __str__(self) -> str:
        texto = (Fore.LIGHTYELLOW_EX + "Nome = `{}´\nLevel = {}\nvida = {}\nmana = {}\nataque = {}\ndefesa = {}\ninteligencia = {}\n".format(self.nome, self.LV,self.vida, self.mana, self.ataque, self.defesa, self.defesa, self.inteligencia) + Style.RESET_ALL)
        return str(texto_devagar.texto(texto))


    
class NPC(Status):

    def __init__(self, nome, vida, mana, ataque, defesa, inteligencia, sorte, LV, xp):
        super().__init__(vida, mana, ataque, defesa, inteligencia, sorte, LV, xp)
        self.nome = nome

    def Causar_dano(self):
        return self.ataque + 0

    def receber_dano(self, dano):
        self.vida = self.vida - dano
        if self.vida <= 0:
            print("o NPC desmaiou")
            return print("o NPC desmaiou")
        else:
            return print("a vida de",self.nome,"é igual a:",self.vida)