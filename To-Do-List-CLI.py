class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f'Task added: "{description}"')

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f'Task removed: "{removed_task.description}"')
        else:
            print("Invalid task number!")

    def mark_task_completed(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].mark_completed()
            print(f'Task marked as complete: "{self.tasks[task_number].description}"')
        else:
            print("Invalid task number!")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def update_task(self, task_number, new_description):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number].description = new_description
            print(f"Task {task_number + 1} updated!")
        else:
            print("Invalid task number!")

    def save_to_file(self, filename="todo_list.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.description}|{task.completed}\n")
        print("Tasks saved to file.")

    def load_from_file(self, filename="todo_list.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    description, completed = line.strip().split("|")
                    task = Task(description)
                    if completed == "True":
                        task.mark_completed()
                    self.tasks.append(task)
            print("Tasks loaded from file.")
        except FileNotFoundError:
            print("File not found.")


def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        todo_list.show_tasks()
        print("\nOptions: [a]dd [r]emove [m]ark [u]pdate [s]ave [l]oad [q]uit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "a":
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)

        elif choice == "r":
            task_number = int(input("Enter task number to remove: ")) - 1
            todo_list.remove_task(task_number)

        elif choice == "m":
            task_number = int(input("Enter task number to mark as complete: ")) - 1
            todo_list.mark_task_completed(task_number)

        elif choice == "u":
            task_number = int(input("Enter task number to update: ")) - 1
            new_description = input("Enter new description: ")
            todo_list.update_task(task_number, new_description)

        elif choice == "s":
            todo_list.save_to_file()

        elif choice == "l":
            todo_list.load_from_file()

        elif choice == "q":
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
