from os import remove
from asyncore import write

"""Classe eu salva e le arquivos em um txt, caso não exita um arquivo txt ele criara um com o nome save1.txt"""
class load_save():
    def __init__ (self, lista, save):
        self.lista = lista
        self.save = save

    """salva uma informação"""
    def salvar(self):
        with open ('save' + str(self.save) + ".txt", mode = "w", encoding= "utf8") as sv:
            for i in self.lista :
                sv.write(str(i) + '\n')
                
    """carrega uma informação"""
    def carregar(self):
        with open ('save' + str(self.save) + ".txt", mode = "r", encoding= "utf8") as cr:
            self.lista = cr.readlines()
            for i in range (0, len(self.lista), 1):
                x = ''
                x = self.lista[i]
                if i == 0:
                    self.lista[i] = x.replace("\n",'')

                else:
                    self.lista[i] = x.replace("\n",'')
                

        return self.lista