from TuringMachine import MT
from linkerMT import linker
import sys


def test_question_2(mot, fichier):
    mt2 = MT(mot, "TM/" + fichier + ".txt")
    mt2.step()

def test_question_3(mot, fichier):
    mt2 = MT(mot, "TM/" + fichier)
    mt2.calcul()

def test_question_5(mot, fichier):
    mt5 = MT(mot, "Q5/" + fichier + ".txt")
    mt5.calcul()

def test_question_7(mot):
    linker("Q7-8/pre_egyptienne", "Q7-8/addition.txt", "Q7-8/post_egyptienne.txt")
    mt7 = MT(mot, "Q7-8/post_egyptienne.txt")
    mt7.calcul()

def test_question_8(mot):
    linker("Q7-8/pre_trie.txt", "Q7-8/left.txt", "Q7-8/post_trie.txt")
    mt8 = MT(mot, "Q7-8/post_trie.txt")
    mt8.calcul()

if __name__ == "__main__":
    if sys.argv[1] == "testQ2":
        test_question_2(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "testQ3":
        test_question_3(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "testQ5":
        test_question_5(sys.argv[2], sys.argv[3].lower())
    elif sys.argv[1] == "testQ7":
        test_question_7(sys.argv[2])  
    elif sys.argv[1] == "testQ8":
        test_question_8(sys.argv[2])
    else:
        raise Exception("Erreur !")
