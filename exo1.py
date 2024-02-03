# Premiere proposition
def transform(chain):
    # On separe les nombres 
    chain_split = [chaine.split(", ") for chaine in chain]
    # On les convertit en entier
    chain_item_int = [[int(item) for item in items]for items in chain_split]
    # On les concatene en enlevant les doublons et en forcant l'ordre croissant
    chain_concat = sorted(set(chain_item_int[0]+chain_item_int[1]),reverse=False)
    # On recuperer les doublons
    doublons = [i for i in chain_item_int[0] if i in chain_item_int[1]]
    
    if len(doublons) == 0:
        return "None"
    
    return f"{sorted(doublons,reverse=True)}:DANSOGO_SEYDOU_MASTER1"

# Deuxieme proposition
def transform1(chain):
    # On sépare les nombres 
    chain_split = [chaine.split(", ") for chaine in chain]
    # On les convertit en ensembles pour faciliter les opérations
    set1, set2 = set(map(int, chain_split[0])), set(map(int, chain_split[1]))
    # On trouve les doublons
    doublons = sorted(set1.intersection(set2), reverse=True)
    
    if not doublons:
        return "None"
    
    return f"{','.join(map(str, doublons))}:DANSOGO_SEYDOU_MASTER1"


# vous ne modifierez rien après cette ligne
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out) # doit afficher ---> 31,4,1:nom_prenom_classe
    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out) # doit afficher ---> None