from step import Step
from atom import Atom

class Dinamic:
    def __init__(self):
        self.steps = []  # Lista de pasos

    def loadxyz(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            step = Step()
            for line in lines[2:]:  # Saltar las dos primeras líneas
                parts = line.split()
                if len(parts) == 4:  # Asegurarse de que la línea tenga 4 partes (elemento y coordenadas)
                    atom = Atom(parts[0], [float(parts[1]), float(parts[2]), float(parts[3])])
                    step.add_atom(atom)
            self.steps.append(step)

    def get_distance(self, index1, index2):
        # Asumiendo que solo hay un paso
        step = self.steps[0]
        return step.atoms[index1].distancia(step.atoms[index2])
