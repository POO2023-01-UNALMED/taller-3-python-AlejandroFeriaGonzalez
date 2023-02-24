class Marca:
    """docstring for Marca."""
    def __init__(self, nombre:str):
        super(Marca, self).__init__()
        self._nombre:str = nombre
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre:str):
        self._nombre = nombre
