import random
from texto import texto_devagar
from colorama import Fore, Style
"""Uma classe para a criação de todos o itens que darão ataque e inteligencia para o personagem"""
class I_Ofensivo():  

    def __init__(self, nome, ataque,inteligencia, tipo, descricao):
        self.nome = nome
        self.ataque = ataque
        self.inteligencia = inteligencia
        self.tipo = tipo # 1 = arcos, 2 = espadas, 3 = cajados
        self.descricao = descricao

    def __str__(self):
        texto = Fore.WHITE + "\nItem: {}\nAtaque: {}\nInteligencia: {}\nTipo: {}\nDescricao: {}".format(self.nome, self.ataque, self.inteligencia, self.tipo, self.descricao) + Style.RESET_ALL
        return str(texto_devagar.texto(texto))
    
    
"""Uma Clase para a criação de todos os itens defencivos, que darão defesa"""
class I_Defencivo ():

    def __init__ (self, nome, defesa, descrisao):
        self.nome = nome
        self.defesa = defesa
        self.descrisao = descrisao

    def __str__(self):
        texto = Fore.WHITE + "\nItem: {}\nDefesa: {}\ndescrição: {}".format(self.nome, self.defesa, self.descrisao) + Style.RESET_ALL
        return str(texto_devagar.texto(texto))
        
"""uma classe com uma lista para juntos todos os itens do jogo em um só lugar e poder chamalos atravez da lista"""
class Itens(I_Ofensivo, I_Defencivo): #uma classe para criar uma lista com todos os itens
    def __init__ (self, item):
        self.item = item
    
    def __str__(self):
        texto = Fore.WHITE + "Item: {}\nAtaque: {}\nDefesa: \n{}{}".format(self.nome, self.ataque, self.inteligencia, self.tipo, self.descrisao) + Style.RESET_ALL
        return str(texto_devagar.texto(texto))

    """armazena os itens na lista"""
    def armazenar_itens(self, armazenar):
        self.item.append(armazenar)

    def get_arma(self, pegar):
        return self.item[pegar - 1]
    def sortear_itens_teste(self):
        return self.item[random.randrange(7)]
    
    def mostras_itens(self):
        a = 0
        for x in self.item:
            print(self.item[a])
            a = a + 1
    
armas = Itens ([],) #uma lista com todos os itens


# lista de itens do jogo
Arco_basico = I_Ofensivo ("Arco Inicial", 20, 0, 1, "\n(Um arco basico feito de madeira)")
armas.armazenar_itens(Arco_basico) 
Arco_avancado = I_Ofensivo ("Arco Avançado", 80, 0, 1, "\n(Um arco reforçado digno de ser utilizador por um bom arqueiro)") #de extrema qualidade muito bem reforçado, ele e pintado em preto e tem o nome de seu criador engravado em si
armas.armazenar_itens(Arco_avancado)
Arco_do_caçador = I_Ofensivo ("Arco do Caçador", 200, 1, 1, "Um arco magico passado por geraçoes de caçadores e elfos")
armas.armazenar_itens(Arco_do_caçador)

espada_basica = I_Ofensivo ("Espada Basica", 15, 0, 2, "\n(uma espada normal com uma aparencia velha)")
armas.armazenar_itens(espada_basica)
espada_avancado = I_Ofensivo ("Espada Avançado", 60, 0, 2, "\n(uma linda que aparenta ter sido feita com muito amor e carinho)")
armas.armazenar_itens(espada_avancado)
espada_lendaria = I_Ofensivo ("Espada Lendaria", 125, 0, 2, "Uma espada encantada capaz de cortar uma montanha ao meio")
armas.armazenar_itens(espada_lendaria)

cajado_basico = I_Ofensivo ("Cajado basico", 5, 15, 3, "\n(Um cajado de madeira\nParece que pegaram o primeiro pedaço de pau que viram pela frente e trouceram até aqui.)")
armas.armazenar_itens(cajado_basico)
cajado_avancado = I_Ofensivo ("Cajado avançado", 8, 50, 3, "\n(uma cajado de madeira, muito bem feito)")
armas.armazenar_itens(cajado_avancado)
cajado_pau = I_Ofensivo ("O Grande Pau", 0, 250, 3, "Um gravetinho que ja foi utilizado por um mago lengendario")
armas.armazenar_itens(cajado_pau)

tamba_de_barril = I_Defencivo ("Tamba de barril", 10, "uma tampa de barril com uma alça para segurar")
armas.armazenar_itens(tamba_de_barril)
escudo_basico = I_Defencivo ("escudo Basico", 25, "\n(Um escudo basico feito de madeira com seu acabamento de metal)")
armas.armazenar_itens(escudo_basico)

