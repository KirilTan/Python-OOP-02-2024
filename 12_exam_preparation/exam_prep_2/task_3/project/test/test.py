from collections import deque
from unittest import main, TestCase
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self):
        self.station = RailwayStation(
            name='Name',
        )
        self.station_with_trains = RailwayStation(
            name='Name2'
        )
        self.station_with_trains.new_arrival_on_board('Train1')
        self.station_with_trains.new_arrival_on_board('Train2')
        self.station_with_trains.new_arrival_on_board('Train3')

    def test_correct_name_input_initialization(self):
        self.assertEqual('Name', self.station.name)
        self.assertEqual(deque(), self.station.arrival_trains)
        self.assertEqual(deque(), self.station.departure_trains)

    def test_incorrect_name_input_expect_value_error(self):
        expected_error_message = "Name should be more than 3 symbols!"

        with self.assertRaises(ValueError) as ve:
            self.station.name = ''

        self.assertEqual(expected_error_message, str(ve.exception))

    def test_incorrect_name_input_border_value_expect_value_error(self):
        expected_error_message = "Name should be more than 3 symbols!"

        with self.assertRaises(ValueError) as ve:
            self.station.name = '123'

        self.assertEqual(expected_error_message, str(ve.exception))

    def test_new_arrival_on_board_expect_success(self):
        train_info = 'Train info'
        expected_result = deque([train_info])

        self.station.new_arrival_on_board(train_info)

        self.assertEqual(expected_result, self.station.arrival_trains)

    def test_train_has_arrived_other_trains_to_arrive_expect_success(self):
        train_info = 'Train3'

        expected_result = f"There are other trains to arrive before {train_info}."

        result = self.station_with_trains.train_has_arrived(train_info)

        self.assertEqual(expected_result, result)

    def test_train_has_arrived_train_to_leave_expect_success(self):
        train_info = 'Train1'

        expected_result = f"{train_info} is on the platform and will leave in 5 minutes."
        expected_deque_arrival_trains = self.station_with_trains.arrival_trains.copy()
        expected_deque_arrival_trains.popleft()

        result = self.station_with_trains.train_has_arrived(train_info)

        self.assertEqual(expected_result, result)
        self.assertEqual(deque([train_info]), self.station_with_trains.departure_trains)
        self.assertEqual(expected_deque_arrival_trains, self.station_with_trains.arrival_trains)

    def test_train_has_left_without_any_trains_in_departure_trains_expect_false(self):
        train_info = 'Train Info'
        expected_result = False

        result = self.station.train_has_left(train_info)

        self.assertEqual(expected_result, result)

    def test_train_has_left_train_to_leave_is_not_next_train_expect_false(self):
        train_info = 'Train3'

        expected_result = False
        expected_deque = self.station_with_trains.departure_trains

        result = self.station_with_trains.train_has_left(train_info)

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_deque, self.station_with_trains.departure_trains)

    def test_train_has_left_train_to_leave_expect_success(self):
        train_info = 'Train1'

        expected_result = True
        expected_deque = deque()

        self.station_with_trains.train_has_arrived(train_info)
        result = self.station_with_trains.train_has_left(train_info)

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_deque, self.station_with_trains.departure_trains)


if __name__ == '__main__':
    main()
