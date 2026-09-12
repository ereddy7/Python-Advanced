class Test:
    x=10; _y=20; __z=30
    def show(self): print(self.x,self._y,self.__z)
t=Test(); t.show(); print(t.x,t._y,t._Test__z)
