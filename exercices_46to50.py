#_____________________________
# Exercice 46 : les diviseurs d'un nombre entier

# def diviseur(n):
#     liste_diviseurs = []

#     for i in range(1,n+1,1):
#         if n%i == 0:
#             liste_diviseurs.append(i)

#     return liste_diviseurs

# if __name__ == '__main__':
#     print(diviseur(9)) 



#_____________________________
# Exercice 47 : vérification de majuscule

# def verifMaj(phrase):
#     verif = 0
#     for car in phrase:
#         if car.isupper() == True:
#             verif += 1
#             break # Ca ne sert à rien de vérifier toutes les lettres à partir du moment où on a trouver une majuscule. 

    
#     if verif > 0 :
#         return True
#     else: 
#         return False 

# if __name__ == '__main__':
#     print(verifMaj("Bonjour ma couillas"))  


# OU SINON 

# def verifmajuscule(phrase):
#     for lettre in phrase:
#         if lettre.isupper():
#             return True
#     return False 

# if __name__ == '__main__':
#     print(verifmajuscule('hello world')) 




#_____________________________
# Exercice 48 : concaténation de listes 

# def concatListe(L1,L2,L3):
#     liste_final = L1 + L2 + L3
#     return liste_final

# if __name__ == '__main__':
#     print(concatListe([0,9,8],[2,6,9],[True,False,"abc"])) 
#     print(concatListe([[38,-1],3,-9],["xz","France"],[])) 



#_____________________________
# Exercice 49 : calcul du nombre de valeurs d'un dictionnaire 

# def nbrValeurDict(d):
#     liste_valeurs = [len(i) for i in list(d.values())]
#     return sum(liste_valeurs)


# OU SINON 

# def nbrValeur(d):
#     liste_cle = list(d.keys()) 
#     nbr_val = 0
#     for cle in liste_cle:
#         nbr_val += len(d[cle])
#     return nbr_val

# if __name__ == '__main__':
#     print(nbrValeurDict({"a":[1,2,3], "b":[3,"p"], "c":[8]})) 
#     print(nbrValeurDict({"Julie":[12,60.1], "Fred":[26,75.6], "David":[]})) 



#_____________________________
# Exercice 50 : concaténation de dictionnaires

# def concatDict(d1,d2):
#     d3 = {} # nouveau dictionnaire qui sera la concaténation des deux autres
#     d1_keys = [i for i in list(d1.keys())] # on récupère les clés de d1
#     d2_keys = [i for i in list(d2.keys())] # on récupère les clés de d2

#     for cle in d1_keys: # on creer les meme clés dans d3 que dans d1 et on y stocke les memes valeurs
#         d3[cle] = d1[cle]

#     for cle in d2_keys: # on creer les meme clés dans d3 que dans d2 et on y stocke les memes valeurs
#         d3[cle] = d2[cle]

#     return d3 


# OU SINON

# def concatenationDict(d1,d2):
#     d1.update(d2) # la méthode update est bien pratique pour concaténer des dictionnaires 
#     return d1 

# if __name__ == '__main__':
#     print(concatenationDict({"a":3, "b":6}, {"c":2, "d":-1}))
#     print(concatenationDict({"d":[2.9,4.1]}, {"p":[]})) 


