import math
from abc import ABC

from models.plate import Plate


class SaladPlate(Plate, ABC):
    """
    A class used to represent a Salad Plate.

    Attributes:
        shape (str): The shape of the salad plate.
        dishwasher_safe (bool): Indicates whether the plate is dishwasher safe or not.

    Methods:
        getMaxFoodWeight(): Returns the maximum weight of food that the plate can hold.
    """
    def __init__(self, diameter=None,
                 material=None,
                 color=None,
                 is_clean=None,
                 has_food=None,
                 shape=None,
                 dishwasher_safe=None):
        """
        Initializes a new SaladPlate object.

        Args:
            diameter (float or None): The diameter of the plate.
            material (str or None): The material used to make the plate.
            color (str or None): The color of the plate.
            is_clean (bool or None): Indicates whether the plate is clean or not.
            has_food (bool or None): Indicates whether the plate has food or not.
            shape (str or None): The shape of the salad plate.
            dishwasher_safe (bool or None): Indicates whether the plate is dishwasher safe or not.
        """
        super().__init__(diameter, material, color, is_clean, has_food)
        self.shape = shape
        self.dishwasher_safe = dishwasher_safe

    def getMaxFoodWeight(self):
        """
        Returns the maximum weight of food that the plate can hold.

        Returns:
            float: The maximum weight of food that the plate can hold.
        """
        radius = self.diameter / 2
        return math.pi * radius * radius * radius / 3.0

    def __str__(self):
        """
        Returns a string representation of the SaladPlate object.

        Returns:
            str: A string representation of the SaladPlate object.
        """
        return f"Diameter: {self.diameter}\n" \
               f"Material: {self.material}\n" \
               f"Color: {self.color}\n" \
               f"is_clean: {self.is_clean}\n" \
               f"has_food: {self.has_food}\n" \
               f"depth: {self.shape}\n" \
               f"soup_type: {self.dishwasher_safe}\n"


salad_plate = SaladPlate(8, "porcelain", "white", True, False, "round", True)
