import tkinter
from tkinter import *
from tkinter import ttk, messagebox

def all_tasks():
    with open("tasks.txt") as file:
        tasks = file.readlines()
    list_items = Variable(value=tasks)
    listbox = Listbox(window, listvariable=list_items, height=15, selectmode=SINGLE, font="Arial 10", bg="#DAD4B5",
                      highlightthickness=0, borderwidth=0)
    listbox.grid(row=3, column=0, columnspan=4, sticky='nsew', pady=30, padx=30)


def add_task():
    def add():
        topic =task_topic_entry.get()
        desc = task_desc_entry.get()
        check = checked.get()
        if desc == "" or topic == "":
            messagebox.showerror(title="Error", message="Enter all feilds.")
            return
        with open("tasks.txt", "a") as file:
            file.write(f"{topic} | {desc} | {check} \n")
        task_topic_entry.delete(0, END)
        task_desc_entry.delete(0, END)
        checked.set("Not Completed")
        messagebox.showinfo(title="Success", message="Task added successfully.")
        all_tasks()


    model = Toplevel(window)
    model.title("To Do List")
    model.geometry("400x320")
    model.resizable(False, False)
    model.config(bg="#F2E8C6")
    frame = Frame(model, height=50, width=400, bg="#952323")
    frame.grid(row=0, column=0, columnspan=4)
    label = Label(frame, compound=TOP, text="To Do List", font='Verdana 25 bold', fg="white", bg="#952323")
    label.place(x=110, y=5)
    task_topic_label = Label(model, text="Enter topic: ", font='Verdana 15', bg="#F2E8C6")
    task_topic_entry = Entry(model)
    task_topic_label.grid(row=1, column=0, pady=15)
    task_topic_entry.grid(row=1, column=1, pady=15)
    task_desc_label = Label(model, text="Enter description: ", font='Verdana 15', bg="#F2E8C6")
    task_desc_entry = Entry(model)
    task_desc_label.grid(row=2, column=0, pady=15)
    task_desc_entry.grid(row=2, column=1, pady=15)
    checked = StringVar()
    checked.set("Completed")
    checkbox = Checkbutton(model, text="Completed", bg="#F2E8C6", font="Arial 15", variable=checked, onvalue="Completed", offvalue="Not Completed")
    checkbox.grid(row=3, column=0, pady=15)
    add_button = Button(model, text="Add task", bg="#A73121", width=12, font='Arial 12 bold', command=add)
    add_button.grid(row=4, column=0, pady=15)
    model.mainloop()

def view_task():
    def view():
        task = ""
        title = task_topic_entry.get()
        with open("tasks.txt") as file:
            tasks = file.readlines()
        for line in tasks:
            if title in line:
                task = line
                break
        if task:
            message = task.split("|")
            text = f"Task Title: {message[0]} \nTask Description:{message[1]}\nStatus of task:{message[2][:-1]}"
            info_label = Label(model, compound=TOP, font="Arial 15", text=text, bg="#F2E8C6")
            info_label.grid(row=3, column=0, columnspan=4)
        else:
            messagebox.showerror(title="Error", message="Task does not exist.")
        task_topic_entry.delete(0, END)


    model = Toplevel(window)
    model.title("To Do List")
    model.geometry("400x320")
    model.resizable(False, False)
    model.config(bg="#F2E8C6")
    frame = Frame(model, height=50, width=400, bg="#952323")
    frame.grid(row=0, column=0, columnspan=4)
    label = Label(frame, compound=TOP, text="To Do List", font='Verdana 25 bold', fg="white", bg="#952323")
    label.place(x=110, y=5)
    task_topic_label = Label(model, text="Enter topic: ", font='Verdana 15', bg="#F2E8C6")
    task_topic_entry = Entry(model)
    task_topic_label.grid(row=1, column=0, pady=15)
    task_topic_entry.grid(row=1, column=1, pady=15)
    view_button = Button(model, text="View task", bg="#A73121", width=12, font='Arial 12 bold', command=view)
    view_button.grid(row=2, column=0, pady=15)


def delete_task():
    def delete():
        title = task_topic_entry.get()
        with open("tasks.txt") as file:
            tasks = file.readlines()
        titles = [a.split(' |')[0] for a in tasks]
        if title in titles:
            with open("tasks.txt", "w") as file:
                for line in tasks:
                    if line.split(' |')[0] != title:
                        file.writelines(line)
            messagebox.showinfo(title="Success", message="Task deleted successfully.")
            task_topic_entry.delete(0, END)
            all_tasks()
        else:
            messagebox.showerror(title="Error", message="Task does not exist.")


    model = Toplevel(window)
    model.title("To Do List")
    model.geometry("400x220")
    model.resizable(False, False)
    model.config(bg="#F2E8C6")
    frame = Frame(model, height=50, width=400, bg="#952323")
    frame.grid(row=0, column=0, columnspan=4)
    label = Label(frame, compound=TOP, text="To Do List", font='Verdana 25 bold', fg="white", bg="#952323")
    label.place(x=110, y=5)
    task_topic_label = Label(model, text="Enter topic: ", font='Verdana 15', bg="#F2E8C6")
    task_topic_entry = Entry(model)
    task_topic_label.grid(row=1, column=0, pady=30)
    task_topic_entry.grid(row=1, column=1, pady=30)
    delete_button = Button(model, text="Delete task", bg="#A73121", width=12, font='Arial 12 bold', command=delete)
    delete_button.grid(row=2, column=0)

