from constantes import TAMAÑO_MATRIZ, COSTO_POR_DEFECTO, matriz_madre
from nodo import Nodo
from algoritmo import a_estrella
from utilidades import crear_matriz, dibujar_matriz, obtener_entrada_usuario

def main():
    matriz = crear_matriz(matriz_madre)  # Crear la matriz de nodos a partir de la matriz madre

    # Obtener entradas del usuario para el punto de inicio y final
    while True:  # Bucle para validar la entrada del usuario
        try:
            inicio_x = int(input("Ingrese la coordenada x del punto de inicio (0-19): "))  # Solicitar la coordenada x del inicio
            inicio_y = int(input("Ingrese la coordenada y del punto de inicio (0-19): "))  # Solicitar la coordenada y del inicio
            fin_x = int(input("Ingrese la coordenada x del punto final (0-19): "))  # Solicitar la coordenada x del final
            fin_y = int(input("Ingrese la coordenada y del punto final (0-19): "))  # Solicitar la coordenada y del final
            if 0 <= inicio_x < TAMAÑO_MATRIZ and 0 <= inicio_y < TAMAÑO_MATRIZ and 0 <= fin_x < TAMAÑO_MATRIZ and 0 <= fin_y < TAMAÑO_MATRIZ:
                break  # Salir del bucle si las coordenadas son válidas
            else:
                print("Coordenadas fuera de rango. Intente de nuevo.")  # Mensaje de error para coordenadas inválidas
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")  # Mensaje de error para entrada no numérica

    obstáculos = obtener_entrada_usuario(inicio_x, inicio_y, fin_x, fin_y)  # Obtener obstáculos del usuario
    for x, y, costo in obstáculos:  # Para cada obstáculo
        matriz[x][y].costo = costo  # Actualizar el costo del nodo correspondiente

    inicio = matriz[inicio_x][inicio_y]  # Nodo de inicio
    inicio.costo = COSTO_POR_DEFECTO  # Establecer el costo del nodo inicial
    fin = matriz[fin_x][fin_y]  # Nodo final
    fin.costo = COSTO_POR_DEFECTO  # Establecer el costo del nodo final

    camino = a_estrella(matriz, inicio, fin)  # Ejecutar el algoritmo A*

    if camino:  # Si se encuentra un camino
        print("Camino encontrado:")  # Mensaje de éxito
        dibujar_matriz(matriz, camino, inicio, fin)  # Dibujar la matriz con el camino encontrado
    else:
        print("No se encontró un camino.")  # Mensaje de fallo

if __name__ == "__main__":
    main()  # Ejecutar la función principal
