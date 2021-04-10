
import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List APP")

def event_add():
    task = task_func.get()
    if task != "":
        lst.insert(tkinter.END, task)
        task_func.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a event.")

taskbox = tkinter.Frame(root)
taskbox.pack()

lst = tkinter.Listbox(taskbox, height=10, width=50)
lst.pack(side=tkinter.LEFT)

scrollbx = tkinter.Scrollbar(taskbox)
scrollbx.pack(side=tkinter.RIGHT, fill=tkinter.Y)

lst.config(yscrollcommand=scrollbx.set)
scrollbx.config(command=lst.yview)

task_func = tkinter.Entry(root, width=50)
task_func.pack()

btn = tkinter.Button(root, text="Add an event", width=48, command=event_add)
btn.pack()



root.mainloop()