### Python

- The python folder contains the source code and resources needed for the command line application (CLI) developed in Workshop 1 of the Software Modeling course. This application allows users to manage a catalog of arcade video game machines, applying object-oriented programming principles.

- Folder Structure

	-arcade_machine.py: This file contains the main class that represents an arcade machine, including its properties and methods for managing purchases and games.
	
	-cli.py: File that implements the command line interface, managing user interaction and the options available in the application.
	
	-games.json: JSON file that stores information about the available games, including their features and identification codes.
	
	-users.json: JSON file that contains user data, allowing to store and retrieve information about customers who make purchases.
	
	-purchases.json: JSON file that records purchases made, including details about the machines purchased and the users who bought them.
	
- Features

	The application includes the following features:
Material Selection: Allows the user to choose the type of materials for a machine to purchase: wood, aluminum, or carbon fiber.
Game List: Displays a list of available games to add to the machine.
Add Games: Allows the user to add games to the machine to purchase using a code.
Finalize Purchase: Processes the purchase of the machine and requests customer information for delivery.

- Requirements

	To run the code, make sure you have Python 3.x installed on your machine. You can run the application using the following command in the terminal:
bash
python python/cli.py

- Contributions
If you would like to contribute improvements or new features, please contact saguadab@udistrital.edu.co
