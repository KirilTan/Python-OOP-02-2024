from ex_1_and_2.project import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    MAMMAL = {
        'name': 'Name',
        'type': 'Type',
        'sound': 'Sound',
        'kingdom': 'animals'
    }

    def setUp(self):
        self.mammal = Mammal(name=TestMammal.MAMMAL['name'],
                             mammal_type=TestMammal.MAMMAL['type'],
                             sound=TestMammal.MAMMAL['sound'])

    def test_init(self):
        self.assertEqual(TestMammal.MAMMAL['name'], self.mammal.name)
        self.assertEqual(TestMammal.MAMMAL['type'], self.mammal.type)
        self.assertEqual(TestMammal.MAMMAL['sound'], self.mammal.sound)

    def test_make_sound_returns_correct_string(self):
        expected_string = f"{TestMammal.MAMMAL['name']} makes {TestMammal.MAMMAL['sound']}"
        self.assertEqual(expected_string, self.mammal.make_sound())

    def test_get_kingdom_returns_correct_string(self):
        expected_string = TestMammal.MAMMAL['kingdom']
        self.assertEqual(expected_string, self.mammal.get_kingdom())

    def test_info_returns_correct_string(self):
        expected_string = f"{TestMammal.MAMMAL['name']} is of type {TestMammal.MAMMAL['type']}"
        self.assertEqual(expected_string, self.mammal.info())


if __name__ == '__main__':
    main()
