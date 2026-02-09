# Anthony Martino
# GitHub username: Antjaze-dotcom
# Date: 5/28/2025
# Description: A board game program where there are two players with simular pieces with speciifc move sets available to each and where the object is to capture their opponent's Warlock (Cuddlefish) pawn.


class FantasyGame:
    """
    Represents a board game object by game_state, turn_status, and board_array (Parent class of the entire project.
    This is the parent class of the project and provides the foundational framework for the game and its most basic operations.
    Contains a player list to keep track of who is playing the game and whose turn it is as well as a list of dictionaries to
    display the game board and assign pawn locations to specific 'keys'.
    """
    def __init__(self):
        self._game_state = "UNFINISHED"
        self._player_list = []
        self._turn_status = None
        self._board_array = [{'A1': '', 'A2': '', 'A3': '', 'A4': '', 'A5': '', 'A6': '', 'A7': ''},
                            {'B1': '', 'B2': '', 'B3': '', 'B4': '', 'B5': '', 'B6': '', 'B7': ''},
                            {'C1': '', 'C2': '', 'C3': '', 'C4': '', 'C5': '', 'C6': '', 'C7': ''},
                            {'D1': '', 'D2': '', 'D3': '', 'D4': '', 'D5': '', 'D6': '', 'D7': ''},
                            {'E1': '', 'E2': '', 'E3': '', 'E4': '', 'E5': '', 'E6': '', 'E7': ''},
                            {'F1': '', 'F2': '', 'F3': '', 'F4': '', 'F5': '', 'F6': '', 'F7': ''},
                            {'G1': '', 'G2': '', 'G3': '', 'G4': '', 'G5': '', 'G6': '', 'G7': ''}]

        print("\nWelcome to Wrathful Warlocks! If this is your first playthrough,\n"
              "feel free to explore the game rules by inputting: unique_game_name.how_to_play\n"
              "\nTo start playing, initialize Player One and Two with a unique user name: player_one = Player('Tangerine')\n"
              "Now, start initializing a total of 7 pawns per player, including a single Warlock each, and give them their own unique names: dragon_one = Dragon('dragon_one')\n"
              "\nNOTE: It is recomended that your pawn names be the same as your pawn instance variables for simplicity.\n"
              "\nThen, add your pawns to your player instance: player_one.add_pawn(dragon_one)\n"
              "and add your player to the game instance: unique_game_name.add_player(player_one)\n"
              )

    def how_to_play(self):
        """
        Returns a string explaining the rules of the game
        """
        print("\nEstimated Play Time:\n"
              "5-10 minutes\n"
              "\nNumber of Players:\n"
              "2\n"
              "\nObjective:\n"
              "To capture the opposing player's Warlock.\n"
              "\nHow to Play:\n"
              "\n 1. Each player selects 7 pawns to command into battle (Dragon, Minotaur, Centaur, Troll, Unicorn, Fay, and a Warlock\n"
              "\n 2. Each pawn has a unique movement type that dictates how they can manuever the battlefield. Some pawns move diagonally like the Unicorn, while others move orthogonally\n    (up/down/left/right) like the Dragon. However, a pawn can always move one space contrary to their movement type.\n"
              "\n 3. Simularly, each pawn also has a unique traversal method, either sliding or jumping\n"
              "        Sliding: This means the pawn can move any nonzero number of spaces up to its max distance so long as it is not blocked by the battlefield's edge or another pawn.\n"
              "        Jumping: This means the pawn must move their max distance but cannot be blocked by another pawn along their route.\n"
              "\n 4. If a pawn lands or slides into an enemy pawn, that pawn is captured and removed from the battlefield. The first to capture the enemy's Warlock wins the game.\n"
              "\n Below are some reference methods that can be called by either player during their turn:\n"
              "\n get_movement_guide - provides a description of the called pawn's movement and traversal type as well as their distance range."
              "\n     Example: print(Warlock.get_movement_guide(Warlock_Two)\n"
              "\n get_board_array - provides a visual overview of the battlefield including pawn placements and their 'Alive' status"
              "\n     Example: print(game_instance_name.get_board_array()) ")
        return

    def set_game_state(self, new_state):
        """
        Sets up game status (EX: 'UNFINISHED', 'TANGERINE_WON', 'AMETHYST_WON')
        """
        self._game_state = new_state

    def get_game_state(self):
        """
        returns current status of game as described in set_game_state
        """
        return self._game_state

    def set_turn_status(self, next_player = 1):
        """
        Sets whosever turn it is in game (EX: 'TANGERINE_TURN', 'AMETHYST_TURN')
        """
        if self._player_list == []:
            return "There are no players in game yet."
        if self._player_list != [] and self._turn_status != self._player_list[0]:
            self._turn_status = self._player_list[0]
        else:
            self._turn_status = self._player_list[next_player]

    def get_turn_status(self):
        """
        returns whosever turn it is in game
        """
        return self._turn_status

    def get_board_array(self):
        """
        Returns gameboard in a grid using a list of dictionaries from A1-G7
        """
        print("\nState of the Battle:\n________________________________________\n")
        for row in self._board_array:
            print(row,"\n")
        return

    def set_up_game(self, location, pawn_obj):
        """
        Sets up pawns on the gameboard. Should only be used before play has begun, then use only make_move.
        :param location: coordinate on board_array where you wish to place pawn
        :param pawn_name: The name of pawn object you wish to place
        """
        for dict in self._board_array:
            if location in dict:
                if dict[location] != '':
                    return "Space taken. Please enter an empty coordinate from A1 - G7"
                if dict[location] == '':
                    dict[location] = pawn_obj
                    pawn_obj.set_location(location)
                else:
                    return "Invalid location. Please enter a coordinate from A1 - G7"

    def add_player(self, player_object_ID):
        """
        Adds a player to player_list through which turns alternate
        :param player_object_ID: The name from which player wishes to be identified over course of game
         """
        if player_object_ID in self._player_list:
            return "Player already in game."
        else:
            self._player_list.append(player_object_ID)
            if len(self._player_list) == 2:
                print("Your almost ready! Now simply place your pawns on the board.\n"
                  "\nBe sure to set your pawns in ONLY the first (A1-A7) and last (G1-G7) columns\n"
                  "of the board: unique_game_name.set_up_game('A1',Dragon_One)\n"
                  "\nOnce both players have 7 pawns, all that's left to do is start playing!\n"
                  "Start by making a move: print(unique_game_name.make_move('A1','D1')\n"
                  "\nRemember, first to capture their opponent's Warlock wins!\n")

    def get_player_list(self):
        """
        Returns the list of added players in game
        """
        return self._player_list

    def make_move(self, location, destination):
        """
        A method that allows the player whose turn it is to move their selected piece to a chosen destination
        so long as that move is considered 'legal' per the game piece class specifications
        :param location: the current location of the game piece
        :param destination: Where the player wishes to move the game piece on the board
        :result: Can return FALSE if invalid input is submitted
        """
        if self.get_game_state() != 'UNFINISHED':
            return "The battle has already concluded commander...\n"

        if self._turn_status == None: # This ensures the turn status is properly set up at first turn
            self.set_turn_status()

        loc_dict = None # dictionary where location key is found
        dest_dict = None # dictionary where destination key is found

        for dict in self._board_array: # This section of code checks to make sure the location inputted is in range of board and has a pawn.
            if location in dict:
                loc_dict = dict
            if destination in dict:
                dest_dict = dict
        if loc_dict is None or dest_dict is None:
            return "Cowards! thou's forces attempt to flee the battlefield!\n"
        if loc_dict[location] == '':
            return 'Tis no force to command at this location...\n'

        if loc_dict[location] != '': # If location chosen contains a pawn, we validate that the pawn belongs to the player whose turn it is.                        pawn = dict[location]
            pawn = loc_dict[location]
            player = self.get_turn_status()
            player_pawns = player.get_pawn_list()
            if pawn not in player_pawns:
                return "The enemy's forces ignore thy commands...\n"

        if pawn.check_legality(location, destination, self._board_array) == False:  # Next, we call check_legailty on the variable 'pawn' to ensure the move from 'location' to 'destination' is legal.
            return 'Apologies commander, but such a move is impossible...\n'
        if pawn.check_legality(location, destination, self._board_array) == True:

            if dest_dict[destination] == '': # Now we check if the destination is occupied. If not, we move pawn to 'destination' and change turn status
                loc_dict[location] = ''
                dest_dict[destination] = pawn
                self.set_turn_status()
                pawn.set_location(dest_dict[destination]) # NEED TO BE FIXED!!!!!!!!!
                return 'Thy warrior is in position...\n'

            if dest_dict[destination] != '': # if so, we check if player already has a pawn at destination. If not, player captures enemy pawn and we change turn status
                mystery_pawn = dest_dict[destination]
                if mystery_pawn in player_pawns:
                    return "Thou would attack thy own warriors? Have mercy commander!\n"
                else:
                    enemy_pawn = mystery_pawn
                    enemy_pawn.set_alive_status('DEAD')
                    loc_dict[location] = ''
                    dest_dict[destination] = pawn
                    pawn.set_location(dest_dict[destination])
                    if isinstance(enemy_pawn,Warlock): # This only occurs if the pawn captured is a Warlock
                        self.set_game_state(f"{player} _WON")
                        self.set_turn_status()
                        return f"A commander tis captured! The fair forces of {player} have proven superior!\n"
                    else:
                        return 'Thy warrior has defeated an enemy!\n'