def update_task():
    def update():
        topic = task_topic_entry.get()
        desc = task_desc_entry.get()
        completed = checked.get()
        with open("tasks.txt", "a") as file:
            file.write(f"{topic} | {desc} | {completed} \n")
        task_topic_entry.delete(0, END)
        task_desc_entry.delete(0, END)
        checked.set("Not Completed")
        messagebox.showinfo(title="Success", message="Task added successfully.")
        all_tasks()


    def search():
        search = search_topic_entry.get()
        with open("tasks.txt") as file:
            tasks = file.readlines()
        titles = [a.split(' |')[0] for a in tasks]
        if search not in titles:
            messagebox.showerror(title="Error", message="Task does not exist")
        else:
            task = [a.split(' | ') for a in tasks if a.split(" |")[0] == search]
            task_topic_entry.insert(0, task[0][0])
            task_desc_entry.insert(0, task[0][1])
            checked.set(task[0][2].split(' ')[0])
            with open("tasks.txt", "w") as file:
                for line in tasks:
                    if line.split(' |')[0] != search:
                        file.writelines(line)

    model = Toplevel(window)
    model.title("To Do List")
    model.geometry("400x450")
    model.resizable(False, False)
    model.config(bg="#F2E8C6")
    frame = Frame(model, height=50, width=400, bg="#952323")
    frame.grid(row=0, column=0, columnspan=4)
    label = Label(frame, compound=TOP, text="To Do List", font='Verdana 25 bold', fg="white", bg="#952323")
    label.place(x=110, y=5)
    search_topic_label = Label(model, text="Enter topic to update: ", font='Verdana 15', bg="#F2E8C6")
    search_topic_entry = Entry(model)
    search_topic_label.grid(row=1, column=0, pady=15)
    search_topic_entry.grid(row=1, column=1, pady=15)
    search_button = Button(model, text="Search task", bg="#A73121", width=12, font='Arial 12 bold', command=search)
    search_button.grid(row=2, column=0, pady=15)
    task_topic_label = Label(model, text="Enter topic: ", font='Verdana 15', bg="#F2E8C6")
    task_topic_entry = Entry(model)
    task_topic_label.grid(row=3, column=0, pady=15)
    task_topic_entry.grid(row=3, column=1, pady=15)
    task_desc_label = Label(model, text="Enter description: ", font='Verdana 15', bg="#F2E8C6")
    task_desc_entry = Entry(model)
    task_desc_label.grid(row=4, column=0, pady=15)
    task_desc_entry.grid(row=4, column=1, pady=15)
    checked = StringVar()
    checked.set("Completed")
    checkbox = Checkbutton(model, text="Completed", bg="#F2E8C6", font="Arial 15", variable=checked,
                           onvalue="Completed", offvalue="Not Completed")
    checkbox.grid(row=5, column=0, pady=15)
    update_button = Button(model, text="Update task", bg="#A73121", width=12, font='Arial 12 bold', command=update)
    update_button.grid(row=6, column=0, pady=15)
    model.mainloop()

window = Tk()
window.title("To Do List")
window.geometry("400x500")
window.resizable(False, False)
window.config(bg="#F2E8C6")
frame = Frame(window, height=50, width=400, bg="#952323")
frame.grid(row=0, column=0, columnspan=4)
label = Label(frame, compound= TOP, text="To Do List", font='Verdana 25 bold', fg="white", bg="#952323")
label.place(x=110, y=5)
add_button = Button(text="Add Task", font='Arial 12 bold', bg="#A73121", width=17, command=add_task)
add_button.grid(row=1, column=0, pady=15)
view_button = Button(text="View Task", font='Arial 12 bold', bg="#A73121", width=17, command=view_task)
view_button.grid(row=1, column=1, pady=15)
delete_button = Button(text="Delete Task", font='Arial 12 bold', bg="#A73121", width=17, command=delete_task)
delete_button.grid(row=2, column=0, pady=15)
update_button = Button(text="Update Task", font='Arial 12 bold', bg="#A73121", width=17, command=update_task)
update_button.grid(row=2, column=1, pady=15)
all_tasks()
window.mainloop()