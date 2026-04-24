import tkinter as tk

root = tk.Tk()
root.title("Task Wrangler")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Add a task to the listbox
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Delete the selected task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])

# Clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Input field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.pack()

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#E53935", fg="white")
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All", command=clear_tasks, bg="#757575", fg="white")
clear_button.pack(pady=5)

root.mainloop()
