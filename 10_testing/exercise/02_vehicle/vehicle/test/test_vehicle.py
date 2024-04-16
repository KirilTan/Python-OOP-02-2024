from unittest import TestCase, main
from ex_1_and_2.project import Vehicle


class TestVehicle(TestCase):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    VEHICLE = {
        'fuel': 1.25,
        'horse_power': 1.00,
        'capacity': 1.25,
        'fuel_consumption': DEFAULT_FUEL_CONSUMPTION
    }

    def setUp(self):
        self.vehicle = Vehicle(fuel=self.VEHICLE['fuel'],
                               horse_power=self.VEHICLE['horse_power'])

    def test_init(self):
        self.assertEqual(TestVehicle.VEHICLE['fuel'], self.vehicle.fuel)
        self.assertEqual(TestVehicle.VEHICLE['capacity'], self.vehicle.capacity)
        self.assertEqual(TestVehicle.VEHICLE['horse_power'], self.vehicle.horse_power)
        self.assertEqual(TestVehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_with_insufficient_fuel_gives_exception(self):
        km_user_input = TestVehicle.VEHICLE['fuel']
        fuel_needed = TestVehicle.DEFAULT_FUEL_CONSUMPTION * km_user_input

        expected_error = Exception
        expected_error_message = 'Not enough fuel'

        with self.assertRaises(expected_error) as ex:
            self.vehicle.drive(km_user_input)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_drive_with_enough_fuel_decreases_fuel(self):
        km_user_input = 1
        fuel_needed = TestVehicle.DEFAULT_FUEL_CONSUMPTION * km_user_input  # 1.25 * 1 = 1.25

        expected_fuel = TestVehicle.VEHICLE['fuel'] - fuel_needed  # 1.25 - 1.25 = 0

        self.vehicle.drive(km_user_input)

        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_refuel_with_too_much_fuel_gives_exception(self):
        fuel_user_input = TestVehicle.VEHICLE['capacity'] + TestVehicle.VEHICLE['capacity']

        expected_error = Exception
        expected_error_message = 'Too much fuel'

        with self.assertRaises(expected_error) as ex:
            self.vehicle.refuel(fuel_user_input)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_refuel_valid_fuel_increases_fuel(self):
        self.vehicle.fuel = 0
        fuel_user_input = TestVehicle.VEHICLE['capacity']

        self.vehicle.refuel(fuel_user_input)

        self.assertEqual(TestVehicle.VEHICLE['capacity'], self.vehicle.fuel)


    def test__str__outputs_correct_string(self):
        expected_string = f"The vehicle has {TestVehicle.VEHICLE['horse_power']} " \
                          f"horse power with {TestVehicle.VEHICLE['fuel']} fuel left " \
                          f"and {TestVehicle.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected_string, str(self.vehicle))


if __name__ == '__main__':
    main()
