# Exercices boucles

## Question 1

À l'aide de la boucle for, calculez la factorielle d'un nombre que vous décidez d'avance et mettez dans une variable.

La factorielle d'un nombre est le produit de ce nombre avec tous les entiers qui le précèdent jusqu'à 1 inclusivement. Donc la factorielle de 5 est 5*4*3*2*1 = 120



## Question 2

Faire une fonction qui vérifie si un nombre positif et entier est premier ou non. Un nombre premier est un nombre qui est divisible par 1 ET lui même seulement. Si un nombre est divisible par autre chose que ces 2 diviseurs distincts, il n'est pas premier.

Exemples:
- les nombre négatifs ne sont pas premiers
- 0 n'est pas premier
- 1 n'est pas premier
- 2 est premier
- 3, 5, 7, 11, 13, 17, etc. sont premiers


## Question 3
a) Faire le code suivant: Dans une boucle while, demandez 3 nombres. À chaque nombre, afficher si le nombre est plus petit, égal ou plus grand que 100. La boucle ne doit pas demander plus de 3 nombres, un à la fois.

b) Prendre le code de la question a) et bonifiez-la: Ajouter la somme des 3 nombres dans l'affichage.

c) Prendre le code de la question b) et ajouter la moyenne des nombre au fur et à mesure qu'on en ajoute. Chercher une solution pour que la moyenne soit exacte, c'est-à-dire qu'elle affiche les décimales.

## Question 4
Voici plusieurs boucles. Testez-les et expliquer ce qui se passe en utilisant les termes appropriés.

```py
# Boucle 1
i = 0
while i < 5:
    print("Passage dans la boucle")

```
```py
# Boucle 2
i = 0
while i > 0:
    i = i + 1
    print(f"i vaut: {i}")

print(f"La valeur finale de i est {i}")
```

```py
# Boucle 3
i = 0
while i >= 0 or i <= 10:
    i = i + 1
    print(f"i vaut: {i}")

print(f"La valeur finale de i est {i}")
```

```py
# Boucle 4
i = 1
while i < 0 and i > 10:
    i = i + 1
    print(f"i vaut: {i}")

print(f"La valeur finale de i est {i}")
```

```py
# Boucle 5
x = 10
while x > 0:
    print("Valeur de x :", x)
    x += 1
```

```py
# Boucle 6
n = 1
while n != 10:
    print("n =", n)
    n += 2 
```

[Retour](01-Rappels.md#Les_boucles)