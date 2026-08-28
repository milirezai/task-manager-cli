from task_repositori import TaskRepositori
from utility import task_serialize,show_task_analysis
from task_validation import TaskValidation

class TaskService():
    
    def __init__(self, data = None):
        self.data = data
    
    def update(self):
        TaskRepositori(self.data).updated()
        
    def completed(self):
        TaskRepositori(self.data).completed()
        
    def uncompleted(self):
        TaskRepositori(self.data).uncompleted()
                                                  
    def search(self):                       
        tasks = TaskRepositori(self.data).search_with_title()
        for task in enumerate(tasks):
            print(task_serialize(task[1]))
                            
    def delete(self):
        TaskRepositori(self.data).delete()
                        
    def create(self):
        TaskValidation(self.data).validate()
        TaskRepositori(self.data).create()       
                     
    def all(self):
        tasks = TaskRepositori().all()
        analysi = tasks[-1]
        tasks.pop()
        for task in enumerate(tasks):
            print(task_serialize(task[1]))
        show_task_analysis(analysi)
        