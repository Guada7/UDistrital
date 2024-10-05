### Workshop 1

-The workshop2 folder contains all the materials and results related to the second workshop of the Software Modeling course. 
In this workshop, students are tasked with enhancing the command line application (CLI) for an arcade video game machine catalog 
by applying creational design patterns and improving software practices.
- Contents

	Workshop Report: A document that includes a class diagram of the solution, technical concerns, design patterns used,
  and adherence to SOLID principles.
	Source Code: Updated code files that implement the new functionalities required for the CLI application.

- Folder Structure

	/report: Contains the report in PDF format that details the development of the workshop.
	/code: Stores the source code files for the application.
	
- Workshop Requirements

	Attributes for Machines: Each machine must have attributes including material, dimensions, weight, power consumption, memory, processors, base price, and video games.
Predefined Machines:
Dance Revolution: Additional attributes include difficulties, arrow cardinalities, and controls price.
Classical Arcade: Additional behaviors such as make_vibration and sound_record_alert.
Shotting Machine and Racing Machine: Must define appropriate attributes.
Virtual Reality: Attributes include glasses type, glasses resolution, and glasses price.
Material Selection: Clients must select a material for their custom machine:
Wood: Increases weight by 10%, decreases price by 5%, increases power consumption by 15%.
Aluminum: Decreases weight by 5%, increases price by 10%, no change in power consumption.
Carbon Fiber: Decreases weight by 15%, increases price by 20%, decreases power consumption by 10%.
Video Game Management: Clients can add video games to registered machines, affecting the machine's price accordingly. Video games must have attributes such as storytelling creator, graphics creator, category, price, and year.
Memory Optimization: Reduce memory usage by avoiding duplicate objects and references where possible.


- Contributions

	If you would like to contribute to the development of this workshop or have questions, please contact saguadab@udistrital.edu.co
