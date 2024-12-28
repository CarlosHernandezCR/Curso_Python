from atom import Atom

class Step:
    def __init__(self):
        self.atoms = []  # Lista de átomos

    def add_atom(self, atom):
        self.atoms.append(atom)
