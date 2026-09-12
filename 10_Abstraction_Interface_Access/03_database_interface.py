from abc import ABC,abstractmethod
class DB(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def disconnect(self): pass
class Oracle(DB):
    def connect(self): print("Connect Oracle")
    def disconnect(self): print("Disconnect Oracle")
x=Oracle(); x.connect(); x.disconnect()
