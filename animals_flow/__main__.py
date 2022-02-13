from animals_flow.animals.base import Animal
from animals_flow.animals.cats import Cat
from animals_flow.animals.dogs import Dog


def main():
    zoo: list[Animal] = [
        Cat(name='Vasya', color='gray', breed='british', age=15),
        Cat(name='Murka', color='black', breed='siberian', age=22),
        Dog('Bobik'),
    ]

    for animal in zoo:
        print(animal.say())


if __name__ == '__main__':
    main()
