#_____________________________
# Exercice 34 : fonction mathématique

# def f(a,b,x):
#     result = a*(x**3) + 2*a*(x**2) + b
#     return result 

# if __name__ == '__main__':  
#     print(f(0,2,2))


#_____________________________
# Exercice 35 : présence d'un élément dans une liste

# def VerifPresence(a,L):
#     if a in L:
#         return True
#     else:
#         return False
    
# if __name__ == '__main__':
#     print(VerifPresence(2,[1,2,3,4,5,6])) 
#     print(VerifPresence(-1,[3,6,9,7,"abcr"])) 



#_____________________________
# Exercice 36 : calcul de la somme des chiffres d'un nombre

# def sommme_chiffre(nb):
#     tot = 0
#     nb = str(nb) 
#     nb = list(nb)
#     for i in range(len(nb)):
#         tot += int(nb[i])
#     return tot 

# if __name__ == '__main__':
#     print(sommme_chiffre(3018)) 




#_____________________________
# Exercice 37 : somme d'une liste d'entiers

# def calculSomme(L):
#     tot = 0
#     for element in L:
#         tot += element
    
#     return tot

# if __name__ == '__main__':
#     print(calculSomme([3,2,6,9,-1,5])) 
#     print(calculSomme([-3,-6,0,1,2,7])) 


#_____________________________
# Exercices 38 : suppression des doublons 

# def supprimerDoublons(L):
#     L_doublons = [] # Liste dans laquelle je vais stocker les chiffres doublons
#     for elem in L:
#         occurence = L.count(elem) # On compte l'occurence de chaque element de la liste
#         if occurence > 1:
#             if (elem,occurence) not in L_doublons: # Si l'occurence est supérieur à 1 et que l'élément n'est pas déjà dans L_doublons, on l'ajoute, avec son nombre d'occurences
#                 L_doublons.append((elem,occurence))

#     for doublons in L_doublons: # On parcours la liste des elements doublons
#         for i in range(doublons[1]-1): # On supprime dans L chaque element doublons le nb de fois d'occurence -1 (pour qu'il en reste au moins un exemplaire)
#             L.remove(doublons[0])

#     return sorted(L) 
    
# if __name__ == '__main__':
#     print(supprimerDoublons([0,3,5,7,3,5,1,-1])) 
#     print(supprimerDoublons([0,5,9,10,3.2,1,-3])) 



# OU SINON 



# def supprimerDoublons_bis(L):
#     for elt in L:
#         elt_occ = L.count(elt)
#         if elt_occ >= 2:
#             for i in range(elt_occ-1):
#                 L.remove(elt)

#     L.sort()
#     return L

# if __name__ == '__main__':
#     print(supprimerDoublons_bis([0,3,5,7,3,5,1,-1]))
#     print(supprimerDoublons_bis([0,5,9,10,3.2,1,-3])) 