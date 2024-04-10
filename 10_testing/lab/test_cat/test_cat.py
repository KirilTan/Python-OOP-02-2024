from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):
    CAT_NAME = 'Name'
    DEFAULT_CAT_SIZE = 0
    DEFAULT_CAT_FED = False
    DEFAULT_CAT_SLEEPY = False

    def setUp(self):
        self.cat = Cat(TestCat.CAT_NAME)

    def test_init(self):
        self.assertEqual(TestCat.CAT_NAME, self.cat.name)
        self.assertEqual(TestCat.DEFAULT_CAT_FED, self.cat.fed)
        self.assertEqual(TestCat.DEFAULT_CAT_SLEEPY, self.cat.sleepy)
        self.assertEqual(TestCat.DEFAULT_CAT_SIZE, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_feeding_cat_when_it_is_fed_raises_exception(self):
        expected_error_message = 'Already fed.'
        self.cat.fed = True

        with self.assertRaises(Exception) as exception:
            self.cat.eat()

        self.assertEqual(expected_error_message, str(exception.exception))

    def test_sleepy_cat_sleeps_and_is_not_sleepy_afterwards(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_making_hungry_cat_sleep_raises_exception(self):
        expected_error_message = 'Cannot sleep while hungry'
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual(expected_error_message, str(ex.exception))


if __name__ == '__main__':
    main()
