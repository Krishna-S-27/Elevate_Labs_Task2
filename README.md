Here is a comprehensive README.md tailored for your Task_2/Todo.py script, featuring detailed explanations, code insights, and credits.

---

# TO-DO List CLI Application

A simple yet effective command-line to-do list manager written in Python. This application lets you add, view, remove, and mark tasks as done, all through an intuitive console interface.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [File Structure](#file-structure)
- [Detailed Functionality](#detailed-functionality)
- [How to Run](#how-to-run)
- [Credits](#credits)

---

## Overview

This project is a part of my internship with Elevate Labs. The `Todo.py` script provides a lightweight way to manage your daily tasks directly from your terminal. It uses only Python's standard libraries (`os` and `json`) and stores all task data locally in a JSON file.

---

## Features

- **View Tasks:** See your current list of tasks with completion status.
- **Add Tasks:** Add new items to your to-do list.
- **Remove Tasks:** Delete tasks you no longer need.
- **Mark as Done:** Mark tasks as completed to track your progress.
- **Persistent Storage:** All tasks are saved in a `TO-Do.json` file so your data is safe between runs.

---

## How It Works

1. **Task Storage:**  
   All tasks are stored in a JSON file (`TO-Do.json`). Each task is a dictionary with two fields:  
   - `"task"`: The task description (string)  
   - `"done"`: Completion status (boolean)

2. **Console Menu:**  
   The main loop presents a numbered menu for actions. Input is taken for your choice and validated.

3. **No Third-Party Dependencies:**  
   Only `os` and `json` from Python's standard library are used—no extra installation required.

---

## File Structure

```
Task_2/
└── Todo.py      # The main CLI application
└── TO-Do.json   # (auto-created) Stores your tasks persistently
```

---

## Detailed Functionality

### Task Loading & Saving

- **load_tasks()**  
  Loads existing tasks from `TO-Do.json`. If the file doesn't exist, it starts with an empty list.

- **save_tasks(operation)**  
  Writes the current task list to `TO-Do.json` in a human-readable (indented) format.

### Task Management

- **view_task(operation)**  
  Displays all tasks with their status (Completed/Pending). If no tasks, informs the user.

- **add_task(operation)**  
  Prompts for a new task description, appends it to the list with `done: False`, and saves.

- **remove_task(operation)**  
  Shows all tasks, prompts for a task number to remove, validates input, removes, and saves.

- **mark_task(operation)**  
  Shows all tasks, prompts for a task number to mark as done, validates input, updates status, and saves.

### Main Program Loop

- Presents a menu:
  1. View Task
  2. Add Task
  3. Remove Task
  4. Mark Task As Done
  5. Exit

- Handles invalid input gracefully, always keeping your data safe.

---

## How to Run

1. **Ensure you have Python installed (version 3.x).**
2. **Navigate to the directory containing `Todo.py`.**
3. **Run the script:**

   ```bash
   python Todo.py
   ```

4. **Follow the on-screen prompts to manage your tasks!**

All your tasks will be saved in `TO-Do.json` in the same directory.

---

## Credits

Developed by Krishna S ([@Krishna-S-27](https://github.com/Krishna-S-27))  
Second task of the Elevate Labs internship  
For queries or feedback, feel free to reach out via GitHub!

---

Enjoy your organized workflow!
