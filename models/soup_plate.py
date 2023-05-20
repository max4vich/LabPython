import math
from abc import ABC

from models.plate import Plate


class SoupPlate(Plate, ABC):
    def __init__(self, diameter=None,
                 material=None,
                 color=None,
                 is_clean=None,
                 has_food=None,
                 depth=None,
                 soup_type=None):
        super().__init__(diameter, material, color, is_clean, has_food)
        self.depth = depth
        self.soup_type = soup_type

    def getMaxFoodWeight(self):
        radius = self.diameter / 2;
        return 0.5 * math.pi * radius * radius * self.depth;

    def __str__(self):
        return f"Diameter: {self.diameter}\n" \
               f"Material: {self.material}\n" \
               f"Color: {self.color}\n" \
               f"is_clean: {self.is_clean}\n" \
               f"has_food: {self.has_food}\n" \
               f"depth: {self.depth}\n" \
               f"soup_type: {self.soup_type}\n"


soup_plate = SoupPlate(10, "ceramic", "white", True, False, 5, "Tomato Soup")
