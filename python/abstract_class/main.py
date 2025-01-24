#! /usr/bin/env python3

from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def print_me(self):
        pass

    # Throws an error because is not implemented in the Child
    # @abstractmethod
    # def dont_implement_me(self):
    #     pass


class Child(Parent):
    def __init__(self, name):
        self.name = name

    def print_me(self):
        print(f"I am a child class, my name is {self.name}.")


c = Child("Charlinho")
c.print_me()
