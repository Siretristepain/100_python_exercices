#_____________________________
# Exercice 16 : Trier une chaine de caractères

def tri(texte):
    texte = list(texte)
    texte.sort() # la méthode sort() retourne une liste
    texte_final = ''.join(texte) 
    return print(texte_final)  

# if __name__ == '__main__':
#     tri('france') 

# OU SINON 

# a = "france"
# a = sorted(a) # la fonction sorted retourne une liste 
# a = ''.join(a)
# print(a) 



#_____________________________
# Exercice 17 : Eléments en commun entre deux listes

L1 = [9,8,7,14,3,2,"a","p","bonjour","b"]
L2 = ["b",1,9.2,6,3,9,"p"] 

# L3 = [i for i in L1 if i in L2] 
# print(L3) 

# OU SINON 

# L3 = set(L1).intersection(set(L2)) # La méthode intersection compare deux éléments de type set et trouve les éléments en communs
# print(L3) 


#_____________________________
# Exercice 18 : trier une liste de tuple 

# L = [("Pomme", 15),("Banane",8),("Fraise",12),("Kiwi",9),("Peche",2)] 

# L.sort(key=lambda x: x[1]) # L'argument key de la méthode sort() permet de selectionner le deuxieme élément du tuple
# print(L) 


#_____________________________
# Exercice 19 : inverser une chaine de caractères

ch = "Bonjour tout le monde"

# final = []
# for i in range(len(ch)-1,-1,-1):
#     final.append(ch[i])

# print(''.join(final))

# OU SINON

# ch_inversed = ch[::-1] # La syntaxe [::-1] fait référence à [debut:fin:pas]. Sans index de debut et de fin et avec -1 en pas, la str est inversée
# print(ch_inversed) 


#_____________________________
# Exercice 20 : les valeurs d'un dictionnaire

dico = {
    "Pomme" : 3,
    "Banane" : 7,
    "Kiwi" : 1,
}

# print(f"Nb de pomme : {dico['Pomme']}\nNb de Banane : {dico['Banane']}") 