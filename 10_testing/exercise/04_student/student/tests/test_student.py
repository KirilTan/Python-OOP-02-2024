from unittest import main, TestCase
from project.student import Student


class TestStudent(TestCase):
    DEFAULT_COURSES_VALUE = {}
    STUDENT = {
        'name': 'name',
        'courses': DEFAULT_COURSES_VALUE  # {course_name: [notes]}
    }

    def setUp(self):
        self.student = Student(name=self.STUDENT['name'])

    def test_init(self):
        self.assertEqual(self.STUDENT['name'], self.student.name)
        self.assertEqual(TestStudent.DEFAULT_COURSES_VALUE, self.student.courses)

    def test_default_courses_value(self):
        self.assertEqual(TestStudent.DEFAULT_COURSES_VALUE, self.student.courses)

    def test_enroll_in_course_that_you_are_already_enrolled_in_updates_notes_and_outputs_string(self):
        expected_output = 'Course already added. Notes have been updated.'

        self.student.courses = {
            'course': ['note', 'note', 'note']
        }
        self.student.enroll(course_name='course',
                             notes=['note'])


if __name__ == "__main__":
    main()
