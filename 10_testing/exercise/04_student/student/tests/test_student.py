from unittest import main, TestCase
from project.student import Student


class TestStudent(TestCase):
    DEFAULT_COURSES_VALUE = {}
    STUDENT = {
        'name': 'Name Surname',
        'courses': DEFAULT_COURSES_VALUE  # {course_name: [notes]}
    }
    STUDENT_WITH_COURSES = {
        'name': 'OtherName Surname',
        'courses': {
            'course': ['note 1', 'note 2', 'note 3']
        }
    }

    def setUp(self):
        self.student = Student(name=self.STUDENT['name'])
        self.student_with_courses = Student(name=self.STUDENT_WITH_COURSES['name'],
                                            courses={'course': ['note 1', 'note 2', 'note 3']})

    def test_init(self):
        self.assertEqual(self.STUDENT['name'], self.student.name)
        self.assertEqual(self.STUDENT['courses'], self.student.courses)

        self.assertEqual(self.STUDENT_WITH_COURSES['name'], self.student_with_courses.name)
        self.assertEqual(self.STUDENT_WITH_COURSES['courses'], self.student_with_courses.courses)

    def test_default_courses_value(self):
        self.assertEqual(TestStudent.DEFAULT_COURSES_VALUE, self.student.courses)

    def test_enroll_in_course_that_you_are_already_enrolled_in_updates_notes_and_outputs_string(self):
        new_notes = ['note 4', 'note 5', 'note 6']

        result = self.student_with_courses.enroll('course', new_notes)

        self.assertEqual("Course already added. Notes have been updated.", result)

        self.assertEqual(['note 1', 'note 2', 'note 3', 'note 4', 'note 5', 'note 6'],
                         self.student_with_courses.courses['course'])

    def test_enroll_in_course_with_third_param_Y_updates_notes(self):
        result = self.student.enroll('course', ['note 1', 'note 2'], 'Y')

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({'course': ['note 1', 'note 2']}, self.student.courses)

    def test_enroll_in_course_that_you_are_not_enrolled_in_adds_the_course_and_notes(self):
        result = self.student.enroll('course', ['note 1', 'note 2'], )

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual({'course': ['note 1', 'note 2']}, self.student.courses)

    def test_enroll_in_course_with_third_param_N_does_not_update_notes(self):
        result = self.student.enroll('course', ['note 1', 'note 2'], 'N')

        self.assertEqual("Course has been added.", result)

        self.assertEqual({'course': []}, self.student.courses)

    def test_add_notes_to_existing_course_updates_notes(self):
        result = self.student_with_courses.add_notes('course', 'note 4')

        self.assertEqual("Notes have been updated", result)

        self.assertEqual(['note 1', 'note 2', 'note 3', 'note 4'],
                         self.student_with_courses.courses['course'])

    def test_add_notes_to_non_existing_course_raises_exception(self):
        expected_exception_type = Exception
        expected_error_message = 'Cannot add notes. Course not found.'

        with self.assertRaises(expected_exception_type) as ex:
            self.student.add_notes('course', 'note')

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_leave_course_removes_the_course_and_notes(self):
        result = self.student_with_courses.leave_course('course')

        self.assertEqual("Course has been removed", result)

        self.assertEqual(self.DEFAULT_COURSES_VALUE, self.student_with_courses.courses)

    def test_leave_course_that_you_are_not_enrolled_in_raises_exception(self):
        expected_exception_type = Exception
        expected_error_message = 'Cannot remove course. Course not found.'

        with self.assertRaises(expected_exception_type) as ex:
            self.student.leave_course('course')

        self.assertEqual(expected_error_message, str(ex.exception))


if __name__ == "__main__":
    main()
