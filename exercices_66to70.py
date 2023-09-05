#_____________________________
# Exercice 66 : écrire dans un fichier


# def ecrireFichier(nomFichier, texte):
#     with open(nomFichier, 'w') as f:
#         f.write(texte)
    
#     return

# if __name__ == '__main__':
#     ecrireFichier('fichier_test_ex66', "Ceci est un test pour voir si ma solution fonctionne.")


#_____________________________
# Exercice 67 : la clé avec le nombre de valeurs uniques maximales

l = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
def cleMaxValeurDict(d):
    for cle in d:
        for i in d[cle]:
            nbr = d[cle].count(i)
            if nbr > 1:
                for j in range(nbr-1):
                    d[cle].remove(i)
    
    return print(max(d, key=lambda x: len(d[x])))

if __name__ == '__main__':
    cleMaxValeurDict({"a":[9,10,9,7,3,1], "b":[5,3,2,2,2], "c":[1,1,1,1,1,1,8,2]})
    cleMaxValeurDict({"dtg":[6,8,1], "fgb":[2.5,"a"], "klm":["p",3,3]}) 

# d = {'mathilde':[25,12,2],
#      'raphael':[24],
#      'lou':[17,14],
#      'barbara':[23],
#      'esteban':[7,20,14,9]}

# print(max(d, key=lambda x: len(d[x])))
        