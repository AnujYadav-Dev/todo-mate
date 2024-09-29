import tkinter as tk
from tkinter import messagebox, Scrollbar, RIGHT, Y, END

class ToDoListGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Classic To-Do List")
        self.root.geometry("400x600")
        self.root.config(bg="#FFF2D7")
        self.tasks = []

        # Create the UI elements
        self.create_widgets()
        self.layout_widgets()

    def create_widgets(self):
        # Create an Entry widget for task input
        self.task_entry_label = tk.Label(self.root, text="Enter Task:", font=("Arial", 12), bg="#FFF2D7")
        self.task_entry = tk.Entry(self.root, width=35, font=("Arial", 12))
        
        # Create Buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Arial", 10), bg="#007bff", fg="white", relief="groove")
        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, font=("Arial", 10), bg="#375E97", fg="white", relief="groove")
        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, font=("Arial", 10), bg="#EE4B2B", fg="white", relief="groove")
        self.mark_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed, font=("Arial", 10), bg="#28a745", fg="white", relief="groove")
        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks, font=("Arial", 10), bg="#FFBB00", fg="white", relief="groove")
        self.load_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks, font=("Arial", 10), bg="#1995AD", fg="white", relief="groove")

        # Task Listbox and Scrollbar
        self.task_listbox_label = tk.Label(self.root, text="To-Do List:", font=("Arial", 12), bg="#FFF2D7")
        self.task_listbox_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.task_listbox = tk.Listbox(self.task_listbox_frame, height=10, width=35, font=("Arial", 12), selectbackground="#007bff")
        self.scrollbar = Scrollbar(self.task_listbox_frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

    def layout_widgets(self):
        # Layout the widgets using grid and pack
        self.task_entry_label.pack(pady=10)
        self.task_entry.pack(pady=5)

        self.add_button.pack(pady=5)
        self.update_button.pack(pady=5)
        self.remove_button.pack(pady=5)
        self.mark_button.pack(pady=5)

        self.task_listbox_label.pack(pady=10)
        self.task_listbox_frame.pack(pady=5)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.save_button.pack(pady=10)
        self.load_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_listbox.insert(END, task)
            self.tasks.append({'description': task, 'completed': False})
            self.task_entry.delete(0, END)
        else:
            messagebox.showwarning("Input Error", "Task description cannot be empty!")

    def update_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            new_description = self.task_entry.get().strip()
            if new_description:
                self.task_listbox.delete(task_index)
                self.task_listbox.insert(task_index, new_description)
                self.tasks[task_index]['description'] = new_description
                self.task_entry.delete(0, END)
            else:
                messagebox.showwarning("Input Error", "New description cannot be empty!")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update")

    def remove_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            self.tasks.pop(task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove")

    def mark_completed(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            task = self.tasks[task_index]
            if not task['completed']:
                task['completed'] = True
                self.task_listbox.delete(task_index)
                self.task_listbox.insert(task_index, f"{task['description']} (Completed)")
            else:
                messagebox.showinfo("Task Completed", "Task is already marked as completed.")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed")

    def save_tasks(self):
        with open("todo_list_gui.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task['description']}|{task['completed']}\n")
        messagebox.showinfo("Save Success", "Tasks saved to file.")

    def load_tasks(self):
        try:
            with open("todo_list_gui.txt", "r") as file:
                self.tasks = []
                self.task_listbox.delete(0, END)
                for line in file:
                    description, completed = line.strip().split("|")
                    completed = completed == "True"
                    self.tasks.append({'description': description, 'completed': completed})
                    if completed:
                        self.task_listbox.insert(END, f"{description} (Completed)")
                    else:
                        self.task_listbox.insert(END, description)
            messagebox.showinfo("Load Success", "Tasks loaded from file.")
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "No saved tasks found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()
