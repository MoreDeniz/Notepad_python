from abc import ABC, abstractmethod

class Operation(ABC):
    def __init__(self, console):
        self.console = console

    @abstractmethod
    def description(self):
        ...
    @abstractmethod
    def run(self):
        ...