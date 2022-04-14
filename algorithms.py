from queue import Queue, PriorityQueue
from graph import Graph
from nod_parcurgere import  NodParcurgere
from time import time
import stopit

@stopit.threading_timeoutable(default="Timed out") 
def breadth_first(gr: Graph, nr_solutii_cautate, f_out, t0):
    NodParcurgere.reset_drumuri()

    coada = Queue()
    coada.put(NodParcurgere(gr.start, None))

    while not coada.empty():
        nod_curent = coada.get()
        if gr.testeaza_scop(nod_curent):
            f_out.write("Solutie:\n")
            nod_curent.afisDrum(f_out, afisCost=True, afisLung=True)
            f_out.write(f"\nTimp: {time() - t0}")
            f_out.write("\n\n----------------\n\n")
            nr_solutii_cautate -= 1
            if nr_solutii_cautate == 0:
                return
        lista_succesori = gr.genereaza_succesori(nod_curent)
        for nod in lista_succesori:
            coada.put(nod)

@stopit.threading_timeoutable(default="Timed out") 
def depth_first(gr: Graph, nr_solutii_cautate, f_out, t0):
    NodParcurgere.reset_drumuri()
    nod_initial = NodParcurgere(gr.start, None)
    return depth_first_aux(gr, nod_initial, nr_solutii_cautate, f_out, t0)

def depth_first_aux(gr:Graph,nod_curent: NodParcurgere, nr_solutii_cautate, f_out, t0):

    if nr_solutii_cautate <= 0:
        return nr_solutii_cautate
    if gr.testeaza_scop(nod_curent):
        f_out.write("Solutie:\n")
        nod_curent.afisDrum(f_out, afisCost=True, afisLung=True)
        f_out.write(f"\nTimp: {time() - t0}")
        f_out.write("\n\n----------------\n\n")
        nr_solutii_cautate -= 1
        if nr_solutii_cautate == 0:
            return nr_solutii_cautate

    lista_succesori = gr.genereaza_succesori(nod_curent)
    for sc in lista_succesori:
        if nr_solutii_cautate != 0:
            nr_solutii_cautate = depth_first_aux(gr, sc, nr_solutii_cautate, f_out, t0)

    return nr_solutii_cautate

@stopit.threading_timeoutable(default="Timed out") 
def depth_first_iterativ(gr: Graph ,nr_solutii_cautate, f_out, t0):
    NodParcurgere.reset_drumuri()
    for i in range(1,gr.numar_incuietori+1):
        if nr_solutii_cautate==0:
            return

    nod_initial = NodParcurgere(gr.start, None)
    nr_solutii_cautate = dfi(gr,nod_initial,7, nr_solutii_cautate, f_out, t0)

def dfi(gr:Graph, nod_curent: NodParcurgere, adancime, nr_solutii_cautate, f_out, t0):
    if adancime == 1 and gr.testeaza_scop(nod_curent):
        f_out.write("Solutie:\n")
        nod_curent.afisDrum(f_out, afisCost=True, afisLung=True)
        f_out.write(f"\nTimp: {time() - t0}")
        f_out.write("\n\n----------------\n\n")
        if nr_solutii_cautate==0:
            return nr_solutii_cautate
        nr_solutii_cautate-=1
    if adancime > 1:
        lista_succesori = gr.genereaza_succesori(nod_curent)
        for sc in lista_succesori:
            if nr_solutii_cautate != 0:
                nr_solutii_cautate = dfi(gr, sc,adancime-1, nr_solutii_cautate, f_out, t0)
    return nr_solutii_cautate

