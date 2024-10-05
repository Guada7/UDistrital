"""
This module defines an abstract class `Game` and its concrete implementations: 
`StandardGame` and `HighDefinitionGame`. 

The `Game` class serves as a blueprint for creating different types of games, 
including methods for adding reviews, converting game data to dictionaries, 
and saving game data to JSON files.

Classes:
    - Game: An abstract base class for all games.
    - StandardGame: A concrete implementation of a standard game.
    - HighDefinitionGame: A concrete implementation of a high-definition game.

Usage:
    This module can be used to create game instances, manage reviews,
    and persist game data in JSON format.
"""
from abc import ABC, abstractmethod
import json

class Game(ABC):
    """Abstract class representing a game.

    This class defines the basic structure and methods that must be
    implemented by any type of game.
    """
    def __init__(self, game_id, title, category, price, storytelling_creator, graphics_creator, year):
        """
        Initializes a new game.

        Args:
            game_id (str): Unique identifier for the game.
            title (str): Title of the game.
            category (str): Category of the game (e.g., action, adventure).
            price (float): Price of the game.
            storytelling_creator (str): Creator of the game's storytelling.
            graphics_creator (str): Creator of the game's graphics.
            year (int): Release year of the game.
        """
        self.game_id = game_id
        self.title = title
        self.category = category
        self.price = price  # Precio del juego
        self.storytelling_creator = storytelling_creator  # Creador del storytelling
        self.graphics_creator = graphics_creator  # Creador de gráficos
        self.year = year  # Año de lanzamiento
        self.reviews = []  # Inicialmente sin reseñas

    @abstractmethod
    def add_review(self, user_id, review):
        """Abstract method to add a review to the game.

        Args:
            user_id (str): Identifier of the user adding the review.
            review (str): Content of the review.
        """
        pass

    @abstractmethod
    def to_dict(self):
        """Converts the game's information to a dictionary.

        Returns:
            dict: Dictionary representation of the game's properties.
        """
        pass

    @abstractmethod
    def save_games(self, games):
        """Saves the list of games to a JSON file.

        Args:
            games (list): List of game instances to save.
        """
        pass

    
    @staticmethod
    def load_games():
        """Loads the list of games from a JSON file.

        Returns:
            list: List of loaded games. If the file is not found,
                  returns an empty list.
        """
        try:
            with open("games.json", "r") as file:
                games_data = json.load(file)
                return games_data
        except FileNotFoundError:
            print("games.json file not found. No games loaded.")
            return []
        except Exception as e:
            print(f"Error loading games: {e}")
            return []

class StandardGame(Game):
    """Class representing a standard game."""

    def __init__(self, game_id, title, category, price, storytelling_creator, graphics_creator, 
                 year):
        """
        Initializes a new standard game.

        Args:
            game_id (str): Unique identifier for the game.
            title (str): Title of the game.
            category (str): Category of the game.
            price (float): Price of the game.
            storytelling_creator (str): Creator of storytelling.
            graphics_creator (str): Creator of graphics.
            year (int): Release year.
        """
        super().__init__(game_id, title, category, price, storytelling_creator, graphics_creator, year)

    def add_review(self, user_id, review):
        """Adds a review to the game.

        Args:
            user_id (str): Identifier of the user adding the review.
            review (str): Content of the review.
        """
        self.reviews.append({"user_id": user_id, "review": review})

    def to_dict(self):
        """Converts the game's information to a dictionary.

        Returns:
            dict: Dictionary representation of the standard game's properties.
        """
        return {
            "game_id": self.game_id,
            "title": self.title,
            "category": self.category,
            "price": self.price,
            "storytelling_creator": self.storytelling_creator,
            "graphics_creator": self.graphics_creator,
            "year": self.year,
            "reviews": self.reviews,
        }

    def save_games(self, games):
        """Saves the list of games to a JSON file.

        Args:
            games (list): List of game instances to save.

        Raises:
            Exception: If an error occurs while saving games to the JSON file.
        """
        try:
            with open("games.json", "w") as file:
                json.dump([game.to_dict() for game in games], file, indent=4)
        except Exception as e:
            print(f"Error saving games: {e}")

class HighDefinitionGame(Game):
    """Class representing a high-definition video game."""

    def __init__(self, game_id, title, category, price, storytelling_creator, graphics_creator, 
                 year):
        """
        Initializes a new high-definition video game.

        Args:
            game_id (str): Unique identifier for the game.
            title (str): Title of the game.
            category (str): Category of the game.
            price (float): Base price of the game. Increased by 10%.
            storytelling_creator (str): Creator of storytelling.
            graphics_creator (str): Creator of graphics.
            year (int): Release year.

        Note:
            The price is increased by 10% from the provided base price.
        """
        super().__init__(game_id, title, category, price * 1.10, storytelling_creator, 
                         graphics_creator, year)  # Aumenta el precio en un 10%

    def add_review(self, user_id, review):
        """Adds a review to the high-definition game.

        Args:
            user_id (str): Identifier of the user adding the review.
            review (str): Content of the review.
        """
        self.reviews.append({"user_id": user_id, "review": review})

    def to_dict(self):
        """Converts high-definition game's information to a dictionary.

        Returns:
            dict: Dictionary representation of high-definition game's properties.
        """
        return {
            "game_id": self.game_id,
            "title": self.title,
            "category": self.category,
            "price": self.price,
            "storytelling_creator": self.storytelling_creator,
            "graphics_creator": self.graphics_creator,
            "year": self.year,
            "reviews": self.reviews,
        }

    def save_games(self, games):
        """Saves the list of games to a JSON file.

       Args:
           games (list): List of game instances to save.

       Raises:
           Exception: If an error occurs while saving games to the JSON file.
       """
        try:
            with open("games.json", "w") as file:
                json.dump([game.to_dict() for game in games], file, indent=4)
        except Exception as e:
            print(f"Error saving games: {e}")