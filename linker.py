##On considère maintenant le modèle de machine de Turing étendu par des instructions d’appel de machine de Turing (comme vu en cours). 
# On rappelle que si une machine M à la transition spéciale (q, a, M′, q′), alors dans l’état q et à la lecture de a elle lance le calcul de la machine M′. 
# Quand M′ a fini son calcul, alors M passe dans l’état q ′. On a en entrée le code de deux machines de Turing M1 et M2 tel que la machine M1 fait des appels à M2. 
# Votre fonction doit produire une machine M3, sans appel à M2 qui réalise le même calcul que M1. Bravo, vous venez de réaliser un linker.

def linker (file1, file2, out):
    with open (file1, "r") as f1:
        lines1 = f1.readlines()

    with open (file2, "r") as f2:
        lines2 = f2.readlines()

    lines3 = []
    for val in lines1:
        if "(" not in val:
            lines3.append(val)
            continue

        line_temp = val.strip().replace(" ", "")[1:-1].split(sep = ',')
        lines3.append("// Début de la Machine de Turing {}'\n".format(line_temp[-2]))

        for val2 in lines2:
            if val2 == "" or val2[0:2] == "//" or val2[0:4] == "name":
                continue
            if val2[0:4].lower() == "init":
                val2 = val2.replace("init:", "")
                init3 = val2
                continue
            if val2[0:6].lower() == "accept":
                val2 = val2.replace("accept:", "")
                accept3 = val2
                continue

            temp = "".format(line_temp[0:-2])
            print(temp)








    with open (out, "w") as f3:
        f3.writelines(lines3)
    print(lines3)










    ##on parcours les lines du premier fichier et on les met dans une liste et a la fin on ecrit la list dans le fichier out ou alors chaque ligne on l'ecrit dans le fichier out
    ## si on tombe sur une transition de la forme ..... -> ..... alors on commence a lire le deuxieme fichier et on fait des trucs dedans  


linker("Turing_Machine/mt1.txt", "Turing_Machine/addition.txt", "Turing_Machine/file3.txt")
"""
    (qappel, (0,0,1), MT2, qfin_appel)
à rajouter dans le .txt
    (qappel,0,0,1,MT2.txt,qfin_appel)

    qfin_appel,0,0,1

à rajouterc dans le nouveau .txt grace au code python :

    qappel,0,0,1
    qinit de MT2,0,0,1,-,-,-

    rajoute toutes les transitions renommé de MT2

    qaccept de MT2, toutes les possibilités
    qfin_appel, les mêmes possibilités,-,-,-

    rajoute la fin MT1


    q0, 1
    (MT2), 0, >


lines1 partie 1
enleve transition spéciale
mets les nouvelles transitions
remets lines1 partie 2

enregistrer dans fichier 3



(qappel,0,0
MT2,qfin_appel)
qapelle,0,0
q1,0,0,-,-


// CODE DE MT1
q0,#,_
q2,_,#,>,<

q0, ----
qleft,-----


//DANS LE FICHIER 2
init : q1
accept: qaccept

q1,0,0
q1,0,0,-,<

q1,0,1
q1,0,1,-,<

q1,1,0
q1,1,0,-,<

q1,1,_
qAccept,1,_,-,>

q1,0,_
qAccept,0,_,-,>


//ON SORT DU FICHiER 2
//SUITE DE MT1
"""



