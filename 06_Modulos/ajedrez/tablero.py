from ficha import Ficha
from PIL import Image

class Tablero:
    def __init__(self, inicio):
        # Create the list of piece objects
        self.posfichas = []
        
        # Map the board coordinates to pixel positions
        # This mapping assumes each square is 60x60 pixels
        # Update these values based on the actual size of your squares
        columnas = {'a': 0, 'b': 45, 'c': 90, 'd': 135, 'e': 180, 'f': 225, 'g': 270, 'h': 315}
        filas = {'1': 315, '2': 270, '3': 225, '4': 180, '5': 135, '6': 90, '7': 45, '8': 0}

        for posicion in inicio:
            # Extract the piece type and board position
            pieza, posicion_tablero = posicion.split('_')
            columna, fila = posicion_tablero
            
            # Map the board position to pixel coordinates
            x = columnas[columna]
            y = filas[fila]

            # Create a Ficha object and add it to the list
            imagen = f'{pieza}.png'  # Construct the image file name
            self.posfichas.append(Ficha(x, y, imagen))

    def pintar_tablero(self):
        # Carga el fondo del tablero
        tablero_img = Image.open('images/tablero.png').convert("RGBA")

        # Itera sobre cada pieza y la pinta en el tablero si es visible
        for ficha in self.posfichas:
            if ficha.visible:
                # Carga la imagen de la ficha y la coloca en su posición
                aux_img = Image.open(ficha.image_location()).convert("RGBA")
                tablero_img.alpha_composite(aux_img, (ficha.X, ficha.Y))

        # Guarda la imagen del tablero con las piezas
        tablero_img.save("jugada.png")

    def cambiar_posicion_ficha(self, posicion_actual, nueva_posicion):
        # Map the board coordinates to pixel positions
        columnas = {'a': 0, 'b': 45, 'c': 90, 'd': 135, 'e': 180, 'f': 225, 'g': 270, 'h': 315}
        filas = {'1': 315, '2': 270, '3': 225, '4': 180, '5': 135, '6': 90, '7': 45, '8': 0}

        # Extract piece type and current board position
        pieza_actual, posicion_tablero_actual = posicion_actual.split('_')
        columna_actual, fila_actual = posicion_tablero_actual

        # Extract new board position
        _, posicion_tablero_nueva = nueva_posicion.split('_')
        columna_nueva, fila_nueva = posicion_tablero_nueva

        # Convert board positions to pixel positions
        x_actual = columnas[columna_actual]
        y_actual = filas[fila_actual]
        x_nueva = columnas[columna_nueva]
        y_nueva = filas[fila_nueva]

        # Find the piece object and update its position
        for ficha in self.posfichas:
            if ficha.X == x_actual and ficha.Y == y_actual and ficha.imagen.startswith(pieza_actual):
                ficha.X = x_nueva
                ficha.Y = y_nueva
                break
        else:
            print(f"No se encontró la ficha en la posición {posicion_actual}")

    def comer_ficha(self, posicion_actual, nueva_posicion):
        # Mapear coordenadas del tablero a posiciones de píxeles
        columnas = {'a': 0, 'b': 45, 'c': 90, 'd': 135, 'e': 180, 'f': 225, 'g': 270, 'h': 315}
        filas = {'1': 315, '2': 270, '3': 225, '4': 180, '5': 135, '6': 90, '7': 45, '8': 0}

        # Extraer tipo de pieza y posición actual en el tablero
        pieza_actual, posicion_tablero_actual = posicion_actual.split('_')
        columna_actual, fila_actual = posicion_tablero_actual

        # Extraer nueva posición en el tablero
        _, posicion_tablero_nueva = nueva_posicion.split('_')
        columna_nueva, fila_nueva = posicion_tablero_nueva

        # Convertir posiciones del tablero a posiciones en píxeles
        x_actual = columnas[columna_actual]
        y_actual = filas[fila_actual]
        x_nueva = columnas[columna_nueva]
        y_nueva = filas[fila_nueva]

        # Encontrar y mover la pieza
        ficha_a_mover = None
        for ficha in self.posfichas:
            if ficha.X == x_actual and ficha.Y == y_actual and ficha.imagen.startswith(pieza_actual):
                ficha_a_mover = ficha
                break

        if ficha_a_mover:
            # Quitar la ficha que está en la nueva posición
            self.posfichas = [ficha for ficha in self.posfichas if not (ficha.X == x_nueva and ficha.Y == y_nueva)]

            # Mover la pieza a la nueva posición
            ficha_a_mover.X = x_nueva
            ficha_a_mover.Y = y_nueva
        else:
            print(f"No se encontró la ficha en la posición {posicion_actual}")