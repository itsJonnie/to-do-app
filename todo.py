from dataclasses import dataclass
from datetime import datetime
import json
import os

@dataclass
class Task:
    description: str
    completed: bool = False
    created_at: str = str(datetime.now())

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def show_menu(self):
        print("\n==== TODO MENU ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Mark task as done")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task.completed else " "
            print(f"{i}. [{status}] {task.description}")

    def add_task(self):
        description = input("Enter task description: ").strip()
        if description:
            task = Task(description=description)
            self.tasks.append(task)
            print("Task added successfully!")
            self.save_tasks()
        else:
            print("Task description cannot be empty!")

    def remove_task(self):
        self.view_tasks()
        if not self.tasks:
            return
        
        try:
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(self.tasks):
                removed_task = self.tasks.pop(index)
                print(f"Removed task: {removed_task.description}")
                self.save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def mark_done(self):
        self.view_tasks()
        if not self.tasks:
            return
        
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].completed = True
                print("Task marked as done!")
                self.save_tasks()
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            tasks_dict = [{'description': t.description, 
                          'completed': t.completed,
                          'created_at': t.created_at} for t in self.tasks]
            json.dump(tasks_dict, f)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                tasks_dict = json.load(f)
                self.tasks = [Task(**task) for task in tasks_dict]

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-5): ")

            try:
                if choice == "1":
                    self.view_tasks()
                elif choice == "2":
                    self.add_task()
                elif choice == "3":
                    self.remove_task()
                elif choice == "4":
                    self.mark_done()
                elif choice == "5":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Try again.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
