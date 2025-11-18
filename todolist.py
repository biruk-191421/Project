#1 for adding 2 for removing and 3 for clearing 
to_do_list = []

def add_task():
    task = input("Enter task to add: ")
    to_do_list.append(task)
    print("Task added:", task)
    
def remove_task():
    index = int(input("Enter task index to remove: "))
    if 0<= index < len(to_do_list):
        removed = to_do_list.pop(index)
        print("Removed:", removed)
    else:
        print("Invalid index")
        
def clear_task():
    to_do_list.clear()
    print("All task cleared.")
    
print("press 1 for adding task")
print("press 2 for removing task")
print("press 3 for clearing task")

choice = int(input("Enter choice: "))
if choice==1:
   add_task()
elif choice==2:
   remove_task()
elif choice==3:
   clear_task()
else:
    print("invailed input")
     