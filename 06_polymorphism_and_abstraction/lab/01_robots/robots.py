class Robot:

    def __init__(self, name: str):
        self.name = name

    @staticmethod
    def num_of_sensors():
        return 1


class MedicalRobot(Robot):

    @staticmethod
    def num_of_sensors():
        return 6


class ChefRobot(Robot):

    @staticmethod
    def num_of_sensors():
        return 4


class WarRobot(Robot):

    @staticmethod
    def num_of_sensors():
        return 12


def number_of_robot_sensors(robot):
    print(robot.num_of_sensors())

basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

number_of_robot_sensors(basic_robot)
number_of_robot_sensors(da_vinci)
number_of_robot_sensors(moley)
number_of_robot_sensors(griffin)
