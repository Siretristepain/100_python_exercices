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

