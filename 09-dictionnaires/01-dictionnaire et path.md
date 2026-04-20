# Conteneur: dictionnaires

En python, il existe plusieurs types de conteneurs pour stocker les informations. Un des conteneurs dont nous auront besoin pour la présentation avec Thomas Vandal est le dictionnaire.

Un dictionnaire est une structure de données qui permet d’associer une clé à une valeur. On peut le voir comme un “mini-tableau” avec des paires :

```py
dictionnaire = {
    "clé": "valeur"
}

# exemple
notes = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}
```

- "Alice" → clé
- 85 → valeur

Pour accéder à une valeur dans le dictionnaire, on utilise la même syntaxe qu'avec les listes, mais au lieu de mettre l'index de la case dans les crochets, on met la clé:
```py
print(notes["Alice"])  # affiche 85
```

## Parcourir un dictionnaire

```py
for valeur in notes:
    print(notes[valeur])

for valeur in notes.values():
    print(valeur)
```



## Préparation à l'atelier de Thomas


*** requis

Dans ce dossier, on a l'atelier de Thomas non-complété. On fera quelques étapes ensemble. Pour démarrer, on crée un nouveau fichier Python dans un dossier nommé par exemple (atelier_naine_brune) et on suit les étapes du fichier atelier.ipynb


Pour l'atelier, on devra télécharger des fichiers de type fits et les placer dans un dossier. Pour que le code soit utilisable dans n'importe quel environnement (dossier), on fera faire la création du dossier par une ligne de commande Python.


```py
from pathlib import Path
from astroquery.mast import Observations

# Les objets "Path" sont plus pratique à manipuler que des strings
data_dir = Path("./data") #nom du dossier à créer. ./ pour indiquer de le créer dans l'emplacement d'où le code est exécuté
data_dir.mkdir(exist_ok = True) # commande qui crée le dossier

# Dictionnaire donnant le nom des fichiers pour chaque filtre (couleur).
files = {
    "f150w": "jw02473-o053_t053_nircam_clear-f150w_i2d.fits",
    "f480m": "jw02473-o053_t053_nircam_clear-f480m_i2d.fits",
}
# clé: f150w et f480m
# valeurs: noms des fichier fits
base_uri = "mast:JWST/product/"
```

Ensuite, on télécharge les 2 fichiers du dictionnaire via l’API (Application Programming Interface) nommée Observations, disponible dans la librairie astroquery.

Une API est un intermédiaire qui permet à un programme de communiquer avec un autre système sans avoir à comprendre son fonctionnement interne.

Dans ce cas-ci, on utilise l’API Observations pour accéder aux données du MAST. On lui demande d’aller chercher des fichiers dans le chemin mast:JWST/product/, auquel on ajoute le nom du fichier.

Les fichiers sont ensuite enregistrés dans le dossier ./data, qui a été créé au préalable, seulement s’ils ne s’y trouvent pas déjà.

```py
for file in files.values():
    file_path = data_dir/file
    if not file_path.exists():
        file_uri= base_uri + file
        print("downloading file", file_uri)
        Observations.download_file(file_uri, local_path = file_path)
```

Complétons quelques étapes de plus en suivant le fichier atelier.ipynb