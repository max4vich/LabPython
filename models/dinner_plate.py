from abc import ABC

from models.plate import Plate


class DinnerPlate(Plate, ABC):
    """
    A class used to represent a Dinner Plate.

    Methods:
        getMaxFoodWeight(): An abstract method to be implemented by concrete dinner plate classes.
    """
    def getMaxFoodWeight(self):
        """
        Abstract method to be implemented by concrete dinner plate classes.

        Returns:
            float: The maximum weight of food that the plate can hold.
        """
        pass

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

