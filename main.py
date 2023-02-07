from module import *  #Importation des modules nécessaires à partir d'un fichier externe.

def main(): # Définition de la fonction principale "main()".
    date = ['', '', ''] # Initialisation d'un tableau vide appelé "date" qui va stocker une date entrée par l'utilisateur.
    for i in range(3): # Utilisation d'une boucle "for" pour itérer 3 fois et demander à l'utilisateur d'entrer chaque élément de la date (jour, mois, année) qui sera stocké dans le tableau "date".
        date[i]=input("Entrer la date dans l'ordre JJ/MM/AAAA : ")


    # Définition d'une variable "url" en utilisant une chaîne de formatage f. Cette variable contient l'URL d'un fichier CSV en ligne qui comprend la date entrée par l'utilisateur
    url = (f"https://files.data.gouv.fr/lcsqa/concentrations-de-polluants-atmospheriques-reglementes/temps-reel/{date[2]}/FR_E2_{date[2]}-{date[1]}-{date[0]}.csv")
    df = donnees(url) #Utilisation de la fonction "donnees()" pour récupérer les données à partir de l'URL et les stocker dans une variable "df".
    df = graph(df) # Utilisation de la fonction "graph()" pour traiter les données contenues dans "df" et les préparer pour une visualisation.
    return df # Retourne le dataframe "df" traité # Utilisation de la fonction "donnees()" pour récupérer les données à 



   