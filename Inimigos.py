import random
from combate import fisicos


class Inimigo: #clase com as informaçoes dos inimigos

    def __init__ (self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def Escolher_Ataque(self, ataque):
        x = random.randrange(3)
        

    def __str__(self):
        return str("-------------------------\n   Um Inimigo Apareceu\n-------------------------\n\nNome Inimigo: {}\nVida: {}\nAtaque: {}\nDefesa: {}".format(self.nome, self.vida, self.ataque, self.defesa))


class lista_inimigos(fisicos): #um lista com todos os inimigos
    
    def __init__ (self, lista):
        self.lista = lista
    
    def Mostra_lista_de_Inimigos(self, lista):
        
        a = 0
        for _ in self.lista:
            print(self.lista[a])
            a = a + 1
    def pegar_um_inimigo(self ,numero):
        return self.lista[numero - 1]

    def sortear_um_inimigo(self):
        return self.lista[random.randrange(3)]
        
    """Linha de ataque para os inimigos utilizados"""

     
ini_lista = lista_inimigos([],)


lobo = Inimigo ("Lobo", 150, 50, 5)
ini_lista.lista.append(lobo)
urso = Inimigo ("Urso", 500, 35, 50)
ini_lista.lista.append(urso)
carangueijo = Inimigo ("caranguiejo", 10, 10, 10)
ini_lista.lista.append(carangueijo)

ladrao = Inimigo ("Ladrão", 1000, 75, 35)
ini_lista.lista.append(ladrao)
guerreiro = Inimigo ("Guerreiro", 5000, 50, 75) 
ini_lista.lista.append(guerreiro)#
mago = Inimigo ("Mago", 750, 200, 25)
ini_lista.lista.append(mago)
chefe = Inimigo("Demonio do castelo", 20000, 100, 0)
ini_lista.lista.append(chefe)

#print(ini_lista.pegar_um_inimigo(7))
