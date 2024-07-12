import heapq
from nodo import Nodo
from utilidades import heuristica, obtener_vecinos, reconstruir_camino
from constantes import TAMAÑO_MATRIZ

def a_estrella(matriz, inicio, fin):
    lista_abierta = []  # Lista de nodos abiertos
    heapq.heappush(lista_abierta, inicio)  # Añadir el nodo inicial a la lista abierta
    inicio.g = 0  # El costo g del nodo inicial es 0
    inicio.f = heuristica(inicio, fin)  # El costo total f del nodo inicial es solo la heurística

    while lista_abierta:  # Mientras haya nodos en la lista abierta
        actual = heapq.heappop(lista_abierta)  # Extraer el nodo con el menor costo f

        if actual == fin:  # Si se alcanza el nodo final, reconstruir el camino
            return reconstruir_camino(actual)

        for vecino in obtener_vecinos(matriz, actual):  # Para cada vecino del nodo actual
            g_tentativo = actual.g + vecino.costo  # Calcular el costo tentativo para llegar al vecino

            if g_tentativo < vecino.g:  # Si el costo tentativo es menor que el costo conocido para el vecino
                vecino.padre = actual  # Actualizar el nodo padre del vecino al nodo actual
                vecino.g = g_tentativo  # Actualizar el costo acumulado para llegar al vecino
                vecino.h = heuristica(vecino, fin)  # Calcular la heurística desde el vecino hasta el nodo final
                vecino.f = vecino.g + vecino.h  # Calcular el costo total f para el vecino
                if vecino not in lista_abierta:  # Si el vecino no está ya en la lista abierta
                    heapq.heappush(lista_abierta, vecino)  # Añadir el vecino a la lista abierta

    return None  # Si no se encuentra camino, devolver None
