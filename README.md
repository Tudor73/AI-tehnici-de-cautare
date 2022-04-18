# AI-tehnici-de-cautare

# Rulare 

python main.py (input_folder) (NSOL) (TIMEOUT) <br>

Exemplu de utilizare: 

    python main.py input_files 4 10

In main.py se apeleaza algoritmii de cautare pe fisierele de input

# Memorarea datelor

Lacatul este format din n incuietori  
O incuietoare are o valoare ( 0 pentru deschis, mai mare sau egal cu 1 pentru inchis), truc (daca este cu truc sau nu) si incuietoare afectata pentru cele cu truc  

Nodul parcurgere contine in info o stare a lacatului ( o lista de incuietori )  
Graful contine starea intiala (lista de incuietori cu valoarea 1), starea scop (lista de incuietori cu valoarea 0 ), numarul k si lista de chei (memorate ca strings)

# Euristici 
## Banala
Verifica daca starea este scop sau nu  

    if tip_euristica == "banala":
        if new_node.info == self.scop:
            return 1
        return 0
## Admisibila 1
Creste valoarea h cu valoarea fiecarei incuietori (astfel starile cu multe noduri inchise vor avea un h mai mare)  

    elif tip_euristica == "admisibila 1":
        h = 0
        for i in new_node.info:
            h += i.value
        return h
## Admisibila 2
Creste valoarea h cu valoarea fiecarei incuietori iar daca incuietoarea este truc adaug valoarea de 2 ori ( ex: daca incuietoarea are valoarea 2 si este truc costul o sa creasca cu 4 pentru ca la fiecare deschidere se inchide alta incuietoare )  

    elif tip_euristica == "admisibila 2":
        h = 0
        for i in new_node.info:
            h += i.value
            if i.truc:
                h += i.value
        return h
## Gresita 
Creste valoarea h cu 1 pentru fiecare incuietoare deschia deci starile cu mai multe incuietori deschise vor avea h mai mare si algoritmul se indeparteaza din ce in ce mai mult de solutie  

    elif tip_euristica == "gresita":
        h = 0
        for i in new_node.info:
            if i.value == 0:
                h += 1
        return h 


