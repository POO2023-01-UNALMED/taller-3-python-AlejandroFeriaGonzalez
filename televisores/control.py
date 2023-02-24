from tv import TV

class Control:
    tv:TV
    
    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()
    
    def canalUp(self):
        self.tv.canalUp()
    
    def canalDown(self):
        self.tv.canalDown()
    
    def volumenUp(self):
        self.tv.volumenUp()
    
    def volumenDown(self):
        self.tv.volumenDown()
    
    def setCanal(self, n:int):
        self.tv.setCanal(n)


    def enlazar(self, tv:TV):
        tv.setControl(self)

    def getTv(self) -> TV:
        return self.tv
    
    def setTv(self, tv:TV) -> None:
        self.tv = tv
