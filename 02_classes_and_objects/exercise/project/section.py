from task import Task


class Section:
    """
    A class that represents a section in a task manager application.

    A section contains a list of tasks and provides methods for adding, completing, and viewing tasks.

    Attributes:
        name (str): The name of the section
        tasks (list): A list of tasks in the section
    """

    def __init__(self, name: str):
        """
        Initialize a new Section object.

        Args:
            name (str): The name of the section
        """
        self.name = name
        self.tasks = []

    def add_task(self, task: Task) -> str:
        """
        Add a task to the section.

        Args:
            task (Task): The task to add

        Returns:
            str: A message indicating whether the task was added or already exists in the section
        """
        if task not in self.tasks:
            self.tasks.append(task)
            return f'Task {task.details()} is added to the section'
        else:
            return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str) -> str:
        """
        Mark a task as completed.

        Args:
            task_name (str): The name of the task to complete

        Returns:
            str: A message indicating whether the task was completed or not found
        """
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f'Completed task {task.name}'
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        """
        Clear completed tasks from the section.

        Returns:
            str: A message indicating the number of tasks cleared
        """
        removed_tasks = [task for task in self.tasks if task.completed]
        self.tasks = [task for task in self.tasks if not task.completed]
        return f'Cleared {len(removed_tasks)} tasks.'

    def view_section(self) -> str:
        """
        Get a view of the section.

        Returns:
            str: A view of the section, including the names and details of the tasks
        """
        section_view = f"Section {self.name}:\n"
        for task in self.tasks:
            section_view += f"{task.details()}\n"
        return section_view.strip()


# Example usage
task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())