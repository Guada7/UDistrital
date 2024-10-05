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
from abc import ABC, abstractmethod

class Machine(ABC):
    """Abstract class representing an arcade machine."""

    def __init__(self, material, color, player_count):

        """
        Initializes an arcade machine.

        Args:
            material (str): Material of the machine.
            color (str): Color of the machine.
            player_count (int): Number of players the machine can support.
        """
        self.material = material
        self.color = color
        self.player_count = player_count
        self.games = []
        self.dimensions = None  # Dimensiones definidas en las clases concretas
        self.weight = None      # Peso definido en las clases concretas
        self.power_consumption = None  # Consumo definido en las clases concretas
        self.processor = None   # Procesador definido en las clases concretas
        self.memory = None      # Memoria definida en las clases concretas
        self.base_price = 500   # Precio base por defecto

    @abstractmethod
    def adjust_attributes(self):
        """Adjusts the specific attributes of the machine."""
        pass

    def add_game(self, game):
        """Adds a game to the machine's game list.

        Args:
            game (Game): Game object to add.
        """
        self.games.append(game)

    def calculate_price(self):
        """Calculates the total price of the machine based on added games.

        Returns:
            float: Total price of the machine.
        """
        total_price = self.base_price
        for game in self.games:
            total_price += game.price * (1.10 if game.price * 1.10 else 1)
        return total_price

    @staticmethod
    def load_machines():
        """Loads the list of machines from a JSON file.

        Returns:
            list: List of loaded machines.
        """
        try:
            with open("machines.json", "r") as file:
                machines_data = json.load(file)
                return machines_data  # Retorna la lista de máquinas
        except FileNotFoundError:
            print("machines.json file not found. No machines loaded.")
            return []
        except Exception as e:
            print(f"Error loading machines: {e}")
            return []
        
    @staticmethod
    def show_available_machines():
        """Displays the available machines."""
        machines = Machine.load_machines()
        print("Available Machines:")
        if machines:
            for machine in machines:
                print(f"- ID: {machine['machine_id']}, Type: {machine['type']}, Material: {machine['material']}, Color: {machine['color']}, Player Count: {machine['player_count']}")
                print(f"  Dimensions: {machine['dimensions']}, Weight: {machine['weight']} kg, Power Consumption: {machine['power_consumption']} W")
                print(f"  Processor: {machine['processor']}, Memory: {machine['memory']}, Base Price: ${machine['base_price']}")
                print("---")
        else:
            print("No machines available.")

class DanceRevolution(Machine):
    """Class representing the Dance Revolution machine."""

    def __init__(self, machine_id, material, color, player_count, difficulties, arrow_cardinalities, 
                 controls_price):
        """
        Initializes a Dance Revolution machine.

        Args:
            machine_id (str): Unique ID for the machine.
            material (str): Material of the machine.
            color (str): Color of the machine.
            player_count (int): Number of players the machine can support.
            difficulties (list): Available difficulty levels.
            arrow_cardinalities (list): Directions of arrows.
            controls_price (float): Price of the controls.
        """
        super().__init__(material, color, player_count)
        self.machine_id = machine_id  # ID único para la máquina
        self.difficulties = difficulties
        self.arrow_cardinalities = arrow_cardinalities
        self.controls_price = controls_price
        
        # Atributos específicos de la máquina
        self.dimensions = "1.5m x 1m x 2m"
        self.weight = 120  
        self.power_consumption = 250  
        self.processor = "Quad-Core"  
        self.memory = "8GB"  
        self.base_price = 700  

    def adjust_attributes(self):
        """Adjusts attributes based on the material used."""
        if self.material == "wood":
            self.base_price *= 0.95
            self.weight *= 1.10
            self.power_consumption *= 1.15
        elif self.material == "aluminum":
            self.base_price *= 1.10
            self.weight *= 0.95
        elif self.material == "carbon fiber":
            self.base_price *= 1.20
            self.weight *= 0.85
            self.power_consumption *= 0.90  

class ClassicalArcade(Machine):
    """Class representing the Classical Arcade machine."""

    def __init__(self, machine_id, material, color, player_count):
        """
        Initializes a Classical Arcade machine.

        Args:
            machine_id (str): Unique ID for the machine.
            material (str): Material of the machine.
            color (str): Color of the machine.
            player_count (int): Number of players the machine can support.
        """
        super().__init__(material, color, player_count)
        self.machine_id = machine_id
        
        # Atributos específicos de la máquina 
        self.dimensions = "1.5m x 1m x 2m"
        self.weight = 110  
        self.power_consumption = 220  
        self.processor = "Dual-Core"  
        self.memory = "4GB"  
        self.base_price = 600  

    def adjust_attributes(self):
        """Adjusts attributes based on the material used."""
        if self.material == "wood":
            self.base_price *= 0.95
            self.weight *= 1.10
            self.power_consumption *= 1.15
        elif self.material == "aluminum":
            self.base_price *= 1.10
            self.weight *= 0.95
        elif self.material == "carbon fiber":
            self.base_price *= 1.20
            self.weight *= 0.85
            self.power_consumption *= 0.90  

