from animals_flow.animals.base import Animal

class Dog(Animal):
    
    def __init__(self, name):
        self.name = name

    def say(self):
        return f'dog {self.name} bark'
