"""
Module principal pour vérifier si une chaîne est un palindrome.
"""
#### Fonction secondaire


def ispalindrome(p):
    """
    Vérifie si la chaîne p est un palindrome.

    :param p: La chaîne à vérifier.
    :return: True si p est un palindrome, False sinon.
    """
    p = p.lower()
    if not isinstance(p, str):
        return False
    translation_table = str.maketrans("éèêëàâîôûç", "eeeeaaiouc", " ,;:.!?-'")
    p = p.translate(translation_table)
    return p == p[::-1]

    # votre code ici

#### Fonction principale

def main():
    """
    Point d'entrée du programme. 
    Teste la fonction ispalindrome avec différentes chaînes.
    """
    print(ispalindrome("A man a plan a canal Panama"))
    print(ispalindrome("La fievre jaune se répend"))

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
