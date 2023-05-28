# pylint: disable = duplicate-code
"""
This module contains the SetManager class which is used for settings.
"""
from managers.plate_manager import PlateManager
from models.soup_plate import SoupPlate
from models.salad_plate import SaladPlate
from models.dinner_plate import DinnerPlate
from models.dessert_plate import DessertPlate


class SetManager:
    """
    The SetManager class manages a set of plates.
    """

    def __init__(self, plate_manager):
        """
        Initializes a SetManager object with a PlateManager object.
        """
        self.plates = plate_manager
        self.index = 0
        self.set_data = []
        for plate in self.plates:
            for color in plate:
                self.set_data.append(color)

    def __iter__(self):
        """
        Returns an iterator for the SetManager object.
        """
        return self

    def __next__(self):
        """
        Returns the next color in the set of plates.
        """
        if self.index >= len(self):
            raise StopIteration
        result = self.set_data[self.index]
        self.index += 1
        return result

    def __len__(self):
        """
        Returns the number of colors in the set of plates.
        """
        return len(self.set_data)

    def __getitem__(self, index):
        """
        Returns the color at the specified index in the set of plates.
        """
        return self.set_data[index]


def main():
    """
    Creates a PlateManager object and adds plates to it.
    Then creates a SetManager object with the PlateManager
    object and prints the colors in the set of plates.
    """
    manager = PlateManager()

    manager.add_plate(SaladPlate(8, "porcelain", "white", True, False, "round", True))
    manager.add_plate(SaladPlate(9, "glass", "black", True, True, "oval", False))

    manager.add_plate(SoupPlate(12, "glass", "white", True, False, 5, "Tomato Soup"))
    manager.add_plate(SoupPlate(10, "ceramic", "green", True, False, 5, "Tomato Soup"))

    manager.add_plate(DinnerPlate(11, "porcelain", "pink", True, False))
    manager.add_plate(DinnerPlate(9, "glass", "black", True, True))

    manager.add_plate(DessertPlate(6, "porcelain", "pink", False, False))
    manager.add_plate(DessertPlate(7, "ceramic", "white", False, True))

    set_manager = SetManager(manager)

    print(len(set_manager))
    for color in set_manager:
        print(color)


if __name__ == "__main__":
    main()
