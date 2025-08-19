# ===============================================
# Trabajo Práctico 1: Estructuras secuenciales
# Nombre y Apellido: Lucas Daniel Perez
# DNI: 39656325
# Fecha de entrega: 18/08/2025
# ===============================================

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre=input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
lugarResidencia=input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugarResidencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
pi=float(3.1416)
radio=float(input("Ingrese el radio del círculo: "))

area= pi*radio**2
perimetro=2*pi*radio

print(f"El área del círculo es {area} y su perímetro {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos=float(input("Ingrese segundos a convertir en horas: "))
horas=segundos/3600
print(f"Los segundos ingresados ({segundos}) esquivalen a {horas:.2f} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
print("Vamos a mostrar tablas de multiplicar")
numero=int(input("Ingrese un numero entero: "))
print()      # Esto imprime una línea vacía

#Utilizo {var:N} para guardar n espacios con la finalidad que al mostrar por pantalla muestre la tabla alineada
for i in range(1,11):
    print(f"{numero:2} x {i:2} = {numero*i:3}")


# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = numero2 = 0

while numero1 == 0:
    numero1=int(input("Ingrese el primer numero entero distinto de cero: "))
    if numero1 == 0:
         print("Error: no puede ser cero, intenta nuevamente.")

while numero2 == 0:
    numero2=int(input("Ingrese el segundo numero entero distinto de cero: "))
    if numero2 == 0:
         print("Error: no puede ser cero, intenta nuevamente.")

suma= numero1 + numero2
division= numero1 / numero2
multiplicacion= numero1 * numero2
resta= numero1 - numero2

print(f"\nLos resultados son: \n{numero1} + {numero2} = {suma} \n{numero1} / {numero2} = {division} \n{numero1} * {numero2} = {multiplicacion} \n{numero1} - {numero2} = {resta}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
# modo:
# 𝐼𝑀𝐶 =𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔/(𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)**2
print("Calculadora de IMC")
altura=float(input("Ingrese su altura (expresada en metros): "))
peso=float(input("Ingrese su peso (expresado en kilogramos): "))

imc = peso / altura**2

print(f"\nSu IMC es: {imc:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
# 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5*𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32
print("Calculadora de grados Fahrenheit")
temperaturaC=float(input("Ingrese temperatura (expresada en grados Celcius): "))

temperaturaF = 9/5 * temperaturaC + 32

print(f"\nLa temperatura ingresada ({temperaturaC} °C) expresada en grados Fahrenheit es: {temperaturaF:.1f} °F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
print("Calculadora de promedios")
numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
numero3=float(input("Ingrese el tercer numero: "))

promedio = (numero1 + numero2 + numero3)/3 

# {var:g} omite ceros innecesarios
print(f"\nEl promedio ente {numero1:g}, {numero2:g} y {numero3:g} es: {promedio:.2f} ")
