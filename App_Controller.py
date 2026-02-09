from FantasyGame import FantasyGame,Pawn,Dragon,Troll,Centaur,Minotaur,Warlock,Unicorn,Fay,Player

class GameSession:
    """
    Creates a game instance that acts as a go-between for the UI and game logic
    """
    def __init__(self):
        self._game = FantasyGame()
        self._PlayerOne = Player(...)
        self._PlayerTwo = Player(...)

        self._game.add_player(self._PlayerOne)
        self._game.add_player(self._PlayerTwo)

    def autoset(self):
        # Resets game in case autoset pressed twice
        self._game = FantasyGame()
        self._PlayerOne = Player(...)
        self._PlayerTwo = Player(...)
        self._game.add_player(self._PlayerOne)
        self._game.add_player(self._PlayerTwo)

        #Creates pawns and assigns pawn_names
        Dragon_One = Dragon("Dragon_One")
        Troll_One = Troll("Troll_One")
        Centaur_One = Centaur("Centaur_One")
        Minotaur_One = Minotaur("Minotaur_One")
        Warlock_One = Warlock("Warlock_One")
        Unicorn_One = Unicorn("Unicorn_One")
        Fay_One = Fay("Fay_One")

        #Adds pawns to player
        self._PlayerOne.add_pawn(Dragon_One)
        self._PlayerOne.add_pawn(Troll_One)
        self._PlayerOne.add_pawn(Centaur_One)
        self._PlayerOne.add_pawn(Minotaur_One)
        self._PlayerOne.add_pawn(Warlock_One)
        self._PlayerOne.add_pawn(Unicorn_One)
        self._PlayerOne.add_pawn(Fay_One)

        #Positions pawns on board
        self._game.set_up_game('A1',Dragon_One)
        self._game.set_up_game('A2',Troll_One)
        self._game.set_up_game('A3',Centaur_One)
        self._game.set_up_game('A4',Minotaur_One)
        self._game.set_up_game('A5',Warlock_One)
        self._game.set_up_game('A6',Unicorn_One)
        self._game.set_up_game('A7',Fay_One)

        Dragon_Two = Dragon("Dragon_Two")
        Troll_Two = Troll("Troll_Two")
        Centaur_Two = Centaur("Centaur_Two")
        Minotaur_Two = Minotaur("Minotaur_Two")
        Warlock_Two = Warlock("Warlock_Two")
        Unicorn_Two = Unicorn("Unicorn_Two")
        Fay_Two = Fay("Fay_Two")

        self._PlayerTwo.add_pawn(Dragon_Two)
        self._PlayerTwo.add_pawn(Troll_Two)
        self._PlayerTwo.add_pawn(Centaur_Two)
        self._PlayerTwo.add_pawn(Minotaur_Two)
        self._PlayerTwo.add_pawn(Warlock_Two)
        self._PlayerTwo.add_pawn(Unicorn_Two)
        self._PlayerTwo.add_pawn(Fay_Two)

        self._game.set_up_game('G1',Dragon_Two)
        self._game.set_up_game('G2',Troll_Two)
        self._game.set_up_game('G3',Centaur_Two)
        self._game.set_up_game('G4',Minotaur_Two)
        self._game.set_up_game('G5',Warlock_Two)
        self._game.set_up_game('G6',Unicorn_Two)
        self._game.set_up_game('G7',Fay_Two)

        #Creates dict to return to UI with placement as key and pawn name as value
        pawn_dict = {}
        for pawn in self._PlayerOne.get_pawn_list():
            pawn_dict[pawn.get_location()] = pawn.get_pawn_name()
        for pawn in self._PlayerTwo.get_pawn_list():
            pawn_dict[pawn.get_location()] = pawn.get_pawn_name()

        return pawn_dict