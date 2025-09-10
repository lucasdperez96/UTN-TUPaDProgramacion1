# ===============================================
# Trabajo Práctico 5: Listas
# Nombre y Apellido: Lucas Daniel Perez
# DNI: 39656325
# Fecha de entrega: 09/09/2025
# ===============================================

# Actividades:
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [8, 4, 2, 8, 9, 5, 4, 10, 7, 4]
promedio=0
contador=0
mayor=notas[0]
menor=notas[0]

for nota in notas :
    print(nota)
    promedio+=nota
    if nota > mayor : 
        mayor=nota
    if nota < menor :
        menor=nota
    contador+=1

promedio/=contador
print(f"Promedio: {promedio}")
print(f"Mayor nota: {mayor}\nMenor nota: {menor}")


# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

n=5 # Elementos a cargar en la lista
lista=[]

for elemento in range(0,n) :
    lista.append(input(f"Ingrese un elemento a la lista ({elemento+1}/{n}): "))

lista_ordenada=sorted(lista)

for elemento in lista_ordenada :
    print(elemento)

respuesta=input("Que producto desea eliminar de la lista? ")

if respuesta in lista_ordenada : 
    lista_ordenada.remove(respuesta)
else :
    print("No existe el elemento que usted desea eliminar")

for elemento in lista_ordenada :
    print(elemento)

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for i in range(15)]
pares=[]
impares=[]

for numero in numeros :
    print(numero, end=" ") # end=" " imprime un valor al lado de otro (omite salto de linea)
    if numero % 2 == 0 :
        pares.append(numero)
    else :
        impares.append(numero)
 
print(f"\ncantidad de numeros pares generados: {len(pares)}")
print(f"cantidad de numeros impares generados: {len(impares)}")


# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

# La consigno no aclara el tipo de dato, asi que mezclo varios
lista = [8,44,'A',12,12,"Palabra",8,1,'z',"Palabra",9.8,2,"palabra",777,9.3,"Palabra"]

lista_final = sorted(lista, key=str) # Le asigno key=str para poder hacer la comparacion y ordenar

i = 1
while i < len(lista_final):
    if lista_final[i] == lista_final[i-1]: # Comparo dato alojado en i con su anterior
        lista_final.pop(i)  # A diferencia de remove() con pop() saco el dato dado un indice
    else:
        i += 1 # Solo si no saque un dato avanzo (la longitud de la lista es variable)

for elemento in lista_final :
    print(elemento, end=" ")


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Alan Monzón","Rocio Moscardi","Facundo Nadaf", "Lucas Perez","Santiago Naranja","Susana Morales","Ayelen Sosa","Javier Rodriguez"]

# Muestro lista inicial
print("Lista de estudiantes:")
for elemento in estudiantes :
    print(elemento)

# Mientras que el usuario no ingrese 1 o 2 repetimos pregunta
valor=-1
while not (valor==1 or valor==2) : 
    print()
    print("¿Desea agregar o eliminar un estudiante? Presione:")
    print("1 - Agregar estudiante")
    print("2 - Eliminar estudiante")
    valor = int(input())
    print("Ingrese nombre del alumno a",end=" ")
    alumno=str.title(input("agregar: " if valor==1 else "eliminar: "))

if valor == 1:
    # si eligio agregar 
    estudiantes.append(alumno)
elif alumno in estudiantes :
    # si eligio borrar
    estudiantes.remove(alumno)
else :
    # ingreso un dato incorrecto
    print("Usted ingresó un estudiante que nose encontraba en la lista")
    
for elemento in estudiantes :
    print(elemento)

# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).

numeros = [55,128,33,64,12,8,1010]
final = numeros[len(numeros)-1]

for i in range(len(numeros)-1,0,-1) :
    numeros[i] = numeros[i-1]
numeros[0]=final

for numero in numeros :
    print(numero,end=" ")

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
# semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [[10,18],[13,20],[5,11],[7,20],[13,22],[14,22],[15,29]]
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
max_amplitud = 0
prom_min=  0
prom_max=  0
dia = -1

