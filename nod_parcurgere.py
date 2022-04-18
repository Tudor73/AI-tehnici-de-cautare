from copy import deepcopy


class Incuietoare:

    """
    Lacatul este format din mai multe incuietori 

    value = 1+ / 0 daca este inchis / deschis 
    truc : bool incuietoarea este cu truc sau nu 
    nod_afectat: nodul pe care incuietoarea il inchide daca aceasta este cu truc
    """
    def __init__(self, value = 1, truc = False, nod_afectat = -1):
        self.value = value
        self.truc = truc
        self.nod_afectat = nod_afectat

    def __eq__(self, incuietoare):
        return self.value == incuietoare.value

    # def __repr__(self):
    #     sir="{ "
    #     for (k,v) in self.__dict__.items() :
    #         sir+="{} = {} ".format(k,v)
    #     return sir + " }"
        
    def __repr__(self):
        sir = "inc("
        if self.value > 0:
            sir +="i," + str(self.value)
        else:
            sir += "d,0"
        sir +=")"
        return sir

class NodParcurgere:

    drumuri_parcurse = [{}] # toate drumurile deja parcurse de algoritm (succesiunea de chei folosita )
    def __init__(self, info: list[Incuietoare], parinte, used_keys= {}, cost=0, cost_mutare = 0, h=0):
        """_summary_

        Args:
            info : lista de incuietori echivalent cu valoarea lacatului 
            parinte : nodul parinte din arborele de parcurgere
            used_keys: cheile folosite pana acum 
            g :  lungimea drumului creste cu 1 pentru fiecare nod adaugat
            cost_mutare : costul creste cu 1 pentru fiecare deschidere
            h : eursitica
        """
        self.info=info  
        self.parinte=parinte 
        self.used_keys = used_keys
        self.cheie = None
        self.cost_mutare = cost_mutare
        self.g=cost 
        self.h=h
        self.f=self.g+self.h

    def obtineDrum(self):
        l=[self]
        nod=self
        while nod.parinte is not None:
            l.insert(0, nod.parinte)
            nod=nod.parinte
        return l
        
    def afisDrum(self, f_out, afisCost=False, afisLung=False): #returneaza si lungimea drumului
        l=self.obtineDrum()
        for nod in l:
            if nod.cheie:
                f_out.write(f"Folosim cheia {str(nod.cheie)}\n")
            f_out.write(f"{str(nod)}\n")
        if afisCost:
            f_out.write(f"Cost: , {self.cost_mutare} \n")
        if afisLung:
            f_out.write(f"Lungime: , {len(l)}")
        return len(l)


    def contineInDrum(self, new_node):
        nodDrum=self
        while nodDrum is not None:
            if nodDrum.used_keys != {} and new_node.used_keys == nodDrum.used_keys:
                return True
            nodDrum=nodDrum.parinte
        
        return False
        
    def drum_deja_parcurs(self, cheie):
        """
        Verifica daca succesiunea de chei a fost deja parcursa

        Adaug cheia curenta in dictionarul used_keys si verific daca dictionarul nou obtinut
            a fost intalnit deja 
        Args:
            cheie: string cheia curenta 

        Returns:
            boolean: daca drumul a fost sau nu parcurs deja 
        """
        copie_dict = deepcopy(self.used_keys)
        if not cheie in copie_dict: 
            copie_dict[cheie] = 1
        else:
            copie_dict[cheie] += 1
        if copie_dict in NodParcurgere.drumuri_parcurse:
            return True
        NodParcurgere.drumuri_parcurse.append(copie_dict)
        return False

    def calculeaza_f(self):
        self.f =  self.g + self.h

    def __lt__(self, node):
        return self.h > node.h
    
    def reset_drumuri():
        NodParcurgere.drumuri_parcurse = [{}]

    def __repr__(self):
        sir=""		
        sir+=str(self.info)
        return(sir)
