from unittest import main, TestCase
from car_manager import Car


class TestCar(TestCase):
    CAR = {
        'make': 'Kia',
        'model': 'Ceed',
        'fuel_consumption': 5,
        'fuel_capacity': 50,
        'default_fuel_amount': 0
    }

    def setUp(self):
        self.car = Car(TestCar.CAR['make'], TestCar.CAR['model'],
                       TestCar.CAR['fuel_consumption'], TestCar.CAR['fuel_capacity'])

    def test_init(self):
        self.assertEqual(TestCar.CAR['make'], self.car.make)
        self.assertEqual(TestCar.CAR['model'], self.car.model)
        self.assertEqual(TestCar.CAR['fuel_consumption'], self.car.fuel_consumption)
        self.assertEqual(TestCar.CAR['fuel_capacity'], self.car.fuel_capacity)
        self.assertEqual(TestCar.CAR['default_fuel_amount'], self.car.fuel_amount)

    def test_make_with_empty_string_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = 'Make cannot be null or empty!'

        with self.assertRaises(expected_exception_type) as ex:
            Car('', 'Ceed', 5, 50)

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_model_with_empty_string_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = 'Model cannot be null or empty!'

        with self.assertRaises(expected_exception_type) as ex:
            Car('Kia', '', 5, 50)

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_fuel_consumption_with_zero_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = 'Fuel consumption cannot be zero or negative!'

        with self.assertRaises(expected_exception_type) as ex:
            Car('Kia', 'Ceed', 0, 50)

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_fuel_capacity_with_negative_number_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = 'Fuel capacity cannot be zero or negative!'

        with self.assertRaises(expected_exception_type) as ex:
            Car('Kia', 'Ceed', 5, -50)

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_fuel_capacity_with_zero_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = 'Fuel capacity cannot be zero or negative!'

        with self.assertRaises(expected_exception_type) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_fuel_amount_with_negative_number_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = 'Fuel amount cannot be negative!'

        with self.assertRaises(expected_exception_type) as ex:
            self.car.fuel_amount = -50

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_refuel_with_zero_fuel_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = "Fuel amount cannot be zero or negative!"

        with self.assertRaises(expected_exception_type) as ex:
            self.car.refuel(0)

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_refuel_with_negative_fuel_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = "Fuel amount cannot be zero or negative!"

        with self.assertRaises(expected_exception_type) as ex:
            self.car.refuel(-50)

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_refuel_with_more_fuel_than_capacity_fills_to_capacity(self):
        self.car.fuel_amount = 50
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_with_not_enough_fuel_raises_exception(self):
        expected_exception_type = Exception
        expected_exception_message = "You don't have enough fuel to drive!"

        self.car.fuel_amount = 0
        with self.assertRaises(expected_exception_type) as ex:
            self.car.drive(1)

        self.assertEqual(expected_exception_message, str(ex.exception))

    def test_drive_with_enough_fuel_drives(self):
        self.car.fuel_amount = 50
        self.car.drive(1)
        self.assertEqual(49.95, self.car.fuel_amount)


if __name__ == "__main__":
    main()
