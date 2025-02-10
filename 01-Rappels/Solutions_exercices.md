# Solutions exercices

# 02-Variables

```py
import scipy.constants as cst

# Question 1

rayon = 3
V = 4 * cst.pi *rayon**3/3

print(f"Le volume d'une sphère de rayon {rayon} est {V:.2f} m³")



# Question 2

masse = float(input("Entrez la masse de l'objet (en kg) : "))
vitesse = float(input("Entrez la vitesse de l'objet (en m/s) : "))

energie_cin = 0.5*masse * vitesse**2

print(f"L'énergie cinétique de l'objet est {energie_cin:.2f} Joules.")



# Question 3

masse_terre = 5.972e24
rayon_terre = 6371

g = cst.G *masse_terre / (rayon_terre*1000) **2

print(f"L'accélération gravitationnelle est: {g: .3f} ")



# Question 4

celsius = float(input("Entrez une température en Celsius pour obtenir l'équivalent en Kelvin: "))

kelvin = celsius + cst.zero_Celsius

print(f"La température équivalente est: {kelvin} Kelvin ")



# Question 5

v_x = float(input("Quelle est la vitesse de l'objet (m/s) ? "))
x_0 = float(input("Quelle est la position initiale (m) ? "))

t = 4.5*60

x = x_0 + v_x*t
print(f"La position après 4,5 minutes est {x} m.")

x = 2 * x_0
t = (x-x_0)/v_x

print(f"Pour parcourir {x} mètres, il faudra {t} secondes")


# Question 6

x = 3 + 4**2  # x= 19, y = .. z = ..
y = -4        # x= 19, y = -4 z = ..
z = y - x	  # x= 19, y = -4 z = -23
x = y * z - 3 # x= 89, y = -4 z = -23
y = 3         # x= 89, y = 3  z = -23
x + y + z     # x= 89, y = 3  z = -23  (aucune affectation)
print(x)
print(y)
print(z)

```

# 03- fonctions

```py
# Question 1

def travail(F,d,theta):
    theta = np.radians(theta)
    return F*d*np.cos(theta)

angle = float(input("Entrez l'angle entre le vecteur force et le vecteur distance (en degrés): "))
force = float(input("Entrez le module de la force: "))
distance = float(input("Entrez le module de la distance: "))
print(f"{travail(force,distance,angle):.2f}")

# Question 2
def chute_libre():
    hauteur = float(input("De quelle hauteur l'objet tombe-t-il? (m) "))
    vf = np.sqrt(2*cst.g*hauteur)
    return vf


print(f"La vitesse à l'atterissage sera de {chute_libre():.2f} m/s")
```

# 04-conditions

```py
from datetime import datetime
#Question 1

def moment_journee(heure):
    """Retourne le moment de la journée en fonction de l'heure donnée."""
    if 6 <= heure <= 12:
        return "le matin"
    elif 13 <= heure <= 18:
        return "l'après-midi"
    elif 19 <= heure <= 23:
        return "le soir"
    else:
        return "la nuit"

heure = -1
    
while(heure < 0 or heure > 24):
    try:
        heure = int(input("Veuillez entrer une heure svp: "))
        if (heure < 0 or heure > 24):
            print("L'heure entrée n'est pas entre 0 et 24")
    except ValueError:
        print("La valeur entrée n'est pas un nombre")

print(f"Vous avez indiqué qu'il est {heure} heures, on est donc {moment_journee(heure)}")


#Question 2
# Demander les longueurs des trois côtés du triangle

valeur_valide = False
while(not(valeur_valide)):
    try:
        a = float(input("Entrez le côté A : "))
        b = float(input("Entrez le côté B : "))
        c = float(input("Entrez le côté C : "))

        # Vérifier si les longueurs forment un triangle valide
        if a + b > c and a + c > b and b + c > a:
            print("Forme un triangle valide")
        else:
            print("Ne forme pas un triangle valide")
        valeur_valide = True
    except ValueError:
        print("Veuillez entrer des valeurs numériques valides.")
        

# Question 3

def bissextile(annee):
    # Vérifier si l'année est divisible par 4, mais pas par 100 sauf si elle est divisible par 400
    if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
        return True
    else:
        return False

#exemple d'utilisation
annee_courante = datetime.now().year
if(bissextile(annee_courante)):
    print(f"l'année courante, {annee_courante} est bissextile")
else:
    print(f"l'année courante, {annee_courante} n'est pas bissextile")
```

# 05-Listes


```py
# Corrigé exercices listes
import numpy as np
import scipy.constants as cst

#Question 1
t = np.arange(0,10,0.1)

gamma = 0.1

def distance_oscillatoire(A, t, f):
    return A * np.exp(-gamma*t)*np.cos(2*np.pi*f*t)


A = float(input("Entrez une Amplitude: "))
f = float(input("Entrez une fréquence: "))

x = distance_oscillatoire(A,t,f)

print(x)

# Question 2

#Array vs listes
# Array: tous les éléments sont de mêmes types
# Liste: les éléments peuvent être de types divers

mon_array = np.array([1,4.5,9,10])
ma_liste = [1,4.5,9,10]
ma_liste2 = ["a", 4, True, "b"] # pas possible en array

# Les traitements faits sur les array se font sur chaque éléments, contrairement a une liste:

print(2 * mon_array)
print(2 * ma_liste)
print(2 * ma_liste2)
                
# Array: meilleur pour les gros datasets
# List: conteneur plus permisif
```

