class Time:
    """
    A class to represent a time of day, with hours, minutes, and seconds.

    Attributes:
        max_hours (int): The maximum number of hours that can be represented.
        max_minutes (int): The maximum number of minutes that can be represented.
        max_seconds (int): The maximum number of seconds that can be represented.
        hours (int): The current number of hours.
        minutes (int): The current number of minutes.
        seconds (int): The current number of seconds.

    Methods:
        __init__(self, hours: int, minutes: int, seconds: int): Initializes a Time object with the specified hours, minutes, and seconds.
        set_time(self, hours: int, minutes: int, seconds: int): Sets the hours, minutes, and seconds of the Time object.
        get_time(self) -> str: Returns a string representation of the current time.
        next_second(self) -> str: Increments the seconds of the Time object, and returns the new time.
    """

    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        """
        Initializes a Time object with the specified hours, minutes, and seconds.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
            seconds (int): The number of seconds.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int) -> None:
        """
        Sets the hours, minutes, and seconds of the Time object.

        Args:
            hours (int): The number of hours.
            minutes (int): The number of minutes.
            seconds (int): The number of seconds.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        """
        Returns a string representation of the current time.

        Returns:
            str: A string representation of the current time, in the format "HH:MM:SS".
        """
        text = f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
        return text

    def next_second(self) -> str:
        """
        Increments the seconds of the Time object, and returns the new time.

        Returns:
            str: The new time, in the format "HH:MM:SS".
        """

        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0

        return self.get_time()


# Example usage
time = Time(9, 30, 59)
print(time.next_second())
print()
time = Time(10, 59, 59)
print(time.next_second())
print()
time = Time(23, 59, 59)
print(time.next_second())
