# Jeu du pendu

from turtle import *
import os, random

screen=Screen()
screen.title("Jeu du pendu par Déborah")

potence = Turtle()
potence.hideturtle()
word = Turtle()
word.hideturtle()
end = Turtle()
end.hideturtle()
end.pencolor("white")

potence.speed(0)
def creation_potence() :
    colormode(255)
    bgcolor(12,57,106)
    potence.pencolor("white")
    potence.pensize(3)
    potence.up()
    potence.goto(-150,-100)
    potence.down()
    potence.fd(25*8)
    potence.bk(25*4)
    potence.left(90)
    potence.fd(25*14)
    potence.bk(25*2)
    potence.right(45)
    potence.fd(25*2.8)
    potence.bk(25*2.8)
    potence.left(45)
    potence.fd(25*2)
    potence.right(90)
    potence.fd(25*8)
    potence.right(90)
    potence.fd(25)
    potence.bk(25)
    potence.left(90)
    potence.bk(25*2)
    potence.right(90)
    potence.fd(25*2)

def etapes_potence(erreur) :
    if erreur == 1 : # TETE
        potence.circle(25)
        potence.left(90)
        potence.up()
        potence.fd(48)
        potence.down()
        potence.dot()
        potence.up()
        potence.bk(5)
        potence.down()
        potence.dot()
        potence.up()
        potence.bk(43)
        potence.down()
        potence.right(90)
        potence.fd(25)
        potence.left(5)
    elif erreur == 2 : # TORSE
        potence.fd(25*5)
        potence.bk(25*3)
        potence.left(110)
    elif erreur == 3 : # BRAS 1
        potence.fd(25*2)
        potence.right(90)
        potence.circle(5)
        potence.left(90)
        potence.bk(25*2)
        potence.right(10)
    elif erreur == 4 : # BRAS 2
        potence.fd(25*2)
        potence.right(90)
        potence.circle(5)
        potence.left(90)
        potence.bk(25*2)
        potence.right(100)
    elif erreur == 5 : # JAMBE 1
        potence.fd(25*3)
        potence.left(50)
        potence.fd(25*3)
        potence.right(90)
        potence.circle(5)
        potence.left(90)
        potence.bk(25*3)
        potence.right(40)
    elif erreur == 6 : # JAMBE 2
        potence.fd(25*3)
        potence.right(90)
        potence.circle(5)
        potence.left(90)

def tirageMot() : # Défini l'emplacement du fichier liste de mot .txt
    dossierCourant = os.path.dirname(__file__)
    fichier = os.path.join(dossierCourant, "liste de mots.txt")

    liste = open(fichier, "r") # Ouverture du fichier en mode lecture
    mots = [] # Liste vide pour stocker tous les mots du fichier

    for mot in liste : # Rempli la liste vide en bouclant sur la liste de mots et rajoute mot par mot dans ma liste tout en supprimant les espaces avant et après grâce à la fonction strip()
        mots.append(mot.strip())
    
    liste.close() # Fermeture du fichier en mode lecture

    mot_mystere = random.choice(mots) # Stock un mot tiré au sort de la liste "mots"

    return mot_mystere



def motVide(mot) :
    listeMots = []
    for caract in mot : # Boucle qui stock autant d'underscore qu'il y a de caractère dans le mot mystère
        listeMots.append("_")
    return listeMots

def affichageMot(liste) :
    word.clear()
    word.up()
    word.pencolor("white")
    word.goto(-400,-225)
    word.write(" ".join(liste), font=("Arial", 30, "bold"))

def test_lettre(lettre, mot) :
    global chance, lettresTrouvees
    if chance <= 5 and lettresTrouvees != len(mot) :
        test = False
        for i in range(len(mot)) :
            if mot[i] == lettre :
                motJoueur[i] = lettre
                test = True
                lettresTrouvees += 1

        if test == False :
            chance+=1
            etapes_potence(chance)
        else :
            affichageMot(motJoueur)
        
        if chance == 6 :
            gameOver(mot)
        elif lettresTrouvees == len(mot) :
            victory(mot)
    

def attribution_touches(mot) : # SELECTION LETTRE + ALT + CTRL + FLECHE DU BAS
    screen.onkeypress(lambda: test_lettre("a", mot), "a")
    screen.onkeypress(lambda: test_lettre("b", mot), "b")
    screen.onkeypress(lambda: test_lettre("c", mot), "c")
    screen.onkeypress(lambda: test_lettre("d", mot), "d")
    screen.onkeypress(lambda: test_lettre("e", mot), "e")
    screen.onkeypress(lambda: test_lettre("f", mot), "f")
    screen.onkeypress(lambda: test_lettre("g", mot), "g")
    screen.onkeypress(lambda: test_lettre("h", mot), "h")
    screen.onkeypress(lambda: test_lettre("i", mot), "i")
    screen.onkeypress(lambda: test_lettre("j", mot), "j")
    screen.onkeypress(lambda: test_lettre("k", mot), "k")
    screen.onkeypress(lambda: test_lettre("l", mot), "l")
    screen.onkeypress(lambda: test_lettre("m", mot), "m")
    screen.onkeypress(lambda: test_lettre("n", mot), "n")
    screen.onkeypress(lambda: test_lettre("o", mot), "o")
    screen.onkeypress(lambda: test_lettre("p", mot), "p")
    screen.onkeypress(lambda: test_lettre("q", mot), "q")
    screen.onkeypress(lambda: test_lettre("r", mot), "r")
    screen.onkeypress(lambda: test_lettre("s", mot), "s")
    screen.onkeypress(lambda: test_lettre("t", mot), "t")
    screen.onkeypress(lambda: test_lettre("u", mot), "u")
    screen.onkeypress(lambda: test_lettre("v", mot), "v")
    screen.onkeypress(lambda: test_lettre("w", mot), "w")
    screen.onkeypress(lambda: test_lettre("x", mot), "x")
    screen.onkeypress(lambda: test_lettre("y", mot), "y")

def gameOver(mot):
    potence.clear()
    word.clear()
    bgcolor(161,40,48)
    end.write(f"GAME OVER...\nThe word was {''.join(mot)}Please, try again !\nInsert coins...", font=("Arial", 15, "bold"))

def victory(mot):
    potence.clear()
    word.clear()
    bgcolor(13,102,35)
    end.write(f"POPOPOOOOOOOOO !\nTu as trouvé le mot '{''.join(mot)}' !\nOMGGGGGGGGGGoiurfhezurheozurhoeiuhgoeurhoeziurheouhioeuhg", font=("Arial", 15, "bold"))

# Résolution du jeu
chance = 0
lettresTrouvees = 0
creation_potence()
# etapes_potence(1)
# etapes_potence(2)
# etapes_potence(3)
# etapes_potence(4)
# etapes_potence(5)
# etapes_potence(6)
mot_mystere = tirageMot()
print(mot_mystere)
motJoueur = motVide(mot_mystere)
affichageMot(motJoueur)
listen()
attribution_touches(mot_mystere)

done()