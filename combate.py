import random
from texto import texto_devagar
from colorama import Fore, Style

"""A classe 'fisicos' é uma classe com os ataques fisicos do game, aqui ficaram armazenados os ataques que personagens com arco e espada utilizaram
os ataques aqui contidos utilizaram o A-T-A-Q-U-E para causar dano"""
class fisicos:
    
    def corte(personagem, inimigo, arma):#player só funciona seequipado com uma arma tipo 2 espada
        if arma.tipo == 2:
            passagem = 1
            if personagem.mana <= 20:
                texto =(Fore.CYAN + "\n<<<mana insuficiente>>>\nVoce precisa de '20' de mana para executar esse ataque".upper() + Style.RESET_ALL)
                texto_devagar.texto(texto)
                passagem = 0
            if inimigo.vida <= 100:
                texto = ("Voce acerta um golpe em um ponto vital do {} ele não tem mais condiçoes e lutar\n".format(inimigo.nome))
                texto_devagar.texto(texto)
                dano = inimigo.vida + 9999
                inimigo.vida = inimigo.vida - dano
                return inimigo.vida
            if passagem == 1:
                personagem.mana = personagem.mana - 20
                dano = (arma.ataque + personagem.ataque) * 4
                inimigo.vida = inimigo.vida - dano
                return inimigo.vida
        else:
            texto =("\n<<<voce precisa de uma espada para executar esse ataque>>>\n".upper())
            texto_devagar.texto(texto)
    
    def tiro_concentrado(personagem, inimigo, arma):
        if arma.tipo == 1:
            
            passagem = 1
            if personagem.mana <= 40:
                texto =(Fore.CYAN + "\n<<<mana insuficiente>>>\nVoce precisa de '40' de mana para executar esse ataque\n".upper() + Style.RESET_ALL)
                texto_devagar.texto(texto)
                passagem = 0
            if inimigo.vida <= 100:
                texto = ("Um tiro certeiro na cabeça do {} o executando antes que ele executar qualquer outra ação\n".format(inimigo.nome))
                texto_devagar.texto(texto)
                dano = inimigo.vida + 9999
                inimigo.vida = inimigo.vida - dano
                return inimigo.vida
            if passagem == 1:
                personagem.mana = personagem.mana - 40
                dano = (arma.ataque + personagem.ataque) * 3 
                inimigo.vida = inimigo.vida - dano
                return inimigo.vida
        else:
            texto =("\n<<<voce precisa de um arco para executar esse ataque>>>\n".upper())
            texto_devagar.texto(texto)

    def lobo_mordida(inimigo, jogador): #inimigo lobo
        sorte = random.randrange(10)
        sorte = sorte + 90
        if sorte == 97:
            texto =("Errou o ataque")
            texto_devagar.texto(texto)
            return 0
        else:
            return (inimigo.ataque + 10) - jogador.defesa / 2


    def patada(inimigo, jogador): #inimigo urso
        sorte = random.randrange(10)
        sorte = sorte + 90
        if sorte == 97:
            texto =("Errou o ataque")
            texto_devagar.texto(texto)
            return 0
        else:
            return (inimigo.ataque * 2) - jogador.defesa / 2

    def chefe_socao(inimigo, jogador):
        texto =(Fore.LIGHTRED_EX + "\no chefe avança rapidamente e lhe acerta um socao\n" + Style.RESET_ALL)
        texto_devagar.texto(texto)
        return (inimigo.ataque * 2) - jogador.defesa / 5

    def corte_sombrio(inimigo, jogador):
        texto =(Fore.LIGHTRED_EX + "\no chefe coloca a espada na bainha e executa um corte que parece cortar a propria realidade\n" + Style.RESET_ALL)
        texto_devagar.texto(texto)
        return (inimigo.ataque * 10)
    
