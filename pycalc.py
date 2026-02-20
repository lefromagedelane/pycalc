def calculatrice():
    
    val1 = int(input("Ecrire le premier nombre : "))
    operateur = input("Ecrire l'opérateur souhaité : ")
    val2 = int(input("Ecrire le deuxième nombre : "))
    
    if operateur == "*":
        resultat = val1 * val2
        print("Résultat :", resultat)

calculatrice()