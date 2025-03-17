# Transformer une chaîne de caractères en équation

sympify est une fonction de la bibliothèque SymPy en Python qui convertit une expression sous forme de chaîne de caractères en une expression mathématique symbolique. sympify peut lever une erreur di l'entrée contient du code invalide!

```py
from sympy import sympify

expr = sympify("2*x + 3")
print(expr)  # Affiche : 2*x + 3
```

Voici un exemple simple où l'utilisateur entre une équation dans un champ de texte (Entry), et lorsqu'il appuie sur un bouton, l'équation est convertie avec sympify et affichée :
```py
import tkinter as tk
from sympy import sympify, symbols

def evaluer_equation():
    """Convertit le texte entré en une expression SymPy et l'affiche."""
    try:
        equation = entree.get()
        x = symbols('x')  # Définition de 'x' pour éviter les erreurs
        expr = sympify(equation)  # Conversion en expression SymPy
        resultat_label.config(text=f"Expression : {expr}") # Pour modifier l'étiquette "resultat_label"
    except Exception as e:
        resultat_label.config(text="Erreur : Entrée invalide")

# Création de la fenêtre principale
root = tk.Tk()
root.title("SymPy avec Tkinter")

# Définir une taille fixe pour empêcher le redimensionnement
root.geometry("350x150")
root.resizable(False, False)

# Champ de saisie
entree = tk.Entry(root, width=30)
entree.pack(pady=10)

# Bouton pour évaluer
bouton = tk.Button(root, text="Évaluer", command=evaluer_equation)
bouton.pack()

# étiquette pour afficher le résultat
resultat_label = tk.Label(root, text="Entrez une équation et appuyez sur Évaluer.", wraplength=320)
resultat_label.pack(pady=10)

# Lancement de l'application
root.mainloop()



```