for i in range(0, len(temperaturas)) :
    amplitud = 0
    for j in range(0, len(temperaturas[i])) :
        if j % 2 == 0:
            prom_min += temperaturas[i][j]
            amplitud -= temperaturas[i][j]
        else :
            prom_max += temperaturas[i][j]
            amplitud += temperaturas[i][j]
        if amplitud > max_amplitud :
            max_amplitud = amplitud
            dia = i

prom_min /= i
prom_max /= i

print(f"Promedio de minimas: {prom_min:.1f}")
print(f"Promedio de maximas: {prom_max:.1f}")
print(f"Dia de mayor amplitud termica: {dias[dia]}")
print(f"Mayor amplitud termica: {max_amplitud} °C")

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

materias = ["Matemática","Programación","Sistemas Operativos"]
promedio1 = ["Promedio por Estudiante"]
alumnos = ["A","B","C","D","E"]
notas = [[8,8,7],[4,5,8],[2,10,8],[7,6,4],[10,8,8]]
vacio = ""
prom_estudiantes = []
prom_materias = [0]*len(notas[0])
prom_estudiante = 0
titulos = materias + promedio1

print()
print("_____________________________________________________________________________________________________________________________________________")
print(f"| {vacio:^25} |",end=" ")
for titulo in titulos :
    print(f"{titulo:^25} |",end=" ")
print("\n---------------------------------------------------------------------------------------------------------------------------------------------")

for i in range (0, len(notas)) :
    print(f"| {alumnos[i]:<25} |",end=" ")
    for j in range (0, len(notas[i])) :
        print(f"{notas[i][j]:>25} |",end=" ")
        prom_estudiante += notas[i][j]
        prom_materias[j]+= notas[i][j]
    prom_estudiante /= len(notas[0])
    prom_estudiantes.append(prom_estudiante)
    prom_estudiante = 0
    print(f" {prom_estudiantes[i]:>24.2f} |",end=" ")
    print()
print("---------------------------------------------------------------------------------------------------------------------------------------------")
vacio = "Promedio de Materias:"
print(f"| {vacio:<25} |",end=" ")
vacio = ""
for valor in prom_materias:
    valor /= len(notas)
    print(f"{valor:>25} |",end=" ")
print(f"{vacio:>25} |",end=" ")
print()
print("---------------------------------------------------------------------------------------------------------------------------------------------")

# SALIDA:
# _____________________________________________________________________________________________________________________________________________
# |                           |        Matemática         |       Programación        |    Sistemas Operativos    |  Promedio por Estudiante  |
# ---------------------------------------------------------------------------------------------------------------------------------------------
# | A                         |                         8 |                         8 |                         7 |                      7.67 |
# | B                         |                         4 |                         5 |                         8 |                      5.67 |
# | C                         |                         2 |                        10 |                         8 |                      6.67 |
# | D                         |                         7 |                         6 |                         4 |                      5.67 |
# | E                         |                        10 |                         8 |                         8 |                      8.67 |
# ---------------------------------------------------------------------------------------------------------------------------------------------
# | Promedio de Materias:     |                       6.2 |                       7.4 |                       7.0 |                           |
# ---------------------------------------------------------------------------------------------------------------------------------------------


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

print("--------------------------------------------------")
print("             xxXO Ta - Te - Ti 0Xxx               ")
print("--------------------------------------------------")
print("Reglas:")
print("- Quien consiga nuna linea vertical, horizontal o diagonal gana! ")
print("- Las coordenadas solo pueden ser un valor nuemrico de 1 a 3")
print("- Jugador 1: O")
print("- Jugador 2: X")

tablero = [["-","-","-"],["-","-","-"],["-","-","-"]]
x = -1
y = -1
nro_jugador = 0
ficha = "-"
# Hay 9 casillas llenables
contador = 9
win = False

