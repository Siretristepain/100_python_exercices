#_____________________________
# Exercice 56 : filtrer les mots suivant leurs longueurs

# def filtrerMots(phrase, longueur_min):
#     phrase = phrase.split()
#     mot_a_suppr = []
#     for mot in phrase:
#         if len(mot) <= longueur_min:
#             mot_a_suppr.append(mot)
    
#     for mot in mot_a_suppr:
#         phrase.remove(mot)
    
#     return ''.join(phrase) 


## OU SINON

# def filtrerMot(phrase, longueur_min):
#     phrase = phrase.split()
#     phrase_filtree = []
#     for mot in phrase:
#         if len(mot) > longueur_min:
#             phrase_filtree.append(mot)
    
#     return ''.join(phrase_filtree) 


# if __name__ == '__main__':
#     print(filtrerMots("Salut toi",4))
#     print(filtrerMots("Quel est ton origine ?", 5)) 



#_____________________________
# Exercice 57 : inverser l'ordre des mots 

# def inverserPhrase(phrase):
#     phrase = phrase.split()
#     phrase_inversee = []
#     for i in range(len(phrase)-1,-1,-1): # debut = len(phrase) -1 ; fin = -1 (pour que l'indice 0 soit compris), pas = -1
#         phrase_inversee.append(phrase[i])

#     return ' '.join(phrase_inversee) 

# if __name__ == '__main__':
#     print(inverserPhrase("Bonjour tout le monde"))
#     print(inverserPhrase("Pomme")) 


#_____________________________
# Exercice 58 : nombre d'occurences dans une liste

# def nombreOccurence(L):
#     liste_occ = []
#     for element in L:
#         occurence = L.count(element)
#         if (element, occurence) not in liste_occ:
#             liste_occ.append((element,occurence))
    
#     return liste_occ

# if __name__ == '__main__':
#     print(nombreOccurence([-4,8,-3,2,1,2,7,9,-3,8,1]))
#     print(nombreOccurence(["a",3,4,"b","a",3])) 


#_____________________________
# Exercice 59 : union de listes dans duplication 

# def unionListe(L1,L2,L3):
#     liste_complete = L1 + L2 + L3 # On concatène les trois listes
#     element_a_suppr = [] # Liste dans laquelle on fera apparaitre les doublons sous forme de tuple (element, nb_occurence)
#     liste_complete.sort()

#     for element in liste_complete:
#         occ = liste_complete.count(element)
#         if occ > 1 and (element, occ) not in element_a_suppr : # si un element apparait plusieurs fois et qu'on la pas deja précédemment remarqué
#             element_a_suppr.append((element, occ)) # on le fait apparaitre dans la liste de doublons à supprimer

#     for element in element_a_suppr: # on parcours la liste de doublons à supprimer
#         for _ in range(element[1]-1): # element[1] correspond au nombre d'occurence de l'element, on veut donc supprimer les doublons autant de fois qu'il apparaissent -1 (car on en veut quand meme un exemplaire)
#             liste_complete.remove(element[0]) # element[0] est l'element en tant de tel

#     return liste_complete



## OU SINON 


# def unionListe(L1,L2,L3):
#     ens1 = set(L1)
#     ens2 = set(L2)
#     ens3 = set(L3)

#     unionEnsemble = ens1 | ens2 | ens3 # L'opérateur | fait l'union au sens mathématique

#     L_union = list(unionEnsemble)

#     L_union.sort()

#     return L_union 


# if __name__ == '__main__':
#     print(unionListe([3,6,9,3],[1,0,3],[12,6,0]))
#     print(unionListe([7,44,-3],[],[7,2,7])) 



#_____________________________
# Exercice 60 : calcul du PGCD selon l'algorithme d'Euclide

# Pour trouver le PGCD de a et b  selon l'algorithme d'Euclide, il faut faire la division euclidienne du plus grand par le plus petit.
# Ensuite on répète l'opération avec le diviseur et le reste. Et ainsi de suite.
# Le PGCD est le dernier reste non nul. 

# def calculPGCD(a,b):
#     dividende = max(a,b)
#     diviseur = min(a,b)

#     if dividende%diviseur == 0: # Cas exceptionnel où le reste vaut 0 dès la premiere itération. Alors le PGCD est directement égal au diviseur
#         return diviseur
    
#     liste_reste = [] # Liste dans laquelle on va faire apparaitre les valeurs des restes
#     reste = 1 # Arbitrairement choisis différent de 0

#     while reste != 0:
#         reste = dividende%diviseur
#         liste_reste.append(reste)
#         dividende = diviseur # Le nouveau dividende est l'ancien diviseur
#         diviseur = reste # Le nouveau diviseur est l'ancien reste
#     return liste_reste[-2] # Puisqu'on trouve forcément un reste nul à la fin, on veut retourner l'avant dernier element de la liste (le dernier reste non nul = PGCD)

# if __name__ == '__main__':
#     print(calculPGCD(3,5))
#     print(calculPGCD(5,15)) 
