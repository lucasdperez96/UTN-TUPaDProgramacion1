# ===============================================
# Trabajo Práctico 4: Estructuras repetitivas
# Nombre y Apellido: Lucas Daniel Perez
# DNI: 39656325
# Fecha de entrega: 05/09/2025
# ===============================================

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(101):
    print(x)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

num = int(input("Ingrese un numero entero:"))
digitos = 1
while num >= 10 :
    num = num / 10
    digitos+=1

print("cantidad de digitos del numero ingresado: ", digitos)