#_____________________________
# Exercice 51 : calcul de la factorielle d'un nombre 

# def calculFactorielle(n):
#     entiers = [i for i in range(1,n+1)]
#     result = 1
#     for i in entiers:
#         result *= i 
#     return result

# if __name__ == '__main__':
#     print(calculFactorielle(3))
#     print(calculFactorielle(9))
#     print(calculFactorielle(0)) 



#_____________________________
# Exercice 52 : diviseurs & multiples 

# def diviseursMult(n,a,nbrSeuil):
#     i = 1
#     liste_multiples_de_n = [] 
#     valeur_stop = n

#     while valeur_stop < nbrSeuil-n:
#         valeur_stop = i*n
#         liste_multiples_de_n.append(valeur_stop)
#         i += 1


#     for element in liste_multiples_de_n:
#         if element%a == 0:
#             liste_multiples_de_n.remove(element)

#     return liste_multiples_de_n


# OU SINON

# def divMult(n,a,nbrSeuil):
#     resultat = []
#     liste_entiers = [i for i in range(nbrSeuil+1)] # tous les entiers jusqu'au nombre seuil

#     for element in liste_entiers:
#         if element%n == 0 and element%a != 0: # La on check les deux conditions simultanément
#             resultat.append(element)

#     return resultat 


# if __name__ == '__main__':
#     print(divMult(5,2,100))
#     print(divMult(11,3,85)) 



#_____________________________
# Exercice 53 : présence d'une voyelle dans une chaine de caracteres

# def presenceVoyelle(phrase):
#     voyelle = ['a','e','i','o','u','y']
#     for car in phrase:
#         if car in voyelle:
#             return True # ! On oublie pas qu'une fonction prends fin à partir du moment où elle rencontre un return
#     return False 

# if __name__ == '__main__':
#     print(presenceVoyelle("Bonjour je vais prendre ma douche"))
#     print(presenceVoyelle("rbhpm")) 



#_____________________________
# Exercice 54 : suppression des espaces dans une phrase 

# def supprEspace(phrase):
#     phrase = phrase.split() # transfome la str en liste de tous les mots. split() et split(" ") retourne la meme chose
#     phrase = ''.join(phrase) # transforme la liste en str à nouveau en regroupant tous les mots sans espaces
#     return phrase 

# if __name__ == '__main__':
#     print(supprEspace("La France est belle !"))
#     print(supprEspace("Je vais prendre mon vélo.")) 



#_____________________________
# Exercice 55 : position d'un élément dans une liste

# def positionEltListe(L,x):
#     indices = []
#     for i in range(len(L)):
#         if L[i] == x:
#             indices.append(i)
    
#     if len(indices) == 0:
#         return "L'élément {} ne se trouve pas dans la liste {}.".format(x, L) 
#     else : 
#         return indices
    
# if __name__ == '__main__':
#     print(positionEltListe([1,2,3,6,8,7,3], 3))
#     print(positionEltListe([6,8,9,1,3,7],-1)) 
