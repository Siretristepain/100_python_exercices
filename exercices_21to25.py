#_____________________________
# Exercice 21 : somme des valeurs d'un dictionnaire

dico = {
    "Pomme" : 15,
    "Banane" : 8,
    "Fraise" : 12,
    "Kiwi" : 9,
    "Peche" : 2,
}

# sum = 0
# for elem in dico.values():
#     sum += elem
# print(sum) 

# OU SINON 

# print(sum(dico.values())) 

#_____________________________
# Exercice 22 : utilisation de la méthode format()

# nb = 187.632587
# txt = "{:.2f}"
# print(txt.format(nb)) 

# OU SINON 

# print("{:.2f}".format(187.632587)) 


#_____________________________
# Exercice 23 : utilisation de la méthode format()

monNom = "Raphael"
age = 24
langage = "Python"

# print("Je m'appelle {monNom} et j'ai {age} ans. J'apprends le langage {langage}.".format(monNom=monNom,age=age,langage=langage))

# OU SINON 

# print("Je m'appelle {0} et j'ai {1} ans. J'apprends le langage {2}. Je suis {0}.".format(monNom, age, langage))

# OU ENCORE 

# print("Je m'appelle {} et j'ai {} ans. J'apprends le langage {}.".format(monNom,age,langage)) 



#_____________________________
# Exercice 24 : afficher la table de 8

# for i in range(0,11):
    # print("8 x {} = {}".format(i, 8*i))



#_____________________________
# Exercice 25 : afficher le dossier courant (repertoire de travail)

# import os

# print(os.getcwd()) # Le module os permet de faire des opérations courantes sur le système d'exploitation : creer/suppr des dossiers/fichiers
