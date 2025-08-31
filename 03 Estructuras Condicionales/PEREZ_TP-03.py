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