# 06-Boucles

```py
# Question 1
def factorielle(n):
    valeur = 0
    if not(isinstance(n,int)):
        message = "La factorielle ne se calcule que sur un entier"
    elif n < 0:
        message = "La factorielle ne peut pas être calculée sur un nombre négatif"
    elif n == 0:
        valeur = 1
        message = "La factorielle de 0 est 1, par convention"
    else :
        valeur = 1
        for i in range(1,n+1):
            valeur = valeur * i
        message = ""
    return(valeur, message)


# Question 2

# Cet algorithme est un algorithme dit "de force brute" et n'est pas très efficace en rapidité
def est_premier(n):
    if n < 2:
        return False
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

#ce test prend quelques secondes/minutes à réaliser!
#print(est_premier(1000000007))

# une façon d'accélérer l'algorithme est de faire la boucle jusqu'à racine de n,
# puisque les autres vérifications sont inutiles
import math
def est_premier_plus_vite(n):
    if n < 2:
        return False
    else:
        for i in range(2,math.sqrt(n)+1): # +1 parce que la dernière valeur est exclue
            if n % i == 0:
                return False
        return True

#Question 3
    
def plus_petit_plus_grand():
    i = 1
    while i <= 3 :
        try:
            nombre = float(input("Entrez un nombre: "))
            if nombre < 100:
                print("le nombre est plus petit que 100")
            elif nombre > 100:
                print("le nombre est plus grand que 100")
            else:
                print("le nombre est plus égale à 100")
                
            i += 1
              
        except ValueError:
            print("Vous devez entrer un nombre!")
                    
#plus_petit_plus_grand()

# Question 4
# Boucle 1
# La boucle continuera à l'infini ou jusqu'à l'atteinte de la valeur max de la capacité de la variable.

# Boucle 2
# On n'entrera jamais dans la boucle puisque 0 n'est pas plus grand que 0. La valeur finale de i est donc 0

# Boucle 3
# Boucle infinie, puisqu'un nombre est toujours plus grand que 0 OU plus petit que 10. Pour avoir les nombres entre 0 et 10,
# il faudrait mettre un and

# Boucle 4
# Il y a un and, mais un nombre ne peut pas être plus grand que 10 ET plus petit que 0 en même temps. On n'entre donc pas
# dans la boucle

# Boucle 5
# x démarre a 10 et incrémente, donc sera toujours plus grand que 0, boucle infinie.

# Boucle 6
# le "n" vaudra tour à tour 1-3-5-7-9-11, etc. ce qui est toujours différent de 10. Boucle infinie!
```

# 06-Graphiques

```py
import numpy as np
import matplotlib.pyplot as plt

# Question 1

def sinus(x):
    return np.sin(x)

x = np.linspace(-2, 2, 100)
y1 = sinus(x)
y2 = x

# Personnaliser les lignes (couleur, pointillés, épaisseur, etc)
#a)
plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

# b)
plt.figure()
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlim(-0.5,0.5)
plt.show()

#c)
def cosinus(x):
    return np.cos(x)

def approx(x):
    return 1 - x**2/2

yb1 = cosinus(x)
yb2 = approx(x)


fig, axes = plt.subplots(4,1, figsize=(6,9))
axes[0].set_title("approx de sinus")
axes[0].set_xlim(-2,2)
axes[0].plot(x,yb1)
axes[0].plot(x,yb2)

axes[1].set_title("approx de sinus")
axes[1].set_xlim(-0.5,0.5)
axes[1].plot(x,yb1)
axes[1].plot(x,yb2)

axes[2].set_title("approx de cosinus")
axes[2].set_xlim(-2,2)
axes[2].plot(x,yb1)
axes[2].plot(x,yb2)

axes[3].set_title("approx de cosinus")
axes[3].set_xlim(-0.5,0.5)
axes[3].plot(x,yb1)
axes[3].plot(x,yb2)

plt.tight_layout()
plt.show()




# Question 2
sequence = "ACGATCATAGCGAGCTAAATCGGTACACTTGTCA"

bases = ["A", "C", "G", "T"]
distribution = []
for base in bases:
    distribution.append(sequence.count(base))

x = np.arange(len(bases))

plt.bar(x, distribution)  
plt.xticks(x, bases)  
plt.xlabel("Bases")  
plt.ylabel("Nombre")  
plt.title(f"Distribution des bases \n dans la séquence {sequence}")  

plt.show()



#Question 3


x = np.linspace(-5, 5, 50)  
y = np.linspace(-5, 5, 50)  
X, Y = np.meshgrid(x, y)   
Z = X**2 - Y**2

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='coolwarm')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Selle de cheval")

plt.show()


```