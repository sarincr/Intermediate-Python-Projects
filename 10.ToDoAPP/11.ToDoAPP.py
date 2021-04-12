import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List by @TokyoEdtech")

def add_events():
    events = events_func.get()
    if events != "":
        lst.insert(tkinter.END, events)
        events_func.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a events.")

def delete_events():
    try:
        events_index = lst.curselection()[0]
        lst.delete(events_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a events.")

def load_events():
    try:
        events = pickle.load(open("events.dat", "rb"))
        lst.delete(0, tkinter.END)
        for events in events:
            lst.insert(tkinter.END, events)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="Cannot find events.dat.")

def save_events():
    events = lst.get(0, lst.size())
    pickle.dump(events, open("events.dat", "wb"))

# Create GUI
eventsbox = tkinter.Frame(root)
eventsbox.pack()

lst = tkinter.Listbox(eventsbox, height=10, width=50)
lst.pack(side=tkinter.LEFT)

scrollbx = tkinter.Scrollbar(eventsbox)
scrollbx.pack(side=tkinter.RIGHT, fill=tkinter.Y)

lst.config(yscrollcommand=scrollbx.set)
scrollbx.config(command=lst.yview)

events_func = tkinter.Entry(root, width=50)
events_func.pack()

btn = tkinter.Button(root, text="Add events", width=48, command=add_events)
btn.pack()

del_events = tkinter.Button(root, text="Delete events", width=48, command=delete_events)
del_events.pack()

ld_events = tkinter.Button(root, text="Load events", width=48, command=load_events)
ld_events.pack(
)

save_events= tkinter.Button(root, text="Save events", width=48, command=save_events)
save_events.pack()

root.mainloop()

