# pylint: disable = duplicate-code
"""
That module contains the DessertPlate class which is used to represent a Dessert Plate.
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
    # pylint: disable = too-many-arguments
    def __init__(self, diameter, material, color, is_clean, has_food):
        """
        Initializes a new SoupPlate object.

        Args:
            diameter (float or None): The diameter of the plate.
            material (str or None): The material used to make the plate.
            color (str or None): The color of the plate.
            is_clean (bool or None): Indicates whether the plate is clean or not.
            has_food (bool or None): Indicates whether the plate has food or not.
            typical_colors_set (set): Set of colors.
        """
        super().__init__(diameter, material, color, is_clean, has_food)
        self.typical_colors_set = {"blue", "aqua"}

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
