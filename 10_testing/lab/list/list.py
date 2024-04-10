from unittest import TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    integer_list_input = [1, 2, 3, 5.5, 'Test']

    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, 5.5, 'Test')

    def test_init_ignores_non_int_values(self):
        only_integer_list = []
        for value in TestIntegerList.integer_list_input:
            if isinstance(value, int):
                only_integer_list.append(value)

        self.assertEqual(only_integer_list, self.integer_list.get_data())

    def test_adding_non_int_values_raises_value_error(self):
        expected_error_type = ValueError
        expected_error_message = 'Element is not Integer'

        with self.assertRaises(expected_error_type) as ve:
            self.integer_list.add('Test')

        self.assertEqual(expected_error_message, str(ve.exception))

    def test_adding_integer_adds_it_to_the_list(self):
        input_data = 4
        expected_result = self.integer_list.get_data().copy() + [input_data]

        self.integer_list.add(input_data)

        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_removing_index_out_of_range_raises_index_error(self):
        expected_error_type = IndexError
        expected_error_message = 'Index is out of range'

        with self.assertRaises(expected_error_type) as ie:
            self.integer_list.remove_index(len(self.integer_list.get_data()) + 1)

        self.assertEqual(expected_error_message, str(ie.exception))

    def test_remove_valid_index_removes_element_at_index(self):
        index_to_remove = 0  # 1
        expected_list = [2, 3]

        self.integer_list.remove_index(index_to_remove)

        new_list = self.integer_list.get_data()

        self.assertEqual(expected_list, new_list)

    def test_get_invalid_index_raises_index_error(self):
        expected_error_type = IndexError
        expected_error_message = 'Index is out of range'

        with self.assertRaises(expected_error_type) as ie:
            self.integer_list.get(len(self.integer_list.get_data()) + 1)

        self.assertEqual(expected_error_message, str(ie.exception))

    def test_get_valid_index_returns_element_at_index(self):
        index_to_get = 0  # 1
        expected_result = self.integer_list.get_data()[index_to_get]

        self.assertEqual(expected_result, self.integer_list.get(index_to_get))

    def test_insert_invalid_index_raises_index_error(self):
        expected_error_type = IndexError
        expected_error_message = 'Index is out of range'

        with self.assertRaises(expected_error_type) as ie:
            self.integer_list.insert(len(self.integer_list.get_data()) + 1, 1)

        self.assertEqual(expected_error_message, str(ie.exception))

    def test_insert_non_int_value_raises_value_error(self):
        expected_error_type = ValueError
        expected_error_message = 'Element is not Integer'

        with self.assertRaises(expected_error_type) as ve:
            self.integer_list.insert(0, 'Test')

        self.assertEqual(expected_error_message, str(ve.exception))

    def test_insert_int_on_valid_index_adds_it_to_the_list(self):
        expected_list = self.integer_list.get_data().copy()
        expected_list.insert(0, 0)

        self.integer_list.insert(0, 0)

        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_get_biggest_returns_biggest_element(self):
        expected_result = 3
        result = self.integer_list.get_biggest()

        self.assertEqual(expected_result, result)

    def test_get_index_returns_index_of_element(self):
        expected_result = 1
        result = self.integer_list.get_index(2)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
