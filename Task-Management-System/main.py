# Katherine Chapkis -- Project 1

from datetime import date

class Task:
    ID_counter = 0

    def __init__(self, name: str, status: str, priority: str, duedate: str, description = None) -> None:
        Task.ID_counter += 1

        self.name = name
        self.description = description

        if priority.lower() != 'low' or "medium" or "high": ValueError
        else: self.priority = priority.title()

        if status.lower() != 'in progress' or "complete": ValueError
        else: self.status = status.title()

        # TO DO: write code to parse through due-date
        # FORMAT: MM-DD-YYYY
        self.duedate = duedate 
            # If overdue, immediately set priority status to HIGH

    def __str__(self) -> str:
        text = '\nTask: {} \nDescription: {} \nPriority: {} \nStatus: {} \nDue: {}'.format(
            self.name, self.description, self.priority, self.status, self.duedate)
        return text 

    def update_status(self, status: str):
        if status.lower() != 'in progress' or "complete": ValueError
        else: self.status = status.title()

    def update_priority(self, priority: str):
        if priority.lower() != 'low' or "medium" or "high": ValueError
        else: self.priority = priority.title()

class Project:
    ID_counter = 0

    def __init__(self, name: str, description: str, tasks: list) -> None:
        Project.ID_counter += 1

        self.name = name
        self.description = description

        for task in tasks:
            if isinstance(task, Task):
                continue
            else: raise TypeError('Individual task must be a Task object.')
        
        self.tasks = tasks

    def __str__(self) -> str:
        text = '\nProject: {} \nDescription: {} \nTasks: '.format(self.name, self.description)

        for task in self.tasks:
            text += '\n' + str(task)
            
        return text

    def add_task(self, task: object):
        self.tasks.append(task)

    def remove_task(self, taskID: int):
        pass

    def get_task(self, taskID: int):
        pass

    def list_tasks(self):
        pass

class ProjectManager:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        # Provide a string overview of all projects
        pass

    def add_project(self, project: object):
        pass

    def get_project(self, projectID: int):
        pass

    def remove_project(self, projectID: int):
        pass

    def list_all_projects(self):
        pass

################################################
    
# User prompted input for new task