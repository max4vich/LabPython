"""
This module contains the DinnerPlate class which is used to represent a Dinner Plate.
"""
from abc import ABC

from models.plate import Plate


class DinnerPlate(Plate, ABC):
    """
    A class used to represent a Dinner Plate.

    Methods:
        get_max_food_weight(): An abstract method to
        be implemented by concrete dinner plate classes.
    """

    # pylint: disable = too-many-arguments
    def __init__(self, diameter, material, color, is_clean, has_food):
        """
        Initializes a new SaladPlate object.

        Args:
            diameter (float or None): The diameter of the plate.
            material (str or None): The material used to make the plate.
            color (str or None): The color of the plate.
            is_clean (bool or None): Indicates whether the plate is clean or not.
            has_food (bool or None): Indicates whether the plate has food or not.
            typical_colors_set (set): Set of colors.
        """
        super().__init__(diameter, material, color, is_clean, has_food)
        self.typical_colors_set = {"red", "black"}

    def get_max_food_weight(self):
        """
        Abstract method to be implemented by concrete dinner plate classes.

        Returns:
            float: The maximum weight of food that the plate can hold.
        """

    def __str__(self):
        """
        Returns a string representation of the DinnerPlate object.

        Returns:
            str: A string representation of the DinnerPlate object.
        """
        return f"Diameter: {self.diameter}\n" \
               f"Material: {self.material}\n" \
               f"Color: {self.color}\n" \
               f"is_clean: {self.is_clean}\n" \
               f"has_food: {self.has_food}\n"
