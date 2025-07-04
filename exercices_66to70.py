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

# l = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
# def cleMaxValeurDict(d):
#     for cle in d:
#         for i in d[cle]:
#             nbr = d[cle].count(i)
#             if nbr > 1:
#                 for j in range(nbr-1):
#                     d[cle].remove(i)
    
#     return print(max(d, key=lambda x: len(d[x])))

# if __name__ == '__main__':
#     cleMaxValeurDict({"a":[9,10,9,7,3,1], "b":[5,3,2,2,2], "c":[1,1,1,1,1,1,8,2]})
#     cleMaxValeurDict({"dtg":[6,8,1], "fgb":[2.5,"a"], "klm":["p",3,3]}) 

# d = {'mathilde':[25,12,2],
#      'raphael':[24],
#      'lou':[17,14],
#      'barbara':[23],
#      'esteban':[7,20,14,9]}

# print(max(d, key=lambda x: len(d[x])))


#_____________________________
# Exercice 68 : demander une liste à l'utilisateur

""" 
Dans ma première méthode : liste_utilisateur(),
Pylance lève une erreur de syntaxe sur "liste_utilisateur[i]" (avant le signe =, dans la boucle for).
Cela est du au fait que initialement, liste_utilisateur est une str et non pas une liste.
Or Pylance analyse le code de façon statique et ne comprends donc pas, mais le code fonctionne bien.
À creuser.
"""

# def liste_utilisateur():
#     # Demander la liste d'entier à l'utilisateur
#     liste_utilisateur = input("Saisir une liste d'entier : ")

#     # On enlève les crochets au début et à la fin de la liste (s'il y en a. Pas d'erreur avec lstrip/rstrip s'il y en a pas).
#     liste_utilisateur = liste_utilisateur.lstrip('[')
#     liste_utilisateur = liste_utilisateur.rstrip(']')

#     # On sépare les entiers par les virgules
#     liste_utilisateur = liste_utilisateur.split(sep=',')

#     # On passe chaque entier en type integer car ils sont en str pour l'instant
#     for i in range(len(liste_utilisateur)):
#         liste_utilisateur[i] = int(liste_utilisateur[i])


#     return liste_utilisateur

# def liste_utilisateur_bis():
#     # Demander la liste d'entier à l'utilisateur
#     saisie = input("Saisir une liste d'entiers (ex: 1, 2, 3) : ")

#     # Nettoyer la saisie et la convertir en liste d'entiers
#     saisie = saisie.strip('[]')
#     liste = [int(x.strip()) for x in saisie.split(',') if x.strip() != '']

#     return liste


if __name__ == '__main__':
    pass