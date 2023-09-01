#_____________________________
# Exercice 61 : lecture d'un fichier

# def lireFichier(chemin):
#     with open(chemin, 'r') as f:
#         contenu = f.read()
#         return contenu

# OU SINON


# def lirefichier(chemin):
#     fichier = open(chemin, 'r')
#     contenu = fichier.read()
#     fichier.close() # Il est essentiel de bien fermer le fichier après ouverture, la méthode with open de la fonction précédente permet de prendre ça en compte automatiquement
#     return contenu
    
# if __name__ == '__main__':
#     print(lirefichier(r"C:\Users\Utilisateur\Desktop\100_python_exercices\fichiertest_ex61.txt"))


#_____________________________
# Exercice 62 : nombre d'occurrences d'un mot dans un fichier

# def nbrOccFichier(chemin,mot):
#     with open(chemin, 'r') as f:
#         contenu = f.read() # lire le contenu du fichier (str)
#         contenu = contenu.split() # sépare tous les mots (list)

#         compteur = 0 # compteur du mot cherché
#         for element in contenu:
#             if element == mot:
#                 compteur += 1
        
#     return "Le mot {} apparait {} fois".format(mot, compteur)

# if __name__ == "__main__":
#     print(nbrOccFichier(r"C:\Users\Utilisateur\Desktop\100_python_exercices\fichiertest_ex62.txt","je"))




#_____________________________
# Exercice 63 : supprimer un caractère d'un fichier

# def supprCarac(chemin, caractere):
#     choix = input("Souhaitez-vous supprimer toutes les itérations du caractère ? (o/n)")
    
#     if choix == "o":
#         with open(chemin, 'r') as f:
#             contenu = f.read()
#             contenu = list(contenu)

#             iteration = contenu.count(caractere)

#             for i in range(iteration):
#                 contenu.remove(caractere)
            
#             return print("".join(contenu))
    
#     if choix == "n":
#         with open(chemin, 'r') as f:
#             contenu = f.read()
#             contenu = list(contenu)
#             contenu.remove(caractere)
#             return print("".join(contenu)) 
        
#     else:
#         return print("Vous n'avez pas saisi un choix valide !") 
    

# if __name__ == "__main__":
#     supprCarac(r"C:\Users\Utilisateur\Desktop\100_python_exercices\fichiertest_ex63.txt","o") 
            

# OU SINON 


# Cette deuxieme méthode a l'avantage de ne pas avoir besoin de transformer le contenu str en list puis inversement mais a le désavantage de modifier le fichier txt.
# def supprCaractere(chemin, caractere):
    
#     with open(chemin, 'r') as f:
#         contenu = f.read()

#     nouveau_contenu = contenu.replace(caractere, "")

#     with open(chemin, 'w') as f:
#         f.write(nouveau_contenu) 

#     return 

# if __name__ == "__main__":
#     supprCaractere(r"C:\Users\Utilisateur\Desktop\100_python_exercices\fichiertest_ex63.txt","o")


#_____________________________
# Exercice 64 : présence d'un nombre dans un fichier

# def presenceNombre(chemin):
#     with open(chemin, 'r') as f:
#         contenu = f.read()
#         contenu = list(contenu)

#         for element in contenu:
#             if element.isdigit():
#                 return print(True)
            
#         return print(False) 
    

# if __name__ == "__main__":
#     presenceNombre(r"C:\Users\Utilisateur\Desktop\100_python_exercices\fichiertest_ex64.txt")




#_____________________________
# Exercice 65 : nombre de fichiers dans un dossier

# from pathlib import Path

# def nombreFichier(chemin):
#     chemin = Path(chemin)
#     compteur_fichier = 0

#     for fichier in chemin.iterdir():
#         compteur_fichier += 1

#     return print("Il y a {} fichier(s) dans le dossier.".format(compteur_fichier))

# if __name__ == "__main__":
#     nombreFichier(r"C:\Users\Utilisateur\Desktop\100_python_exercices")


# OU SINON 

# import os 

# def nombreFichiers(chemin):

#     nb_fichier = 0

#     contenu_dossier = os.listdir(chemin) # donne uniquement les noms (et non les chemins entiers) de tout ce qui est présent dans le dossier

#     for element in contenu_dossier:
#         if os.path.isfile(os.path.join(chemin, element)) == True:
#             nb_fichier += 1
#     return print("Il y a {} fichier(s) dans le dossier.".format(nb_fichier)) 
 
# if __name__ == "__main__":
#     nombreFichiers(r"C:\Users\Utilisateur\Desktop\100_python_exercices") 


# !!! La deuxieme méthode pour compter les fichiers donne un fichier en moins par rapport à la première méthode car on vérifie bien si les elements dans le dossier
# sont des fichiers. Or le .git n'est pas un fichier mais un dossier ! Dans la première méthode on a pas été très rigoureux et on a pas vérifier si les elements 
# dans le dossier étaient bien des fichiers.