# interface utilisateur

# Librairie TKinter

Tkinter est le module standard de Python pour créer des interfaces graphiques. Il permet d'ajouter des boutons, des étiquettes, des entrées texte, des cases à cocher, des menus, etc.

Au départ, il faut importer la librairie (et l'installer si nécessaire). Ensuite, on crée une fenêtre qui est un objet de la classe Tk, dans la librairie tkinter. 

```py
import tkinter as tk

root = tk.Tk()  # root est une instance de l'objet de la classe Tk (le conteneur)

root.mainloop()  # boucle infinie qui attend les événements pour y réagir (tant que la fenêtre est ouverte)
```

On peut modifier la fenêtre:

```py
import tkinter as tk

root = tk.Tk()
root.title("Ceci est un exemple")
root.geometry("600x700")

root.mainloop() 
```

## Ajout de wigdet à l'intérieur de la fenêtre


## Label
Pour afficher du texte dans la fenêtre (objet nommé fenetre), on s'y prend de la manière suivante:


```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk. à chaque élément appelé de cette librairie

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x700")

# nommer l'objet avec un nom significatif, y mettre un tk.Label
etiquette = tk.Label(fenetre, text="Ceci est un label (étiquette)")
etiquette.pack()  

fenetre.mainloop() 
```

- Dans tk.Label, on spécifie la fenêtre et le texte. On peut aussi personnaliser le tout:

On utilise etiquette.pack() pour afficher le Label dans la fenêtre.



## RadioButton (cercles à cocher pour sélectionner)

D'abord, pour ajouter les boutons de type "RadioButton", on doit les définir et les mettre dans une fenêtre. Ensuite, on crée une variable, ici nommée "valeur_selectionnee" dans laquelle on met un type de variable (entier (IntVar), chaîne de caractères (StringVar), décimal (DoubleVar) ou booléen (BooleanVar))

- Dans le code ci-dessous, dans la définition des 3 RadioButton, on met la valeur que la variable prendra quand on sélectionnera le bouton associé. 
```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk.

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x700")

valeur_selectionnee = tk.IntVar()
choix1 = tk.Radiobutton(fenetre, text = "Première option", variable = valeur_selectionnee, value = 1, font = ("Arial",20))
choix2 = tk.Radiobutton(fenetre, text = "Deuxième option", variable = valeur_selectionnee, value = 2, font = ("Arial",20))
choix3 = tk.Radiobutton(fenetre, text = "Troisième option", variable = valeur_selectionnee, value = 3, font = ("Arial",20))
choix1.pack(anchor="w", pady=20, padx = 20) # Le pady et padx, c'est pour ajouter de l'espace en y ou en x
choix2.pack(anchor="w") #les lettres de points cardinaux
choix3.pack(anchor="w")


fenetre.mainloop() 
```

## Générer une action
Pour que la valeur de la variable soit utilisée et s'intègre dans un code quand vous cliquez sur le choix, il faut l'action (paramètre) command.

On peut faire déclencher du code à la sélection même d'un choix, sinon, on peut le faire quand on clique sur un bouton, par exemple.

### déclenchement immédiat 

Pour qu'il se produise un déclenchement de code lorsqu'on clique sur un bouton, on doit ajouter un paramètre "command" dans la définition du bouton. Dans ce paramètre, on passe une référence de fonction **lambda** suivi de ":" et ensuite l'appel à la fonction désirée. Si on souhaite passer la valeur de la variable valeur_selectionnee, il faut inscrire .get() à la fin.

```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk.

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x700")

def mise_a_jour(valeur):
    #Mettre le code ici
    print(valeur) # Par exemple, on ne fait qu'imprimer.

valeur_selectionnee = tk.IntVar()
choix1 = tk.Radiobutton(fenetre, text= "Première option",variable= valeur_selectionnee,value=1, command=lambda:mise_a_jour(valeur_selectionnee.get()))
choix2 = tk.Radiobutton(fenetre, text= "Deuxième option",variable= valeur_selectionnee,value=2, command=lambda:mise_a_jour(valeur_selectionnee.get()))
choix3 = tk.Radiobutton(fenetre, text= "Troisième option",variable= valeur_selectionnee,value=3, command=lambda:mise_a_jour(valeur_selectionnee.get()))
choix1.pack() 
choix2.pack() 
choix3.pack()

fenetre.mainloop() 
```



### déclenchement dans un clique de bouton

On peut aussi utiliser la syntaxe ci-dessous pour la section ci-haut (command=mise_a_jour + nom_de_la_variable.get() dans la fonction)

```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk.

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x700")

def mise_a_jour():
    #Mettre le code ici
    print(valeur_selectionnee.get())

valeur_selectionnee = tk.IntVar()
choix1 = tk.Radiobutton(fenetre, text = "Première option", variable = valeur_selectionnee, value = 1)
choix2 = tk.Radiobutton(fenetre, text = "Deuxième option", variable = valeur_selectionnee, value = 2)
choix3 = tk.Radiobutton(fenetre, text = "Troisième option", variable = valeur_selectionnee, value = 3)
choix1.pack() 
choix2.pack() 
choix3.pack()

bouton1 = tk.Button(fenetre, text="OK",command = mise_a_jour)
bouton1.pack()

fenetre.mainloop() 
```