#_____________________________________________________________________________________________________________________________

class Pawn:
    """
     Represents pawn objects that inherit from the FantasyGame and are uniquely represented by its alive_status
     This class inherits from the FantasyGame class but is also the parent class to all 'game piece' classes (i.e. Dragon, troll, etc.)
     It provides the basic framework for how each subsequent game piece class can interact within the FantasyGame class.
    """
    def __init__(self, alive_status, location, move_type, move_direction, move_range, pawn_name, game_state, turn_status):
        self._alive_status = alive_status
        self._location = location
        self._move_type = move_type
        self._move_direction = move_direction
        self._move_range = move_range
        self._pawn_name = pawn_name
        self._game_state = game_state
        self._turn_status = turn_status

    def get_pawn_name(self):
        return self._pawn_name

    def set_alive_status(self, new_alive_status):
        """
        Sets whether the game piece is still active on game board or not ('ALIVE' = active, 'DEAD' = inactive)
        """
        self._alive_status = new_alive_status

    def get_alive_status(self):
        """
        Returns alive status of pawn
        """
        return self._alive_status

    def get_location(self):
        """
        Returns location of pawn object for player
        """
        return self._location

    def set_location(self, new_location):
        """
        updates location of pawn on board
        """
        self._location = new_location

    def get_movement_guide(self):
        """
        Returns a list containing pawn's move_direction, move_type, and move_range
        """
        return [self._move_direction, self._move_type, self._move_range]

