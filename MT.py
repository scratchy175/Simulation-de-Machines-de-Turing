
class MT:
    def __init__(self, mot, fichier):
        self.mot = mot
        self.fichier = fichier
        self.etat_accept = ""
        self.etat_courant = ""
        self.etat_bandes = []
        self.position_tetes = []
        self.ouvrir_fichier()

    def ouvrir_fichier(self):
        with open(self.fichier, "r") as f:
            for line in f:
                
                
                









mt1 = MT("1110","fichier1.txt")