@stopit.threading_timeoutable(default="Timed out") 
def a_star(gr: Graph, nr_solutii_cautate, f_out, t0, euristica = "admisibila 2",):
    NodParcurgere.reset_drumuri()
    pq = PriorityQueue()
    pq.put((0, NodParcurgere(gr.start, None)))
    while not pq.empty():
        item = pq.get()
        nod_curent = item[1]

        if gr.testeaza_scop(nod_curent):
            f_out.write("Solutie:\n")
            nod_curent.afisDrum(f_out, afisCost=True, afisLung=True)
            f_out.write(f"\nTimp: {time() - t0}")
            f_out.write("\n\n----------------\n\n")
            nr_solutii_cautate-=1
            if nr_solutii_cautate==0:
                return
        lSuccesori=gr.genereaza_succesori(nod_curent, euristica)	
        for s in lSuccesori:
            pq.put((s.f, s))
            
@stopit.threading_timeoutable(default="Timed out")
def a_star_optimizat(gr: Graph, f_out, t0, euristica = "admisibila 2"):
    NodParcurgere.reset_drumuri()
    l_open=[NodParcurgere(gr.start, None)]
    l_closed=[]
    while len(l_open)>0:
        nod_curent=l_open.pop(0)
        l_closed.append(nod_curent)
        if gr.testeaza_scop(nod_curent):
            f_out.write("Solutie:\n")
            nod_curent.afisDrum(f_out, afisCost=True, afisLung=True)
            f_out.write(f"\nTimp: {time() - t0}")
            f_out.write("\n\n----------------\n\n")
            return
        lSuccesori=gr.genereaza_succesori(nod_curent, euristica)	
        for s in lSuccesori:
            gasitC=False
            for nodC in l_open:
                if s.info==nodC.info:
                    gasitC=True
                    if s.f>=nodC.f:
                        lSuccesori.remove(s)
                    else:
                        l_open.remove(nodC)
                    break
            if not gasitC:
                for nodC in l_closed:
                    if s.info==nodC.info:
                        if s.f>=nodC.f:
                            lSuccesori.remove(s)
                        else:
                            l_closed.remove(nodC)
                        break
        for s in lSuccesori:
            i=0
            gasit_loc=False
            for i in range(len(l_open)):
                if l_open[i].f>s.f or (l_open[i].f==s.f and l_open[i].g<=s.g) :
                    gasit_loc=True
                    break
            if gasit_loc:
                l_open.insert(i,s)
            else:
                l_open.append(s)

@stopit.threading_timeoutable(default="Timed out")
def ida_star(gr: Graph, nr_solutii_cautate, f_out, t0):
    NodParcurgere.reset_drumuri()
    nodStart=NodParcurgere(gr.start,None)
    limita=nodStart.f
    while True:

        print("Limita de pornire: ", limita)
        nr_solutii_cautate, rez= construieste_drum(gr, nodStart,limita,nr_solutii_cautate, f_out, t0)
        if rez=="gata":
            break
        if rez==float('inf'):
            print("Nu mai exista solutii!")
            break
        limita=rez
        print(">>> Limita noua: ", limita)


def construieste_drum(gr:Graph, nod_curent:NodParcurgere, limita, nr_solutii_cautate, f_out, t0):
    print("A ajuns la: ", nod_curent)
    if nod_curent.f>limita:
        return nr_solutii_cautate, nod_curent.f
    if gr.testeaza_scop(nod_curent) and nod_curent.f==limita :
        f_out.write("Solutie:\n")
        nod_curent.afisDrum(f_out, afisCost=True, afisLung=True)
        f_out.write(f"{limita} \n")
        f_out.write(f"\nTimp: {time() - t0}")
        f_out.write("\n\n----------------\n\n")
        nr_solutii_cautate-=1
        if nr_solutii_cautate==0:
            return 0, "gata"

    lSuccesori=gr.genereaza_succesori(nod_curent)	
    minim=float('inf')
    for s in lSuccesori:
        nr_solutii_cautate, rez=construieste_drum(gr, s, limita, nr_solutii_cautate, f_out, t0)
        if rez=="gata":
            return 0,"gata"

        print("Compara ", rez, " cu ", minim)
        if rez<minim:
            minim=rez
            print("Noul minim: ", minim)
    return nr_solutii_cautate, minim

