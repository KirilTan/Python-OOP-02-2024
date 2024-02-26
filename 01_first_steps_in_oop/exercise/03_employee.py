class Employee:
    """
    Represents an employee with a unique ID, name, and salary.

    Attributes:
        id (int|float): Unique identifier for the employee.
        first_name (str): Employee's first name.
        last_name (str): Employee's last name.
        salary (int|float): Monthly salary of the employee.

    Methods:
        get_full_name: Returns the full name of the employee.
        get_annual_salary: Calculates and returns the annual salary of the employee.
        raise_salary: Increases the employee's salary by a specified amount.
    """

    def __init__(self, _id: int or float, first_name: str, last_name: str, salary: int or float):
        """
        Initializes a new Employee instance with the given id, first name, last name, and salary.

        Parameters:
            id (int|float): Unique identifier for the employee.
            first_name (str): Employee's first name.
            last_name (str): Employee's last name.
            salary (int|float): Monthly salary of the employee.
        """
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        """
        Returns the full name of the employee by concatenating the first and last names.

        Returns:
            str: The full name of the employee.
        """
        return f'{self.first_name} {self.last_name}'

    def get_annual_salary(self) -> int or float:
        """
        Calculates and returns the annual salary of the employee based on their monthly salary.

        Returns:
            int|float: The annual salary of the employee.
        """
        return self.salary * 12

    def raise_salary(self, amount: int or float) -> int or float:
        """
        Increases the employee's monthly salary by a specified amount and returns the new salary.

        Parameters:
            amount (int|float): The amount by which to raise the employee's salary.

        Returns:
            int|float: The employee's new monthly salary after the raise.
        """
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())
