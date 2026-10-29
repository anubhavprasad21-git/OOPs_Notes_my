from abc import ABC , abstractmethod

class omegle(ABC):
    @abstractmethod
    def clock(self):
        pass

class polo(omegle):
    def clock(self):
        pass

class bike(omegle):
    def clock(self):
        pass

obj=polo()
obj1=bike()