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

# def liste_utilisateur():
#     # Demander la liste d'entier à l'utilisateur
#     liste_utilisateur = input("Saisir une liste d'entier : ")

#     # On enlève les crochets au début et à la fin de la liste (s'il y en a. Pas d'erreur avec lstrip/rstrip s'il y en a pas).
#     liste_utilisateur = liste_utilisateur.lstrip('[')
#     liste_utilisateur = liste_utilisateur.rstrip(']')

#     # On sépare les entiers par les virgules
#     tes = liste_utilisateur.split(sep=',')

#     # On passe chaque entier en type integer car ils sont en str pour l'instant
#     for i in range(len(tes)):
#         tes[i] = int(tes[i])


#     return liste_utilisateur



# def liste_utilisateur_bis():
#     # Demander la liste d'entier à l'utilisateur
#     saisie = input("Saisir une liste d'entiers (ex: 1, 2, 3) : ")

#     # Nettoyer la saisie et la convertir en liste d'entiers
#     saisie = saisie.strip('[]')
#     liste = [int(x.strip()) for x in saisie.split(',') if x.strip() != '']

#     return liste


#_____________________________
# Exercice 69 : nombre de jours et d'heures
# import logging

# logging.basicConfig(level=logging.INFO)

# def nbrJourHeure(dateDebut, dateFin):
#     """
#     Méthodologie :
#     Axiome : partons du principe que la date de debut est toujours antérieure à la date de fin.

#     - si les années sont identiques sur les 2 dates, alors c'est assez simple car soit :
#         - le mois de la date de fin est supérieure à la date de début et on peut facilement calculer le delta
#         - soit les mois sont identitiques mais alors le jour de la date de fin est supérieur à la date de début et on peut facilement calculer le delta
    
#     - si les années sont différentes sur les 2 dates, c'est plus compliqué car alors le mois de la 2ème date peut être antérieur à celui de la première.
#         - on se place au 1er janvier de l'année de la date de fin.
#         - on calcul l'écart entre le 1er janvier et la date de fin.
#         - on fait la différence entre année de la date de fin et année de la date de début (deltaAnnee).
#         - le nombre d'années COMPLETES entre date de début et date de fin corresponds à daltaAnnee - 1.
#         - ensuite on se place au 31 décembre de l'année de la date de début et on calcule le delta avec la date de début.
#     """

#     DAYS_PER_MONTH = [31,28,31,30,31,30,31,31,30,31,30,31]

#     # On convertis nos dates en listes, format : [YYYY, MM, JJ]
#     debut = [int(i) for i in dateDebut.split('/')]
#     fin = [int(i) for i in dateFin.split('/')]

#     nb_jour = 0

#     delta_years = fin[0] - debut[0]

#     # Cas où il y plus d'un an d'écart
#     if delta_years > 1:
#         logging.debug(f"--> Il y a des années complètes entre les 2 dates")

#         # On ajoute les jours des années complètes d'écart
#         nb_jour += sum(DAYS_PER_MONTH) * (delta_years - 1)
#         logging.debug("_________________________________________________________________")
#         logging.debug(f"Nombre d'années complètes d'écart : {delta_years - 1}")
#         logging.debug(f"Nombre de jours ajoutés : {sum(DAYS_PER_MONTH) * (delta_years - 1)}")
#         logging.debug("_________________________________________________________________")

#         # On ajoute les jours des mois complets restant de l'année de début
#         nb_jour += sum(DAYS_PER_MONTH[debut[1]:])
#         logging.debug(f"Mois de l'année de la date de début : {debut[1]}")
#         logging.debug(f"Nombre de mois complets : {12 - 1}")
#         logging.debug(f"Nombre de jours ajoutés : {sum(DAYS_PER_MONTH[debut[1]:])} ")
#         logging.debug("_________________________________________________________________")

