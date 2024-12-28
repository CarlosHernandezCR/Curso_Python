class Atom:
    def __init__(self, Z, r):
        self.Z = Z  # Símbolo del elemento
        self.r = r  # Posición en forma de lista [x, y, z]

    def distancia(self, atomo2):
        return ((self.r[0] - atomo2.r[0])**2 + (self.r[1] - atomo2.r[1])**2 + (self.r[2] - atomo2.r[2])**2)**0.5
