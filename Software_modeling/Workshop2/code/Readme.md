### Code

- The python folder contains the source code and resources needed for the command line application (CLI) developed in
  Workshop 2 of the Software Modeling course. This application enhances the management of a catalog of arcade video game
  machines by applying creational design patterns and improving software practices.
	
- Features

	The application includes the following features:
Material Selection: Allows the user to choose the type of materials for a machine to purchase: wood, aluminum, or carbon fiber.
Game List: Displays a list of available games to add to the machine.
Add Games: Allows the user to add games to the machine to purchase using a code.
Finalize Purchase: Processes the purchase of the machine and requests customer information for delivery..

- New Requirements

	All machines must have attributes: material, dimensions, weight, power consumption, memory, processors, base price, and video games.
Predefined machines include:
Dance Revolution: Additional attributes such as difficulties, arrow cardinalities, and controls price.
Classical Arcade: Additional behaviors like make_vibration and sound_record_alert.
New machines: Shotting Machine and Racing Machine with defined attributes.
Virtual Reality: Attributes include glasses type, glasses resolution, and glasses price.
Clients must select one predefined machine and a material type to create a custom machine with specific adjustments based on material choice:
Wood: +10% weight, -5% price, +15% power consumption.
Aluminum: -5% weight, +10% price, no change in power consumption.
Carbon Fiber: -15% weight, +20% price, -10% power consumption.
Users can add video games to registered machines; prices will adjust accordingly based on video game attributes (e.g., standard vs. high definition).
Memory optimization is crucial; reduce duplicate object creation.
Requirements
To run the code, ensure you have Python 3.x installed on your machine. You can run the application using the following command in the terminal:
bash
python python/cli.py

- Contributions
If you would like to contribute improvements or new features, please contact saguadab@udistrital.edu.co
