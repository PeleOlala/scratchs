def valeurs(dico):
    d_l = list(dico.keys())
    d_l.sort()
    return [ dico[i] for i in d_l]
  
print(valeurs({'3': 'trois', '2': 'deux', '6': 'six', '5': 'cinq', '4': 'quatre', '1': 'un'}))
    
