class Smartphone:
    """
    A basic smartphone class with attributes for memory, apps, and power status.

    Args:
        memory (int or float): The memory capacity of the phone, in gigabytes.

    Attributes:
        memory (int or float): The memory capacity of the phone, in gigabytes.
        apps (list): A list of apps installed on the phone.
        is_on (bool): A boolean indicating whether the phone is turned on or off.

    Methods:
        power(self) -> None: Toggles the power status of the phone.
        install(self, app: str, app_memory: int or float) -> str: Installs an app on the phone.
        status(self) -> str: Returns a status message about the phone's memory and app count.

    """

    def __init__(self, memory: int or float):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        """Toggles the power status of the phone."""
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int or float) -> str:
        """
        Installs an app on the phone.

        Args:
            app (str): The name of the app to install.
            app_memory (int or float): The memory usage of the app, in gigabytes.

        Returns:
            str: A message indicating the result of the installation attempt.

        """
        if app_memory <= self.memory and self.is_on:  # Enough memory to install the app and the phone is turned on
            self.apps.append(app)  # Add the app to the list of installed apps
            self.memory -= app_memory  # Reduce the phone's memory
            return f'Installing {app}'

        elif app_memory <= self.memory and not self.is_on:  # Enough memory to install the app but the phone is turned off
            return f'Turn on your phone to install {app}'

        else:
            return f'Not enough memory to install {app}'

    def status(self) -> str:
        """
        Returns a status message about the phone's memory and app count.

        Returns:
            str: A message containing the phone's memory usage and app count.

        """
        total_apps_count = len(self.apps)
        text = f'Total apps: {total_apps_count}. Memory left: {self.memory}'
        return text


# Example usage
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
