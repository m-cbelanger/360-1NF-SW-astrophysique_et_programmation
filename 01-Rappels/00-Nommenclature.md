Voici les règles de nomenclature convenues généralement en Python:

| **Élément**           | **Règles de Nomenclature**                                                                 |
|------------------------|--------------------------------------------------------------------------------------------|
| **Variables**          | - Utiliser des lettres minuscules, avec des mots séparés par des underscores (`snake_case`).  |
|                        | - Les noms doivent être explicites (ex. `age_utilisateur` et non `a`).                      |
| **Constantes**         | - Utiliser des lettres majuscules avec des underscores (`UPPER_CASE`).                      |
|                        | - Exemple : `NOMBRE_MAX` ou `TAXE_TPS`.                                                    |
| **Fonctions**          | - Utiliser `snake_case`.                                                                   |
|                        | - Exemple : `calcul_moyenne()` ou `afficher_message()`.                                     |
| **Classes**            | - Utiliser `PascalCase` (majuscule pour chaque mot).                                       |
|                        | - Exemple : `Voiture`, `UtilisateurPremium`.                                               |
| **Méthodes de classes**| - Même règle que pour les fonctions : `snake_case`.                                         |
| **Modules**            | - Noms en minuscules, parfois avec des underscores si nécessaire.                          |
|                        | - Exemple : `mon_module.py`, `analyse_donnees.py`.                                         |
| **Packages**           | - Noms en minuscules, sans underscores si possible.                                        |
|                        | - Exemple : `monpackage`.                                                                 |
| **Attributs privés**   | - Préfixer le nom avec un underscore (`_`) pour indiquer que l’attribut est privé.          |
|                        | - Exemple : `_variable_privee`.                                                            |
| **Attributs protégés** | - Préfixer le nom avec deux underscores (`__`) pour éviter tout conflit de noms.            |
|                        | - Exemple : `__variable_protegee`.                                                         |
| **Variables globales** | - Utiliser `UPPER_CASE` et des noms explicites pour des variables globales.                 |
| **Mots réservés**      | - Ne jamais utiliser les mots-clés Python comme noms (ex. `def`, `class`, `import`, `print`, etc.).  |
