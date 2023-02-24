from marca import Marca
from control import Control


class TV:
    numTV = 0
    _canal = 1
    _precio = 500
    _volumen = 1
    _control: Control

    @classmethod
    def add1numTV(cls):
        cls.numTV += 1

    def __init__(self, marca: Marca, estado: bool) -> None:
        self._marca = marca
        self.estado = estado
        self.add1numTV()

    def setCanal(self, canal: int) -> None:
        self._canal = canal

    def setPrecio(self, precio: int) -> None:
        self._precio = precio

    def setVolumen(self, volumen: int) -> None:
        self._volumen = volumen

    def setControl(self, control: Control) -> None:
        self._control = control

    def setMarca(self, marca: Marca) -> None:
        self._marca = marca

    def getCanal(self) -> int:
        return self._canal

    def getPrecio(self) -> int:
        return self._precio

    def getVolumen(self) -> int:
        return self._volumen

    def getControl(self) -> Control:
        return self._control

    def getMarca(self) -> Marca:
        return self._marca

    @classmethod
    def setNumTV(cls, n: int) -> None:
        cls.numTV = n

    @classmethod
    def getNumTV(cls) -> int:
        return cls.numTV

    def getEstado(self) -> bool:
        return self.estado
    # fin gets and sets

    # * cambiar de encendido a apagado (estado)
    def turnOn(self) -> None:
        self.estado = True

    def turnOff(self) -> None:
        self.estado = False

    # * cambio de canal
    def canalUp(self) -> None:
        if (self._canal+1 in range(1, 121) and self.estado == True):
            self._canal += 1

    def canalDown(self) -> None:
        if (self._canal-1 in range(1, 121) and self.estado == True):
            self._canal -= 1

    # * cambio de volumen
    def volumenUp(self) -> None:
        if (self._volumen+1 in range(0,8) and self.estado == True):
            self._volumen += 1
    
    def volumenDown(self) -> None:
        if (self._volumen-1 in range(0,8) and self.estado == True):
            self._volumen -= 1
