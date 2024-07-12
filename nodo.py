class Nodo:
    def __init__(self, x, y, costo):
        self.x = x  # Coordenada x del nodo
        self.y = y  # Coordenada y del nodo
        self.costo = costo  # Costo para moverse a este nodo
        self.g = float('inf')  # Coste desde el inicio hasta este nodo
        self.h = 0  # Coste estimado desde este nodo hasta el final (heurística)
        self.f = float('inf')  # Coste total (g + h)
        self.padre = None  # Nodo padre para reconstruir el camino

    def __lt__(self, otro):
        return self.f < otro.f  # Comparación basada en el costo total f
