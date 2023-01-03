class MT:
    def __init__(self, mot = "", fichier = "None"):
        self.name = "Machine de Turing Sans Nom"
        self.fichier = fichier
        self.etat_accept = ""
        self.etat_courant = ""
        self.transition = {}
        self.position_tetes = []
        mot += "_"
        self.etat_bandes = [list(mot)]
        if fichier != "None":
            self.ouvrir_fichier()


    def ouvrir_fichier(self):
        cpt = 0
        with open(self.fichier, "r") as f:
            for line in f:
                line = line.strip().replace(" ", "").lower()
                if line == "" or line[:2] == "//":
                    continue
                elif line[:4] == "name":
                    name = line.replace("name:", "")
                    self.name = name
                elif cpt == 0:
                    line = line.replace("init:", "")
                    self.etat_courant = line
                    cpt += 1
                elif cpt == 1:
                    line = line.replace("accept:", "")
                    self.etat_accept = line
                    cpt += 1

                elif (cpt % 2) == 0:
                    line_temp_1 = line.split(sep = ",", maxsplit = 1)
                    etat, conditions = line_temp_1[0], tuple(line_temp_1[1].split(sep = ","))
                    if etat not in self.transition.keys():
                        self.transition[etat] = {}
                    cpt += 1

                elif (cpt % 2) == 1:
                    line_temp = line.split(sep = ",", maxsplit = 1)
                    etat_suivant = line_temp[0]
                    line_temp = line_temp[1].split(sep = ",")
                    symboles, directions = line_temp[:(len(line_temp)//2)], line_temp[(len(line_temp)//2):]
                    self.transition[etat][conditions] = (etat_suivant, symboles, directions)
                    cpt += 1


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
        print(f'Name : {self.name}', sep = '')
        while all(self.position_tetes[i] >= 0 and self.position_tetes[i] < len(self.etat_bandes[i]) for i in range(len(self.position_tetes))) and self.etat_accept != self.etat_courant and (cpt < 100_000):
            affichage(self, cpt)
            cpt += 1
            if not self.step():
                print("Rejected")
                return False
        print("\nAccepted")


def affichage(MT=MT(), step='Undefined'):
    maximum = len(max(MT.etat_bandes, key=len))
    print(f'\n\nStep : {step}', sep = '')
    print(f'State : {MT.etat_courant}', sep = '')
    for i in range(len(MT.etat_bandes)):
        bande = MT.etat_bandes[i]
        longueur = len(bande)
        tete = MT.position_tetes[i]
        print("--" * maximum)
        print(" ".join(bande) + " _" * (maximum - longueur), sep="")
        print(" " * (2 * tete) + '▲')
