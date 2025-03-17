# Consignes:

- Vous avez droit à TOUT pour faire ce travail (je vous encourage à fouiller, à utiliser l'intelligence artificielle également)
- Le but est de remettre un code fonctionnel et DE LE COMPRENDRE.
- Vous êtes libres de changer plusieurs éléments, de prendre l'approche que vous voulez avec l'esthétisme que vous voulez. 
- Il est pratiquement impossible de voir 2 codes identiques. Attention au plagiat, celui-ci entraînera la note de 0. Le plagiat est la copie intégrale du travail de quelqu'un d'autre.

Ce travail vaut 10% de la session. Il est important de regarder la grille de correction pour ne rien oublier.

Le projet est de faire une petite application qui résout des équations. 



Éléments essentiels:
- L'application prend le texte d'équation et en fait la résolution. Le texte mal rentré NE FAIT PAS planter l'application, mais donne un avertissement et efface les entrées.
- 2 options pour une équation ou la rencontre entre 2 équations. 
    - Le bouton de type radiobutton doit être sélectionné pour indiquer on se trouve dans quelle situation
    - Le bouton de type radiobutton doit se cocher tout seul si on sélectionne un espace pour entrer l'équation (voir exemple plus loin)
- On peut spécifier une valeur initiale pour la recherche de solution avec la méthode de Newton-Raphson et lui mettre une valeur par défaut.
- La résolution doit fonctionner pour tous les éléments mathématiques de cette liste: +,-,*,/,sin, cos, tan,cot, sec, csc, asin, acos, atan, acot, asec, acsc, exp, log, sqrt, valeur de pi. Les autres manipulations ne seront pas testées.
-Il doit y avoir un bouton pour regarder le graphique de l'équation seule ou le graphique des 2 équations ensemble, selon le radiobutton coché. 
- Il doit y avoir l'option d'effacer tous les champs, ce qui remet une valeur initiale par défaut.
- Porter attention à la disposition et la facilité d'utilisation de l'application.

Voici une vidéo de 4 min avec plusieurs exemples. Ceux-ci sont listés en-dessous. Ce sont de très bons exemples pour détecter des failles et des cas précis à ne pas oublier. J'utiliserai cette liste pour la correction
[📥 Télécharger la vidéo (4 min, MKV)](../img/tp2.mp4)

```py
"""
1 équation:
- 3  aucune solution
- 3*x + 6   réponse -2
- 3*x**2-5*x-20  2 réponses
- 3*x^2-5*x-9  fonctionne aussi avec ^
- sin(x) - 4*pi    Aucune solution
- 2*sin(x) - pi/2    réponse: 0.9033 (et autres)

- exp(x+9)-8  réponse 6,9206
- 3/x +9  réponse de -0.3333
- atan(x)-1 réponse 1.5574
- sqrt(x+9) - 1  réponse: -8

2 équations
- cos(x) et x  réponse 0.7391
- cos(x) et exp(x)  réponses multiples 
"""
```

