"""
This module contains the DessertPlate class which is used to represent a Dessert Plate.
"""
from abc import ABC

from models.plate import Plate


class DessertPlate(Plate, ABC):
    """
    A class used to represent a Dessert Plate.

    Methods:
        get_max_food_weight(): An abstract method to be
        implemented by concrete dessert plate classes.
    """
    def get_max_food_weight(self):
        """
        Abstract method to be implemented by concrete dessert plate classes.
        """

    def __str__(self):
        """
        Returns a string representation of the DessertPlate object.

        Returns:
            str: A string representation of the DessertPlate object.
        """
        return f"Diameter: {self.diameter}\n" \
               f"Material: {self.material}\n" \
               f"Color: {self.color}\n" \
               f"is_clean: {self.is_clean}\n" \
               f"has_food: {self.has_food}\n"
