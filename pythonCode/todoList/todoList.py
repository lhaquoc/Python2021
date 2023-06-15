import tkinter
from tkinter import *

root = Tk()
root.title("To Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)
task_list = []

def addTask():
    task = task_entry.get() #get task from entry
    task_entry.delete(0, END) # clear text in entry
    if task:
        with open("task_list.txt", 'a') as task_file: # open task_file
            task_file.write(f"\n{task}") # write the new task into file
        task_list.append(task)
        listbox.insert(END, task) # show the new task 

def deleteTask():
    global task_list

    for i in listbox.curselection():
        print(listbox.get(i))
        print("delete task " + str(i + 1))
        
    task = str(listbox.get(ANCHOR)) #lay ra task duoc chon trong list tren UI
    if task in task_list:
        task_list.remove(task) # xoa task trong list, task dong thoi nam o 2 noi, listbox, list
        with open("task_list.txt", "w") as task_file: # ghi de cac task dang ton tai
            for task in task_list:
                task_file.write(task+"\n")
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("task_list.txt", "r") as task_file:
            tasks = task_file.readlines()
            print(tasks)
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
        
                
    except:
        file = open("task_list.txt", "w")
        file.close()
# icon
image_icon = PhotoImage(file="Image/task.png")
root.iconphoto(False, image_icon)

# top bar
image_topbar = PhotoImage(file="Image/topbar.png")
image_dock = PhotoImage(file="Image/dock.png")
image_note = PhotoImage(file="Image/task.png")
Label(root, image=image_topbar).place(x=0,y=0)
Label(root, image=image_dock, bg="#32405b").place(x=30, y=25)
Label(root, image=image_note, bg="#32405b").place(x=350, y=25)
heading = Label(root, text="ALL TASK", font="arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main

frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=21, font="arial 20", bd=0)
task_entry.place(x=10, y=7) # thao voi giao dien
task_entry.focus()

button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=addTask)
button.place(x=280, y=7)

# list box
frame_task = Frame(root, width=400, height=280, bg="white")
frame_task.pack(pady=(250, 0))
listbox = Listbox(frame_task, font=("arial", 12), width=55, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame_task)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# load task from file
openTaskFile()
print(task_list)
# delete
delete_icon = PhotoImage(file="Image/delete.png")
Button(root, image=delete_icon, bg="black", bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

root.mainloop()
