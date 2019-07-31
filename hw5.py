-----------------
Assigment #5
NArmitage
----------------

infile ="/ToDo.txt"

with open(infile, 'r') as todo_file:
    lines = readlines(infile)
  

task_dict = ()
    
for line in lines:
   task = lines split(",")[0]
   priority = lines split(",")[1]
   task_dict= { }
   print(line)
   task= line[0]
   priority= line[2]
   task_dict[task]= priority
    
todo_list = open('Todo.txt', 'r')
tasks = todo_list.readlines()
todo_list.close()

tasks = [task.strip() for task in tasks]

task_dict()
    task_dict[str(task.split(',') [0])] = task.split(',')[1]
   
while(True):
    option = int(input('Menu of Options:\n1) Show current data\2)
    Add a new item\3) 
    Remove an existing item\4) 
    Save data to file\n5) 
    Exit program\n')
    
    if option == 1:
        for key in task_dict:
            print{f'{key} :{task_dict{key}')
    
elif option == 2:
    new_data = input('Enter new task in form of: task,priority\n')
    task_dict{str(new_data.split(',') [0] = new_data.split(',')
    
elif option == 3:
    delte_data = input('Enter task to delete\n')
    try:
       task_dict.pop(delete_data)
    except KeyError:
        print('Key not found!')
        
elif option == 4:
    todo_list = open('ToDo.txt', 'w')
    for key in task_dict:
        todo_list.writelines(f'{key},{task_dict[key]}\n')
        todo_list.close()
       
elif option == 5:
    todo_list = open('ToDo.txt', 'w')
    for key in task_dict:
        todo_list.writelines('f{key}, {task_dict[key]}\n')
        todo_list.close()
        quite()
        
else:
    print('Invalid option')
    

          
          
          
          
   