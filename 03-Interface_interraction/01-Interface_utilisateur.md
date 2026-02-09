# Interface utilisateur

# Librairie TKinter

Tkinter est le module standard de Python pour créer des interfaces graphiques. Il permet d'ajouter des boutons, des étiquettes, des entrées texte, des cases à cocher, des menus, etc.

Au départ, il faut importer la librairie (et l'installer si nécessaire). Ensuite, on crée une fenêtre qui est un objet de la classe Tk, dans la librairie tkinter. 

```py
import tkinter as tk

fenetre = tk.Tk()  # fenetre est une instance de l'objet de la classe Tk (le conteneur)

fenetre.mainloop()  # boucle infinie qui attend les événements pour y réagir (tant que la fenêtre est ouverte)
```

On peut modifier la fenêtre:

```py
import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x300")

fenetre.mainloop() 
```

## Ajout de wigdet à l'intérieur de la fenêtre


## Le widget Label
Pour afficher du texte dans la fenêtre (objet nommé fenetre), on s'y prend de la manière suivante:


```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk. à chaque élément appelé de cette librairie

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x300")

# nommer l'objet avec un nom significatif, y mettre un tk.Label
etiquette = tk.Label(fenetre, text="Ceci est un label (étiquette)")
etiquette.pack()  

fenetre.mainloop() 
```


On utilise etiquette.pack() pour afficher le Label dans la fenêtre.



## Le widget RadioButton (cercles à cocher pour sélectionner)

D'abord, pour ajouter les boutons de type "RadioButton", on doit les définir et les mettre dans une fenêtre. Ensuite, on crée une variable, ici nommée "valeur_selectionnee" dans laquelle on met un type de variable (entier (IntVar), chaîne de caractères (StringVar), décimal (DoubleVar) ou booléen (BooleanVar))

- Dans le code ci-dessous, dans la définition des 3 RadioButton, on met la valeur que la variable prendra quand on sélectionnera le bouton associé. 
```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk.

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x300")

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

### Déclenchement immédiat 

Pour qu'il se produise un déclenchement de code lorsqu'on clique sur un bouton, on doit ajouter un paramètre "command" dans la définition du bouton. Dans ce paramètre, on passe une référence de fonction **lambda** suivi de ":" et ensuite l'appel à la fonction désirée. Si on souhaite passer la valeur de la variable valeur_selectionnee, il faut inscrire .get() à la fin.
> note: lambda sert à "faire patienter" la commande (l'appel à la fonction) jusqu'à ce qu'on clique sur le bouton pour effectuer l'appel à la fonction plutôt que de l'activer dès sa création

> note 2: .get() sert à récupérer la valeur actuelle d'un widget ou d'une variable tkInter. en effet, quand on déclare une variable en faisant valeur_selectionnee = tk.StringVar(), la variable valeur_selectionnee ne contient pas un nombre utilisable par Python, c'est un OBJET (concept de Classe et d'objet... un univers!) 


```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk.

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x300")

def mise_a_jour(valeur):
    #Mettre le code ici
    print(valeur) # Par exemple, on ne fait qu'imprimer en console.

valeur_selectionnee = tk.IntVar()
choix1 = tk.Radiobutton(fenetre, text= "Première option",variable= valeur_selectionnee,value=1, command=lambda:mise_a_jour(valeur_selectionnee.get()))
choix2 = tk.Radiobutton(fenetre, text= "Deuxième option",variable= valeur_selectionnee,value=2, command=lambda:mise_a_jour(valeur_selectionnee.get()))
choix3 = tk.Radiobutton(fenetre, text= "Troisième option",variable= valeur_selectionnee,value=3, command=lambda:mise_a_jour(valeur_selectionnee.get()))
choix1.pack() 
choix2.pack() 
choix3.pack()

fenetre.mainloop() 
```



## Le widget Button
### Déclenchement dans un clique de bouton

On peut aussi utiliser la syntaxe ci-dessous pour la section ci-haut (command=mise_a_jour + nom_de_la_variable.get() dans la fonction)

```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk.

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x300")

def mise_a_jour(valeur):
    #Mettre le code ici
    print(valeur)

valeur_selectionnee = tk.IntVar()
choix1 = tk.Radiobutton(fenetre, text = "Première option", variable = valeur_selectionnee, value = 1)
choix2 = tk.Radiobutton(fenetre, text = "Deuxième option", variable = valeur_selectionnee, value = 2)
choix3 = tk.Radiobutton(fenetre, text = "Troisième option", variable = valeur_selectionnee, value = 3)
choix1.pack() 
choix2.pack() 
choix3.pack()

un_bouton = tk.Button(fenetre, text="OK",command = lambda: mise_a_jour(valeur_selectionnee.get()))
un_bouton.pack()

fenetre.mainloop() 
```

## le widget Entry (plage d'entrée de formulaire)

Le widget Entry permet à l’utilisateur d’entrer du texte à l’aide du clavier.

On associe généralement un Entry à une variable spéciale de Tkinter comme StringVar.

```py
import tkinter as tk
#from tkinter import *     pour ne pas avoir à dire tk.

fenetre = tk.Tk()
fenetre.title("Ceci est un exemple")
fenetre.geometry("600x300")


def ecrire(texte):
    print(texte)
    
texte_saisi = tk.StringVar()
saisie = tk.Entry(fenetre, textvariable = texte_saisi)
saisie.pack()

un_bouton = tk.Button(fenetre, text="OK",command = lambda: ecrire(texte_saisi.get()))
un_bouton.pack()

fenetre.mainloop() 
```

Si on souhaite mettre une valeur par défaut, on peut préremplir le champ:

```py
texte_saisi = tk.StringVar()
texte_saisi.set("allo")
saisie = tk.Entry(fenetre, textvariable = texte_saisi)
saisie.pack()
```

On peut aussi effacer le contenu de l'Entry. Imaginons le cas où on veut effacer le contenu de la case si l'entrée est différente de "allo". La fonction peut s'en charger et utiliser la méthode delete sur l'objet saisie (variable de type tk.entry). Dans delete, on doit dire de quel caractère à quel caractère on veut effacer. 
```py
def ecrire(texte):
    if texte != "allo":
        saisie.delete(0,len(texte)) # efface tout de la lettre à la position 0 à la lettre de la position de la longueur du mot
    else :
        print("bravo, le mot entré est le bon")
```

## Réaction d'un label

Si on veut faire apparaître ou modifier le contenu d'un label dans la fenêtre, on peut jouer dans les configurations du label:

```py
import tkinter as tk


def changer_label(label):
    label.config(text="Texte changé !", fg="red", bg="yellow")
    
def effacer_label(label):
    label.config(text="", bg=fenetre.cget("bg"))

fenetre = tk.Tk()
fenetre.geometry("300x150")
fenetre.title("Exemple Label dynamique")


mon_label = tk.Label(fenetre, text="Texte initial", font=("Arial", 16), fg="black")
mon_label.pack(pady=20)


bouton = tk.Button(fenetre, text="Changer le Label", command=lambda:changer_label(mon_label))
bouton.pack()
bouton2 = tk.Button(fenetre, text="Effacer le label", command=lambda:effacer_label(mon_label))
bouton2.pack()

fenetre.mainloop()
```