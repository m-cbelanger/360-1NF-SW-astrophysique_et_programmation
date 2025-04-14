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
    print("Bienvenue dans notre programme de calculs!")

def message_erreur(message):
    print(f"Erreur : {message}")
```

### Fichier principal: main

Le fichier **main.py** est le fichier principal où l'on va orchestrer l'exécution du programme. Dans ce fichier, on importe les fonctions nécessaires des autres modules et on les utilise.

```py
# Importation des fonctions des modules
from math_operations import addition, racine
from utils import message_bienvenue, message_erreur

def main():
    # Affichage d'un message de bienvenue
    message_bienvenue()

    # Exemple d'addition
    print("Calcul d'une somme")
    try: # Pour palier aux entrées non-numériques
        a = float(input("Entrer un premier nombre: "))
        b = float(input("Entrer un deuxième nombre: "))
        result = addition(a, b)
        print(f"La somme de {a} et {b} est {result}")
    except ValueError as e:
        message_erreur(str(e))
              


    print("Calcul d'une racine carrée")
    try:
        nombre = float(input("Entrer un nombre: "))
        root = racine(nombre)
        print(f"La racine carrée de {nombre} est {root}")

    except ValueError as e:
        message_erreur(str(e))


if __name__ == "__main__":
    main()
```

### Explications:

- Modules : Les fichiers operations_math.py et utils.py sont des modules. Ils contiennent des fonctions que nous allons réutiliser dans notre fichier principal.

- Importation de fonctions : Dans le fichier main.py, nous importons spécifiquement les fonctions dont nous avons besoin (addition, racine, message_bienvenue, message_erreur).

- main() : La fonction main() est le point d'entrée du programme. Elle est exécutée lorsque le fichier main.py est exécuté. C'est dans cette fonction que tout débute.

- Protection avec if __name__ == "__main__" : Cette ligne permet de s'assurer que la fonction main() ne sera exécutée que lorsque le fichier main.py est exécuté directement (et non lorsqu'il est importé dans un autre fichier). C'est la ligne à mettre à la fin du fichier pour lui donner le point de départ.


### Pour que ça fonctionne:

- mettre les 3 fichiers dans le même dossier 
- ne faire play que sur le fichier main.py

### Exercice:

Faire un module nommé calculs. Dans ce module, on fera une fonction nommée *hypotenuse* qui prend 2 paramètres a et b et qui DOIT utiliser les fonctions addition et racine du module math_operations.


Ajoutez la questions "Entrez la première cathète d'un triangle rectangle" et "Entrez la deuxième cathète d'un triangle rectangle" dans le module main() pour ensuite afficher le calcul de l'hypoténuse.