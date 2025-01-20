# Exercices sur les variables

### Question 1
1. Calculez le volume d'une sphère de 3 m de rayon en définissant au préalable une variable pour le *rayon*. Le volume d'une sphère est définit par l'équation ci-dessous. Ne pas oublier de prendre la constante dans une librairie pour pi (numpy, scipy constants, etc.) dans le calcul. Afficher la réponse avec l'écriture f-string dans le print.

$$
V=4\pi r^3/3 
$$

2. Modifier le code pour que l'utilisateur puisse fournir la valeur du rayon de la sphère dont il souhaite le volume.
    
### Question 2

Écrire le code qui convertit l'énergie cinétique d'un objet en Joules. La formule pour cela est:

$$
E_c = 0.5\cdot m \cdot v^2 
$$

Demander à l'utilisateur d'entrer la masse *m* et la vitesse *v*. Assurez-vous que les entrées sont converties en flottant (float). Gardez 2 décimales à la réponse.

### Question 3
Sachant que la constante gravitationnelle universelle est $G$, disponible dans les constantes scipy, que la masse de la terre est 
$M = 5.972 \times 10^{24}  kg$ et que le rayon de la terre est $ R =  6 371 km$, 

écrivez le programme qui calcule le module de l'accélération gravitationnelle à la surface de la terre. La formule pour calculer le module du champ gravitationnel à la surface de la terre est: 
$g = GM/R^2$
Définir les variables et les constantes, faire le calcul et affichez-le. Les mesures sont en mètre et en kg dans la formule.


### Question 4
Écrivez un algorithme pour convertir une température de degrés Celsius à Kelvin. La formule est:

$$
K = C + 273.15  
$$

Ne pas utiliser 273.15 directement, trouver la constante dans scipy. Demander à l'utilisateur d'entrer la température voulue en Celsius.

### Question 5

En physique, la position d'un objet $x$ en mouvement à une vitesse constante $v_x$ se calcule selon la règle suivante:

$$
x = x_0 + v_x t
$$

la position est en mètres, le temps en secondes et la vitesse en mètres par secondes. Demander la vitesse et la position initiale (en x) à un utilisateur. Donner la position finale de l'utilisateur en notation scientifique à 3 décimales, sachant que le déplacement a lieu depuis 4.5 minutes. Donner le temps écoulé en secondes avec 1 décimale si la position finale est à 2 fois la position en mètres du point de départ.

### Question 6
Voici une séquence d'expression dans un programme. Que seront les valeurs de x, y et z au moment de les imprimer? Faire la **trace** de la valeur des variables à chaque ligne.

```py
x = 3 + 4**2
y = -4
z = y - x
x = y * z - 3
y = 3
x + y + z
print(x)
print(y)
print(z)
```





[Retour](01-Rappels.md#Les_variables)