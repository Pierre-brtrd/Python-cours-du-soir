# Importation de la bibliothèque Tkinter
from tkinter import *

# Définition de la variable fenêtre
fenetre = Tk()

# Définition du titre de la fenêtre
fenetre.title("Calculatrice")

# Configuration de la taille de la fenêtre
fenetre.configure(bg="#353535")

# Définition des variables
val1 = IntVar()
val2 = IntVar()
resultat = IntVar()


def addition():
    valeur1 = val1.get()
    valeur2 = val2.get()
    resultat.set(valeur1 + valeur2)


def soustraction():
    valeur1 = val1.get()
    valeur2 = val2.get()
    resultat.set(valeur1 - valeur2)


def multiply():
    valeur1 = val1.get()
    valeur2 = val2.get()
    resultat.set(valeur1 * valeur2)


def division():
    valeur1 = val1.get()
    valeur2 = val2.get()
    resultat.set(valeur1 / valeur2)


# Création éléments
text1 = Label(fenetre, text="Première valeur", width=15)
text2 = Label(fenetre, text="Deuxième valeur", width=15)
text3 = Label(fenetre, text="Résultat", width=15)

input1 = Entry(fenetre, textvariable=val1, width=25)
input2 = Entry(fenetre, textvariable=val2, width=25)
text_resultat = Label(fenetre, textvariable=resultat, width=25)

boutonPlus = Button(fenetre, text="+", width=5, command=addition)
boutonMoins = Button(fenetre, text="-", width=5, command=soustraction)
boutonFois = Button(fenetre, text="*", width=5, command=multiply)
boutonDiv = Button(fenetre, text="/", width=5, command=division)

boutonQuit = Button(fenetre, text="Quitter", width=10, command=fenetre.destroy)

# Placement éléments
text1.grid(row=0, column=0, padx=10, pady=10)
text2.grid(row=1, column=0, padx=10, pady=10)
text3.grid(row=2, column=0, padx=10, pady=10)

input1.grid(row=0, column=1, padx=10, pady=10)
input2.grid(row=1, column=1, padx=10, pady=10)
text_resultat.grid(row=2, column=1, padx=10, pady=10)

boutonPlus.grid(row=0, column=2, padx=10, pady=10)
boutonMoins.grid(row=1, column=2, padx=10, pady=10)
boutonFois.grid(row=2, column=2, padx=10, pady=10)
boutonDiv.grid(row=3, column=2, padx=10, pady=10)

boutonQuit.grid(row=4, columnspan=3, padx=10, pady=10)

# Lancement de la fenêtre
fenetre.mainloop()
