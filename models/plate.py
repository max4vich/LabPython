from abc import ABC, abstractmethod


class Plate(ABC):
    def __init__(self, diameter=None,
                 material=None,
                 color=None,
                 is_clean=None,
                 has_food=None):
        self.diameter = diameter
        self.material = material
        self.color = color
        self.is_clean = is_clean
        self.has_food = has_food

    @abstractmethod
    def getMaxFoodWeight(self):
        pass
