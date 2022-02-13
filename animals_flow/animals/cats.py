from animals_flow.animals.base import Animal


class Cat(Animal):

    def __init__(self, name, color, breed, age):
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
    
    def __str__(self):
        return f'[{self.breed}] {self.name} <{self.age} age> color: {self.color}'

    def __repr__(self):
        return f"Cat('{self.name}', '{self.color}', '{self.breed}', '{self.age}')"

    def say(self):
        if self.breed == 'british':
            return f'{self} says MIAU!!!'

        return f'{self} says miau'
