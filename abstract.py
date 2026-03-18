"""from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Brak")
d = Dog()
d.sound()"""
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def press(self):
        pass
class Bike(Vehicle):
    def press(self):
        print("Break")
d = Bike()
d.press()