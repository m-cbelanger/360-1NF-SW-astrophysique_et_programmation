# Exercices conditions

## Question 1

Dans une fonction nommée moment_journee(heure), retourner le mot "matin" si l'heure est entre 6 et 12, "après-midi" si l'heure est entre 13 et 18, "soirée" si l'heure est entre 19 et 23 et "nuit" pour le reste. Demandez l'heure à l'utilisateur avant de l'envoyer à la fonction. Assurez-vous que l'heure entrée est un entier valide.



## Question 2

Demandez à l'utilisateur de saisir les longueurs des trois côtés d'un triangle. Vérifiez si ces longueurs peuvent former un triangle valide (la somme des longueurs de deux côtés doit être toujours supérieure à la longueur du troisième côté). Affichez :

- "Forme un triangle valide" si les longueurs sont valides,
- "Ne forme pas un triangle valide" sinon.

Exemple:
```
Entrez le côté A : 3
Entrez le côté B : 4
Entrez le côté C : 5
Résultat : Forme un triangle valide
```

## Question 3

Dire si l'année fournit en paramètre à une fonction nommée bissextile(annee) est une année bissextile en retournant True ou False.

Si l'année est divisible par 4 et (pas divisible par 100 ou divisible par 400), alors l'année est bissextile.

Exemples d'années bissextiles :
- 2020 (divisible par 4)
- 1600 (divisible par 400)
- 2000 (divisible par 400)
- 2400 (divisible par 400)

Exemples d'années non bissextiles :
- 1900 (divisible par 100 mais pas par 400)
- 2100 (divisible par 100 mais pas par 400)
- 2023 (pas divisible par 4)
