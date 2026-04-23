import tkinter as tk

root = tk.Tk()
root.title("Task Wrangler")
root.geometry("400x400")

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=40, height=10)
task_listbox.pack(pady=10)

root.mainloop()
