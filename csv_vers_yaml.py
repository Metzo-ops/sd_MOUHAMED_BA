def transform_csv_en_yaml():
    # d'abord,transformation du fichier csv en dictionnaire
    import csv,yaml
    vid = []
    file = open("donnees.csv","r") 
    pagediccsv = csv.DictReader(file) 
    for i in pagediccsv:
        vid.append(i)
        #transformation du dictionnaire en fichier yaml
        mkf = open("ficyaml.yaml","w")
        B = yaml.dump(vid)
        return B    