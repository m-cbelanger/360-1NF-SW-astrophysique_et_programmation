# Interface avec image cliquable

Pour parvenir à suivre les étapes ci-dessous, il faudra 2 images jpeg fournies dans le dossier img ci-présent.

```py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def choisir(valeur, cadre):
    choix.set(valeur)
    print("Choix sélectionné :", valeur)

    # Éteindre tous les cadres
    for c in cadres:
        c.config(highlightthickness=0)
    # Mettre en surbrillance le cadre sélectionné
    cadre.config(highlightbackground="red", highlightthickness=3)

# Créer la fenêtre principale
fen = tk.Tk()
fen.title("Choix avec images")
fen.geometry("500x300")

# Variable pour stocker le choix
choix = tk.StringVar(value="")

# Charger les images
img1 = ImageTk.PhotoImage(Image.open("chat.jpg").resize((200, 200)))
img2 = ImageTk.PhotoImage(Image.open("chien.jpg").resize((200, 200)))

# Liste pour garder la référence des cadres
cadres = []

# Créer un cadre contenant l'image du chat
cadre1 = tk.Frame(fen, highlightthickness=0)
cadre1.grid(row=0, column=0, padx=10, pady=10)
cadres.append(cadre1)

btn1 = tk.Button(cadre1, image=img1, command=lambda: choisir("chat", cadre1))
btn1.pack()

# Créer un cadre contenant l'image du chien
cadre2 = tk.Frame(fen, highlightthickness=0)
cadre2.grid(row=0, column=1, padx=10, pady=10)
cadres.append(cadre2)

btn2 = tk.Button(cadre2, image=img2, command=lambda: choisir("chien", cadre2))
btn2.pack()

# Bouton pour valider la sélection
def afficher_selection():
    if choix.get():
        messagebox.showinfo("Sélection", f"Vous avez choisi : {choix.get()}")
    else:
        messagebox.showwarning("Attention", "Aucun choix n'a été fait.")

btn_valider = tk.Button(fen, text="Valider", command=afficher_selection)
btn_valider.grid(row=1, column=0, columnspan=2, pady=10)

fen.mainloop()
```