from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker(
            name='John',
            salary=100,
            energy=10
        )

    def test_correct_init(self):
        self.assertEqual(self.worker.name, 'John')
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_worker_can_work_when_he_has_energy_expected_outcome_increase_money_decrease_energy(self):
        iterations = 2
        expected_money = self.worker.salary * iterations
        expected_energy = self.worker.energy - iterations

        for _ in range(iterations):
            self.worker.work()

        self.assertEqual(self.worker.money, expected_money)
        self.assertEqual(self.worker.energy, expected_energy)

    def test_worker_can_work_without_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as exception:
            self.worker.work()

        self.assertEqual(str(exception.exception), 'Not enough energy.')

    def test_worker_regenerates_energy_when_resting(self):
        iterations = 1
        expected_energy = self.worker.energy + iterations

        for _ in range(iterations):
            self.worker.rest()

        self.assertEqual(self.worker.energy, expected_energy)

    def test_get_info_returns_correct_string(self):
        self.assertEqual(self.worker.get_info(), 'John has saved 0 money.')


if __name__ == '__main__':
    main()
