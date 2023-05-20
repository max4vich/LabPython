from abc import ABC

from models.plate import Plate


class DessertPlate(Plate, ABC):
    """
    A class used to represent a Dessert Plate.

    Methods:
        getMaxFoodWeight(): An abstract method to be implemented by concrete dessert plate classes.
    """
    def getMaxFoodWeight(self):
        """
        Abstract method to be implemented by concrete dessert plate classes.

        Returns:
            float: The maximum weight of food that the plate can hold.
        """
        pass

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

