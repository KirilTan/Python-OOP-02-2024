from unittest import main, TestCase
from ex_3.project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant(name='Test',
                                     capacity=10)

    def test_correct_init_all_valid_inputs(self):
        self.assertEqual('Test', self.restaurant.name)
        self.assertEqual(10, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_empty_name_input_expect_value_error(self):
        expected_error_message = "Invalid name!"

        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ''

        self.assertEqual(expected_error_message, str(ve.exception))

    def test_whitespace_name_input_expect_value_error(self):
        expected_error_message = "Invalid name!"

        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = '    '

        self.assertEqual(expected_error_message, str(ve.exception))

    def test_capacity_less_than_zero_expect_value_error(self):
        expected_error_message = "Invalid capacity!"

        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1

        self.assertEqual(expected_error_message, str(ve.exception))

    def test_capacity_is_zero_expect_success(self):
        self.restaurant.capacity = 0
        self.assertEqual(0, self.restaurant.capacity)

    def test_add_waiter_expect_success(self):
        result = self.restaurant.add_waiter("John")

        self.assertIn({"name": "John"}, self.restaurant.waiters)
        self.assertEqual("The waiter John has been added.", result)

    def test_add_waiter_when_restaurant_is_full_expect_failure(self):
        self.restaurant.capacity = 1
        self.restaurant.add_waiter("John")

        result = self.restaurant.add_waiter("Jane")

        self.assertEqual("No more places!", result)

    def test_add_existing_waiter_expect_failure(self):
        self.restaurant.add_waiter("John")

        result = self.restaurant.add_waiter("John")

        self.assertEqual("The waiter John already exists!", result)

    def test_remove_waiter_expect_success(self):
        self.restaurant.add_waiter("John")
        result = self.restaurant.remove_waiter("John")
        self.assertEqual("The waiter John has been removed.", result)
        self.assertEqual([], self.restaurant.waiters)

    def test_remove__non_existent_waiter_expect_failure(self):
        result = self.restaurant.remove_waiter("John")
        self.assertEqual("No waiter found with the name John.", result)

    def test_get_total_earnings_initially_zero(self):
        self.assertEqual(0, self.restaurant.get_total_earnings())

    def test_get_total_earnings_after_adding_earnings_expect_success(self):
        self.restaurant.add_waiter("John")
        self.restaurant.waiters[0]['total_earnings'] = 500

        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[1]['total_earnings'] = 1000

        self.assertEqual(1500, self.restaurant.get_total_earnings())

    def test_get_waiters_with_filter_min_earnings_expect_success(self):
        self.restaurant.add_waiter("John")
        self.restaurant.waiters[0]['total_earnings'] = 500

        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[1]['total_earnings'] = 1000

        filtered_waiters = self.restaurant.get_waiters(min_earnings=700)

        self.assertEqual([{"name": "Jane", "total_earnings": 1000}], filtered_waiters)

    def test_get_waiters_with_filter_max_earnings(self):
        self.restaurant.add_waiter("John")
        self.restaurant.waiters[0]['total_earnings'] = 500

        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[1]['total_earnings'] = 1000

        filtered_waiters = self.restaurant.get_waiters(max_earnings=700)

        self.assertEqual([{"name": "John", "total_earnings": 500}], filtered_waiters)


if __name__ == '__main__':
    main()
