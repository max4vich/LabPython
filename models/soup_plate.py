# pylint: disable = duplicate-code
"""
This module contains the SoupPlate class which is used to represent a Soup Plate.
"""
import math
from abc import ABC

from models.plate import Plate


class SoupPlate(Plate, ABC):
    """
    A class used to represent a Soup Plate.

    Attributes:
        depth (float): The depth of the soup plate.
        soup_type (str): The type of soup the plate is intended for.

    Methods:
        get_max_food_weight(): Returns the maximum weight of food that the plate can hold.
    """

    # pylint: disable = too-many-arguments
    def __init__(self, diameter=None,
                 material=None,
                 color=None,
                 is_clean=None,
                 has_food=None,
                 depth=None,
                 soup_type=None):
        """
        Initializes a new SoupPlate object.

        Args:
            diameter (float or None): The diameter of the plate.
            material (str or None): The material used to make the plate.
            color (str or None): The color of the plate.
            is_clean (bool or None): Indicates whether the plate is clean or not.
            has_food (bool or None): Indicates whether the plate has food or not.
            depth (float or None): The depth of the soup plate.
            soup_type (str or None): The type of soup the plate is intended for.
            typical_colors_set (set): Set of colors.
        """
        super().__init__(diameter, material, color, is_clean, has_food)
        self.depth = depth
        self.soup_type = soup_type
        self.typical_colors_set = {"yellow", "white"}

    def get_max_food_weight(self):
        """
        Returns the maximum weight of food that the plate can hold.

        Returns:
            float: The maximum weight of food that the plate can hold.
        """
        radius = self.diameter / 2
        return 0.5 * math.pi * radius * radius * self.depth

    def __str__(self):
        """
        Returns a string representation of the SoupPlate object.

        Returns:
            str: A string representation of the SoupPlate object.
        """
        # pylint: disable = duplicate-code
        return f"Diameter: {self.diameter} \n"\
               f"Material: {self.material} \n"\
               f"Color: {self.color} \n"\
               f"is_clean: {self.is_clean} \n"\
               f"has_food: {self.has_food} \n"\
               f"depth: {self.depth} \n"\
               f"soup_type: {self.soup_type} \n"
