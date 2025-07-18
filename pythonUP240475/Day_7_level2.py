# Level 2
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
#1-4
A.update(B)
print("#1 A actualizado con B:", A)

print("#2 Intersección de B y A:", B.intersection(A))

print("#3 ¿Un set puede ser un set o subset o superset?")
print("¿A es subconjunto de B?:", A.issubset(B))

print("#4 ¿A y B son disjuntos?:", A.isdisjoint(B))
#5-7
A.update(B)
B.update(A)

print("#6 Diferencia A - B:", A.difference(B))
print("   Diferencia B - A:", B.difference(A))

del A
del B