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
