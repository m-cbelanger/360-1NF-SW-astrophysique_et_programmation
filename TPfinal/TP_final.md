# Projet final (15%)

Le projet est de faire une petite application qui résout des équations et fait des graphiques.

Le code de l'interface est imposé, le modifier le moins possible. CERTAINS ÉLÉMENTS ONT ÉTÉ OMIS pour me permettre d'évaluer votre compréhension du transport des données et de la structuration du code. La fonction effacer_tout est disponible aussi et doit restée telle qu'elle est.





Éléments essentiels:
- L'application prend le texte d'équation et en fait la résolution. Le texte mal rentré NE FAIT PAS planter l'application, mais donne un avertissement et efface les entrées.
- 2 options pour une équation ou la rencontre entre 2 équations. 
    - Le bouton de type radiobutton doit être sélectionné pour indiquer on se trouve dans quelle situation
    - Le bouton de type radiobutton doit se cocher tout seul si on sélectionne un espace pour entrer l'équation (voir exemple plus loin)
- On peut spécifier une valeur initiale pour la recherche de solution avec la méthode de Newton-Raphson et lui mettre une valeur par défaut. La méthode de Newton DOIT apparaître quelque part dans la résolution.
- La résolution doit fonctionner pour tous les éléments mathématiques de cette liste: +,-,*,/,sin, cos, tan, exp, valeur de pi. Les autres manipulations ne seront pas testées.
-Il doit y avoir un bouton pour regarder le graphique de l'équation seule ou le graphique des 2 équations ensemble, selon le radiobutton coché. 
- Il doit y avoir l'option d'effacer tous les champs, ce qui remet une valeur initiale par défaut.
- Porter attention à la disposition et la facilité d'utilisation de l'application.
- Chaque fonction doit fonctionner indépendamment du module dans lequel elle se trouve (donc paramètres obligatoires, pas de variables globales)

Voici le fonctionnement attendu:

![](img/TPfinal.gif)


Les fonctions suivantes seront testées:

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

2 équations
- cos(x) et x  réponse 0.7391
- cos(x) et exp(x)  réponses multiples 
"""
```