#         # On ajoute les jours restants du mois en cours (on récupère le nombre de jour du mois en cours auxquels on soustraits le jour de la date) de la date de début
#         nb_jour += DAYS_PER_MONTH[debut[1] - 1] - debut[2]
#         logging.debug(f"Jour de la date de début : {debut[2]}")
#         logging.debug(f"Nombre de jours ajoutés : {DAYS_PER_MONTH[debut[1] - 1] - debut[2]}")
#         logging.debug("_________________________________________________________________")

#         # On ajoute les jours des mois complets fait de l'année de fin
#         nb_jour += sum(DAYS_PER_MONTH[:fin[1] - 1])
#         logging.debug(f"Mois de la date de fin : {fin[1]}")
#         logging.debug(f"Nombre de mois terminés l'année de fin : {fin[1] - 1}")
#         logging.debug(f"Nombre de jours ajoutés : {sum(DAYS_PER_MONTH[:fin[1] - 1])}")
#         logging.debug("_________________________________________________________________")

#         # On ajoute les jours faits du mois en cours de la date de fin
#         nb_jour += fin[2]
#         logging.debug(f"Jour de la date de fin : {fin[2]}")
#         logging.debug(f"Nombre de jours ajoutés : {fin[2]}")
#         logging.debug("_________________________________________________________________")

#         print(nb_jour)

#     # Cas où il y a moins d'un an d'écart
#     elif delta_years == 1:
#         logging.debug(f"--> Il y a moins d'une année complète entre les 2 dates mais elles ont 2 années différentes")
#         # On ajoute les jours des mois complets restant de l'année de début
#         nb_jour += sum(DAYS_PER_MONTH[debut[1]:])
#         logging.debug(f"Mois de l'année de la date de début : {debut[1]}")
#         logging.debug(f"Nombre de mois complets : {12 - 1}")
#         logging.debug(f"Nombre de jours ajoutés : {sum(DAYS_PER_MONTH[debut[1]:])} ")
#         logging.debug("_________________________________________________________________")

#         # On ajoute les jours restants du mois en cours (on récupère le nombre de jour du mois en cours auxquels on soustraits le jour de la date) de la date de début
#         nb_jour += DAYS_PER_MONTH[debut[1] - 1] - debut[2]
#         logging.debug(f"Jour de la date de début : {debut[2]}")
#         logging.debug(f"Nombre de jours ajoutés : {DAYS_PER_MONTH[debut[1] - 1] - debut[2]}")
#         logging.debug("_________________________________________________________________")

#         # On ajoute les jours des mois complets fait de l'année de fin
#         nb_jour += sum(DAYS_PER_MONTH[:fin[1] - 1])
#         logging.debug(f"Mois de la date de fin : {fin[1]}")
#         logging.debug(f"Nombre de mois terminés l'année de fin : {fin[1] - 1}")
#         logging.debug(f"Nombre de jours ajoutés : {sum(DAYS_PER_MONTH[:fin[1] - 1])}")
#         logging.debug("_________________________________________________________________")

#         # On ajoute les jours faits du mois en cours de la date de fin
#         nb_jour += fin[2]
#         logging.debug(f"Jour de la date de fin : {fin[2]}")
#         logging.debug(f"Nombre de jours ajoutés : {fin[2]}")
#         logging.debug("_________________________________________________________________")

#         print(nb_jour)

#     # Cas où les 2 dates sont la même année
#     elif delta_years == 0:
#         logging.debug(f"--> Les 2 dates sont la même année")
#         delta_month = fin[1] - debut[1]

#         # Cas où il y a plus d'un mois complet d'écart
#         if delta_month > 1:
#             logging.debug("Il y a des mois entiers d'écart entre les 2 dates")

#             # On ajoute les jours restant du mois de début + les jours fais du mois de fin
#             nb_jour += (DAYS_PER_MONTH[debut[1] - 1] - debut[2]) + fin[2]
#             logging.debug(f"Jour de debut : {debut[2]} et mois de debut : {debut[1]}")
#             logging.debug(f"Jour de fin : {fin[2]}")
#             logging.debug(f"Nombre de jours ajoutés : {(DAYS_PER_MONTH[debut[1] - 1] - debut[2]) + fin[2]}")
#             logging.debug("_________________________________________________________________")

