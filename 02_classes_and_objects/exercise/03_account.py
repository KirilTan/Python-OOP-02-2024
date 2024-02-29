class Account:
    """
    This class represents a bank account.

    Args:
        _id (int): The unique account ID.
        name (str): The account holder's name.
        balance (int, optional): The current account balance. Defaults to 0.

    Attributes:
        id (int): The unique account ID.
        name (str): The account holder's name.
        balance (int): The current account balance.

    Methods:
        credit(amount: int) -> int: Adds an amount to the account balance and returns the new balance.
        debit(amount: int) -> int or str: Subtracts an amount from the account balance.
        If the amount is greater than or equal to the current balance, returns the new balance.
        If the amount is less than the current balance, returns a string indicating that the amount exceeded the balance.
        info() -> str: Returns a string containing information about the account,
        including the account holder's name, account ID, and current balance.
    """

    def __init__(self, _id: int, name: str, balance: int = 0):
        self.id = _id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        """
        Adds an amount to the account balance and returns the new balance.

        Args:
            amount (int): The amount to add to the balance.

        Returns:
            int: The new account balance.
        """
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> int or str:
        """
        Subtracts an amount from the account balance.
        If the amount is greater than or equal to the current balance, returns the new balance.
        If the amount is less than the current balance, returns a string indicating that the amount exceeded the balance.

        Args:
            amount (int): The amount to subtract from the balance.

        Returns:
            int or str: The new account balance if the debit was successful,
                        or a string indicating that the amount exceeded the balance if the debit was not successful.
        """
        if amount <= self.balance:
            self.balance -= amount
            return self.balance

        return "Amount exceeded balance"

    def info(self) -> str:
        """
        Returns a string containing information about the account,
        including the account holder's name, account ID, and current balance.

        Returns:
            str: A string containing information about the account.
        """
        text = f"User {self.name} with account {self.id} has {self.balance} balance"
        return text


# Example usage
account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())
print("---")
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
