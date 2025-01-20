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

