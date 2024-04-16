from unittest import main, TestCase
from ex_1_and_2.project import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot(
            category='Mountain',
            part_type='Type A',
            capacity=100,
            memory=10
        )

        self.robot_with_installed_software = ClimbingRobot(
            category='Mountain',
            part_type='Type A',
            capacity=100,
            memory=10
        )
        self.robot_with_installed_software.installed_software = [
            {'name': 'A', 'capacity_consumption': 49, 'memory_consumption': 9},
            {'name': 'B', 'capacity_consumption': 50, 'memory_consumption': 5}
        ]

    def test_correct_init_with_all_valid_params(self):
        self.assertEqual('Mountain', self.robot.category)
        self.assertEqual('Type A', self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(10, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_incorrect_category_gives_value_error_and_str(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'Incorrect category'

        self.assertEqual(f"Category should be one of {self.ALLOWED_CATEGORIES}", str(ve.exception))

    def test_get_used_capacity_expect_success(self):
        expected_result = sum(s['capacity_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_get_available_capacity_expect_success(self):
        expected_result = (self.robot_with_installed_software.capacity -
                           sum(s['capacity_consumption'] for s in self.robot_with_installed_software.installed_software))
        result = self.robot_with_installed_software.get_available_capacity()

        self.assertEqual(expected_result, result)

    def test_get_used_memory_expect_success(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_installed_software.installed_software)
        result = self.robot_with_installed_software.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_get_available_memory_expect_success(self):
        expected_result = (self.robot_with_installed_software.memory -
                           sum(s['memory_consumption'] for s in
                               self.robot_with_installed_software.installed_software))
        result = self.robot_with_installed_software.get_available_memory()

        self.assertEqual(expected_result, result)

    def test_install_software_with_more_capacity_consumption_than_available_expect_failure(self):
        software = {'name': 'c', 'capacity_consumption': 101, 'memory_consumption': 0}

        result = self.robot.install_software(software)

        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual(expected_result, result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_more_memory_consumption_than_available_expect_failure(self):
        software = {'name': 'c', 'capacity_consumption': 0, 'memory_consumption': 11}

        result = self.robot.install_software(software)

        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual(expected_result, result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_capacity_and_memory_consumption_over_limit_expect_failure(self):
        software = {'name': 'c', 'capacity_consumption': 101, 'memory_consumption': 11}

        result = self.robot.install_software(software)

        expected_result = f"Software '{software['name']}' cannot be installed on {self.robot.category} part."

        self.assertEqual(expected_result, result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_border_values_expect_success(self):
        software = {'name': 'c', 'capacity_consumption': 100, 'memory_consumption': 10}

        expected_result = f"Software '{software['name']}' successfully installed on {self.robot.category} part."

        result = self.robot.install_software(software)

        self.assertEqual(expected_result, result)
        self.assertEqual([software], self.robot.installed_software)


if __name__ == '__main__':
    main()

