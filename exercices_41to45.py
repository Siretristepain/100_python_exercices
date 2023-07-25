#_____________________________
# Exercice 41 : somme d'une sous liste

# def sommeSousListe(L,i,j):
#     total = 0
#     for elem in range(i,j+1):
#         total += L[elem]
#     return total 

# if __name__ == '__main__':
#     print(sommeSousListe([4,10,12,16,18],2,4))
#     print(sommeSousListe([2,4,6,8,10,12],0,2))



#_____________________________
# Exercice 42 : création de motif

# L'exercice ne demandait que de réaliser un motif à 6 lignes.
# J'ai poussé l'exercice un peu plus loin en créant une fonction qui permet de choisir le nombre de lignes que l'on veut.
# On remarque que la ligne i+1 possède 2 étoiles de plus que la ligne i, SAUF pour les deux premières lignes où il y à 1 étoile puis 2.

# def motif(nb_lignes):
#     print('*\n**') # On affuche toujours 1 étoile sur la première ligne et 2 sur la deuxième --> notre fonction ne fonctionne par pour nb_lignes = 0 ou 1.
#     nb_lignes -= 2 # Je soustrait 2 au nb_lignes. Cela correspond aux deux premieres lignes que j'affiche quoiqu'il arrive.
#     nb_etoiles = 4 
#     for i in range(1, nb_lignes+1):
#         for j in range(nb_etoiles):
#             print('*', end='') # On affiche autant d'étoiles que la valeur nb_etoiles sur une ligne
#         print() # On revient à la ligne
#         nb_etoiles += 2 # On ajoute 2 à nb_etoiles pour qu'il y ait deux etoiles de plus à la prochaine ligne

# if __name__ == '__main__':
#     motif(6) 


# OU SINON 

# for nbr_etoile in range(1,11):
#     if nbr_etoile%2 == 0 or nbr_etoile == 1:
#         print("*"*nbr_etoile) 





#_____________________________
# Exercice 43 : recréation de la fonction min

# def minimum(L):
#     plus_petit = L[0]
#     for element in L:
#         if element < plus_petit:
#             plus_petit = element
#     return plus_petit

# if __name__ =='__main__':
#     print(minimum([-9,2,4,1,8]))
#     print(minimum([-3,1,7,8,2,3])) 


#_____________________________
# Exercice 44 : recréation de la fonction len

# def longueur(L):
#     long = 0
#     for element in L:
#         long += 1
#     return long

# if __name__ == '__main__':
#     print(longueur([3,6,7,"abde",[1,3,57],True])) 
#     print(longueur([])) 



#_____________________________
# Exercice 45 : calcul de la moyenne d'une liste 

# def moyenneListe(L):
#     somme = 0
#     for element in L :
#         somme += element

#     moyenne = somme / len(L) 
#     return moyenne 

# if __name__ == '__main__':
#     print(moyenneListe([1,2,3,4,5,6,7])) 
#     print(moyenneListe([3,0,-1,5,6,9,17])) 