# =========================================
# PRÁCTICA - EXCEPCIONES
# PYTHON INTERMEDIO
# =========================================


# EJERCICIO 1
print("\n--- Ejercicio 1 ---")

numero1 = 10
numero2 = 0

try:
    resultado = numero1 / numero2
    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")


# EJERCICIO 2
print("\n--- Ejercicio 2 ---")

numero = 10
texto = "20"

try:
    resultado = numero + texto
    print("Resultado:", resultado)

except TypeError:
    print("Error: no se puede sumar un número con una cadena de texto.")


# EJERCICIO 3
print("\n--- Ejercicio 3 ---")

persona = {
    "nombre": "Juan",
    "edad": 25
}

try:
    print(persona["apellido"])

except KeyError:
    print("Error: la clave buscada no existe en el diccionario.")


# EJERCICIO 4
print("\n--- Ejercicio 4 ---")

nombre_archivo = "archivo.txt"

try:
    with open(nombre_archivo, "r") as archivo:
        contenido = archivo.read()
        print(contenido)

except FileNotFoundError:
    print("Error: el archivo no existe.")

    with open(nombre_archivo, "w") as archivo:
        archivo.write("Archivo creado correctamente.")

    print("Se creó el archivo:", nombre_archivo)


# EJERCICIO 5
print("\n--- Ejercicio 5 ---")

try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    resultado = numero1 / numero2

except ValueError:
    print("Error: debe ingresar números válidos.")

except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

else:
    print("Resultado:", resultado)

finally:
    print("Fin del programa.")