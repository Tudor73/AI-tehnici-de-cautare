import os
import sys
from graph import Graph
from nod_parcurgere import NodParcurgere
from time import time
from algorithms import breadth_first, depth_first, depth_first_iterativ, a_star, a_star_optimizat, ida_star
'''
TO DO 

afisare ca in cerinta 
linie de comanda parametri
documentatie 


'''

if __name__ == "__main__":
    
    input_folder = sys.argv[1]
    NSOL = int(sys.argv[2])
    TIMEOUT = int(sys.argv[3])   

    lista_fisiere= os.listdir(input_folder)

    if not os.path.exists("folder_output"):
        os.mkdir("folder_output")

    for nume_fisier in lista_fisiere:
        nume_fisier_output = "output_" + nume_fisier 
        f_out = open("folder_output/" + nume_fisier_output, 'w')

        path = f"./{input_folder}/{nume_fisier}"
        gr = Graph(os.path.join(os.path.dirname(__file__), path))

        f_out.write("BREADTH_FIRST: \n\n")
        t0 = time()
        breadth_first(gr,NSOL, f_out, t0,timeout = TIMEOUT)
        f_out.write("DEPTH_FIRST: \n\n")
        t0 = time()
        f_out.write(f"{depth_first(gr,NSOL,f_out,t0, timeout = TIMEOUT)}\n")
        f_out.write("\nDEPTH_FIRST_ITERATIV: \n\n")
        t0 = time()
        depth_first_iterativ(gr, NSOL,f_out,t0, timeout = TIMEOUT)
        f_out.write("\nA_STAR (euristica 1): \n\n")
        t0 = time()
        a_star(gr,NSOL, f_out, t0, euristica = "admisibila 1", timeout = TIMEOUT)
        f_out.write("\nA_STAR (euristica 2): \n\n")
        t0 = time()
        a_star(gr,NSOL, f_out, t0, euristica= "admisibila 2", timeout = TIMEOUT)
        f_out.write("\nA_STAR (banala): \n\n")
        t0 = time()
        a_star(gr,NSOL, f_out, t0, euristica = "banala", timeout = TIMEOUT)
        f_out.write("\nA_STAR (gresita): \n\n")
        t0 = time()
        a_star(gr,NSOL, f_out, t0, euristica = "gresita", timeout = TIMEOUT)
        f_out.write("\nA_STAR_OPTIMIZAT (euristica 1): \n\n")
        t0 = time()
        a_star_optimizat(gr, f_out, t0, euristica="admisibila 1", timeout = TIMEOUT)
        f_out.write("\nA_STAR_OPTIMIZAT (euristica 2): \n\n")
        t0 = time()
        a_star_optimizat(gr, f_out, t0, euristica="admisibila 2", timeout = TIMEOUT)
        # ida_star(gr, 5)