def transform_yaml_en_json() :
    import yaml
    import json
     # convertissons notre fichier yaml en dictionnaire
    with open ("yaml_file.yaml","r" ) as yamfil:
        kinp  = yaml.load(yamfil)
        print(kinp)
     #convertissons notre dict en json
        ist = []
        for i in kinp:
            ist.append(i)
        dc = open("doc.json","w") 
        A = json.dump(ist,dc)
        print(A)  

transform_yaml_en_json()     
