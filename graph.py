import copy

from nod_parcurgere import NodParcurgere
from nod_parcurgere import Incuietoare

class Graph: 
    """
    
    start = starea initiala (lista de incuietori cu valoarea 1)
    scop = starea finala (lista de incuietori cu valoare 0)

    """    
    def __init__(self, nume_fisier):
        f = open(nume_fisier, 'r')
        self.numar_incuietori = int(f.readline().strip()) 
        self.start = [Incuietoare(1) for i in range(self.numar_incuietori)] # 1 inseamna inchis 
        self.scop = [Incuietoare(0) for i in range(self.numar_incuietori)] # 0 inseamna deschis
        self.k = int(f.readline().strip())
        
        line = f.readline()
        while '->' in line:
            numere = [int(i) for i in line.strip().split('->')]
            self.start[numere[0]].truc = True  
            self.start[numere[0]].nod_afectat = numere[1]
            line = f.readline()
        self.keys = []
        while line:
            self.keys.append(line.strip())
            line = f.readline()
        
        
    def testeaza_scop(self, nod_curent:NodParcurgere):
        for i in range(self.numar_incuietori):
            if nod_curent.info[i] != self.scop[i]:
                return False

        return True
    
    def genereaza_succesori(self, nod_curent: NodParcurgere, euristica = "admisibila 2") -> list[NodParcurgere]:
        """
            functia de generare succesori dintr-un nod dat
        Args:
            nod_curent (NodParcurgere): 
            euristica (str, optional):  Defaults to "admisibila 2".

        Returns:
            list[NodParcurgere]: lista de noduri generate 
        """
        lista_succesori = []
        for cheie in self.keys: 
            if not cheie in nod_curent.used_keys or nod_curent.used_keys[cheie]  < self.k: 
                # daca nu am folosit cheia sau am folosit-o de mai putin de k ori
                if not nod_curent.drum_deja_parcurs(cheie): # verific daca drumul a fost deja parcurs
                    new_node = self.aplica_cheie(cheie, nod_curent) # returneaza nodul nou dupa aplicarea cheii
                    new_node.parinte = nod_curent
                    new_node.h = self.calculeaza_h(new_node, euristica)
                    new_node.g += 1       # lungimea drumului creste cu 1 
                    new_node.calculeaza_f()
                    new_node.cheie = cheie
                    if not cheie in new_node.used_keys:
                        new_node.used_keys[cheie] = 1
                    else:
                        new_node.used_keys[cheie] += 1
                    lista_succesori.append(new_node)
        return lista_succesori

    def aplica_cheie(self, cheie: str, nod_curent: NodParcurgere) -> NodParcurgere:
        """ 
        Schimb valoarea lacatului in functie de cheie
        Args:
            cheie (str)
            nod_curent (NodParcurgere):

        Returns:
            NodParcurgere
        """
        copie_nod_curent = copy.deepcopy(nod_curent) # creez un nou nod din nodul curent
        for i in range(len(cheie)):
            if cheie[i] == "g":
                continue
            elif cheie[i] == "i":
                copie_nod_curent.info[i].value += 1
            elif cheie[i] == "d" and copie_nod_curent.info[i].value > 0: # daca nu este deja deschis 
                copie_nod_curent.info[i].value -= 1
                copie_nod_curent.cost_mutare += 1 # costul creste cu 1 pentru fiecare deschidere
                if copie_nod_curent.info[i].truc: # daca incuietoarea este una truc 
                    indice_nod_incuiat = copie_nod_curent.info[i].nod_afectat 
                    copie_nod_curent.info[indice_nod_incuiat].value += 1 # adaug 1 la valoarea nodului afectat
                        
        return copie_nod_curent

    def calculeaza_h(self, new_node: NodParcurgere, tip_euristica="banala"):
        if tip_euristica == "banala":
            if new_node.info == self.scop:
                return 1
            return 0

        elif tip_euristica == "gresita":
            h = 0
            for i in new_node.info:
                if i.value == 0:
                    h += 1
            return h 
        elif tip_euristica == "admisibila 1":
            """
                cresc euristica cu valoarea lacatului 
            """
            h = 0
            for i in new_node.info:
                h += i.value
            return h

        elif tip_euristica == "admisibila 2":
            """
                cresc euristica cu valoarea lacatului iar daca incuietoarea este truc adaug valoarea de 2 ori
            """
            h = 0
            for i in new_node.info:
                h += i.value
                if i.truc:
                    h += i.value
            return h
    def __repr__(self):
        sir=""
        for (k,v) in self.__dict__.items() :
            sir+="{} = {}\n".format(k,v)
        return(sir)