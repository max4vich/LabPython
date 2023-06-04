"""
This module contains the PlateManager class which is used to manage a collection of Plate objects.
"""
from models.dessert_plate import DessertPlate
from models.dinner_plate import DinnerPlate
from models.salad_plate import SaladPlate
from models.soup_plate import SoupPlate


class PlateManager:
    """
    A class used to manage a collection of Plate objects.

    Attributes:
        plates (list): A list of Plate objects.
    """
    plates = []

    # pylint: disable = no-self-argument
    def print_arg_count(func):
        """
        A decorator that prints the number of arguments passed to a function before calling it.

        Args:
            func: The function to decorate.

        Returns:
            The decorated function.
        """
        def wrapper(*args, **kwargs):
            """
            The wrapper function that counts the number of
            arguments and prints the result before calling the
            original function.

            Args:
                *args: The positional arguments passed to the original function.
                **kwargs: The keyword arguments passed to the original function.

            Returns:
                The result of calling the original function with the given arguments.
            """
            arg_count = len(args) + len(kwargs)
            # pylint: disable = no-member
            print(f"{func.__name__} called with {arg_count} arguments")
            # pylint: disable = not-callable
            return func(*args, **kwargs)

        return wrapper

    def limit_calls(max_calls):
        """
        A decorator factory that creates a decorator
        that limits the number of times a function can be called.

        Args:
            max_calls: The maximum number of times the decorated function can be called.

        Returns:
            The decorator that limits the number of times a function can be called.
        """
        def decorator(func):
            """
            The decorator that limits the number of times a function can be called.

            Args:
                func: The function to decorate.

            Returns:
                The decorated function.
            """
            func.calls = 0

            def wrapper(*args, **kwargs):
                """
                The wrapper function that checks if the maximum number of
                calls has been reached and raises an exception if it has.
                Otherwise, it increments the call count and calls the original function.

                Args:
                    *args: The positional arguments passed to the original function.
                    **kwargs: The keyword arguments passed to the original function.

                Returns:
                    The result of calling the original function with the given arguments.

                Raises:
                    Exception: If the maximum number of calls has been reached.
                """

                if func.calls >= max_calls:
                    # pylint: disable = broad-exception-raised
                    raise Exception("too many calls")
                func.calls += 1
                return func(*args, **kwargs)

            return wrapper

        return decorator

    #@limit_calls(3)
    @print_arg_count
    def add_plate(self, plate):
        """
        Adds a Plate object to the plates list.

        Args:
            plate (Plate): The Plate object to be added.
        """
        self.plates.append(plate)

    # pylint: disable = too-many-function-args
    @limit_calls(3)
    @print_arg_count
    def find_all_plates_with_diameter_greater_than(self, diameter):
        """
        Finds all Plate objects in the plates list with a diameter greater than the specified value.

        Args:
            diameter (float): The diameter value to compare against.

        Returns:
            list: A list of Plate objects with a diameter greater than the specified value.
        """
        return list(filter(lambda plate: plate.diameter > diameter, self.plates))

    # pylint: disable = too-many-function-args
    @limit_calls(3)
    @print_arg_count
    def find_all_plates_made_from_glass(self):
        """
        Finds all Plate objects in the plates list made from glass.

        Returns:
            list: A list of Plate objects made from glass.
        """
        return list(filter(lambda plate: plate.material == "glass", self.plates))

    def __len__(self):
        """
        Returns the number of Plate objects in the plates list.

        Returns:
        int: The number of Plate objects in the plates list.
        """
        return len(self.plates)

    def __getitem__(self, index):
        """
        Returns the Plate object at the specified index in the plates list.

        Args:
        index (int): The index of the Plate object to return.

        Returns:
        Plate: The Plate object at the specified index in the plates list.
        """
        return self.plates[index]

    def __iter__(self):
        """
        Returns an iterator for the plates list.

        Returns:
        iterator: An iterator for the plates list.
        """
        return iter(self.plates)

    # pylint: disable = too-many-function-args
    @limit_calls(3)
    @print_arg_count
    def get_all_max_weight_food(self):
        """
        Returns a list of maximum food weights for all plates in the plates list.

        Returns:
        list: A list of maximum food weights for all plates in the plates list.
        """
        return [plate.get_max_food_weight() for plate in self.plates]

    # pylint: disable = too-many-function-args
    @limit_calls(3)
    @print_arg_count
    def zipped_list_with_objects(self):
        """
        Prints a zipped list containing tuples of (index, plate) for all plates in the plates list.

        Returns:
        None
        """
        enumerated = list(enumerate(self.plates))
        for plate in enumerated:
            print(f"{plate}")

    @limit_calls(3)
    @print_arg_count
    def zipped_list_with_all_max_weight_food(self):
        """
        Prints a zipped list containing tuples of (plate, max_food_weight)
        for all plates in the plates list.

        Returns:
        None
        """
        result = list(zip(self.plates, self.get_all_max_weight_food()))
        for plate in result:
            print(f"{str(plate)}")

    @limit_calls(3)
    @print_arg_count
    def get_plate_attributes_by_type(self, data_type):
        """
        Prints a dictionary containing attributes and
        their values for each plate in the plates list
        where attribute value type matches data_type.

        Args:
        data_type (type): The type to match attribute values against.

        Returns:
        None
        """
        for plate in self.plates:
            # pylint: disable = unidiomatic-typecheck
            plate_attributes = {key: value for key, value in plate.__dict__.items()
                                if type(value) == data_type}
            print(plate_attributes)

    # pylint: disable = too-many-function-args
    @limit_calls(3)
    @print_arg_count
    def check_all_any_of_plates(self, condition):
        """
        Checks if all or any of the plates in the plates list meet a specified condition.

        Args:
        condition (function): A function that takes a Plate object
        as input and returns a boolean value.

        Returns:
        dict: A dictionary containing two keys - "all" and "any" -
        with boolean values indicating if all or any of the plates meet
        the specified condition respectively.
        """
        all_result = all(condition(plate) for plate in self.plates)
        any_result = any(condition(plate) for plate in self.plates)
        return {"all": all_result, "any": any_result}


def main():
    """
    The main method of the PlateManager class.
    Demonstrates the usage of the class and its methods.
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

    for plate in manager.plates:
        print(str(plate))

    print("\nDef: find_all_plates_with_diameter_greater_than(10)\n")
    filtered_plates = manager.find_all_plates_with_diameter_greater_than(10)
    for plate in filtered_plates:
        print(str(plate))

    print("\nDef: find_all_plates_made_from_glass\n")
    filtered_plates = manager.find_all_plates_made_from_glass()
    for plate in filtered_plates:
        print(str(plate))
    # pylint: disable = unnecessary-dunder-call
    print(manager.__len__())
    # pylint: disable = unnecessary-dunder-call
    print(manager.__getitem__(2))

    print("1. Метод get_max_food_weight у List Comprehension: ")
    print(manager.get_all_max_weight_food())
    print()

    print("2. Метод склейки (порядковий номер і об'єкт): ")
    manager.zipped_list_with_objects()
    print()

    print("3. Метод склейки (об'єкт і метод get_max_food_weight): ")
    manager.zipped_list_with_all_max_weight_food()
    print()

    print("4. Метод using __dict__: ")
    manager.get_plate_attributes_by_type(int)
    print()

    print("5. Методи all() та any()")
    print(manager.check_all_any_of_plates(lambda plate: plate.diameter == 7))


if __name__ == "__main__":
    main()
