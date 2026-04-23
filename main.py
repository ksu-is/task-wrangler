import tkinter as tk

root = tk.Tk()
root.title("Task Wrangler")
root.geometry("400x400")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task")
add_button.pack()

root.mainloop()
