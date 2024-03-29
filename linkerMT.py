# On considère maintenant le modèle de machine de Turing étendu par des instructions d’appel de machine de Turing (comme vu en cours). 
# On rappelle que si une machine M à la transition spéciale (q, a, M′, q′), alors dans l’état q et à la lecture de a elle lance le calcul de la machine M′. 
# Quand M′ a fini son calcul, alors M passe dans l’état q ′. On a en entrée le code de deux machines de Turing M1 et M2 tel que la machine M1 fait des appels à M2. 
# Votre fonction doit produire une machine M3, sans appel à M2 qui réalise le même calcul que M1. Bravo, vous venez de réaliser un linker.

def linker(file1, file2, out):
    with open (file1, "r") as f1:
        lines1 = f1.readlines()

    lines3 = []
    accept3 = "$None$"
    for val in lines1:
        if "(" not in val[0]:
            lines3.append(val)
            continue

        # Format d'un appel du linker (qappel,0,0,1,MT2,qfinappel)
        line_temp = val.strip().replace(" ", "")[1:-1].split(sep = ',')
        titre = line_temp[-2]
        lines3.append(f"\n// Début de l'appel de la Machine de Turing {titre}\n\n")

        with open(f'Q7-8/{titre}.txt', "r") as f2:
            lines2 = f2.readlines()

        for val2 in lines2:
            if val2 == "\n" or val2[:2] == "//" or val2[:4] == "name":
                lines3.append(val2)
                continue
            if val2[:4].lower() == "init":
                init3 = val2.replace("init:", "").strip()
                continue

            if val2[:6].lower() == "accept":
                accept3 = val2.replace("accept:", "").strip()

                transition = ','.join(line_temp[:-2])
                lines3.extend(
                    (
                        transition + "\n",
                        titre
                        + init3
                        + ','
                        + ','.join(line_temp[1:-2])
                        + ','
                        + ','.join(['-' for _ in range(len(line_temp[1:-2]))])
                        + '\n',
                    )
                )
                continue

            if accept3 in val2:
                lines3.append(val2.replace(accept3, line_temp[-1]))
                continue

            lines3.append(titre + val2)
        lines3.append(f"\n// Fin de l'appel de la Machine de Turing {titre}\n\n")

    with open (out, "w") as f3:
        f3.writelines(lines3)
