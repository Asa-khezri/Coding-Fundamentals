# ----------------------------------------------------------------------------------------------
# Public variable
Task = []

# ----------------------------------------------------------------------------------------------
# Add an item to the list
def AddToList():
    Entry = input("Enter your task: ")
    print("The", Entry, "is added")
    Task.append({"Title":Entry,"Complete":False})

# ----------------------------------------------------------------------------------------------
# Print all list   
def PrintList():
    if len(Task) == 0:
        print("\t","No todos for today! :)")            
    else:
        print("The all list: ")
        no = 1
        for i in Task:
            if i["Complete"] == True:
                print(no,"-","[x]",i["Title"])
            else:
                print(no,"-","[ ]",i["Title"])
            no+=1

# ----------------------------------------------------------------------------------------------
# Complete an item into the list
def CompleteTask():
    try:
        CompleteItem = int(input("Enter your number: "))-1
        Task[CompleteItem]["Complete"] = True
        print(f'"{Task[CompleteItem]["Title"]}" is completed.')
    except IndexError:
        print('Unable to check: index is out of bound.')
    Save()

# ----------------------------------------------------------------------------------------------
# Remove an item from the list
def RemoveTask():
    PrintList()
    try:
        RemoveItem = int(input("Enter your number: "))-1
        deletedTask = Task.pop(RemoveItem)
        print(f'"{deletedTask["Title"]}" is deleted.')
        Save()  
    except IndexError:
        print(' Unable to remove: index is out of bound.')
    except ValueError:
        print('Unable to remove: index is not a number.') 

# ----------------------------------------------------------------------------------------------
# Save an item    
def Save():
    file = open("Uncomplete.txt","w")
    for i in Task:
        if i["Complete"] == False:
            file.write(i["Title"] + "\n")    
    file.close()
    
    file = open("Complete.txt","w")
    for i in Task:
        if i["Complete"] == True:
            file.write(i["Title"] + "\n")    
    file.close()

# ----------------------------------------------------------------------------------------------
# Load the list
def Load():
    file = open("Uncomplete.txt", "r")
    for line in file:
        Task.append({"Title":line.replace("\n",""),"Complete": False})
    file.close()

    file = open("Complete.txt", "r")
    for line in file:
        Task.append({"Title":line.replace("\n",""),"Complete": True})
    file.close()
Load() 