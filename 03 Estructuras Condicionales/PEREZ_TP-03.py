# ===============================================
# Trabajo Práctico 3: Estructuras condicionales
# Nombre y Apellido: Lucas Daniel Perez
# DNI: 39656325
# Fecha de entrega: 31/08/2025
# ===============================================

# Actividades
# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
mayoria_edad = int(18)
if edad >= mayoria_edad:
    print("Es mayor de edad")
elif edad >= 0 or edad > 18: #Excede lo solicitado en la consigna pero es una mejora
    print("Es menor de edad")
else:
    print("Valor ingreasado incorrecto")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.

nota = float(input("Ingrese su nota: "))
aprobado = float(6)

if nota >= aprobado : 
    print ("Aprobado")
else :
    print ("Desaprobado")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0 :
    print("Ha ingresado un número par")
else :
    print("Por favor, ingrese un número par")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad < 12 :
    print("Niño/a: menor de 12 años.")
elif edad >= 12 and edad < 18 : 
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif edad >= 18 and edad < 30 : 
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif edad >= 30 :
    print("Adulto/a: mayor o igual que 30 años.")
else : #Excede lo solicitado en la consigna, mejora para no permitir edades negativas
    print("Error: Edad ingresada menor a 0")