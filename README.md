
# To-Do List Application

This project includes both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** version of a To-Do List application, implemented in Python.

## Features

### CLI Version
- Add tasks
- Update tasks
- Remove tasks
- Mark tasks as completed
- View all tasks
- Save and load tasks to/from a file

### GUI Version
- Clean, classic interface using `tkinter`
- Add tasks with ease
- Update or remove selected tasks
- Mark tasks as completed
- Save and load tasks to/from a file
- Scrollable task list

---

## Requirements

### CLI Version
- Python 3.x

### GUI Version
- Python 3.x
- `tkinter` module (usually pre-installed with Python)

---

## How to Run

### CLI Version
1. **Clone or download** this repository.
2. Run the CLI version with:
   \`\`\`bash
   python todo_list_cli.py
   \`\`\`
   Use the options presented in the CLI to manage your tasks.

### GUI Version
1. Clone or download this repository.
2. Run the GUI version with:
   \`\`\`bash
   python todo_list_gui.py
   \`\`\`
   A windowed interface will appear where you can manage your tasks with ease.

---

## File Structure

\`\`\`plaintext
├── todo_list_cli.py    # CLI version of the To-Do List
├── todo_list_gui.py    # GUI version of the To-Do List using tkinter
└── README.md           # This file
\`\`\`

---

## How to Save and Load Tasks

The tasks will be saved to a `.txt` file (`todo_list_cli.txt` or `todo_list_gui.txt` depending on the version).
- Use the **Save** button (in GUI) or select the save option in CLI to save your tasks.
- Load previously saved tasks using the **Load** button (in GUI) or select the load option in CLI.

---

## Future Improvements

- Add more customization options for the GUI (themes, colors, etc.).
- Implement task categorization (e.g., work, personal, etc.).
- Sync tasks between CLI and GUI versions using a shared task file.
