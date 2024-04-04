class vowels:
    VOWELS_LIST = ['a', 'e', 'i', 'o', 'u']

    def __init__(self, word: str):
        self.word = word
        self.index = -1
        self.vowels_list = [c for c in self.word if c.lower() in self.VOWELS_LIST]

    def __iter__(self):
        return iter(self.vowels_list)


# Test code
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
