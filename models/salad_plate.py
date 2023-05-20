import math
from abc import ABC

from models.plate import Plate


class SaladPlate(Plate, ABC):
    def __init__(self, diameter=None,
                 material=None,
                 color=None,
                 is_clean=None,
                 has_food=None,
                 shape=None,
                 dishwasher_safe=None):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.shape = shape
        self.dishwasher_safe = dishwasher_safe

    def getMaxFoodWeight(self):
        radius = self.diameter / 2
        return math.pi * radius * radius * radius / 3.0

    def __str__(self):
        return f"Diameter: {self.diameter}\n" \
               f"Material: {self.material}\n" \
               f"Color: {self.color}\n" \
               f"is_clean: {self.is_clean}\n" \
               f"has_food: {self.has_food}\n" \
               f"depth: {self.shape}\n" \
               f"soup_type: {self.dishwasher_safe}\n"


salad_plate = SaladPlate(8, "porcelain", "white", True, False, "round", True)
