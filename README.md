---

## ✅ Python Todo App (CLI)

A simple, interactive command-line **Todo List Application** built with Python.  
Supports task creation, viewing, completion tracking, and persistent storage using JSON.

---

### 📦 Features

- Add new tasks with descriptions
- View all tasks with status
- Mark tasks as completed
- Remove specific tasks
- Save and load tasks automatically from `tasks.json`
- Tracks creation time of each task

---

### 🧠 Tech Highlights

- Python 3+
- `@dataclass` for clean task modeling
- `json` for local data storage
- `datetime` for timestamping
- Exception-safe input handling

---

### 🚀 Getting Started

#### ✅ 1. Clone the repo or copy the script:

```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

#### ✅ 2. Run the app:

```bash
python todo.py
```

> If you're using a different filename, update `todo.py` accordingly.

---

### 📝 Sample Interaction

```
==== TODO MENU ====
1. View tasks
2. Add task
3. Remove task
4. Mark task as done
5. Exit

Choose an option (1-5): 2
Enter task description: Learn Python
Task added successfully!
```

---

### 💾 Task Storage

- All tasks are saved to a local file named `tasks.json`
- Tasks persist between sessions

---

### 🔧 Customization Ideas

- Add task priorities or due dates
- Implement recurring tasks
- Convert to a web app (Flask/FastAPI)
- Add colorized terminal output

---

### 👤 Author

Created by **Jonathan Sher** — aspiring Python developer on a journey to FAANG.  
Feel free to fork or build on top of this project!