# Emulo un do while
while True :
    # Muestro tablero en cada vuelta 
    for i in range(0, len(tablero)) :
        print()
        for j in range(0, len(tablero[i])) :
            print (f"{tablero[i][j]:^5}",end=" ") 
        print()
    print()
    # Antes que anda decremento el contador (empieza en 8 y temina en 0 -> 9 ciclos)
    contador-=1
    # Si el contador llegó a -1  o alguien ganó me voy 
    if contador < 0  or win :
        break
    # Dependiendo si es par o impar se el turno de cada jugador
    if contador % 2 == 0:
        nro_jugador = 1
        ficha = "O"  
    else :
        nro_jugador = 2
        ficha = "X"
    print(f"Turno del jugador {nro_jugador}: ")
    x = int(input("Ingrese coordenada X : "))
    y = int(input("Ingrese coordenada Y : "))
    # Valido que el dato sea correcto
    while x > 3 or x < 1 or y > 3 or y < 1 or tablero[x-1][y-1] != '-':
        print("Ese lugar ya está ocupado o es una coordenada erronea, elija otra coordenada :")
        x = int(input("Ingrese coordenada X (fila):  "))
        y = int(input("Ingrese coordenada Y (columna): "))
    tablero[x-1][y-1] = ficha
    # Combinaicones necesarias para ganar:
    # [11,22,33][11,12,13][21,22,23][31,32,33][11,21,31][12,22,32][13,23,33][31,22,13]
    win= (
    ((tablero[0][0] == tablero[1][1] == tablero[2][2]) and tablero[0][0] != "-") or
    ((tablero[0][0] == tablero[0][1] == tablero[0][2]) and tablero[0][0] != "-") or
    ((tablero[1][0] == tablero[1][1] == tablero[1][2]) and tablero[1][0] != "-") or
    ((tablero[2][0] == tablero[2][1] == tablero[2][2]) and tablero[2][0] != "-") or
    ((tablero[0][0] == tablero[1][0] == tablero[2][0]) and tablero[0][0] != "-") or
    ((tablero[0][1] == tablero[1][1] == tablero[2][1]) and tablero[0][1] != "-") or
    ((tablero[0][2] == tablero[1][2] == tablero[2][2]) and tablero[0][2] != "-") or
    ((tablero[2][0] == tablero[1][1] == tablero[0][2]) and tablero[2][0] != "-")
    )   
    
        
# Si el contador no llego al final sé que alguien ganó    
if contador > -1 :
    print(f"Ganador: Jugador {nro_jugador}")
else:
    print("Empate!")

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
productos = ["Arroz", "Fideos", "Galletitas", "Pan"]
ventas = [[100,80.6,30,95,36.8,12.5,123],[20.2,10.6,40,125,18.8,9.6,93.9],[50,66.6,90,115,37.5,8.9,33],[22,105.3,35.5,18.60,17,44.7,39]]

ventas_producto = []
total_producto = 0
ventas_dia = [0]*len(ventas[0])
index = 0
max_ventas=0

for producto in ventas :
    for venta in producto :
        total_producto += venta
        ventas_dia[index] += venta
        index += 1
    index = 0
    ventas_producto.append(total_producto)
    total_producto=0

for i in range(0, len(ventas)) :
    if max_ventas < ventas_producto[i] :
        max_ventas = ventas_producto[i]
        index = i
    print(f"Total vendido de {productos[i]:<10} : ${ventas_producto[i]:>5.2f}")
print()
print(f"Producto mas vendido de la semana: {productos[index]} con ${max_ventas:.2f}")
print()
index=0
max_ventas=0
for j in range(0, len(ventas[0])) :
    if max_ventas < ventas_dia[j] :
        max_ventas = ventas_dia[j]
        index = j
    print(f"Total vendido el dia {dias[j]:<10} : ${ventas_dia[j]:>5.2f}")
print()
print(f"Día de mayores ventas totales: {dias[index]} con ${max_ventas:.2f}")