#_____________________________________________________________________________________________________________________________

class Dragon(Pawn):
    """
    Represents a Dragon pawn object for the FantasyGame represented uniquely in that its
    move_direction = 'JUMPING', move_type = 'ORTHOGONAL' and move_range = 3
    """
    def __init__(self,pawn_name):
        super().__init__('ALIVE', 'NONE', 'JUMPING', 'ORTHOGONAL', 3, pawn_name, 'ONGOING', 'PLAYER_ONE')


    def check_legality(self, location, destination, board):
        """
        :param location: current placement of the Dragon pawn being moved
        :param destination: intended placement of the Dragon pawn being moved
        :param board: The game board being used to make these moves (provided by make_move)
        :return:
        """
        x_coordinate_translator = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6} # Used to translate coordinates like 'A1' to indexing coordinates for board
        y_coordinate_translator = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

        loc_x_coord = 0 #Iniitialzie all coordinate variables to zero
        loc_y_coord = 0
        dest_x_coord = 0
        dest_y_coord = 0

        loc_x_coord = x_coordinate_translator[location[0]] #Takes the first letter in location string and converts it to index coordinate
        loc_y_coord = y_coordinate_translator[location[1]]
        dest_x_coord = x_coordinate_translator[destination[0]]
        dest_y_coord = y_coordinate_translator[destination[1]]

        distance = self.get_movement_guide() # Initializes the range of the pawn
        distance = distance[2]

        if abs(loc_x_coord - dest_x_coord) == distance and abs(loc_y_coord - dest_y_coord) == 0:# Tests that destination is a true jump from x coordinate in an orthogonal direction from
            return True

        if abs(loc_y_coord - dest_y_coord) == distance and abs(loc_x_coord - dest_x_coord) == 0: # Tests that destination is a true jump from y coordinate in an orthogonal direction
            return True

        if abs(loc_x_coord - dest_x_coord) == 1 and abs(loc_y_coord - dest_y_coord) == 1: # Tests if pawn is moving diagonally by one which is valid
            return True

       # if (loc_x_coord - dest_x_coord) < distance or (loc_y_coord - dest_y_coord) < distance: # If distance between location and destination is below jumping range, we test if going any further would put pawn out of bounds. If so, move is legal
       #     if (dest_x_coord + 1) > 7 or (dest_x_coord - 1) < 0 or (dest_y_coord + 1) > 7 or (dest_y_coord - 1) < 0:
       #         return True

        else:
            return False

    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Dragon(" + repr(self._alive_status) + ")"

#_____________________________________________________________________________________________________________________________

class Troll(Pawn):
    """
    Represents a Troll pawn object for the FantasyGame represented uniquely in that its
    move_direction = 'ORTHOGONAL', move_type = 'SLIDING' and move_range = 1
    """
    def __init__(self,pawn_name):
        super().__init__('ALIVE', 'NONE', 'SLIDING', 'ORTHOGONAL', 1 ,pawn_name, 'ONGOING','PLAYER_ONE')


    def check_legality(self, location, destination, board):
        """
        :param location: current placement of the Dragon pawn being moved
        :param destination: intended placement of the Dragon pawn being moved
        :param board: The game board being used to make these moves (provided by make_move)
        :return:
        """
        x_coordinate_translator = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6} # Used to translate coordinates like 'A1' to indexing coordinates for board
        y_coordinate_translator = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

        loc_x_coord = 0 #Iniitialzie all coordinate variables to zero
        loc_y_coord = 0
        dest_x_coord = 0
        dest_y_coord = 0

        loc_x_coord = x_coordinate_translator[location[0]] #Takes the first letter in location string and converts it to index coordinate
        loc_y_coord = y_coordinate_translator[location[1]]
        dest_x_coord = x_coordinate_translator[destination[0]]
        dest_y_coord = y_coordinate_translator[destination[1]]

        distance = self.get_movement_guide() # Initializes the range of the pawn
        distance = distance[2]

        if abs(loc_x_coord - dest_x_coord) == distance and abs(loc_y_coord - dest_y_coord) == 0:  # Tests that destination is a true slide from x coordinate to one space in an orthogonal direction
            return True

        if abs(loc_y_coord - dest_y_coord) == distance and abs(loc_x_coord - dest_x_coord) == 0:  # Tests that destination is a true slide from y coordinate in an orthogonal direction
            return True

        if abs(loc_x_coord - dest_x_coord) == 1 and abs(loc_y_coord - dest_y_coord) == 1:  # Tests if pawn is moving diagonally by one which is valid
            return True

        else:
            return False

    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Troll(" + repr(self._alive_status) + ")"

