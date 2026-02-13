# Gestion des erreurs

En Python, le bloc try...except est utilisé pour gérer les erreurs et éviter que le programme ne s'arrête brutalement lorsqu'une exception se produit.

### Syntaxe de base:

```py
try:
    # Code susceptible de générer une erreur
    x = int(input("Entrez un nombre : "))  
    resultat = 10 / x  
    print("Résultat :", resultat)
except ZeroDivisionError:
    print("Erreur : Division par zéro interdite.")
except ValueError:
    print("Erreur : Vous devez entrer un nombre entier.")
except Exception as e:
    print("Une erreur s'est produite :", e)

```

### Explications

- Le bloc try : contient le code qui pourrait provoquer une erreur.
- Le bloc except : capture l'erreur et exécute un code alternatif.
- Spécifier un type d'exception (ZeroDivisionError, ValueError, etc.) : permet de gérer différentes erreurs de manière ciblée.
- Utiliser Exception as e : capture n'importe quelle erreur et affiche son message.


## Else et finally

```py
try:
    nombre = int(input("Entrez un nombre : "))
    print("Le double est :", nombre * 2)
except ValueError:
    print("Erreur : Vous devez entrer un entier.")
else:
    print("Aucune erreur, tout s'est bien passé !")
finally:
    print("Fin du programme.")
```

# Fenêtre de type pop-up

Pour avertir l'utilisateur, il est intéressant de délaisser la console et de mettre les messages dans des messagebox. Pour se faire, on importe un module de la librairie tkinter:

```py
from tkinter import messagebox
```

## Principaux types de boîte de dialogue

### Boîtes d'affichage simple

- message d'information. C'est le titre d'abord, le message ensuite
```py
messagebox.showinfo("Information", "Opération réussie !")
```

- message d'avertissement.
```py
messagebox.showwarning("Avertissement", "Attention à cette action !")
```

- message d'erreur.
```py
messagebox.showerror("Erreur", "Une erreur est survenue.")
```

### Boîtes de confirmation

- oui/non
```py
reponse = messagebox.askyesno("Confirmation", "Voulez-vous continuer ?")
if reponse:
    print("L'utilisateur a cliqué sur Oui")
else:
    print("L'utilisateur a cliqué sur Non")
```

- oui/non/annuler

```py
reponse = messagebox.askyesnocancel("Choix", "Souhaitez-vous enregistrer avant de quitter ?")
if reponse is True:
    print("Oui, enregistrer")
elif reponse is False:
    print("Non, ne pas enregistrer")
else:
    print("Annuler")

```

## Exemple complet

```py
import tkinter as tk
from tkinter import messagebox

def afficher_info():
    messagebox.showinfo("Bienvenue", "Bienvenue dans notre application Tkinter !")
    
def afficher_validation(nombre):
    try:
        valeur = int(nombre)
    except ValueError:
        messagebox.showerror("Erreur", "Attention, il fallait entrer un nombre entier")
    else:
        messagebox.showinfo("Bravo", f"Bravo! vous avez entré le nombre {valeur}!")
        


fenetre = tk.Tk()
fenetre.title("Exemple Tkinter")



boutonInfo = tk.Button(fenetre, text="Afficher une info",width = 50, command=lambda:afficher_info())

etiquette = tk.Label(fenetre,text="entrez un nombre: ")

nombre_saisi = tk.StringVar()
entree = tk.Entry(fenetre,textvariable=nombre_saisi)

boutonValider = tk.Button(fenetre, text="Valider le nombre",width = 50, command=lambda:afficher_validation(nombre_saisi.get()))

etiquette.grid(row=0, column=0, padx=20, pady=10, sticky="w")
entree.grid(row=0, column=1, padx=20, pady=10, sticky="e")
boutonValider.grid(row=1, padx=20,pady=10, columnspan=2)
boutonInfo.grid(row=2, padx=20,pady=10, columnspan=2)

fenetre.mainloop()

```

> Note: il est tout à fait possible de mettre un autre try dans un except.