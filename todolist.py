class ToDoTask: #Class initialises attributes of a task
    def __init__(self, task, category, deadline=None):
        self.task = task
        self.category = category
        self.deadline = deadline  

    def __str__(self): #States the task name, what category it is in and its deadline
        return f"Task: {self.task} | Category: {self.category} | Deadline: {self.deadline or 'No deadline'}"


class ToDoManager: # Manages to do list
    def __init__(self):
        self.tasks = {
            'School': {},
            'Home': {}
        }  #Nested Dictionary to make the code shorter 

    def add_task(self, task, category, deadline=None): # Adds new task to a certain category
        if category not in self.tasks:
            raise ValueError(f"Invalid category: {category}")
        if task in self.tasks[category]: #New task won't be add if it is already in the dictionary
            raise ValueError("Task already exists in this category.")
        else:
            self.tasks[category][task] = ToDoTask(task, category, deadline)

    def edit_task(self, task, category, new_task=None, new_deadline=None): #Allows user to change properties of a task including its category and deadline
        if category not in self.tasks or task not in self.tasks[category]:
            raise ValueError("Task not found in this category.")

        task_obj = self.tasks[category][task]

        if new_task and new_task != task:
            del self.tasks[category][task]
            task_obj.task = new_task
            self.tasks[category][new_task] = task_obj

       
        if new_deadline:
            task_obj.deadline = new_deadline

    def remove_task(self, task, category): #Method to remove tasks from the to-do list
        if category not in self.tasks or task not in self.tasks[category]:
            raise ValueError("Task not found in this category.") # Raises error if task is not in the category
        else: 
            del self.tasks[category][task] #Deletes task from 

    def list_tasks(self, category=None):
        output = []
        if category is not None:
            if category not in self.tasks: #If task is not in a specific category, raises error
                raise ValueError("Invalid category.")
            for task_name in self.tasks[category]:
                task_obj = self.tasks[category][task_name]
                output.append(str(task_obj))
        else:
            for cat in self.tasks:
                for task_name in self.tasks[cat]:
                    task_obj = self.tasks[cat][task_name]
                    output.append(str(task_obj))
        return output


class ToDoListFacade:
    def __init__(self):
        self.manager = ToDoManager()

    def add_task(self, task, category, deadline=None):
        self.manager.add_task(task, category, deadline)

    def edit_task(self, task, category, new_task=None, new_deadline=None):
        self.manager.edit_task(task, category, new_task, new_deadline)

    def delete_task(self, task, category):
        self.manager.remove_task(task, category)

    def show_tasks(self, category=None): #A method to print the whole to-do list
        print("\nTO-DO LIST")
        tasks = self.manager.list_tasks(category)
        if not tasks:
            print("No tasks found.")
        else:
            for task in tasks:
                print(task)

if __name__ == '__main__':
    todo = ToDoListFacade()
    
    todo.add_task("English Essay", "School", "20/6/25") #Add some tasks
    todo.add_task("Mow lawn", "Home", "19/6/25")
    todo.add_task("Science Notes", "School")
    
    todo.show_tasks() #Display all tasks

    todo.edit_task("English Essay", "School", new_task="Complete English Essay", new_deadline="22 June 2025") #Edit an existing task
    todo.delete_task("Mow lawn", "Home") #Deletes task

