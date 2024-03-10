from abc import ABC, abstractmethod

class User(ABC):
    """Abstract base class for a generic user.

    Attributes:
        var_test (int): A class level variable for demonstration purposes.
    """
    
    var_test = 100

    @abstractmethod
    def login():
        """Abstract method to be implemented for user login functionality."""
        pass

    def non_abstract():
        """Example method that does nothing but is not abstract."""
        pass

    def non_abstract_implemented():
        """Example method that simply returns 0.

        Returns:
            int: Returns 0.
        """
        return 0

    @staticmethod
    def abstract_static_test():
        """Static method example that returns 1.

        Returns:
            int: Returns 1.
        """
        return 1

class Player(User):
    """Represents a player which is a type of User.

    Attributes:
        week_free_game (str): Class variable for the free game of the week.
        players (int): Class variable to keep track of the number of Player instances.
    """
    
    week_free_game = "Spiderman"
    players = 0

    def __init__(self, first_name, last_name, games):
        """Initializes a new Player instance with given first name, last name, and games.

        Args:
            first_name (str): The first name of the player.
            last_name (str): The last name of the player.
            games (iterable): An iterable of games owned by the player.
        """
        self.first_name = first_name
        self.last_name = last_name
        try:
            games.__iter__()
        except AttributeError:
            print('Iterable is expected as argument for "games" parameter')
            self.games = None
        else:
            self.games = list(games)

        self.email_ = first_name.lower() + "." + last_name.lower() + "@gmail.com"
        Player.players += 1

    @property
    def email(self):
        """str: The email address of the player."""
        return self.email_

    @email.setter
    def email(self, email):
        """Sets the player's email if it's valid.

        Args:
            email (str): The email address to set for the player.
        """
        if self.is_valid_email(email):
            self.email_ = email
        else:
            print("Given email was not valid")

    def login(self):
        """Simulates the player logging in."""
        print("Logging in...")

    def full_name(self) -> str:
        """Generates the full name of the player.

        Returns:
            str: The full name of the player.
        """
        return f"{self.first_name} {self.last_name}"

    def get_free_game(self):
        """Returns the current week's free game.

        Returns:
            str: The free game of the week.
        """
        return Player.week_free_game

    def player_info(self):
        """Prints information about the player."""
        print(f"First name: {self.first_name}")
        print(f"Second name: {self.last_name}")
        print("Games collection:")
        print("-------------------")
        for game in self.games:
            print(game)
        print("-------------------")

    @classmethod
    def add_free_game(cls, game):
        """Adds a game to the week's free game list.

        Args:
            game (str): The game to add to the free game list.
        """
        if isinstance(cls.week_free_game, str):
            cls.week_free_game = [cls.week_free_game, game]
        else:
            cls.week_free_game.append(game)

    @classmethod
    def parse_instance_string(cls, instance_string):
        """Creates a Player instance from a string representation.

        Args:
            instance_string (str): The string representation of the instance.

        Returns:
            Player: A new Player instance created from the string.
        """
        games_index = instance_string.index("[")
        first_name, last_name = instance_string[:games_index - 1].split(",")
        games = instance_string[games_index + 1:-1]
        return cls(first_name, last_name, games.split(","))

    @staticmethod
    def is_valid_email(email):
        """Validates an email address.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        if "@" in email and "." in email and email.count("@") == 1:
            domain = email.split('@')[1]
            return domain.endswith(('com', 'pl', 'de'))
        return False

    def __len__(self):
        """Determines the number of games the player owns.

        Returns:
            int: The number of games in the player's collection.
        """
        return len(self.games)



