Guide = input("1-Entrer 'add' pour faire une Addition.\n 2-Entrer 'sous' pour faire une Soustraction.\n 3-Entrer 'mul' pour faire une Multiplication.\n 4-Entrer 'div' pour faire une Division.\n 5-Entrer 'res' pour trouver un Modulo.\n 6-Entrer 'expo' pour calculer un Exposant.\n")

choix= input('*Entrez votre choix: ')

def Addition():
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la deuxieme valeur: '))
    add = val1 + val2
    return add

def Soustraction():
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la deuxieme valeur: '))
    sous = val1 - val2
    return sous

def Multiplication():
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la deuxieme valeur: '))
    mul = val1 * val2
    return mul

def Division():
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la deuxieme valeur: '))
    div = val1 / val2
    return div

def Modulo():
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la deuxieme valeur: '))
    res = val1 % val2
    return res

def Exposant():
    val1 = int(input('Entrez la premiere valeur: '))
    val2 = int(input('Entrez la deuxieme valeur: '))
    expo = val1 ** val2
    return expo


while choix != ['add','sous','mul','div','res','expo']:

 if choix == 'add':
     print('Le resultat est: ',Addition())
     print()
 elif choix == 'sous':
     print('Le resultat est: ',Soustraction())
     print()
 elif choix == 'mul':
     print('Le resultat est: ',Multiplication())
     print()
 elif choix == 'div':
     print('Le resultat est:',Division())
     print()
 elif choix == 'res':
     print('Le resultat est: ',Modulo())
     print()
 elif choix == 'expo':
     print('Le resultat est: ',Exposant())
     print()
 else:
     print('Ce choix ne convient pas, essayer a nouveau')
     choix = input('*Entrez votre choix: ')
     print('Ce choix est convenable')
      