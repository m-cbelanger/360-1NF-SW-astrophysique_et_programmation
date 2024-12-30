# Rappels de programmation

## Variables

### Affectation de valeur
Une variable est un objet que l'on nomme et auquel il est possible d'attribuer une valeur ou une expression. La variable peut être utilisée et modifiée (en remplaçant sa valeur). Pour affecter une valeur à une variable, il est primordial d'utiliser le symbole = et de mettre le nom de la variable à gauche de l'égalité.

[nom variable] = [valeur à mettre dans la variable]

```py
# attribuer la valeur de 7 dans la variable nommée x
x = 7
```

L'interprétation d'un programme se fait de haut en bas. Dans l'exemple ci-dessous, que vaudra la variable *vitesse* après la lecture du programme de quelques lignes ci-dessous?

```py
vitesse = 0
temps_deplacement = 15   # remarquez la nommenclature avec la barre de soulignement
deplacement_metres = 10

vitesse = deplacement / temps
```

### Types
Les variables peuvent être de plusieurs types: entier, décimal, chaîne de caractères (str), booléen, etc.

```py
a = 56 # entier
b = 45.5 # décimal
c = "bonjour"  # chaîne (appelée string ou str)
d = False 
```

On a aussi la possibilité de définir des constantes. Celles-ci seront toujours en majuscule

```py
G = -9.81
TAXES = 0.15
```

#### Notation scientifique

Il est possible d'écrire ou de lire des nombre qui sont présentés en notation scientifique. Par exemple:

```py
rayon_de_la_terre = 6.37e6   # 6.37 x 10^6 = 6 370 000
```

### Affectation multiple sur une ligne

En Python, il est possible d'affecter plusieurs valeurs à plusieurs variables en même temps sur une ligne. On peut aussi écrire en *f-string*, ce qui permet d'intégrer directement des expressions ou des variables dans une chaîne en les entourant d'accolades {}.

```py
x,y,z = 2,5,6
print(f"La valeur de x est {x}")
print(f"La valeur de y est {y}")
print(f"La valeur de z est {z}")

division = y/z
print(f"La valeur de {y} divisé par {z} est {division:.2f}") 
```

L'expression .2f, précisément pour la variable division, indique d'arrondir la variable *division* à 2 décimales.

[Exercice variables](exercice_variables.md)


## Organisation_des_données

### Les listes

Pour créer une liste, il faut déclarer un nom, suivi du symbole d'égalité puis des valeurs à mettre dans la liste, entre crochets [].

```py
nombres = [3,6,1]
print(nombres)
```

Pour accéder à un élément de la liste, il faut appeler son indice. RAPPEL: le premier élément d'une liste a un indice de 0.

```py
print(nombres[0])
print(nombres[1])
print(nombres[2])

# On peut aussi y aller à l'envers:
print(nombres[-1]) # dernier
print(nombres[-2]) # avant-dernier
print(nombres[-3]) # avant-avant-dernier

print(len(nombres)) # pour imprimer la quantité de valeurs dans la liste
```

### Numpy et les listes

Pour pouvoir remplir une liste avec plusieurs valeurs qui suivent une régularité, on utilise la librairie Numpy, à écrire avant d'en avoir besoin. 

```py
import numpy as np  #numpy est la librairie, np est l'alias de la librairie (raccourci)
```

On peut ainsi remplir une liste avec, par exemple, des valeurs de 1 à 100 comme ceci:

```py
valeurs_x = np.linspace(1,100,100) 
print(valeurs_x) #pour voir le résultat
```

Voici tous les détails de la fonction linspace:
```py
np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

```
Paramètres :
- start : Début de l'intervalle.
- stop : Fin de l'intervalle.
- num (par défaut = 50) : Nombre de points à générer.
- endpoint (par défaut = True) : Inclut la valeur de fin dans la séquence.
- retstep (par défaut = False) : Si True, retourne également l'espacement entre les valeurs.
- dtype : Type de données des résultats (optionnel).

**RAPPEL**: On doit placer les paramètres en ordre dans les parenthèses d'appel, sinon on doit nommer le paramètre et donner sa valeur avec le symbole =.


## Les boucles


## Les conditions


## Les graphiques


## Les fichiers externes