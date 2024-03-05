class Stack:

    def __init__(self):
        self.data: list = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self) -> bool:
        return False if self.data else True

    def __str__(self) -> str:
        text = ', '.join(reversed(self.data))
        return f'[{text}]'
