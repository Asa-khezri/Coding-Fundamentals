from Function import *

# ----------------------------------------------------------------------------------------------
# Print Welcome command to show a user how to use command and run the program
Welcome = '''
Command Line Todo application
=============================

Command line arguments:
    -l   Lists all the tasks
    -a   Adds a new task
    -r   Removes an task
    -c   Completes an task
'''
print(Welcome)

# ----------------------------------------------------------------------------------------------
# Run the function that user choose
while True:
    Com = input("What is your command? ")
    if Com == "-a":
        AddToList()
        Save()
    elif Com == "-l":
        PrintList()
    elif Com == "-c":
        CompleteTask()
    elif Com == "-r":
        RemoveTask()
    else:
        print("Unsupported argument.")
        print(Welcome)