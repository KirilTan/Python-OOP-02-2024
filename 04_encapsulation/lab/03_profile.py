class Profile:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        valid_length = len(value) >= 8
        uppercase_present = len([char for char in value if char.isupper()]) > 0
        digit_present = len([char for char in value if char.isdigit()]) > 0

        if not valid_length or not uppercase_present or not digit_present:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = value

    def __str__(self):
        text = f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'
        return text


# Test code
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
