class Control:
    tv = None
    
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


    def enlazar(self, tv):
        tv.setControl(self)

    def getTv(self):
        return self.tv
    
    def setTv(self, tv) -> None:
        self.tv = tv
