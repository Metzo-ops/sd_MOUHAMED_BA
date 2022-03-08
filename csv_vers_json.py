import json
from queue import Empty


def transform_csv_en_json() :
    # d'abord,transformation du fichier csv en dictionnaire
    import csv,json
    vide = []
    file = open("donnees.csv","r") 
    pagediccsv = csv.DictReader(file) 
    for i in pagediccsv:
        vide.append(i)
    #transformation du dictionnaire en fichier json
    empty = open("del.json","w") 
    A = json.dump(vide,empty)
    print(A)

transform_csv_en_json()        
