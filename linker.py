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
        if "(" not in val or ")":
            lines3.append(val)
            continue
        if "(" in val:
            temp = val
            continue
        temp = lines1[lines1.index(val)-1]
        lines3.append("// Description de la machine M'\n")
        lines3.append(val.replace(" ", "")[1:])
        for val2 in lines2:
            if val2[0:2] == "//":
                continue
            if val2[0:4].lower() == "init":
                #val2[5:] + val suivant
                
                pass
#recuperer init du lines 2 et changer les inits


    with open (out, "w") as f3:
        f3.writelines(lines1)
    print(lines3)
    ##on parcours les lines du premier fichier et on les met dans une liste et a la fin on ecrit la list dans le fichier out ou alors chaque ligne on l'ecrit dans le fichier out
    ## si on tombe sur une transition de la forme ..... -> ..... alors on commence a lire le deuxieme fichier et on fait des trucs dedans  


linker("mt1.txt", "mt1.txt", "file3.txt")
"""
    (qappel, (0,0,1), MT2, qfin_appel)
à rajouter dans le .txt
    (qappel,0,0,1
    MT2.txt,0,0,1,-,-,-)

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

"""

