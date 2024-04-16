from ex_1_and_2.project import Employee
from ex_1_and_2.project import Person


class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'
