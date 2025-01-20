# Importer la librairie pandas et lui donner l'alias pd
import pandas as pd
import matplotlib.pyplot as graph
import numpy
# Lire le fichier CSV. df est un terme utilisé pour datafile
df = pd.read_csv("eclipse_solaire.csv")
print(df.columns)
# Afficher un résumé des 5 premières lignes
print(df.head())

# Configurer pandas pour afficher plus de colonnes
pd.set_option('display.max_columns', 6)


liste = df.iloc[:, 0].tolist()   #toutes les lignes de la colonne 0 (la première)
liste2 = df['Temperature'].tolist()

print(liste)

#df.to_excel('eclipse_solaire.xlsx', index=False)
#Exercice graphique
# Convertir la colonne 'Timestamp' en format datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
temps = df['Timestamp'].tolist()
luminosite = df.iloc[:,1].tolist()

graph.figure(figsize=(10, 6))
graph.plot(temps, luminosite, color='green',marker='o', linestyle='-')

graph.title('Luminosité au fil du temps')
graph.xlabel('Temps')
graph.ylabel('Luminosité (%)')
graph.grid(True)
graph.xticks(rotation=45)
graph.tight_layout()
graph.show()


