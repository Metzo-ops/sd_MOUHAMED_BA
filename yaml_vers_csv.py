def transform_yaml_en_csv() :
    import yaml
    # convertissons notre fichier yaml en dictionnaire
    with open ("yaml_file.yaml","r" ) as yamfil:
        kinp  = yaml.load(yamfil)
        print(kinp)
    #maintenant,convertissons notre  dictionnaire en csv    

transform_yaml_en_csv()        