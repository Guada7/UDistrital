"""
This module contains the class definitions and methods for managing an arcade machine system.

Author: Santiago Alejandro Guada Bohorquez <saguadab@udistrital.edu.co>

This file is part of ArcadeMachine-UD.

ArcadeMachine-UD is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

ArcadeMachine-UD is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with ArcadeMachine-UD. If not, see <https://www.gnu.org/licenses/>.
"""

import json
from datetime import datetime
import os


class User:
    """
    Class that represents a user.

    Attributes:
        id (int): Unique identifier of the user.
        name (str): User's name.
        phone (str): User's phone number.

    Methods:
        validate_name(name): Validates the user's name.
        validate_phone(phone): Validates the user's phone number.
    """

    def __init__(self, name, phone):
        self.id = None
        self.name = self.validate_name(name)
        self.phone = self.validate_phone(phone)

    def validate_name(self, name):
        """Validates the user's name.

        This method verifies that the name provided is a string containing only letters, including 
        spaces contains only letters, including spaces. Compound names such as “Jose Maria” are 
        considered valid.

        Args:
            name (str): The name to validate.

        Returns:
            str: The name validated if valid; otherwise, returns None and displays an error message.

        """
        if isinstance(name, str) and name.replace(" ", "").isalpha():
            return name
        print("Name must be a string containing only letters and spaces.")
        return None

    def validate_phone(self, phone):
        """Validates the user's phone number.

        This method verifies that the telephone number provided is a 
        string containing only digits and that its length does not 
        exceed 15 characters.

        Args:
            phone (str): The phone number to validate.

        Returns:
            str: The validated phone number if valid; otherwise, returns 
            None and displays an error message.
        
        Raises:
            ValueError: If the phone number is not a string or contains 
            non-numeric characters.

        """
        if isinstance(phone, str) and phone.isdigit() and len(phone) <= 15:
            return phone
        print("Phone number must be digits only with a maximum of 15 characters.")
        return None


class Game:
    """Class representing a game.

    Attributes:
        game_id (str): Identifier of the game.
        title (str): Game title.
        category (str): Game category.
        reviews (list): List of reviews of the game.

    Methods:
        add_review(user_id, review): Adds a review to the game.
        to_dict(): Converts the game information to a dictionary.
        save_games(games): Saves the list of games to a JSON file.
    """
    def __init__(self, game_id, title, category, reviews=None):
        self.game_id = game_id
        self.title = title
        self.category = category
        self.reviews = reviews if reviews is not None else []

    def add_review(self, user_id, review):
        """Add a review to the game.

        This method allows a user to add a review to the game, 
        associating the review with the ID of the user providing 
        the review.

        Args:
            user_id (str): The ID of the user leaving the review.
            review (str): The content of the review to be added.
        
        Returns:
            None.
        """
        self.reviews.append({"user_id": user_id, "review": review})

    def to_dict(self):
        """Converts game information to a dictionary.

        This method creates and returns a dictionary containing the 
        game attributes, including the game ID, title, category and 
        reviews.

        Returns:
            dict: A dictionary representing the game information.
        """
        return {
            "game_id": self.game_id,
            "title": self.title,
            "category": self.category,
            "reviews": self.reviews,
        }

    def save_games(self, games):
        """Saves the list of games in a JSON file.

        This method takes a list of game objects and serializes them 
        in JSON format, saving them in a file named 'games.json'.
        If an error occurs during the saving process, an error message 
        is printed.

        Args:
            games (list): list of Game objects to be saved.

        Returns:
            None
        
        Raises:
            IOError: If an error occurs when trying to write to the file.
        """
        try:
            with open("games.json", "w") as file:
                json.dump([game.to_dict() for game in games], file, indent=4)
        except Exception as e:
            print(f"Error saving games: {e}")