#_____________________________________________________________________________________________________________________________

class Centaur(Pawn):
    """
    Represents a Centaur pawn object for the FantasyGame represented uniquely in that its
    move_direction = 'ORTHOGONAL', move_type = 'SLIDING' and move_range = 3
    """
    def __init__(self,pawn_name):
        super().__init__('ALIVE', 'NONE', 'SLIDING', 'ORTHOGONAL', 3, pawn_name, 'ONGOING','PLAYER_ONE')


    def check_legality(self, location, destination, board):
        """
        :param location: current placement of the Dragon pawn being moved
        :param destination: intended placement of the Dragon pawn being moved
        :param board: The game board being used to make these moves (provided by make_move)
        :return:
        """
        x_coordinate_translator = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6} # Used to translate coordinates like 'A1' to indexing coordinates for board
        y_coordinate_translator = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

        loc_x_coord = 0 #Iniitialzie all coordinate variables to zero
        loc_y_coord = 0
        dest_x_coord = 0
        dest_y_coord = 0

        loc_x_coord = x_coordinate_translator[location[0]] #Takes the first letter in location string and converts it to index coordinate
        loc_y_coord = y_coordinate_translator[location[1]]
        dest_x_coord = x_coordinate_translator[destination[0]]
        dest_y_coord = y_coordinate_translator[destination[1]]

        distance = self.get_movement_guide() # Initializes the range of the pawn
        distance = distance[2]

        if abs(loc_y_coord - dest_y_coord) <= distance and abs(loc_x_coord - dest_x_coord) == 0: # Tests that destination is a true slide along y_axis

            moves = abs(dest_y_coord - loc_y_coord)  # num of spaces between y coordinates
            letter_coord = location[0]  # represents the x axis of location coordinate
            number_coord = int(location[1])  # represents the y axis of location coordinate converted to an int to allow for increment/decrement

            if (loc_y_coord - dest_y_coord) > 0: #Would mean we're moving up y axis to destination
                while moves > 0:
                   new_location = letter_coord + str(number_coord - 1) # do this to check the next space to ensure it is empty. Convert int back to str so board_array can read it
                   if board[loc_x_coord][new_location] == '':
                       moves -= 1
                       number_coord = int(new_location[1])
                   else:
                       return False
                return True

            if (loc_y_coord - dest_y_coord) < 0:  # Would mean we're moving down y axis to destination
                while moves > 0:
                    new_location = letter_coord + str(number_coord + 1)  # do this to check the next space to ensure it is empty. Convert int back to str so board_array can read it
                    if board[loc_x_coord][new_location] == '':
                        moves -= 1
                        number_coord = int(new_location[1])
                    else:
                        return False
                return True

        if abs(loc_x_coord - dest_x_coord) <= distance and abs(loc_y_coord - dest_y_coord) == 0:  # Tests that destination is a true slide along x_axis

            moves = abs(dest_x_coord - loc_x_coord)  # num of spaces between x coordinates
            letter_coord = location[0]  # represents the x axis of location coordinate
            number_coord = int(location[1])  # represents the y axis of location coordinate converted to an int to allow for increment/decrement

            if (loc_x_coord - dest_x_coord) < 0:  # Would mean we're moving left on y axis to destination
                while moves > 0:
                    new_location = chr(ord(letter_coord)+1) + str(number_coord)    # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivilent and add, then back again.(a to b)
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                            else:
                                return False
                return True

            if (loc_x_coord - dest_x_coord) > 0:  # Would mean we're moving right on the y axis to destination
                while moves > 0:
                    new_location = chr(ord(letter_coord) - 1) + str(number_coord)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivilent and subtract, then back again.(b to a)
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                            else:
                                return False
                return True

        if abs(loc_x_coord - dest_x_coord) == 1 and abs(loc_y_coord - dest_y_coord) == 1:  # Tests if pawn is moving diagonally by one which is valid
            return True
        else:
            return False

    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Centaur(" + repr(self._alive_status) + ")"

#_____________________________________________________________________________________________________________________________

