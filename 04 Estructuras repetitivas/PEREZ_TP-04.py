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

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("Suma de rangos numericos!\nEste programa suma todos los numeros comprendidos en un rango definido por usted (excluyendo las cotas).")
ini = int(input("Ingrese numero inicial: "))
fin = int(input("Ingrese numero final: "))
strSuma=""
suma = 0

for x in range(ini+1,fin):
    strSuma+=str(x) if x==ini+1 else " + " + str(x)
    suma+=x
    
print(f"Resultado:\n{strSuma} = {suma}")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

print("Suma de enteros!\n-Ingrese los numeros uno a uno para sumar\n-Ingrese 0 para salir.")

numero=int(input("ingrese un numero: ")) 
suma=0
while numero != 0 :
    suma += numero
    numero=int(input("ingrese un numero: "))
    if numero == 0 :
        break
    print(f"{suma} + {numero} = {suma+numero}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

print("Adivine el numero!")
numeroAleatorio = random.randint(0, 9)
numero=int(input("Ingrese un numero: "))
count=1

while(numero != numeroAleatorio):
    print("Incorrecto, siga intentando.")
    count+=1
    numero=int(input("Ingrese un numero: "))
print(f"Correcto! el numero era {numeroAleatorio}, usted realizó {count} intento(s)." )