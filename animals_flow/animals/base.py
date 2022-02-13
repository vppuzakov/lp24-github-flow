from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def say(self):
        raise NotImplementedError
