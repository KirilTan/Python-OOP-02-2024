class Programmer:
    """
    Represents a programmer with a specific set of programming skills and the ability to learn new languages.

    Attributes:
        name (str): The name of the programmer.
        language (str): The current programming language the programmer is skilled in.
        skills (int): The level of skills the programmer has.
    """

    def __init__(self, name: str, language: str, skills: int):
        """
        Initializes a new Programmer instance.

        Parameters:
            name (str): The name of the programmer.
            language (str): The current programming language of the programmer.
            skills (int): The skill level of the programmer.

        """
        self.name = name
        self.language = language
        self.skills = skills

    def watch_course(self, course_name: str, language: str, skills_earned: int) -> str:
        """
        Increases the programmer's skills if they watch a course in their current language.

        Parameters:
            course_name (str): The name of the course being watched.
            language (str): The programming language of the course.
            skills_earned (int): The number of skills earned from watching the course.

        Returns:
            str: A message indicating the outcome of watching the course.

        """
        if self.language == language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return f'{self.name} does not know {language}'

    def change_language(self, new_language: str, skills_needed: int) -> str:
        """
        Attempts to change the programmer's current programming language to a new one, given they have the required skills.

        Parameters:
            new_language (str): The new programming language the programmer wants to switch to.
            skills_needed (int): The amount of skills needed to switch to the new language.

        Returns:
            str: A message indicating whether the programmer successfully switched languages or why they couldn't.

        """
        if self.skills >= skills_needed and self.language != new_language:
            old_language = self.language
            self.language = new_language
            return f"{self.name} switched from {old_language} to {new_language}"

        elif self.skills >= skills_needed and self.language == new_language:
            return f"{self.name} already knows {self.language}"

        else:
            needed_skills = skills_needed - self.skills
            return f"{self.name} needs {needed_skills} more skills"


# Example usage
programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
