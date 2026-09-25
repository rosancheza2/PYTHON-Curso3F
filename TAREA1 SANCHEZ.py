
# Practica
# Curso de Python Intermedio - Tecno3F

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Conjunto A:", A)
print("Conjunto B:", B)
print()

# 1) Elementos que se encuentran en A o en B, o en ambos
union = A | B
print("1) Unión:", union)

# 2) Elementos que se encuentran en A y en B
interseccion = A & B
print("2) Intersección:", interseccion)

# 3) Elementos que se encuentran en A o en B, pero no en ambos
dif_simetrica = A ^ B
print("3) Diferencia simétrica:", dif_simetrica)

# 4) ¿A es subconjunto de B?
es_subconjunto = A.issubset(B)
print(f"4) ¿{A} es subconjunto de {B}? {es_subconjunto}")

# 5) Número de elementos de un conjunto
cantidad = len(A)
print(f"5) Cantidad de elementos de {A}: {cantidad}")