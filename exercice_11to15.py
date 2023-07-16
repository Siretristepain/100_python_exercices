#_______________________
# Exercice 11 : compréhension de liste conditionnelle

# mes_nombres_pairs = [i for i in range(1,11) if i%2==0]
# print(mes_nombres_pairs) 


#_______________________
# Exercice 12 : trier une liste 

# ma_liste = [6,8,3,4,1,12,2,9.2]
# ma_liste = sorted(ma_liste)
# print(ma_liste) 

# OU SINON

# ma_liste = [6,8,3,4,1,12,2,9.2]
# ma_liste.sort()
# print(ma_liste) 


#_______________________
# Exercice 13 : calculer l'occurrence d'un élément

L = [3,2,2,1,9,1,2,3,7]

# compteur = 0 
# for i in range(len(L)):
#     if L[i] == 1:
#         compteur += 1

# print(f"1 apparait {compteur} fois.") 


# OU TOUT SIMPLEMENT

# nb_occurrence = L.count(1)
# print(nb_occurrence) 



#_______________________
# Exercice 14 : ajouter des éléments à une liste

# L = [] 

# # L += [10,25,30,45,90,'ab','cd','ef']
# # print(L)  

# # OU SINON 

# elem_a_ajouter = [10,25,30,45,90,'ab','cd','ef']
# for i in elem_a_ajouter:
#     L.append(i)

# print(L) 



#_______________________
# Exercice 15 : compréhension de liste et travail sur les listes

# L = [i for i in range(1,11)]
# L1 = []

# for i in range(0,len(L),3):
#     L1.append(L[i]) 
# print(L1) 

# OU SINON 

# for i in range(len(L)):     # Avec cette méthode on agit sur l'élément d'itération i .
#     if i%3 == 0:
#         L1.append(L[i]) 
# print(L1) 