class ShootingMachine(Machine):
    """Class representing the Shooting Machine."""

    def __init__(self, machine_id, material, color, player_count, gun_type):
        """
         Initializes a Shooting Machine.

         Args:
             machine_id (str): Unique ID for the machine.
             material (str): Material of the machine.
             color (str): Color of the machine.
             player_count (int): Number of players the machine can support.
             gun_type (str): Type of gun used in gameplay.
         """
        super().__init__(material, color, player_count)
        self.machine_id = machine_id  

          # Atributos específicos
        self.gun_type = gun_type  
        
        # Atributos específicos de la máquina 
        self.dimensions = "1.5m x 1m x 2m"  
        self.weight = 130  
        self.power_consumption = 240  
        self.processor = "Quad-Core"  
        self.memory = "8GB"  
        self.base_price = 650

    def adjust_attributes(self):
       """Adjusts attributes based on the material used."""
       if   self.material == "wood":
            self.base_price *=0.95
            self.weight *=1.10
            self.power_consumption *=1.15 
       elif  self.material == "aluminum":
            self.base_price *=1.10
            self.weight *=0.95
       elif  self.material == "carbon fiber":
            self.base_price *=1.20
            self.weight *=0.85
            self.power_consumption *=0.90 

class RacingMachine(Machine):
    """Class representing the Racing Machine."""

    def __init__(self, machine_id, material, color, player_count, steering_type):
        """
         Initializes a Racing Machine.

         Args:
             machine_id (str): Unique ID for the machine.
             material (str): Material of the machine.
             color (str): Color of the machine.
             player_count (int): Number of players the machine can support.
             steering_type (str): Type of steering used in gameplay.
         """
        super().__init__(material, color, player_count)
        self.machine_id = machine_id  

         # Atributos específicos 
        self.steering_type = steering_type  
        
        # Atributos específicos de la máquina 
        self.dimensions = "1.5m x 1m x 2m"  
        self.weight = 125  
        self.power_consumption = 230  
        self.processor = "Hexa-Core"  
        self.memory = "16GB"  
        self.base_price = 700 

    def adjust_attributes(self):
       """Adjusts attributes based on the material used."""
       if self.material == "wood":
           self.base_price *=0.95
           self.weight *=1.10
           self.power_consumption *=1.15 
       elif self.material == "aluminum":
           self.base_price *=1.10
           self.weight *=0.95
       elif self.material == "carbon fiber":
           self.base_price *=1.20
           self.weight *=0.85
           self.power_consumption *=0.90

class VirtualReality(Machine):
    """Class representing the Virtual Reality Machine."""

    def __init__(self, machine_id, material, color, player_count, glasses_type, resolution):
        """
         Initializes a Virtual Reality Machine.

         Args:
             machine_id (str): Unique ID for the machine.
             material (str): Material of the machine.
             color (str): Color of the machine.
             player_count (int): Number of players the machine can support.
             glasses_type (str): Type of glasses used in gameplay.
             resolution (str): Resolution of virtual gameplay.
         """
        super().__init__(material, color, player_count)
        self.machine_id = machine_id  

          # Atributos específicos
        self.glasses_type = glasses_type  # Tipo de gafas
        self.resolution = resolution        # Resolución de la máquina
        
        # Atributos específicos de la máquina
        self.dimensions = "1.5m x 1m x 2m"  # Dimensiones específicas
        self.weight = 140                    # Peso específico (en kg)
        self.power_consumption = 300         # Consumo específico (en W)
        self.processor = "Octa-Core"         # Procesador específico
        self.memory = "16GB"                 # Memoria específica
        self.base_price = 800 

    def adjust_attributes(self):
       """Adjusts attributes based on the material used."""
       if self.material == "wood":
           self.base_price *= 0.95
           self.weight *= 1.10
           self.power_consumption *= 1.15
       elif self.material == "aluminum":
           self.base_price *= 1.10
           self.weight *= 0.95
       elif self.material == "carbon fiber":
           self.base_price *= 1.20
           self.weight *= 0.85
           self.power_consumption *= 0.90