class Minotaur(Pawn):
    """
    Represents a Minotuar pawn object for the FantasyGame represented uniquely in that its
     move_direction = 'ORTHOGONAL', move_type = 'JUMPING' and move_range = 2
    """
    def __init__(self,pawn_name):
        super().__init__('ALIVE', 'NONE', 'JUMPING', 'ORTHOGONAL', 2, pawn_name, 'ONGOING','PLAYER_ONE')

    def check_legality(self, location, destination, board):
        """
        :param location: current placement of the Dragon pawn being moved
        :param destination: intended placement of the Dragon pawn being moved
        :param board: The game board being used to make these moves (provided by make_move)
        :return:
        """
        x_coordinate_translator = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6} # Used to translate coordinates like 'A1' to indexing coordinates for board
        y_coordinate_translator = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

        loc_x_coord = 0 #Iniitialzie all coordinate variables to zero
        loc_y_coord = 0
        dest_x_coord = 0
        dest_y_coord = 0

        loc_x_coord = x_coordinate_translator[location[0]] #Takes the first letter in location string and converts it to index coordinate
        loc_y_coord = y_coordinate_translator[location[1]]
        dest_x_coord = x_coordinate_translator[destination[0]]
        dest_y_coord = y_coordinate_translator[destination[1]]

        distance = self.get_movement_guide() # Initializes the range of the pawn
        distance = distance[2]

        if abs(loc_x_coord - dest_x_coord) == distance and abs(
                loc_y_coord - dest_y_coord) == 0:  # Tests that destination is a true jump from x coordinate in an orthogonal direction from
            return True

        if abs(loc_y_coord - dest_y_coord) == distance and abs(
                loc_x_coord - dest_x_coord) == 0:  # Tests that destination is a true jump from y coordinate in an orthogonal direction
            return True

        if abs(loc_x_coord - dest_x_coord) == 1 and abs(
                loc_y_coord - dest_y_coord) == 1:  # Tests if pawn is moving diagonally by one which is valid
            return True

        else:
            return False

    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Minotaur(" + repr(self._alive_status) + ")"

#_____________________________________________________________________________________________________________________________

