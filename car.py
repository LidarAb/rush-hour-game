class Car:
    """
    The class allows to create car objects, save their position coordinate
    and move them according to their orientation.
    """
    HORIZONTAL = 1
    VERTICAL = 0

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = int(length)
        self.location = location
        self.__orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coordinates = [self.location]
        if self.__orientation == Car.VERTICAL:
            for i in range(1, self.__length):
                coordinates.append((self.location[0] + i, self.location[1]))
        else:
            for i in range(1, self.__length):
                coordinates.append((self.location[0], self.location[1] + i))
        return coordinates

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements
        permitted by this car.
        """
        if self.__orientation == Car.VERTICAL:
            moves_dict = {'u': "cause the car move one step up",
                          'd': "cause the car move one step down"}
        else:
            moves_dict = {'r': "cause the car move one step right",
                          'l': "cause the car move one step left"}
        return moves_dict

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this
        move to be legal.
        """
        coordinates = self.car_coordinates()
        if movekey == 'u':
            return [(coordinates[0][0] - 1, coordinates[0][1])]
        elif movekey == 'd':
            return [(coordinates[-1][0] + 1, coordinates[-1][1])]
        elif movekey == 'r':
            return [(coordinates[-1][0], coordinates[-1][1] + 1)]
        elif movekey == 'l':
            return [(coordinates[0][0], coordinates[0][1] - 1)]

    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey not in self.possible_moves():
            return False

        new_cord = self.movement_requirements(movekey)[0]
        if movekey == 'd':
            new_cord = (new_cord[0] - self.__length + 1, new_cord[1])
        elif movekey == 'r':
            new_cord = (new_cord[0], new_cord[1] - self.__length + 1)

        self.location = new_cord
        return True

    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.__name
