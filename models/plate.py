from abc import ABC, abstractmethod

"""
Plate - parent class
"""


class Plate(ABC):
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
        """
        self.diameter = diameter
        self.material = material
        self.color = color
        self.is_clean = is_clean
        self.has_food = has_food

    @abstractmethod
    def getMaxFoodWeight(self):
        pass
        """
        Abstract method to be implemented by concrete plate classes.
    
        Returns:
            float: The maximum weight of food that the plate can hold.
        """