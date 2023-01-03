import MT
import linker
import sys

def test_question_2(mot, fichier):
    mt2 = MT(mot, fichier + ".txt")
    mt2.step()

def test_question_3(mot, fichier):
    mt2 = MT(mot, fichier)
    mt2.calcul()


def test_question_5(mot, fichier):
    mt5 = MT(mot, fichier + ".txt")
    mt5.calcul()

def test_question_7(mot):
    linker("pre_egyptienne", "addition.txt", "post_egyptienne.txt")
    mt7 = MT(mot, "post_egyptienne.txt")
    mt7.calcul()

def test_question_8(mot):
    linker("pre_trie.txt", "left.txt", "post_trie.txt")
    mt8 = MT(mot, "post_trie.txt")
    mt8.calcul()





if __name__ == "__main__":
    if sys.argv[0] == "testQ2":
        test_question_2(sys.argv[1], sys.argv[2])
    elif sys.argv[0] == "testQ3":
        test_question_3(sys.argv[1], sys.argv[2])
    elif sys.argv[0] == "testQ5":
        test_question_5(sys.argv[1], sys.argv[2])
    elif sys.argv[0] == "testQ7":
        test_question_7(sys.argv[1])  
    elif sys.argv[0] == "testQ8":
        test_question_8(sys.argv[1])
    else:
        raise Exception("Erreur !")
        
        