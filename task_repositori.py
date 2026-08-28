from task import Task
from json_storage import JsonStorage
from utility import analysi_tasks,update_task
from datetime import datetime

class TaskRepositori():
    
    def __init__(self, data = None):
        self.data = data
    
    def all(self):
        tasks_list = []
        statuses = []
        for index,task in enumerate(JsonStorage().load()):
            tasks_list.append(Task(
                task.get('id'),task.get('title'),task.get('description'),
                task.get('status'),task.get('created_at'),task.get('updated_at')
            ))
            statuses.append(task.get('status'))
        tasks_list.append(analysi_tasks(tasks_list, statuses))            
        return tasks_list    
        
    def create(self):
        storage = JsonStorage()
        tasks = storage.load()
        id = len(tasks) + 1
        tasks.append({
            "id": id, "title": self.data.get('title'), "description": self.data.get('description'),
            "status": 'uncompleted', "created_at": datetime.now().date().isoformat(), "updated_at": ''
            })
        storage.save(tasks)
        
    def updated(self, data = None):
        data = data if data else self.data
        storage = JsonStorage()
        tasks = storage.load()
        task = storage.load()[data.get('id') - 1]
        if data.get('title'):
            task['title'] = data.get('title')
        if data.get('description'):
            task['description'] = data.get('description')
        if data.get('status'):
            task['status'] = data.get('status')  
        task['updated_at'] = datetime.now().date().isoformat()    
        tasks.pop(task.get('id') -1)
        tasks.insert(task.get('id') - 1 , task)
        storage.save(tasks)            
            
    def completed(self):
        data = {'id': self.data , 'status': 'completed'}
        self.updated(data)

    def uncompleted(self):
        data = {'id': self.data , 'status': 'uncompleted'}
        self.updated(data)
    
    def delete(self):
        storage = JsonStorage()
        tasks = storage.load()
        tasks.pop(self.data - 1)
        storage.save(tasks)
    
    def search_with_title(self):
        search_tasks = []
        for index,task in enumerate(JsonStorage().load()):
            if self.data in task.get('title'):
                search_tasks.append(Task(
                task.get('id'),task.get('title'),task.get('description'),
                task.get('status'),task.get('created_at'),task.get('updated_at')
            ))
        return search_tasks        
            