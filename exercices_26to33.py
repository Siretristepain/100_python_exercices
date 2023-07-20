#_____________________________
# Exercice 26 : supprimer un element d'une liste

# L = [1,2,3,4,5]
# L.remove(1) # retire uniquement la première occurence 
# print(L) 



#_____________________________
# Exercice 27 : récupérer l'extension d'un fichier

import pathlib
import os

# dossier_courant = pathlib.Path(os.getcwd()) # Je récupère le chemin du dossier courant et je le transforme en objet pathlib
# liste_des_fichiers = [x for x in dossier_courant.iterdir() if x.is_file] # Méthode pour récupérer tous les fichiers d'un dossier (ici le dossier courant)
# # print(liste_des_fichiers) # Pour afficher tous les fichiers de la liste
# for fichier in liste_des_fichiers:
#     print(fichier.suffix) 


# OU SINON 

# chemin_fichier = r'C:\Users\Utilisateur\Desktop\100_python_exercices\exercices_26to30.py'
# nom_fichier = os.path.basename(chemin_fichier) # On récupère le nom du fichier, c'est à dire la fin du chemin_fichier --> str
# extension_fichier = print(nom_fichier.split('.')[-1]) # On converti le nom de notre fichier en liste en splitant sur le point et on récupère le dernier élément de la liste



#_____________________________
# Exercice 28 : temps d'execution d'un script

# import timeit

# def table_8():
#     for i in range(11):
#         print("8 x {} = {}".format(i, i*8))

# script_time = timeit.timeit(table_8, number=1)
# print("Le script à mis {} seconde.".format(script_time)) 


# OU SINON 


# import time 

# debut = time.time() # On stocke le temps au debut du programme

# for i in range(11):
#     print("8 x {} = {}".format(i, i*8))

# fin = time.time() # On stocke le temps à la fin du programme 

# print("Le script a mis {:.10f} seconde.".format(fin-debut)) 




#_____________________________
# Exercice 29 : mélanger aléatoirement une liste

# import random

# L = [3,6,8,7,2,"s","ch","d"]
# random.shuffle(L)
# print(L) 


#_____________________________
# Exercice 30 : générer aléatoirement un nombre

# import random 
# print(random.randint(20,30)) 



#_____________________________
# Exercice 31 : affichage de motif 

# for i in range(8):
#     for j in range(5,21):
#         print(j, end=' ') # l'instruction end=' ' permet de dire que l'on veut un espace à la suite de ce qu'on affiche
#     print() # l'instruction print() seule permet de dire que l'on souhaite aller à la ligne 



#_____________________________
# Exercice 32 : compréhension de liste

# L = [3,6,9,12,15,18,21,24]
# L1 = [i/3 for i in L]
# print(L1) 


#_____________________________
# Exercice 33 : compréhension de liste 

# L = [-6,5,-3,-1,2,8,-3.6]
# L1 = [i for i in L if i>0]
# print(L1) 