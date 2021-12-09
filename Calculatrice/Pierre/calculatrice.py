# Importation de la bibliothèque Tkinter
from tkinter import *

# Définition de la variable fenêtre
fenetre = Tk()

# Définition du titre de la fenêtre
fenetre.title("Cas Tkinter")

# Configuration de la taille de la fenêtre
fenetre.configure(bg="#353535")

phrase = StringVar()

# Création éléments
input1 = Entry(fenetre, width=25, textvariable=phrase)


def show_text():
    text1 = Label(fenetre, text=phrase.get())
    text1.grid(row=1, padx=10, pady=10)


bouton1 = Button(fenetre, text="click", command=show_text)

# Placement éléments
input1.grid(padx=10, pady=10)
bouton1.grid(row=0, column=1, padx=10, pady=10)

# Lancement de la fenêtre
fenetre.mainloop()
