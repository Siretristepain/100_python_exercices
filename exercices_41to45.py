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



