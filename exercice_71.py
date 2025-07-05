import math

def fonctTrigo(x):
    """Le but de cet exercice est juste d'utiliser le module math.

    Args:
        x (float): la valeur x de l'équation.

    Returns:
        float: le résultat de l'équation.
    """
    return math.cos(x)*math.sin(x)+math.sin(x)+8

if __name__ == '__main__':
    print(fonctTrigo(math.pi/4))
    print(fonctTrigo(math.pi))