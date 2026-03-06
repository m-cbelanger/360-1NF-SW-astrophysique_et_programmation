# Séparer un projet Python en modules

En Python, il est courant de diviser un projet en plusieurs fichiers (modules) afin d'organiser le code de manière logique et éviter un fichier unique trop volumineux. Chaque fichier Python est considéré comme un module, et les modules peuvent être importés dans d'autres fichiers pour réutiliser du code.

Imaginons que nous ayons un projet où nous devons effectuer des calculs mathématiques et afficher des résultats. Voici une organisation possible du projet :

```
mon_projet/
│
├── main.py           # Le fichier principal qui exécute le programme
├── math_operations.py  # Un module pour des opérations mathématiques
└── utils.py          # Un module avec des fonctions utilitaires
```

### Création des modules

Fichier  "module" **operations_math.py**

Ce module contient des fonctions qui effectuent des calculs. Par exemple, une fonction pour additionner deux nombres et une autre pour calculer la racine carrée.

```py

import math  # Importation de la bibliothèque mathématique standard

def addition(a, b):
    return a + b

def racine(a):
    if a < 0:
        raise ValueError("Impossible de calculer la racine carrée d'un nombre négatif.")
    return math.sqrt(a)
```

Fichier "module" **utils.py**

Ce module contient des fonctions utilitaires, comme une fonction pour afficher un message d'accueil ou d'erreur.

```py
def message_bienvenue():
    print("Bienvenue dans notre programme de calcul!")

def message_erreur(message):
    print(f"Erreur décelée: {message}")
```

### Fichier principal: main

Le fichier **main.py** est le fichier principal où l'on va orchestrer l'exécution du programme. Dans ce fichier, on importe les fonctions nécessaires des autres modules et on les utilise.

```py
# Importation des fonctions des modules
import operations_math as mo
import utils as u

def main():
    # Affichage d'un message de bienvenue
    u.message_bienvenue()

    # Exemple d'addition
    print("Calcul d'une somme")
    try: # Pour palier aux entrées non-numériques
        a = float(input("Entrer un premier nombre: "))
        b = float(input("Entrer un deuxième nombre: "))
        result = mo.addition(a, b)
        print(f"La somme de {a} et {b} est {result}")
    except ValueError as e:
        u.message_erreur(str(e))
              


    print("Calcul d'une racine carrée")
    try:
        nombre = float(input("Entrer un nombre: "))
        root = mo.racine(nombre)
        print(f"La racine carrée de {nombre} est {root}")

    except ValueError as e:
        u.message_erreur(str(e))


if __name__ == "__main__": 
    main() # appel la fonction main(). Le nom de cette fonction aurait pu être différent.

```

### Explications:

- Modules : Les fichiers operations_math.py et utils.py sont des modules. Ils contiennent des fonctions que nous allons réutiliser dans notre fichier principal.

- Importation de fonctions : Dans le fichier main.py, nous importons les modules avec un alias, comme lorsqu'on import numpy as np ou matplotlib as plt, par exemple.

- main() : La fonction main() est le point d'entrée du programme. Elle est exécutée lorsque le fichier main.py est exécuté. C'est dans cette fonction que tout débute.

- Protection avec if __name__ == "\__main\___" : Cette condition est invariable (peu importe le nom du fichier ou de la fonction de départ) permet de s'assurer que la fonction main() ne sera exécutée que lorsque le fichier main.py est exécuté directement (et non lorsqu'il est importé dans un autre fichier). C'est la ligne à mettre à la fin du fichier pour lui donner le point de départ.


### Pour que ça fonctionne:

- mettre les 3 fichiers dans le même dossier 
- ne faire play que sur le fichier central, ici main.py

