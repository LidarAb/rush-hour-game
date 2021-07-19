class Board:
    """
    This class can create board object with size 7X7.
    The purpose of the calls is to add cars to the board, and to move cars on
    the board according to constraints  (location, name, other cars locations).
    """
    BOARD_SIDE = 7
    END = (3, 7)

    def __init__(self):
        self.cars_in_board = {}

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        board_lst = [['_' for i in range(Board.BOARD_SIDE)] for j in
                     range(Board.BOARD_SIDE)]
        board_lst[3].append('E')
        for car in self.cars_in_board.values():
            car_name = car.get_name()
            for cord in car.car_coordinates():
                row = cord[0]
                col = cord[1]
                board_lst[row][col] = car_name
        board_str = ''
        for j in board_lst:
            line = ' '.join(j) + '\n'
            board_str += line
        return board_str

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cells = []
        for i in range(Board.BOARD_SIDE):
            for j in range(Board.BOARD_SIDE):
                cells.append((i, j))
        cells.append((3, 7))
        return cells

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        possible_moves = []
        for car in self.cars_in_board.values():
            for movekey in car.possible_moves():
                new_cord = car.movement_requirements(movekey)[0]
                if not self.cell_content(new_cord) and new_cord in \
                        self.cell_list():
                    possible_moves.append((car.get_name(), movekey,
                                           car.possible_moves()[movekey]))
        return possible_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be
        filled for victory.
        :return: (row,col) of goal location
        """
        return self.END

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        for car in self.cars_in_board.values():
            if coordinate in car.car_coordinates():
                return car.get_name()
        return None

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for cord in car.car_coordinates():
            if cord not in self.cell_list():
                return False
            if self.cell_content(cord):
                return False
            if car.get_name() in self.cars_in_board:
                return False
        self.cars_in_board[car.get_name()] = car
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for tup in self.possible_moves():
            if name in tup and movekey in tup:
                self.cars_in_board[name].move(movekey)
                return True
        return False

