#importation des modules
from pandas import * 
import matplotlib.pyplot as plt


#nom du fichier

def donnees(url):
#lire le fichier csv
    df = read_csv(url, sep=";")

#filtre du site et des polluants
    df = df[['Date de début', 'Polluant','valeur brute']][df['nom site'] == 'VITRY-SUR-SEINE']

#filtre/sélection des colonnes
    df = pivot_table(df, values='valeur brute', columns= 'Polluant', index= 'Date de début')#ON modifie le dataframe df en un tableau en 2 axes. L'axes des lignes sera le paramètre index sois date de debut et l'axes des colonnes qui sera relatif a chaque nom de polluant grace au paramètre columns
    #enfin le tableau sera rempli par les valeurs dans le rapport Date de debut/Polluant
    for i in range(len(df.index.values)):
        df.index.values[i] = df.index.values[i].split(' ')[1]

    for i in df.keys():#on parcours chaque clefs du dataframe df
        for j in df[i]: #on parcours chaque valeur de chaque polluant pour verifier si la concentration depasse les normes ou non
#on creer une suite de condition si le polluant depasse la conczentration maximal autorisé alors cela renvoit une notification textuelle  ainsi que ca concentration
            if i == 'NO2' and j >= 40.00:
                print(f"Alerte depassement du polluant : {i} concentration égale a {j}")
            if i == 'NOX as NO2' and j >= 30.00:
                print(f"Alerte depassement du polluant : {i} concentration égale a {j}")

            if i == 'O3' and j >= 120.00:
                print(f"Alerte depassement du polluant : {i} concentration égale a {j}")

            if i == 'PM10' and j >= 50.00:
                print(f"Alerte depassement du polluant : {i} concentration égale a {j}")
            if i == 'PM2.5' and j >= 25.00:
                print(f"Alerte depassement du polluant : {i} concentration égale a {j}")
            if i == 'NO' and j >= 2.50:
 
 
                print(f"Alerte depassement du polluant : {i} concentration égale a {j}")
    return df





def graph(df): #La fonction "graph()" prend en entrée un dataframe "df".

    graph = df.plot() #Utilise la méthode "plot()" du dataframe pour créer un graphique à partir des données contenues dans "df".
    print(df) #Utilise la méthode "print()" pour afficher le contenu complet du dataframe "df".
    print(df.mean(axis=0)) #Utiliser la méthode "mean()" pour calculer la moyenne des valeurs contenues dans "df" pour chaque colonne. Elle prend en paramètre "axis=0" pour indiquer que les calculs doivent être effectués sur les colonnes.
    print(df.describe()) #Utilise la méthode "describe()" pour obtenir des statistiques de base (comme la moyenne, l'écart-type, etc) pour chaque colonne du dataframe.
    return df #Retourne le dataframe "df" non modifié.

 