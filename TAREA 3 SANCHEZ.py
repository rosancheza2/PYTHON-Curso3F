# EJERCICIO 1

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

mayor = numero1 if numero1 > numero2 else numero2

print("El mayor es:", mayor)


# EJERCICIO 2

def buscar_palabra(palabra, *args):
    resultado = "La palabra está en la lista" if palabra in args else "La palabra no está en la lista"
    print(resultado)


palabra = input("Ingrese la palabra a buscar: ")
buscar_palabra(palabra, "python", "java", "javascript", "c++")


# EJERCICIO 3

numero = int(input("Ingrese un numero: "))

resultado = "Par" if numero % 2 == 0 else "Impar"

print(resultado)


# EJERCICIO 4

def calcular_promedio(*args):
    promedio = sum(args) / len(args) if len(args) > 0 else 0
    print("Promedio:", promedio)


calcular_promedio(10, 8, 7, 9)


# EJERCICIO 5

def mostrar_datos(*args):
    mensaje = args if len(args) >= 2 else "Error: se necesitan al menos 2 argumentos"
    print(mensaje)


mostrar_datos("Rosalia")