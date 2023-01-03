
class MT:
    def __init__(self, mot = "", fichier = "None"):
        self.fichier = fichier
        self.etat_accept = ""
        self.etat_courant = ""
        self.transition = dict()
        self.position_tetes = list()
        mot += "_"
        self.etat_bandes = [list(mot)]
        if fichier != "None":
            self.ouvrir_fichier()


    def ouvrir_fichier(self):
        cpt = 0
        with open(self.fichier, "r") as f:
            for line in f:
                line = line.strip().replace(" ", "").lower()
                if line == "" or line[0:2] == "//" or line[0:4] == "name":
                    continue
                if cpt == 0:
                    line = line.replace("init:", "")
                    self.etat_courant = line
                    cpt += 1
                    continue
                if cpt == 1:
                    line = line.replace("accept:", "")
                    self.etat_accept = line
                    cpt += 1
                    continue
                if (cpt % 2) == 0:
                    line_temp_1 = line.split(sep = ",", maxsplit = 1)
                    etat, conditions = line_temp_1[0], tuple(line_temp_1[1].split(sep = ","))
                    if etat not in self.transition.keys():
                        self.transition[etat] = {}
                    cpt += 1
                    continue

                if (cpt % 2) == 1:
                    line_temp = line.split(sep = ",", maxsplit = 1)
                    etat_suivant = line_temp[0]
                    line_temp = line_temp[1].split(sep = ",")
                    symboles, directions = line_temp[:(len(line_temp)//2)], line_temp[(len(line_temp)//2):]
                    self.transition[etat][conditions] = (etat_suivant, symboles, directions)
                    cpt += 1
                    continue

        self.position_tetes = [0 for _ in range(len(line_temp_1[1].split(sep = ",")))]
        for _ in range(len(line_temp_1[1].split(sep = ",")) - 1):
            self.etat_bandes.append(['_'])

                
    def step(self):
        tetes = tuple()
        for i in range(len(self.position_tetes)):
            tetes += tuple(self.etat_bandes[i][self.position_tetes[i]])

        try:
            etat_suivant, nouveaux_symboles, directions = self.transition[self.etat_courant][tetes]
        except KeyError:
            print('faux')
            return False

        for i in range(len(self.position_tetes)):
            if self.position_tetes[i] == 0 and directions[i] == '<':
                self.etat_bandes[i].insert(0, '_')
                self.position_tetes[i] += 1
            elif self.position_tetes[i] == len(self.etat_bandes[i]) - 1 and directions[i] == '>': 
                self.etat_bandes[i].append('_')

            self.etat_bandes[i][self.position_tetes[i]] = nouveaux_symboles[i]
            if directions[i] == '>':
                self.position_tetes[i] += 1
            elif directions[i] == '<':
                self.position_tetes[i] -= 1
        self.etat_courant = etat_suivant
        return True


    def calcul(self):
        cpt = 0
        while all(self.position_tetes[i] >= 0 and self.position_tetes[i] < len(self.etat_bandes[i]) for i in range(len(self.position_tetes))) and self.etat_accept != self.etat_courant and (cpt < 100_000):
            cpt += 1
            if self.step():
                print("")
            else:
                print("Erreur")
                return False
            for bande in self.etat_bandes:
                print(bande)
            print(self.etat_courant)
        print("fini")

"""
M1.txt
(q5M1,(0,1,0),Left3,q6M1)
q5M1, 0, 0,0
qleft1 0,0,0, -,-,<
qleft1, 0, 1,0
qleft1 0,1,0, -,-,<"""

#insert(0, x) au debut ; append(x) a la fin
mt1 = MT("111#1110","TM/mt1.txt")
#print(mt1.transition)
#print(tuple(("1,2,3,4,5".split(sep=",", maxsplit=1)[1]).split(",")))
#mt1.step()
#print(mt1.transition[mt1.etat_courant][('0',)])
mt1.calcul()


"""def linker (fichier1, fichier2):
    #(qappel, 0, MT2, qfin_appel)
    # qappel, 0
    # MT2.txt, qfin_appel
    # fichier.txt, qfin_appel

    # if alors lire fichier
    mt2 = MT("111#1110","mt2.txt")
    qappel, 0
    qinit, 0, >

    qaccept, 0
    qfin_appel, 0, -

    pass"""


#linker("mt1.txt", "mt2.txt")
#mt3 = MT("111#1110", "./TM/mt1.txt")





