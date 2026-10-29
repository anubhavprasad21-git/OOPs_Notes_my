from abc import ABC , abstractmethod

class omegle(ABC):
    @abstractmethod
    def clock(self):
        pass

class polo(omegle):
    pass

class bike(omegle):
    pass

obj=polo()
obj1=bike()
        