class ArcadeMachine:
    """Class representing an arcade machine.

    This class allows you to manage an arcade machine, including
    adding games and completing purchases. 

    Attributes:
        material (str): Material of the machine (e.g. wood, aluminum).
        color (str): Color of the machine.
        player_count (int): Number of players it can support.
        games (list): List of games that are available on the machine.

    Methods:
        add_game(game): Adds a game to the machine.
        finalize_purchase(user_id, address): Finalize the purchase of the machine.
    """
    def __init__(self, material, color, player_count):
        self.material = material
        self.color = color
        self.player_count = player_count
        self.games = []

    def add_game(self, game):
        """Add a game to the arcade machine.

        This method allows you to add a game object to the list of 
        games available in the arcade machine.

        Args:
            game (Game): The Game object to be added to the machine.

        Returns:
            None
        """
        self.games.append(game)

    def finalize_purchase(self, user_id, address):
        """Finalizes the purchase of the arcade machine.

        This method records the purchase of the arcade machine, 
        including user details and delivery address. Verifies 
        that at least one game has been added to the machine before 
        finalizing the purchase.

        Args:
            user_id (str): The ID of the user making the purchase.
            address (str): The delivery address of the machine.

        Returns:
            None

        Raises:
            ValueError: If no games have been added to the machine 
            prior to checkout finalizing the purchase.
        """
        if not self.games:
            print(
                "You must add at least one game to the machine before finalizing the purchase."
            )
            return

        purchase = {
            "user_id": user_id,
            "address": address,
            "machine": {
                "material": self.material,
                "color": self.color,
                "player_count": self.player_count,
                "games": [game.title for game in self.games],
            },
            "date": datetime.now().strftime("%Y-%m-%d"),
        }
        save_purchases(purchase)
        print(f"Purchase finalized for user {user_id}.")


def save_users(users):
    """Saves the list of users in a JSON file.

    This method takes a list of user objects and serializes them 
    in JSON format, saving them in a file named 'users.json'.
    If an error occurs during the saving process, an error message 
    is printed.

    Args:
        users (list): list of User objects to be saved.

    Returns:
        None

    Raises:
        IOError: If an error occurs when trying to write to the file.
    """
    try:
        with open("users.json", "w") as file:
            json.dump([user.__dict__ for user in users], file, indent=2)
    except Exception as e:
        print(f"Error saving users: {e}")


def save_purchases(purchase):
    """Stores a purchase in the purchases JSON file.

    This method takes a dictionary representing a purchase and adds 
    it to the 'purchases.json' file. If the file does not exist or is
    empty, a new list of purchases is created. If an error occurs
    occurs during the saving process, an error message is printed.

    Args:
        purchase (dict): dictionary representing a purchase.

    Returns:
        None

    Raises:
        IOError: If an error occurs when trying to write to the file.
    """
    try:
        if os.path.exists("purchases.json") and os.path.getsize("purchases.json") > 0:
            with open("purchases.json", "r") as file:
                purchases = json.load(file)
        else:
            purchases = []

        purchases.append(purchase)

        with open("purchases.json", "w") as file:
            json.dump(purchases, file, indent=4)
    except Exception as e:
        print(f"Error saving purchase: {e}")


def load_users():
    """Loads the list of users from a JSON file.

    This method attempts to read the file 'users.json' and deserializes 
    its contents into a list of User objects. If the file does not exist,
    an empty list is returned.

    Returns:
        list: List of User objects loaded from the file. If the
        file does not exist, an empty list is returned.

    Raises:
        FileNotFoundError: If the file 'users.json' is not found.
        Exception: If an error occurs when trying to read or deserialize the file.
    """
    try:
        with open("users.json", "r") as file:
            user_dicts = json.load(file)
            users = [
                User(user_dict["name"], user_dict["phone"]) for user_dict in user_dicts
            ]
            for i, user in enumerate(users):
                user.id = i + 1
            return users
    except FileNotFoundError:
        return []


def load_games():
    """Loads the list of games from a JSON file.

    This method attempts to read the file 'games.json' and deserializes 
    its contents into a list of Game objects. If the file does not exist
    or is empty, an empty list is returned.

    Returns:
        list: List of Game objects loaded from the file. If the
        file does not exist or is empty, an empty list is returned.

    Raises:
        FileNotFoundError: If the file 'games.json' is not found.
        Exception: If an error occurs when trying to read or deserialize the file.
    """
    try:
        with open("games.json", "r") as file:
            games_data = json.load(file)
            return [
                Game(
                    game["game_id"],
                    game["title"],
                    game["category"],
                    game.get("reviews", []),
                )
                for game in games_data
            ]
    except FileNotFoundError:
        print("games.json file not found. No games loaded.")
        return []
    except Exception as e:
        print(f"Error loading games: {e}")
        return []


def load_purchases():
    """Loads the shopping list from a JSON file.

    This method attempts to read the file 'purchases.json' and deserializes 
    its contents into a list of dictionaries representing purchases. 
    If the file does not exist, an empty list is returned.

    Returns:
        list: List of dictionaries representing purchases loaded from the file.
        If the file does not exist, returns an empty list.

    Raises:
        FileNotFoundError: If the file 'purchases.json' is not found.
        Exception: If an error occurs when trying to read or deserialize the file.
    """
    try:
        with open("purchases.json", "r") as file:
            purchases = json.load(file)
            return purchases
    except FileNotFoundError:
        return []
