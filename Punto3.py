class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f"({self.x}, {self.y})"

    def opuesto(self):
        return Punto(-self.x, -self.y)

    def mover(self, dx=0, dy=0):
        self.x += dx
        self.y += dy


class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, distancia):
        self._punto_a.mover(dx=distancia)
        self._punto_b.mover(dx=distancia)

    def mueve_izquierda(self, distancia):
        self._punto_a.mover(dx=-distancia)
        self._punto_b.mover(dx=-distancia)

    def mueve_arriba(self, distancia):
        self._punto_a.mover(dy=distancia)
        self._punto_b.mover(dy=distancia)

    def mueve_abajo(self, distancia):
        self._punto_a.mover(dy=-distancia)
        self._punto_b.mover(dy=-distancia)

    def impresion(self):
        return f"Línea de {self._punto_a.impresion()} a {self._punto_b.impresion()}"