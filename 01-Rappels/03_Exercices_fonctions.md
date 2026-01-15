# Exercices sur les fonctions

## Question 1

Le travail $W$ d'une force constante est donnée par:

$$
W = F \cdot d \cdot cos(\theta)
$$

créer une fonction nommée *travail* qui calcule *W*
Demandez à l'utilisateur d'entrer les valeurs suivantes avant de passer ces valeurs en paramètres:

- F : la force (en N),

- d : la distance parcourue (en m),

- θ : l’angle entre la force et le déplacement. On demande à l'utilisateur l'angle en degré, mais notre fonction doit convertir l'angle en radian pour l'utiliser dans le calcul. Fouillez comment convertir un degré en radians avec numpy!



## Question 2

La vitesse finale $v_f$ d’un objet en chute libre est donnée par

$$
v_f = \sqrt{2gh}
$$

où g est la constante de gravité (utiliser la constante scipy), $h$ est la hauteur de chute et $v_f$ est la vitesse à l'arrivée au sol.

Faire la fonction qui demande à l'utilisateur de fournir les valeurs PENDANT l'exécution de la fonction et qui fournit la vitesse finale.