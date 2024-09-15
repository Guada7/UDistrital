"""
This module provides a simple command-line interface (CLI) for managing an arcade machine system.

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

from arcade_machine import (
    User,
    ArcadeMachine,
    Game,
    load_users,
    load_games,
    save_users,
    load_purchases,
)


def validate_name(name):
    """Validates the user's name.

    This method verifies that the name provided is a string
    containing only letters and spaces. Compound names such
    as “Jose Maria” are considered valid.

    Args:
        name (str): The name to validate.

    Returns:
        str: The name validated if valid; otherwise, returns
        None and displays an error message.

    Raises:
        ValueError: If the name is not a string or contains non-alphabetic characters.
    """
    return isinstance(name, str) and name.replace(" ", "").isalpha()


def validate_phone(phone):
    """Validates the user's phone number.

    This method verifies that the telephone number provided is a
    string containing only digits and that its length does not
    exceed 15 characters.

    Args:
        phone (str): The phone number to validate.

    Returns:
        str: The validated phone number if valid; otherwise,
        returns None and displays an error message.

    Raises:
        ValueError: If the phone number is not a string or contains
        non-numeric characters.
    """
    return isinstance(phone, str) and phone.isdigit() and len(phone) <= 15


def create_user(users):
    """Creates users and saves them in a JSON file.

    This method takes a list of User objects, creates the users
    and saves them in the file 'users.json'. If a user already exists,
    it is skipped and continues with the next user. If an
    error occurs during the saving process, an error message is printed.

    Args:
        users (list): list of User objects to be created.

    Returns:
        None

    Raises:
        IOError: If an error occurs when trying to write to the file.
    """
    while True:
        name = input("Enter your name: ")
        if validate_name(name):
            break
        else:
            print(
                "Name must be a string containing only letters and spaces. Please try again."
            )

    while True:
        phone = input("Enter your phone number: ")
        if validate_phone(phone):
            break
        else:
            print(
                "Phone number must be digits only with a maximum of 15 characters. Please try again."
            )

    user = User(name, phone)
    user.id = len(users) + 1
    users.append(user)
    print(f"User created with ID: {user.id}")
    save_users(users)


def show_available_games():
    """Displays available games and allows users to leave reviews.

    This method loads the list of games from the 'games.json' file,
    displays the details of each available game, and allows users to 
    leave reviews for the selected games. If there are no games available, 
    the user is informed.

    Returns:
        None

    Raises:
        Exception: if an error occurs when loading the games from the archive.
    """
    games = load_games()
    print("Available games:")
    if games:
        for game in games:
            print(f"- Code: {game.game_id}, Title: {game.title} ({game.category})")
            if game.reviews:
                print("   Reviews:")
                for review in game.reviews:
                    print(f"   - {review['review']} (User ID: {review['user_id']})")
            else:
                print("   No reviews available.")
            print("---")
    else:
        print("No games available.")

    while True:
        users = load_users()
        leave_review = input("Do you want to leave a review? (yes/no): ")
        if leave_review.lower() == "yes":
            user_id = input("Enter your user ID: ")

            if not any(user.id == int(user_id) for user in users):
                print("Invalid user ID. Please try again.")
                continue

            game_code = input("Enter the code of the game to review: ")

            game = next((g for g in games if g.game_id == game_code), None)
            if game:
                review = input("Enter your review: ")
                game.add_review(user_id, review)
                game.save_games(games)
                print("Review added successfully!")
            else:
                print("Invalid game code. Please try again.")
        elif leave_review.lower() == "no":
            break
        else:
            print("Invalid option. Please enter 'yes' or 'no'.")


def finalize_purchase(users):
    """Finalize the purchase of the arcade machine.

    This method allows a user to finalize the purchase of an arcade machine,
    including the user's details and delivery address. Verifies that at 
    least one game has been added to the machine before allowing the purchase 
    to be finalized.

    Args:
        users (list): list of User objects representing users.

    Returns:
        None

    Raises:
        ValueError: If no games have been added to the machine before the purchase is
        the purchase was completed.
    """
    user_id = input("Enter your user ID: ")

    if not any(user.id == int(user_id) for user in users):
        print("User ID does not exist. Please try again.")
        return

    address = input("Enter your delivery address: ")

    valid_materials = ["wood", "aluminum", "carbon fiber"]
    while True:
        material = input("Choose material (wood, aluminum, carbon fiber): ")
        if material in valid_materials:
            break
        else:
            print(
                "Invalid material. Please choose one of the following: wood, aluminum, carbon fiber."
            )

    color = input("Choose color: ")

    while True:
        player_count = input("Choose number of players (1 or 2): ")
        if player_count in ["1", "2"]:
            player_count = int(player_count)
            break
        else:
            print("Invalid number of players. Please choose either 1 or 2.")

    machine = ArcadeMachine(material, color, player_count)

    while True:
        game_code = input(
            "Enter the code of the game to add (or type 'done' to finish): "
        )
        if game_code.lower() == "done":
            break

        games = load_games()
        game = next((g for g in games if g.game_id == game_code), None)
        if game:
            machine.add_game(Game(game.game_id, game.title, game.category))
            print(f"Added {game.title} to the machine.")
        else:
            print("Game code not found. Please try again.")

    machine.finalize_purchase(user_id, address)


def show_user_purchases():
    """Displays purchases made by a specific user.

    This method allows the user to enter their ID and, if valid,
    displays a list of all purchases he/she has made. If the user has
    user has no registered purchases, the user is informed.

    Returns:
        None

    Raises:
        Exception: if an error occurs when loading purchases from file.
    """
    user_id = input("Enter your user ID to view your purchases: ")
    purchases = load_purchases()
    user_purchases = [p for p in purchases if p["user_id"] == user_id]

    if user_purchases:
        for purchase in user_purchases:
            print(f"Purchase ID: {purchase['user_id']}")
            print(f"Address: {purchase['address']}")
            print(f"Machine Material: {purchase['machine']['material']}")
            print(f"Machine Color: {purchase['machine']['color']}")
            print(f"Machine Player Count: {purchase['machine']['player_count']}")
            print(f"Machine Games: {', '.join(purchase['machine']['games'])}")
            print(f"Date: {purchase['date']}")
            print("---")
    else:
        print(f"No purchases found for user with ID {user_id}.")


def main():
    """Main function that executes the command line interface.

    This method provides an interactive menu that allows users 
    to perform various actions, such as creating a new user, 
    displaying available games, finalizing purchases and displaying 
    user purchases.The function will continue to run until the user 
    decides to exit.

    Returns:
        None

    Raises:
        Exception: If an error occurs in the execution of any of the menu operations.
    """
    users = load_users()

    print("Welcome to the Arcade Machine Catalog!")

    while True:
        print("\nMenu:")
        print("1. Create User")
        print("2. Show Available Games")
        print("3. Finalize Purchase")
        print("4. Show User Purchases")
        print("5. Exit")

        choice = input("Select an option (1-5): ")
        if choice == "1":
            create_user(users)
        elif choice == "2":
            show_available_games()
        elif choice == "3":
            finalize_purchase(users)
        elif choice == "4":
            show_user_purchases()
        elif choice == "5":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
