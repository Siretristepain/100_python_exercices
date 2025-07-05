from math import prod

""" 
Le but de l'exercice est de stocker dans une liste tous les entiers positifs de trois chiffres de la forme ABC tels que,
pour chaque entier, la somme de ces chiffre A+B+C soit un diviseur du produit de ces chiffres AxBxC.

Ex : 514 vérifie cette propriété car 5+1+4 = 10 est un diviseur de 5x1x4 = 20.
"""

def resolution():
    """Méthode qui renvoie tous les entiers positifs de 3 chiffres dont la somme des chiffres qui composent le nombre
    est un diviseur de la multiplication de ces 3 chiffres.

    Returns:
        list: Liste des nombres trouvés.
    """
    L = []

    # On va boucler de 100 à 999
    for i in range(100, 1000):

        # On convertis le nombre en liste d'entier pour dissocier son nombre des centaines, des dizaines et des unités
        list_number = [int(j) for j in str(i)]

        # On calcule la somme et le produits des chiffres qui compose le nombre
        sum_number = sum(list_number)
        times_number = prod(list_number)

        # Si sum_number est un diviseur de times_number on l'ajoute à L (cad si le reste de la division Euclidienne vaut 0)
        if times_number % sum_number == 0:
            L.append(i)

    return L

if __name__ == '__main__':
    print(resolution())
