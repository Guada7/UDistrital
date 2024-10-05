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

import json
from datetime import datetime
from user import User
from game import Game
from machine import Machine


def create_user(users):
    """
    Create a new user and save it to the users list and JSON file.

    Args:
        users (list): The list of existing users.

    Prompts the user for their name and phone number, assigns a unique ID,
    and appends the new user to the list. The updated list is saved to
    'users.json'.
    """
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")

    user_id = max([user["id"] for user in users], default=0) + 1
    new_user = User(name, phone)
    new_user.id = user_id

    users.append({"id": new_user.id, "name": new_user.name, "phone": new_user.phone})

    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

    print(f"User created with ID: {new_user.id}")


def show_games():
    """
    Display all available games.

    Loads games from the Game class and prints their details.
    If no games are available, informs the user.
    """
    games = Game.load_games()
    if games:
        for game in games:
            print(
                f"ID: {game['game_id']}, Title: {game['title']}, Price: ${game['price']}"
            )
    else:
        print("No games available.")


def show_machines():
    """
    Display all available arcade machines.

    Loads machines from the Machine class and prints their details.
    If no machines are available, informs the user.
    """
    machines = Machine.load_machines()
    if machines:
        for machine in machines:
            print(
                f"ID: {machine['machine_id']}, Type: {machine['type']}, Material: {machine['material']}, Color: {machine['color']}, Player Count: {machine['player_count']}"
            )
            print(
                f"Dimensions: {machine['dimensions']}, Weight: {machine['weight']} kg, Power Consumption: {machine['power_consumption']} W"
            )
            print(
                f"Processor: {machine['processor']}, Memory: {machine['memory']}, Base Price: ${machine['base_price']}"
            )
            print("---")
    else:
        print("No machines available.")


def buy_machine(users):
    """
    Facilitate the purchase of an arcade machine by a user.

    Args:
        users (list): The list of existing users.

    Prompts the user for their ID, address, and machine code. Allows them to modify
    machine properties such as material and player count. Computes total price,
    saves purchase details to 'purchases.json', and confirms purchase.
    """
    user_id = int(input("Enter your user ID: "))

    if not any(user["id"] == user_id for user in users):
        print("User ID not found.")
        return

    address = input("Enter your address: ")

    machine_code = input("Enter the machine code you want to buy: ")

    machines = Machine.load_machines()
    machine = next((m for m in machines if m["machine_id"] == machine_code), None)

    if not machine:
        print("Machine code not found.")
        return

    material_change = (
        input("Do you want to change the material? (yes/no): ").lower() == "yes"
    )

    if material_change:
        new_material = input("Enter new material (wood/aluminum/carbon fiber): ")
        machine["material"] = new_material

    player_count = int(
        input(
            "Enter number of players (current is {}): ".format(machine["player_count"])
        )
    )
    machine["player_count"] = player_count

    color = input("Enter color (current is {}): ".format(machine["color"]))
    machine["color"] = color

    games_to_add = []
    while True:
        game_code = input("Enter game code to add (or type 'done' to finish): ")
        if game_code.lower() == "done":
            break

        games = Game.load_games()
        game = next((g for g in games if g["game_id"] == game_code), None)

        if game:
            games_to_add.append(game)
            print(f"Added game: {game['title']}")
        else:
            print("Game code not found.")

    total_price = machine["base_price"]
    for game in games_to_add:
        total_price += game["price"]

    purchase_summary = {
        "user_id": user_id,
        "address": address,
        "machine_code": machine_code,
        "material": machine["material"],
        "color": machine["color"],
        "player_count": player_count,
        "total_price": total_price,
        "games_added": [game["title"] for game in games_to_add],
        "purchase_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    try:
        with open("purchases.json", "r") as file:
            purchases = json.load(file)
            if not isinstance(purchases, list):
                raise ValueError("Invalid JSON format. Expected a list.")
    except (FileNotFoundError, ValueError):
        purchases = []

    purchases.append(purchase_summary)

    with open("purchases.json", "w") as file:
        json.dump(purchases, file, indent=4)

    print(f"Purchase completed. Summary: {purchase_summary}")


def view_purchases(user_id):
    """
   View all purchases made by a specific user.

   Args:
       user_id (int): The ID of the user whose purchases are to be viewed.

   Loads purchases from 'purchases.json' and displays them. If no purchases are found,
   informs the user.
   """
    try:
        with open("purchases.json", "r") as file:
            purchases = json.load(file)

        user_purchases = [p for p in purchases if p.get("user_id") == user_id]

        if user_purchases:
            for purchase in user_purchases:
                print(purchase)
        else:
            print("No purchases found for this ID.")

    except FileNotFoundError:
        print("No purchases have been made yet.")


def main():
    """
   Main function that runs the command-line interface for managing arcade machines.

   Loads existing users from 'users.json' and presents options to create users,
   show games/machines, buy machines, or view purchases. Runs until exit is chosen.
   """
    try:
        with open("users.json", "r") as file:
            users = json.load(file)

        while True:
            print(
                "\n1. Create User\n2. Show Games\n3. Show Machines\n4. Buy Machine\n5. View Purchases\n6. Exit"
            )
            choice = int(input("Choose an option: "))

            if choice == 1:
                create_user(users)
            elif choice == 2:
                show_games()
            elif choice == 3:
                show_machines()
            elif choice == 4:
                buy_machine(users)
            elif choice == 5:
                user_id = int(input("Enter your user ID to view purchases: "))
                view_purchases(user_id)
            elif choice == 6:
                break
            else:
                print("Invalid option. Please try again.")

    except FileNotFoundError as e:
        print(f"Error loading files: {e}")


if __name__ == "__main__":
    main()
