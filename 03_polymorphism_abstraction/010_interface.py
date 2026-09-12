from abc import ABC,abstractmethod
class DBInterface(ABC):
    @abstractmethod
    def connect(self): pass
    @abstractmethod
    def disconnect(self): pass
class Oracle(DBInterface):
    def connect(self): print("Connecting")
    def disconnect(self): print("Disconnecting")
db=Oracle(); db.connect(); db.disconnect()