class Warlock(Pawn):
    """
    Represents a Warlock pawn object for the FantasyGame represented uniquely in that its
    move_direction = 'DIAGONAL', move_type = 'SLIDING' and move_range = 2
    (If this pawn's alive_status is 'DEAD' game ends)
    """
    def __init__(self,pawn_name):
        super().__init__('ALIVE', 'NONE', 'SLIDING', 'DIAGONAL', 2, pawn_name, 'ONGOING','PLAYER_ONE')

    def check_legality(self, location, destination, board):
        """
        :param location: current placement of the Dragon pawn being moved
        :param destination: intended placement of the Dragon pawn being moved
        :param board: The game board being used to make these moves (provided by make_move)
        :return:
        """
        x_coordinate_translator = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6} # Used to translate coordinates like 'A1' to indexing coordinates for board
        y_coordinate_translator = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

        loc_x_coord = 0 #Iniitialzie all coordinate variables to zero
        loc_y_coord = 0
        dest_x_coord = 0
        dest_y_coord = 0

        loc_x_coord = x_coordinate_translator[location[0]] #Takes the first letter in location string and converts it to index coordinate
        loc_y_coord = y_coordinate_translator[location[1]]
        dest_x_coord = x_coordinate_translator[destination[0]]
        dest_y_coord = y_coordinate_translator[destination[1]]

        distance = self.get_movement_guide() # Initializes the range of the pawn
        distance = distance[2]

        if abs(loc_y_coord - dest_y_coord) == 1 and abs(loc_x_coord - dest_x_coord) == 0:  # Tests that destination is a true slide by one along y_axis which is allowed
            return True

        if abs(loc_x_coord - dest_x_coord) == 1 and abs(loc_y_coord - dest_y_coord) == 0:  # Tests that destination is a true slide by one along x_axis which is allowed
            return True

        if abs(loc_x_coord - dest_x_coord) == abs(loc_y_coord - dest_y_coord) <= distance:  # Tests if pawn is moving diagonally

            moves = abs(dest_y_coord - loc_y_coord)
            letter_coord = location[0]  # represents the x axis of location coordinate
            number_coord = int(location[1])  # represents the y axis of location coordinate converted to an int to allow for increment/decrement

            if (loc_x_coord - dest_x_coord) <= 0 and (loc_y_coord - dest_y_coord) >= 0: # tests spaces moving diagonally up from left to right
               while moves > 0:
                   number_coord = int(number_coord) # because after each loop number_coord is turned into a string
                   new_location = chr(ord(letter_coord) + 1) + str(number_coord - 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent do necessary increment/ decrement, then back again
                   for dict in board:
                       if new_location in dict:
                           if dict[new_location] == '':
                               moves -= 1
                               letter_coord = new_location[0]
                               number_coord = new_location[1]
                           else:
                               return False
               return True


            if (loc_x_coord - dest_x_coord) >= 0 and (loc_y_coord - dest_y_coord) >= 0: # tests spaces moving diagonally up from right to left
                while moves > 0:
                    number_coord = int(number_coord)  # because after each loop number_coord is turned into a string
                    new_location = chr(ord(letter_coord) - 1) + str(number_coord - 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent do necessary increment/ decrement, then back again
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                                number_coord = new_location[1]
                            else:
                                return False
                return True

            if (loc_x_coord - dest_x_coord) <= 0 and (loc_y_coord - dest_y_coord) <= 0: # tests spaces moving diagonally down from left to right
                while moves > 0:
                    number_coord = int(number_coord)  # because after each loop number_coord is turned into a string
                    new_location = chr(ord(letter_coord) + 1) + str(number_coord + 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent do necessary increment/ decrement, then back again.
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                                number_coord = new_location[1]
                            else:
                                return False
                return True

            if (loc_x_coord - dest_x_coord) >= 0 and (loc_y_coord - dest_y_coord) <= 0: # tests spaces moving diagonally down from right to left
                while moves > 0:
                    number_coord = int(number_coord)  # because after each loop number_coord is turned into a string
                    new_location = chr(ord(letter_coord) - 1) + str(number_coord + 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent, do necessary increment/ decrement, then back again.
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                                number_coord = new_location[1]
                            else:
                                return False
                return True
        return False


    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Warlock(" + repr(self._alive_status) + ")"

#_____________________________________________________________________________________________________________________________

class Unicorn(Pawn):
    """
    Represents a Unicorn pawn object for the FantasyGame represented uniquely in that its
    move_direction = 'DIAGONAL', move_type = 'SLIDING' and move_range = 3
    """
    def __init__(self,pawn_name):
        super().__init__('ALIVE', 'NONE', 'SLIDING', 'DIAGONAL', 3, pawn_name, 'ONGOING','PLAYER_ONE')

    def check_legality(self, location, destination, board):
        """
        :param location: current placement of the Dragon pawn being moved
        :param destination: intended placement of the Dragon pawn being moved
        :param board: The game board being used to make these moves (provided by make_move)
        :return:
        """
        x_coordinate_translator = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6} # Used to translate coordinates like 'A1' to indexing coordinates for board
        y_coordinate_translator = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

        loc_x_coord = 0 #Iniitialzie all coordinate variables to zero
        loc_y_coord = 0
        dest_x_coord = 0
        dest_y_coord = 0

        loc_x_coord = x_coordinate_translator[location[0]] #Takes the first letter in location string and converts it to index coordinate
        loc_y_coord = y_coordinate_translator[location[1]]
        dest_x_coord = x_coordinate_translator[destination[0]]
        dest_y_coord = y_coordinate_translator[destination[1]]

        distance = self.get_movement_guide() # Initializes the range of the pawn
        distance = distance[2]

        if abs(loc_y_coord - dest_y_coord) == 1 and abs(loc_x_coord - dest_x_coord) == 0:  # Tests that destination is a true slide by one along y_axis which is allowed
            return True

        if abs(loc_x_coord - dest_x_coord) == 1 and abs(loc_y_coord - dest_y_coord) == 0:  # Tests that destination is a true slide by one along x_axis which is allowed
            return True

        if abs(loc_x_coord - dest_x_coord) == abs(loc_y_coord - dest_y_coord) <= distance:  # Tests if pawn is moving diagonally

            moves = abs(dest_y_coord - loc_y_coord)
            letter_coord = location[0]  # represents the x axis of location coordinate
            number_coord = int(location[1])  # represents the y axis of location coordinate converted to an int to allow for increment/decrement

            if (loc_x_coord - dest_x_coord) <= 0 and (loc_y_coord - dest_y_coord) >= 0: # tests spaces moving diagonally up from left to right
               while moves > 0:
                   number_coord = int(number_coord) # because after each loop number_coord is turned into a string
                   new_location = chr(ord(letter_coord) + 1) + str(number_coord - 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent do necessary increment/ decrement, then back again
                   for dict in board:
                       if new_location in dict:
                           if dict[new_location] == '':
                               moves -= 1
                               letter_coord = new_location[0]
                               number_coord = new_location[1]
                           else:
                               return False
               return True


            if (loc_x_coord - dest_x_coord) >= 0 and (loc_y_coord - dest_y_coord) >= 0: # tests spaces moving diagonally up from right to left
                while moves > 0:
                    number_coord = int(number_coord)  # because after each loop number_coord is turned into a string
                    new_location = chr(ord(letter_coord) - 1) + str(number_coord - 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent do necessary increment/ decrement, then back again
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                                number_coord = new_location[1]
                            else:
                                return False
                return True

            if (loc_x_coord - dest_x_coord) <= 0 and (loc_y_coord - dest_y_coord) <= 0: # tests spaces moving diagonally down from left to right
                while moves > 0:
                    number_coord = int(number_coord)  # because after each loop number_coord is turned into a string
                    new_location = chr(ord(letter_coord) + 1) + str(number_coord + 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent do necessary increment/ decrement, then back again.
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                                number_coord = new_location[1]
                            else:
                                return False
                return True

            if (loc_x_coord - dest_x_coord) >= 0 and (loc_y_coord - dest_y_coord) <= 0: # tests spaces moving diagonally down from right to left
                while moves > 0:
                    number_coord = int(number_coord)  # because after each loop number_coord is turned into a string
                    new_location = chr(ord(letter_coord) - 1) + str(number_coord + 1)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivalent, do necessary increment/ decrement, then back again.
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                                number_coord = new_location[1]
                            else:
                                return False
                return True
        return False

    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Unicorn(" + repr(self._alive_status) + ")"

#_____________________________________________________________________________________________________________________________

class Fay(Pawn):
    """
    Represents a Fay pawn object for the FantasyGame represented uniquely in that its
    move_direction = 'ORTHOGONAL', move_type = 'SLIDING' and move_range = 4
    """
    def __init__(self,pawn_name):
        super().__init__('ALIVE', 'NONE', 'SLIDING', 'ORTHOGONAL', 4, pawn_name, 'ONGOING','PLAYER_ONE')

    def check_legality(self, location, destination, board):
        """
        :param location: current placement of the Dragon pawn being moved
        :param destination: intended placement of the Dragon pawn being moved
        :param board: The game board being used to make these moves (provided by make_move)
        :return:
        """
        x_coordinate_translator = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6} # Used to translate coordinates like 'A1' to indexing coordinates for board
        y_coordinate_translator = {'1':0, '2':1, '3':2, '4':3, '5':4, '6':5, '7':6}

        loc_x_coord = 0 #Iniitialzie all coordinate variables to zero
        loc_y_coord = 0
        dest_x_coord = 0
        dest_y_coord = 0

        loc_x_coord = x_coordinate_translator[location[0]] #Takes the first letter in location string and converts it to index coordinate
        loc_y_coord = y_coordinate_translator[location[1]]
        dest_x_coord = x_coordinate_translator[destination[0]]
        dest_y_coord = y_coordinate_translator[destination[1]]

        distance = self.get_movement_guide() # Initializes the range of the pawn
        distance = distance[2]

        if abs(loc_y_coord - dest_y_coord) <= distance and abs(loc_x_coord - dest_x_coord) == 0: # Tests that destination is a true slide along y_axis

            moves = abs(dest_y_coord - loc_y_coord)  # num of spaces between y coordinates
            letter_coord = location[0]  # represents the x axis of location coordinate
            number_coord = int(location[1])  # represents the y axis of location coordinate converted to an int to allow for increment/decrement

            if (loc_y_coord - dest_y_coord) > 0: #Would mean we're moving up y axis to destination
                while moves > 0:
                   new_location = letter_coord + str(number_coord - 1) # do this to check the next space to ensure it is empty. Convert int back to str so board_array can read it
                   if board[loc_x_coord][new_location] == '':
                       moves -= 1
                       number_coord = int(new_location[1])
                   else:
                       return False
                return True

            if (loc_y_coord - dest_y_coord) < 0:  # Would mean we're moving down y axis to destination
                while moves > 0:
                    new_location = letter_coord + str(number_coord + 1)  # do this to check the next space to ensure it is empty. Convert int back to str so board_array can read it
                    if board[loc_x_coord][new_location] == '':
                        moves -= 1
                        number_coord = int(new_location[1])
                    else:
                        return False
                return True

        if abs(loc_x_coord - dest_x_coord) <= distance and abs(loc_y_coord - dest_y_coord) == 0:  # Tests that destination is a true slide along x_axis

            moves = abs(dest_x_coord - loc_x_coord)  # num of spaces between x coordinates
            letter_coord = location[0]  # represents the x axis of location coordinate
            number_coord = int(location[1])  # represents the y axis of location coordinate converted to an int to allow for increment/decrement

            if (loc_x_coord - dest_x_coord) < 0:  # Would mean we're moving left on y axis to destination
                while moves > 0:
                    new_location = chr(ord(letter_coord)+1) + str(number_coord)    # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivilent and add, then back again.(a to b)
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                            else:
                                return False
                return True

            if (loc_x_coord - dest_x_coord) > 0:  # Would mean we're moving right on the y axis to destination
                while moves > 0:
                    new_location = chr(ord(letter_coord) - 1) + str(number_coord)  # do this to check the next space to ensure it is empty. Convert string to ASCII numerical equivilent and subtract, then back again.(b to a)
                    for dict in board:
                        if new_location in dict:
                            if dict[new_location] == '':
                                moves -= 1
                                letter_coord = new_location[0]
                            else:
                                return False
                return True

        if abs(loc_x_coord - dest_x_coord) == 1 and abs(loc_y_coord - dest_y_coord) == 1:  # Tests if pawn is moving diagonally by one which is valid
            return True
        else:
            return False

    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Fay(" + repr(self._alive_status) + ")"

#_____________________________________________________________________________________________________________________________

class Player:
    """
    Represents a player object who is in charge of controlling pawns on their turn. Uniquely represented by player_ID.
    Inherits from only the FantasyGame class but can be assigned pawn objects through the pawn_list data attribute so that
    the player can use them to play the game.
    """

    def __init__(self, player_name):
        self._player_name = player_name
        self._pawn_list = []

    def add_pawn(self, pawn_name):
        """
        Adds a pawn to player's repetoire that they can use during course of game so long as alive_status is 'ALIVE'
        :param pawn_name: Name of the pawn class you wish to include
        """
        if pawn_name in self._pawn_list:
            return "Pawn already added."
        else:
            self._pawn_list.append(pawn_name)
            if len(self._pawn_list) == 1:
                print("")

    def get_pawn_list(self):
        """
        Returns player's list of pawns
        """
        return self._pawn_list

    def remove_pawn(self, pawn_name):
        """
        Removes a pawn from player's repetoire so that it cant be used during course of game. Ideally should only be used in event player pawn alive_status is 'DEAD'
        :param pawn_name: Name of pawn class you wish to remove
        :return: "Pawn not in list" if pawn is already not in pawn_list
        """
        if pawn_name not in self._pawn_list:
            return "Pawn not in list."
        else:
            index = self._pawn_list.index(pawn_name)
            del self._pawn_list[index]

    def __repr__(self):
        """Makes pawn object more readable when returned"""
        return "Player(" + repr(self._player_name) + ")"

#_____________________________________________________________________________________________________________________________

#Wrathful_Warlocks = FantasyGame()
#Wrathful_Warlocks.how_to_play()

#Player_One = Player('Tangerine')

#Dragon_One = Dragon("Dragon_One")
#Troll_One = Troll("Troll_One")
#Centaur_One = Centaur("Centaur_One")
#Minotaur_One = Minotaur("Minotaur_One")
#Warlock_One = Warlock("Warlock_One")
#Unicorn_One = Unicorn("Unicorn_One")
#Fay_One = Fay("Fay_One")

#Player_One.add_pawn(Dragon_One)
#Player_One.add_pawn(Troll_One)
#Player_One.add_pawn(Centaur_One)
#Player_One.add_pawn(Minotaur_One)
#Player_One.add_pawn(Warlock_One)
#Player_One.add_pawn(Unicorn_One)
#Player_One.add_pawn(Fay_One)

#Player_Two = Player('Amethyst')

#Dragon_Two = Dragon("Dragon_Two")
#Troll_Two = Troll("Troll_Two")
#Centaur_Two = Centaur("Centaur_Two")
#Minotaur_Two = Minotaur("Minotaur_Two")
#Warlock_Two = Warlock("Warlock_Two")
#Unicorn_Two = Unicorn("Unicorn_Two")
#Fay_Two = Fay("Fay_Two")

#Player_Two.add_pawn(Dragon_Two)
#Player_Two.add_pawn(Troll_Two)
#Player_Two.add_pawn(Centaur_Two)
#Player_Two.add_pawn(Minotaur_Two)
#Player_Two.add_pawn(Warlock_Two)
#Player_Two.add_pawn(Unicorn_Two)
#Player_Two.add_pawn(Fay_Two)

#Wrathful_Warlocks.add_player(Player_One)
#Wrathful_Warlocks.add_player(Player_Two)

#Wrathful_Warlocks.set_up_game('A1',Dragon_One)
#Wrathful_Warlocks.set_up_game('A2',Troll_One)
#Wrathful_Warlocks.set_up_game('A3',Centaur_One)
#Wrathful_Warlocks.set_up_game('A4',Minotaur_One)
#Wrathful_Warlocks.set_up_game('A5',Warlock_One)
#Wrathful_Warlocks.set_up_game('A6',Unicorn_One)
#Wrathful_Warlocks.set_up_game('A7',Fay_One)
#Wrathful_Warlocks.set_up_game('G1',Dragon_Two)
#Wrathful_Warlocks.set_up_game('G2',Troll_Two)
#Wrathful_Warlocks.set_up_game('G3',Centaur_Two)
#Wrathful_Warlocks.set_up_game('G4',Minotaur_Two)
#Wrathful_Warlocks.set_up_game('G5',Warlock_Two)
#Wrathful_Warlocks.set_up_game('G6',Unicorn_Two)
#Wrathful_Warlocks.set_up_game('G7',Fay_Two)

#Player One turn:
#print(Dragon.get_movement_guide(Dragon_One))
#print(Wrathful_Warlocks.make_move('A1','D1'))

#Player Two turn:
#print(Warlock.get_movement_guide(Warlock_Two))
#print(Wrathful_Warlocks.make_move('G5','E3'))

#Player One turn:
#print(Wrathful_Warlocks.get_board_array())
#print(Wrathful_Warlocks.make_move('G1','F2'))
#print(Wrathful_Warlocks.make_move('D1','D4'))

#Player Two turn:
#print(Wrathful_Warlocks.make_move('G4','G3'))
#print(Wrathful_Warlocks.make_move('G4','G2'))
#print(Minotaur.get_movement_guide(Minotaur_Two))
#print(Wrathful_Warlocks.make_move('G4','E4'))

#Player One turn
#print(Wrathful_Warlocks.make_move('D4','E3'))

#Player Two turn:
#print(Wrathful_Warlocks.make_move('G1','F2'))


