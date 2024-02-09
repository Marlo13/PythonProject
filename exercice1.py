'''Exercice 5 : Liste des carrés créez une liste contenant les carrés des nombbres en 1 et 10 (inclus)
'''
liste = [i**2 for i in range(11)]
#print(liste)

'''Filtrage par Longueur de Mot
Étant donné une liste de mots, écrivez une fonction qui retourne une 
nouvelle liste contenant uniquement les mots ayant plus de 4 caractères.'''

liste = ["hello", "world", "python", "is", "awesome","be", "language", "to", "learn"]
liste2 = []
for i in liste:
    if len(i) > 4:
        liste2.append(i)

#print(liste2)

'''Exercice 8:
Comptage d'Occurrences
Écrivez une fonction qui compte le nombre d'occurrences de chaque élément 
dans une liste et retourne un dictionnaire avec ces comptages.
'''
import json
def count_occurence(list1):
    list2 = {}
    for x in list1:
        list2[x] = f" apparait {liste.count(x)} fois"

    formated_list = json.dumps(list2,indent=1)
    print(formated_list)

liste = ['a', 'a' ,'a' ,'x' ,'x', 'x',1 ,2, 4, 1, 2, 2, 2,9 ,9,"Hello","Hello","Hello","Hello","Hello","Hello","Hello","cat","car","car"]
count_occurence(liste)
