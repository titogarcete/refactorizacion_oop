from constantes import TAMAÑO_MATRIZ
from nodo import Nodo

def heuristica(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)  # Distancia Manhattan entre dos nodos

def obtener_vecinos(matriz, nodo):
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Direcciones de movimiento (arriba, abajo, izquierda, derecha)
    vecinos = []  # Lista para almacenar los vecinos válidos

    for dx, dy in direcciones:  # Para cada dirección posible
        x, y = nodo.x + dx, nodo.y + dy  # Calcular las coordenadas del vecino
        if 0 <= x < TAMAÑO_MATRIZ and 0 <= y < TAMAÑO_MATRIZ:  # Verificar si las coordenadas están dentro de los límites de la matriz
            vecinos.append(matriz[x][y])  # Añadir el vecino válido a la lista

    return vecinos  # Devolver la lista de vecinos

def reconstruir_camino(nodo):
    camino = []  # Lista para almacenar el camino
    while nodo:  # Mientras haya un nodo
        camino.append((nodo.x, nodo.y))  # Añadir el nodo al camino
        nodo = nodo.padre  # Moverse al nodo padre
    return camino[::-1]  # Devolver el camino en orden inverso

def crear_matriz(costos):
    return [[Nodo(x, y, costos[x][y]) for y in range(TAMAÑO_MATRIZ)] for x in range(TAMAÑO_MATRIZ)]  # Crear una matriz de nodos a partir de los costos

def dibujar_matriz(matriz, camino, inicio, fin):
    for i in range(TAMAÑO_MATRIZ):  # Recorrer las filas de la matriz
        for j in range(TAMAÑO_MATRIZ):  # Recorrer las columnas de la matriz
            if (i, j) == (inicio.x, inicio.y):  # Si es la celda de inicio
                simbolo = 'I'  # Usar 'I' para el inicio
            elif (i, j) == (fin.x, fin.y):  # Si es la celda final
                simbolo = 'F'  # Usar 'F' para el final
            elif (i, j) in camino:  # Si la celda está en el camino encontrado
                simbolo = '*'  # Usar '*' para el camino
            else:  # Para las otras celdas
                simbolo = str(matriz[i][j].costo)  # Usar el costo de la celda
            print(simbolo, end=' ')  # Imprimir el símbolo con un espacio
        print()  # Nueva línea al final de la fila

def obtener_entrada_usuario(inicio_x, inicio_y, fin_x, fin_y):
    obstáculos = []  # Lista para almacenar los obstáculos
    for i in range(3):  # Solicitar tres obstáculos
        while True:  # Bucle para validar la entrada del usuario
            try:
                x = int(input(f"Ingrese la coordenada x del obstáculo tipo {i+1} (0-{TAMAÑO_MATRIZ-1}): "))  # Solicitar la coordenada x
                y = int(input(f"Ingrese la coordenada y del obstáculo tipo {i+1} (0-{TAMAÑO_MATRIZ-1}): "))  # Solicitar la coordenada y
                if 0 <= x < TAMAÑO_MATRIZ and 0 <= y < TAMAÑO_MATRIZ and (x, y) != (inicio_x, inicio_y) and (x, y) != (fin_x, fin_y):  # Verificar si las coordenadas están dentro de los límites de la matriz y no colisionan con inicio o fin
                    obstáculos.append((x, y, COSTOS_OBSTACULOS[i]))  # Añadir el obstáculo a la lista con el costo correspondiente
                    break  # Salir del bucle
                else:
                    print("Coordenadas fuera de rango o colisionan con inicio/final. Intente de nuevo.")  # Mensaje de error para coordenadas inválidas
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")  # Mensaje de error para entrada no numérica
    return obstáculos  # Devolver la lista de obstáculos
