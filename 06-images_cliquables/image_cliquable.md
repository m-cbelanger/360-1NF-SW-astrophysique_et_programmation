# Interface avec image cliquable

Pour parvenir à suivre les étapes ci-dessous, il faudra 2 images jpeg fournies dans le dossier img ci-présent.

```py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def choisir(valeur, cadre, cadres, choix):
    # Puisque le choix envoyé est une variable de tkinter, elle est un objet mutable
    # On peut donc changer sa valeur (.set()) de l'endroit où on l'appelle.
    choix.set(valeur)
    # un print pour voir la réaction quand on clique
    print("Choix sélectionné :", valeur)
    
    # Éteindre les highlights
    for element in cadres:
        element.config(highlightthickness=0)
    # allumer celui qui a été cliqué
    cadre.config(highlightbackground="light blue", highlightthickness=2)


def afficher_selection(choix):
    if choix != "":
        messagebox.showinfo("Sélection", f"Vous avez choisi : {choix}")
    else:
        messagebox.showwarning("Attention", "Aucun choix n'a été fait.")


def creer_fenetre():
    fenetre = tk.Tk()
    fenetre.title("Choix avec images")
    fenetre.geometry("455x300")

    choix = tk.StringVar(value="")
    
    # Les photos doivent être dans le même dossier que le fichier .py ici présent
    img1 = ImageTk.PhotoImage(Image.open("chat.jpg").resize((200, 200)))
    img2 = ImageTk.PhotoImage(Image.open("chien.jpg").resize((200, 200)))
    
    # On crée 2 Frame dans la fenetre principale, c'est un type d'objet comme les widgets
    cadre1 = tk.Frame(fenetre, highlightthickness=0)
    cadre1.grid(row=0, column=0, padx=10, pady=10)
    cadre2 = tk.Frame(fenetre, highlightthickness=0)
    cadre2.grid(row=0, column=1, padx=10, pady=10)
    
    # on les met dans la même collection (liste) pour les parcourir dans la fonction choisir
    cadres = []
    cadres.append(cadre1)
    cadres.append(cadre2)

    # On peut disposer les paramètres sur plusieurs lignes, pour plus de lisibilité
    btn1 = tk.Button(
        cadre1, # ce bouton est dans le Frame cadre1 et non dans la fenetre
        image=img1,
        command=lambda: choisir("chat", cadre1, cadres, choix)
    )
    # Puisqu'on est dans l'evironnement restreint de cadre1, on peut mettre pack au lieu de grid, c'est le seul élément
    btn1.pack()

    btn2 = tk.Button(
        cadre2, # ce bouton est dans le Frame cadre2 et non dans la fenetre
        image=img2,
        command=lambda: choisir("chien", cadre2, cadres, choix)
    )
    btn2.pack()

    btn_valider = tk.Button(
        fenetre, # ce bouton est dans la fenêtre directement
        text="Valider",
        width=40,
        command=lambda: afficher_selection(choix.get())
    )
    btn_valider.grid(row=1, column=0, columnspan=2, pady=10)

    fenetre.mainloop()

if __name__== "__main__":
    creer_fenetre()

```