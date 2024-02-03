lst1 = list(range(1200, 2000, 135))

# Générer lst2 
lst2 = []
for i in lst1:
    if i % 2 == 0:
        lst2.append(i * 2)  # (2)

# Générer les listes o et e avec des boucles et des conditions
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
o = []
e = []

for x in numbers:
    if x % 2 == 0:
        o.append(x)
    else:
        e.append(x)

print(lst1)
print(lst2)
print(o)
print(e)

# L'autre maniere d'additionner 2 entier

a,b = 3,4
r = sum([a,b]) 
print(r)
