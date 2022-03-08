from asyncore import write
import csv
from fileinput import filename
from nis import match


def transform_json_en_csv() :
    import json
# je veux ouvrir ma page json comme dictionaire
    with open("page0.json") as file:
        page = json.load(file)
        print(page) 
# maintenant, je veux convertir mon dictionnaire en fichier csv  
           
    # je crée un fichier lex.csv(en csv) pour y ecrire , que je mets dans l'objet loop    
    loop = open("lex.csv","w")
    mak = csv.writer(loop,page)
    # je fais intervenir le writer qui sert à ecrire ,là, il ecrit mon dictionnaire en csv
    #writer = csv.DictWriter(loop, fieldnames=)
    #je ferme mon loop    
    loop.close()
    
transform_json_en_csv()