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

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for x in range(100,0,-2) :
    print(x)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

print("Suma de enteros positivos:\nEste rograma calcula la suma de todos los numeros comprendidos entre cero y un numo ingresado por usted")
numero = int(input("Ingrese un numero: "))
strSuma="0"
suma = 0

for x in range(1,numero):
    strSuma+=" + " + str(x)
    suma+=x

# El enunciado no aclara si el numero ingresado debe formar parte de la suma
# Yo decidí incluirlo
strSuma+=" + " + str(numero)
suma+=numero

print(f"Resultado:\n{strSuma} = {suma}")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# La consigna no aclara si hay que hacer distincion de numeros repetidos, yo decidí que no se distinguen
n=100
print(f"El siguiente programa le pedira el ingreso de {n} numeros y los contará segun sean: ")
print("-Positivos\n-Negativos\n-Pares\n-Impares")
print()
positivo=0
negativo=0
par=0
impar=0
numero=0

for x in range( 0 , n ) :
    numero=int(input("Ingrese un numero: "))
    if numero >=0 :
        positivo += 1
    else :
        negativo += 1
    if numero % 2 == 0 :
        par += 1
    else :
        impar += 1
print()
print("resultados:")
print(f"-Positivos: {positivo}\n-Negativos: {negativo}\n-Pares: {par}\n-Impares: {impar}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

n = 100
print(f"El siguiente programa calcula la media entre {n} numeros enteros ingresados por usted: ")
resultado = 0

for x in range( 0 , n ) :
    numero = int(input("Ingrese un numero: "))
    resultado += numero
resultado /= n
print()
print(f"Resultado: {resultado}")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745

# La forma sencilla de hacer este ejercicio es tomado los numeros como string, pero 
# decidí tomar tanto el numero ingresado como el invertido como entero, ya que creo que, aunque no lo aclara, el ejercicio apunta a eso.

print ("El siguiente programa invierte el orden de los digitos de un numero ingresado por usted: ")
numero = int(input("Ingrese un numero: "))
invertido=0
while numero >= 10 :
    # Me quedo el resto de dividir por diez (Ultima cifra)
    invertido += numero % 10
    # Multiplico por diez (agrega un digito para sumer el siguiente)
    invertido *= 10
    # Elimino del nro original el digito ya procesado
    numero //= 10

# Ultima suma que me queda fuera del ciclo
invertido += numero

print (invertido)

# La desventaja de este metodo (usando enteros y no string) es que si el usuario ingresa un nro terminado en cero
# al darlo vuelta se pierde por ser un cero a la izquierda.