"""
Plate - parent class
"""
from abc import ABC, abstractmethod

from exceptions.exceptions import ColorError
from exceptions.logging import logged


# pylint: disable = too-few-public-methods
class Plate(ABC):
    """
    A class used to represent a Plate.

    Attributes:
    diameter (float or None): The diameter of the plate.
    material (str or None): The material used to make the plate.
    color (str or None): The color of the plate.
    is_clean (bool or None): Indicates whether the plate is clean or not.
    has_food (bool or None): Indicates whether the plate has food or not.
    """
    # pylint: disable = too-many-arguments
    @logged(ColorError, mode="file")
    def __init__(self, diameter=None,
                 material=None,
                 color=None,
                 is_clean=None,
                 has_food=None):
        """
        Initializes a new Plate object.

        Args:
            diameter (float or None): The diameter of the plate.
            material (str or None): The material used to make the plate.
            color (str or None): The color of the plate.
            is_clean (bool or None): Indicates whether the plate is clean or not.
            has_food (bool or None): Indicates whether the plate has food or not.
            typical_colors_set (set): Set of colors for subclasses
        """
        self.diameter = diameter
        self.material = material
        if isinstance(color, str):
            self.color = color
        else:
            raise ColorError(color)
        self.is_clean = is_clean
        self.has_food = has_food
        self.typical_colors_set = set()

    @abstractmethod
    def get_max_food_weight(self):
        """
        Abstract method to be implemented by concrete plate classes.

        Returns:
            float: The maximum weight of food that the plate can hold.
        """

    def __iter__(self):
        return iter(self.typical_colors_set)
