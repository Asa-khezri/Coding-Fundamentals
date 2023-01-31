from cProfile import label
from tkinter import *
from turtle import bgcolor

root = Tk()
root.title("Todo Application")
root.geometry("310x300")
root.configure(bg="#77c4e1")

# ----------------------------------------------------------------------------------------------
lb=Listbox(root, width=48)
lb.place(x=10,y=10)
En = Entry(root, width=48)
En.place(x=10,y=180)

# ----------------------------------------------------------------------------------------------
# Add a new item into the list
def Add_Button():
    lb.insert(END, En.get())
    Save_button()

mybutton_add = Button(root, text = "Add to the list", command= Add_Button, width=18)
mybutton_add.place(x=10,y=205)

# ----------------------------------------------------------------------------------------------
# Remove the item in the list
def Remove_Button():
    if len(lb.curselection()):
        lb.delete(lb.curselection()[0])
    Save_button()

mybutton_remove = Button(root, text = "Remove from the list", command= Remove_Button, width=18)
mybutton_remove.place(x=165,y=205)

# ----------------------------------------------------------------------------------------------
# Save the item in the list
def Save_button():
    file = open("Uncomplete.txt","w")
    for i in lb.get(0, END):
        file.write(i + "\n")
    file.close()   

# ----------------------------------------------------------------------------------------------
# Load the item in the listbox
def Load():
    file = open("Uncomplete.txt","r")
    f1 = file.readlines()
    for x in f1:
        lb.insert(END, x.replace("\n", ""))
Load()

root.mainloop()