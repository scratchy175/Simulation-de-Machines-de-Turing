
class MT:
    def __init__(self, mot, fichier):
        self.mot = mot
        self.fichier = fichier
        self.etat_accept = ""
        self.etat_courant = ""
        self.etat_bandes = list(mot)
        self.position_tetes = []
        self.transition = {}
        self.ouvrir_fichier()

    def ouvrir_fichier(self):
        cpt = 0
        with open(self.fichier, "r") as f:
            temp = ""
            for line in f:
                line = line.strip('\n')
                if cpt == 0:
                    self.etat_courant = line
                elif cpt == 1:
                    self.etat_accept = line
                elif temp == "" and line != "":
                    self.transition[line] = ""
                    temp = line
                elif line != "":
                    self.transition[temp] = line
                    temp = ""
                cpt += 1






mt1 = MT("1110","mt1.txt")
print(mt1.transition)
