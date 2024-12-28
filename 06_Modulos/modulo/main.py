from dinamic import Dinamic

def main():
    file_path = "../C60.xyz"  # Reemplaza con la ruta correcta al archivo C60.xyz
    index1 = 4  # Índice del primer átomo (5 en términos humanos)
    index2 = 41  # Índice del segundo átomo (42 en términos humanos)

    din = Dinamic()
    din.loadxyz(file_path)
    distance = din.get_distance(index1, index2)

    print(f"La distancia entre los átomos 5 y 42 es: {distance}")

if __name__ == "__main__":
    main()
