from tkinter import *
from random import *

fenetre = Tk()

fenetre.title('Jeux du dés')

fenetre.configure(bg="#353535")

resultat = StringVar()


def jeux():
    number = randint(1, 6)
    resultat.set(number)


resultat.set("On va lancer le dés")

bouton1 = Button(fenetre, text="Jouer", command=jeux)

text1 = Label(fenetre, textvariable=resultat, width=30)

bouton1.grid(row=0, column=0, padx=10, pady=10)
text1.grid(row=1, column=0, padx=10, pady=10)

fenetre.mainloop()
