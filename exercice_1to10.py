#____________________________
# Exercice 1 : assignation de variable

# a = 1
# b = "France"
# c = 36.2
# print(a,b,c)

#____________________________
# Exercice 2 : modification de variable

# ch = "salut"
# ch = "ça va"
# print(ch) 

#____________________________
# Exercice 3 : conversion de variables

# x = 3
# y = 8.5

# x = str(x)
# y = str(y)

# print(f"type de x : {type(x)}, type de y : {type(y)}")

#____________________________
# Exercice 4 : interaction avec l'utilisateur 

# poids = input("Votre poids en kg : ")

# print(f"Votre poids est de {poids} kg.")


#____________________________
# Exercice 5 : vérification à l'aide d'instructions conditionnelles (if)

# var = "Bonjour"

# if type(var) == str:
#     print("Chaine de caractères")
# elif type(var) == int:
#     print("Entier")


#____________________________
# Exercice 6 : if + comparateur logique

# d = 5

# if d >= 0:
#     print("Positif")
# else : 
#     print("Négatif")


#____________________________
# Exercice 7 : if + comparateur logique

# age = int(input("Quel est votre âge? --> ")) # ! input retour une str par défaut

# if age >= 18:
#     print("L'utilisateur est majeur")
# else:
#     print("L'utilisateur est mineur") 


#____________________________
# Exercice 8 : boucles for et while 

# for i in range(0,21):
#     print(i)

# a = 0
# while a < 21:
#     print(a)
#     a += 1


#____________________________
# Exercice 9 : boucles for et while et opérateur modulo 

# for i in range(10,21):
#     if i % 2 != 0:
#         print(i) 


# compteur = 10 
# while compteur <= 20:
#     if compteur % 2 != 0:
#         print(compteur) 
#     compteur += 1 


#____________________________
# Exercice 10 : compréhension de liste

# mes_nombres = [i for i in range(1,11)]
# print(mes_nombres) 