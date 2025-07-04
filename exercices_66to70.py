#_____________________________
# Exercice 66 : écrire dans un fichier


# def ecrireFichier(nomFichier, texte):
#     with open(nomFichier, 'w') as f:
#         f.write(texte)
    
#     return

# if __name__ == '__main__':
#     ecrireFichier('fichier_test_ex66', "Ceci est un test pour voir si ma solution fonctionne.")


#_____________________________
# Exercice 67 : la clé avec le nombre de valeurs uniques maximales

# l = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
# def cleMaxValeurDict(d):
#     for cle in d:
#         for i in d[cle]:
#             nbr = d[cle].count(i)
#             if nbr > 1:
#                 for j in range(nbr-1):
#                     d[cle].remove(i)
    
#     return print(max(d, key=lambda x: len(d[x])))

# if __name__ == '__main__':
#     cleMaxValeurDict({"a":[9,10,9,7,3,1], "b":[5,3,2,2,2], "c":[1,1,1,1,1,1,8,2]})
#     cleMaxValeurDict({"dtg":[6,8,1], "fgb":[2.5,"a"], "klm":["p",3,3]}) 

# d = {'mathilde':[25,12,2],
#      'raphael':[24],
#      'lou':[17,14],
#      'barbara':[23],
#      'esteban':[7,20,14,9]}

# print(max(d, key=lambda x: len(d[x])))


#_____________________________
# Exercice 68 : demander une liste à l'utilisateur

""" 
Dans ma première méthode : liste_utilisateur(),
Pylance lève une erreur de syntaxe sur "liste_utilisateur[i]" (avant le signe =, dans la boucle for).
Cela est du au fait que initialement, liste_utilisateur est une str et non pas une liste.
Or Pylance analyse le code de façon statique et ne comprends donc pas, mais le code fonctionne bien.
À creuser.

Explications :

On peut utiliser les crochets sur des str pour accéder à un caractère MAIS, en Python,
une str est immutable, ce qui signifie que l'on ne peut pas modifier un caractère dans une chaîne existante.

À l'inverse, les list sont des objets mutables, c'est à fire que l'on peut modifier ses éléments avec
une assignation comme : liste[i] = valeur.

>>>
phrase = "bonjour"
print(phrase[2])

phrase[2] = 'o'
print(phrase)
>>>

Le code ci-dessus donne :

'n'
    phrase[2] = 'o'
TypeError: 'str' object does not support item assignment

--> on voit bien que les crochets fonctionnent pour accéder à un élément de la str mais ne permettent pas l'assignation.

C'est exactement la même chose dans ma méthode liste_utilisateur.
Initialement c'est une str, mais en lui appliquant la méthode split(), elle devient une liste, mais Pylance ne le voit pas.
C'est pour ça que le code fonctionne alors que Pylance nous souligne une erreur.

Ce que je ne comprends pas, c'est pourquoi en faisant :
def liste_utilisateur():
    chaine = input("Saisir une liste d'entier : ")
    chaine = chaine.strip('[]')
    liste = chaine.split(',')
    for i in range(len(liste)):
        liste[i] = int(liste[i])
    return liste

L'erreur persisite malgré le changement de variable.

Explications ChatGPT (ça vaut ce que ça vaut) :

⚠️ Pourquoi Pylance signale encore une erreur même après avoir changé le nom de la variable ?
En fait, ce n’est pas uniquement une question de nom, c’est une question de type déduit par Pylance à un instant donné dans le code.

Prenons ça ligne par ligne dans ce code :

python
Copier
Modifier
chaine = input("Saisir une liste d'entier : ")
chaine = chaine.strip('[]')
liste = chaine.split(',')  # ← Ici, Pylance comprend : "liste est une list[str]"
for i in range(len(liste)):
    liste[i] = int(liste[i])  # ← 🔴 Problème ici pour Pylance !
Ce que fait Pylance :

À la ligne liste = chaine.split(','), il déduit que liste est de type list[str].

À la ligne suivante, tu fais une modification "in-place" du contenu avec liste[i] = int(...).

Et là, Pylance est en panique parce que :

Il a vu que liste était une list[str],

Tu lui dis maintenant que ce sera une list[int] après modification,

Donc, il signale une incohérence de type entre avant et après.

👉 C’est une limitation de l’analyse de type "naïve" : Pylance ne suit pas les mutations internes aussi bien que Python à l’exécution.
"""

def liste_utilisateur():
    # Demander la liste d'entier à l'utilisateur
    liste_utilisateur = input("Saisir une liste d'entier : ")

    # On enlève les crochets au début et à la fin de la liste (s'il y en a. Pas d'erreur avec lstrip/rstrip s'il y en a pas).
    liste_utilisateur = liste_utilisateur.lstrip('[')
    liste_utilisateur = liste_utilisateur.rstrip(']')

    # On sépare les entiers par les virgules
    tes = liste_utilisateur.split(sep=',')

    # On passe chaque entier en type integer car ils sont en str pour l'instant
    for i in range(len(tes)):
        tes[i] = int(tes[i])


    return liste_utilisateur



# def liste_utilisateur_bis():
#     # Demander la liste d'entier à l'utilisateur
#     saisie = input("Saisir une liste d'entiers (ex: 1, 2, 3) : ")

#     # Nettoyer la saisie et la convertir en liste d'entiers
#     saisie = saisie.strip('[]')
#     liste = [int(x.strip()) for x in saisie.split(',') if x.strip() != '']

#     return liste


if __name__ == '__main__':
    pass