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

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# La función len() en Python devuelve la longitud (cantidad de elementos) de un objeto (retorna int). Aplicada a un string obtenemos la longitud de palabra
password = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
longitud = len(password)
if longitud >= 8 and longitud <= 14 : 
    print("Ha ingresado una contraseña correcta")
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el
# siguiente:
# from statistics import mode, median, mean
# mi_lista = [1,2,5,5,3]
# mean(mi_lista)
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
# import random
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

import random
from statistics import mode, median, mean

print("Prediccion de forma de una distribucion normal segun media, mediana y moda: ")
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda :
    print("Sesgo positivo")
elif media < mediana and mediana < moda :
    print("Sesgo positivo")
elif media == mediana == moda :
    print("Sesgo positivo")
else : 
    print("No cumple las condiciones")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

#Para resolver esto voy a interpretar a el string ingresado como una lista de caracteres.
#Tambien voy a hacer uso de las funciones str.upper() y str.lower() para simplificar un poco el codigo

texto = input("Ingrese una frase o palabra: ")
longitud = len(texto)
ultima_letra = str.upper(texto[longitud-1]) #convierto siempre a mayuscula para simplificar validacion
salida = texto+"!" if ultima_letra == "A" or ultima_letra == "E" or ultima_letra == "I" or ultima_letra == "O" or ultima_letra == "U" else texto #Uso operador ternario para variar un poco
print(salida)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# upper() convierte texto en mayúscula, lower() en minúscula, title() cambia el inicio de cada palabra a mayuscula y luego todo el resto a minuscula,
# agrego capitalize() que es parecida a title() pero lo hace sobre solo la primer palabra.
# ahora bien, como sabe title() donde empieza cada palabra?
# title() en Python detecta el inicio de cada palabra usando los separadores de palabras, que son principalmente:
# -Espacios (" ")
# -Signos de puntuación (como . , ; : ! ? -)
# -Saltos de línea o tabulaciones
# Básicamente, cualquier carácter que no sea una letra ni un número marca un posible “corte” y hace que la siguiente letra sea mayúscula.

nombre = input("Ingrese su nombre: ")
print()
valor = int(input("Ahora ingrese uno de los siguientes valores:\n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro."))

# Aprovechando que estamos en version posterior a la 3.10 de python voy a usar match en lugar de un if anidado

match valor :
    case 1:
        print(str.upper(nombre))
    case 2:
        print(str.lower(nombre))
    case 3:
        print(str.title(nombre))
    case _:
        print("Usted ingreso un valor distinto a 1, 2 o 3")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese magnitud de un terremoto: "))

if magnitud < 3 :
    print(""""Muy leve" (imperceptible).""")
elif magnitud >= 3 and magnitud < 4 :
    print(""""Leve" (ligeramente perceptible).""")
elif magnitud >= 4 and magnitud < 5 :
    print(""""Moderado" (sentido por personas, pero generalmente no causa daños).""")
elif magnitud >= 4 and magnitud < 6 :
    print(""""Fuerte" (puede causar daños en estructuras débiles).""")
elif magnitud >= 6 and magnitud < 7 :
    print(""""Muy Fuerte" (puede causar daños significativos).""")
else :
    print(""""Extremo" (puede causar graves daños a gran escala).""")

# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# +--------------------------------------------------------+-------------------------------+-------------------------------+
# | Periodo del año                                        | Hemisferio Norte              | Hemisferio Sur                |
# +--------------------------------------------------------+-------------------------------+-------------------------------+
# | Desde el 21 de diciembre hasta el 20 de marzo          | Invierno                      | Verano                        |
# | Desde el 21 de marzo hasta el 20 de junio              | Primavera                     | Otoño                         |
# | Desde el 21 de junio hasta el 20 de septiembre         | Verano                        | Invierno                      |
# | Desde el 21 de septiembre hasta el 20 de diciembre     | Otoño                         | Primavera                     |
# +--------------------------------------------------------+-------------------------------+-------------------------------+
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese el hemisferio en el que se encuentra (N/S): ").upper()
hemisferio = hemisferio[0] #Por si ingresan una palabra me quedo solo una letra

# para no complicarme de momento asumo que el usuario colocará valores en el rango especificado
mes = int(input("Ingrese el mes del año en formato numerico (numero de 1 a 12): "))
dia = int(input("que dia es hoy (numero de 1 a 31): "))

# Dos listas que me permiten saber la estacion segun el emisferio
norte = ["Invierno","Primavera","Verano","Otoño"]
sur = ["Verano","Otoño","Invierno","Primavera"]

# Setea la lista segun el emisferio elegido 
lista_estaciones = norte if hemisferio == 'N' else sur

# Necesito que el indice me coincida para cada trimestre del año entoces:
# si el mes es enero : 1 % 3 != 0 -> 1 // 3 = 0
# si el mes es febrero : 2 % 3 != 0 -> 2 // 3 = 0
# si el mes es marzo : 1 % 3 == 0 -> 3 // 3 = 1 (este valor no me sirve, restamos uno para que entre en el primer trimestre)
indice_estaciones = mes // 3 if (mes % 3 != 0 ) else (mes // 3) -1

if dia >= 21 :
    # Si el indice de estaciones es igual al tamaño de la lista de estaciones quiere decir que debo reiniciar el ciclo (volver al principio de la lista)
    print(lista_estaciones[indice_estaciones+1]) if indice_estaciones+1<len(lista_estaciones) else print(lista_estaciones[0])
else :
    print(lista_estaciones[indice_estaciones])
    