"""A classe Magicos, contem os ataques magicos do jogos para seram utilizados por personagens com cajado
o status predominante aqui é a inteligencia"""
class Magicos:

    def bola_fogo (personagem, inimigo, arma):
        passagem = 0
        if arma.tipo == 3:
            passagem = 1
            if personagem.mana <= 49:
                texto =("\n<<<mana insuficiente>>>\nVoce precisa de '50' de mana para executar essa ação\n".upper())
                texto_devagar.texto(texto)
                passagem = 0
                return passagem

            if passagem == 1:
                personagem.mana = personagem.mana - 50
                ataque = personagem.inteligencia * 2 + 20
                inimigo.vida = inimigo.vida - ataque
                return inimigo.vida
        else:
            texto =("\n<<<voce precisa de um cajado para executar esse ataque>>>\n".upper())
            texto_devagar.texto(texto)
            
    def Caixao_De_gelo (personagem, inimigo, arma):
        passagem = 0
        if arma.tipo == 3:
            passagem = 1

            if personagem.mana < 5000:
                texto =(Fore.CYAN + "\n<<<mana insuficiente>>>\nVoce precisa de '5000' de mana para executar essa magia\n".upper() + Style.RESET_ALL)
                texto_devagar.texto(texto)
                passagem = 0
                return 0
            if inimigo.vida <= 10000:
    
                texto =(Fore.BLUE + "Uma tespestade de gelo é formada em volta do {}\n".format(inimigo.nome) + Style.RESET_ALL)
                texto_devagar.texto(texto)
                texto =(Fore.LIGHTRED_EX + "{}: O que esta a con...\n".format(inimigo.nome) + Style.RESET_ALL)
                texto_devagar.texto(texto)
                texto =(Fore.BLUE +"Antes que o {} pode se dizer mais qualquer coisa\nTUDO em volta virou gelo\n".format(inimigo.nome) + Style.RESET_ALL)
                texto_devagar.texto(texto)

                texto =(Fore.BLUE +"O {}, esta completamente imovel preso em um caixão denso de gelo transparente\n".format(inimigo.nome) + Style.RESET_ALL)
                texto_devagar.texto(texto)
                texto =(Fore.GREEN + "{}: Tão lindo, imovel como uma pintura em um quadro\n".format(personagem.nome) + Style.RESET_ALL)
                texto_devagar.texto(texto)
                texto =(Fore.GREEN + "{}: Bom, ja que a frozen não vai mais se mexer".format(personagem.nome) + Fore.BLACK + " NUNCA MAIS " + Fore.GREEN + "Eu vou em bora\n" + Style.RESET_ALL)
                texto_devagar.texto(texto)
                texto =(Fore.BLUE +"Você se vira e vai em bora atravessando um mar de flocos de neve, deixando uma trilha por onde passa.\n" + Style.RESET_ALL)
                texto_devagar.texto(texto)
                texto =(Fore.GREEN + "{}: Meus pulmoes estão congelando é melhor sair logo daqui...\n".format(personagem.nome) + Style.RESET_ALL)
                texto_devagar.texto(texto)
                dano = inimigo.vida - inimigo.vida - 1
                inimigo.vida = dano
                return inimigo.vida

            if passagem == 1:
                personagem.mana = personagem.mana - 5000
                dano = (personagem.inteligencia * 16) + 120 
                inimigo.vida -= dano
                return inimigo.vida
        else:
            texto =("\n<<<voce precisa de um cajado para executar esse ataque>>>\n".upper())
            texto_devagar.texto(texto)

"""A classe suporte contem açoes que fortalecem o perssonagem, curando-o aumentando o seu ataque ou defesa, as açoes aqui só afetam o personagem"""

class Suporte:

    def Restaurar_Mana(personagem, item):
        if(item.tipo == 1 or item.tipo == 2):
            texto =("Você respira fundo, reajusta a sua posição de combate e fortalece a sua determinação\n",Fore.GREEN + "{}: È AGORA POHAAAA!!!, nunca que eu perderia para um demmonia froxo como você\n".format(personagem.nome) + Style.RESET_ALL)
            texto_devagar.texto(texto)
            input("\n---------------->>>Digite qualquer coisa para continuar<<<----------------\n")
            personagem.mana = personagem.mana + 300
            return personagem.mana
        elif(item.tipo == 3):
            texto =("Você respira fundo, e se lembra dos seus ensinamentos na academia de magos")
            texto_devagar.texto(texto)
            input("\n---------------->>>Digite qualquer coisa para continuar<<<----------------\n")
            personagem.mana = personagem.mana + 500
            return personagem.mana
   
    def Cura(personagem):
        if personagem.mana <= 99:
            texto =(Fore.CYAN + "\n<<<mana insuficiente>>>\nVoce precisa de '5000' de mana para executar essa ação\n".upper() + Style.RESET_ALL)
            texto_devagar.texto(texto)
            passagem = 0
            cura = 0
            return cura

        personagem.mana = personagem.mana - 100
        passagem = 1
        if passagem == 1:
            cura = personagem.inteligencia + 1000
            return cura

    def O_D_I_O(personagem):
        texto =(Fore.YELLOW + "{}: T-O__P-U-T-O `-´".format(personagem.nome) + Style.RESET_ALL)
        texto_devagar.texto(texto)
        texto =("Seu Ataque foi Dobrado")
        texto_devagar.texto(texto)
        texto =("E Sua Inteligencia Diminuio")
        texto_devagar.texto(texto)
        return 2

"""Classe que executa o ataque de inimigos, caso novos inimigos sejam adicionados devesse alterar aqui"""
class Inimigo_ataque(fisicos, Magicos, Suporte):

    def ataque_do_inimigo(inimigo, personagem):
        texto =("O {} ataca!!!".format(inimigo.nome, personagem))
        texto_devagar.texto(texto)
        if inimigo.nome == 'Lobo':
            ataque = fisicos.lobo_mordida(inimigo, personagem)
            return ataque
        elif inimigo.nome == 'Urso':
            ataque = fisicos.patada(inimigo, personagem)
            return ataque
        elif inimigo.nome == "Demonio do castelo":

            chose = random.randrange(1, 5)
            if chose == 1:
                ataque = fisicos.chefe_socao(inimigo, personagem)
                texto =("O dano recebido foi: {}".format(ataque))
                texto_devagar.texto(texto)
                return ataque
            elif chose == 2:
                ataque = fisicos.chefe_socao(inimigo, personagem)
                texto =("O dano recebido foi: {}".format(ataque))
                texto_devagar.texto(texto)
                return ataque
            elif chose == 3:
                ataque = fisicos.chefe_socao(inimigo, personagem)
                texto =("O dano recebido foi: {}".format(ataque))
                texto_devagar.texto(texto)
                return ataque
            elif chose == 4:
                ataque = fisicos.corte_sombrio(inimigo, personagem)
                texto =("O dano recebido foi: {}".format(ataque))
                texto_devagar.texto(texto)
                return ataque