#             # On ajoute tous les jours des mois complets faits entre les 2 mois de début et de fin
#             nb_jour += sum(DAYS_PER_MONTH[debut[1]:fin[1] - 1])
#             logging.debug(f"Mois de départ : {debut[1]}")
#             logging.debug(f"Mois de fin : {fin[1]}")
#             logging.debug(f"Nombre de mois entier d'écart : {len(DAYS_PER_MONTH[debut[1]:fin[1] - 1])}")
#             logging.debug("_________________________________________________________________")

#             print(nb_jour)

#         elif delta_month == 1:
#             logging.debug(f"Les 2 dates sont sur des mois consécutifs (donc moins d'un mois d'écart mais pas le même mois quand même)")
#             # On ajoute les jours qui reste à faire entre la date de début et la fin du moi + les jours déjà faits du mois de la date de fin
#             nb_jour += (DAYS_PER_MONTH[debut[1] - 1] - debut[2]) + fin[2]

#             logging.debug(f"Jour de debut : {debut[2]} et mois de debut : {debut[1]}")
#             logging.debug(f"Jour de fin : {fin[2]}")
#             logging.debug(f"Nombre de jours ajoutés : {(DAYS_PER_MONTH[debut[1] - 1] - debut[2]) + fin[2]}")
#             logging.debug("_________________________________________________________________")

#             print(nb_jour)

#         elif delta_month == 0:
#             logging.debug("Les 2 dates sont le même mois")

#             nb_jour += fin[2] - debut[2]
#             logging.debug(f"Jour du début : {debut[2]}")
#             logging.debug(f"Jour de fin : {fin[2]}")
#             logging.debug(f"Nombres de jours ajoutés : {fin[2] - debut[2]}")
#             logging.debug("_________________________________________________________________")

#             print(nb_jour)



#         else:
#             raise ValueError("Les dates renseignées ne sont pas correctes. Les deux dates ont la même année mais le mois de la date de fin est antérieur à celui de la date de début.")

#     else:
#         raise ValueError("Les dates renseignées ne sont pas correctes. L'année de fin doit être supérieure à l'année de début.")

#     print(f"*** Résultats ***")
#     return print((nb_jour, nb_jour*24))

#_____________________________
# Exercice 70 : Générer aléatoirement un mot de passe

import random

def genererMDP(caracteres, taillemdp):
    """Méthode qui génère un mot de passe de longueur 'taillemdp' avec uniquement des caractères contenus dans 'caracteres'.

    Fonctionnement :
    L'idée est de séléctionner un caractère aléatoire dans la str des caractères autorisés via le module random, autant de fois que taillemdp.
    J'ai choisis de faire une liste en compréhension mais il aurait été possible (et plus lisible) de faire une boucle for.

    Args:
        caracteres (str): tous les caractères autorisés dans le mot de passe.
        taillemdp (int): longueur souhaitée pour le mot de passe.

    Returns:
        str : Le mot de passe.
    """

    mdp = [caracteres[random.randint(0, len(caracteres)-1)] for i in range(taillemdp)]
    return print(''.join(mdp))


if __name__ == '__main__':
    # Ex69
    # nbrJourHeure(dateDebut="2020/01/01", dateFin="2025/01/01")
    # nbrJourHeure(dateDebut="2022/10/10", dateFin="2025/05/07")
    # nbrJourHeure(dateDebut="2024/10/01", dateFin="2025/05/05")
    # nbrJourHeure(dateDebut="2025/10/01", dateFin="2025/10/10")
    # nbrJourHeure(dateDebut="2025/03/10", dateFin="2025/04/09")
    # nbrJourHeure(dateDebut="2025/10/01", dateFin="2025/10/10")
    # nbrJourHeure(dateDebut="2024/03/08", dateFin="2024/09/10")

    # Ex70
    genererMDP("abc/#123456789",10)
