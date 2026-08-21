from storage import Storage
from task_resource import TaskResource

class Task():
    
    def update(self, id, data)-> bool:
        tasks = Storage().load()
        if len(tasks) < id:
            return False
        for index,task in enumerate(tasks):
            if id == index:
                if data[0]:
                    task['title'] = data[0]
                if data[1]:
                    task['description'] = data[1] 
                if data[2]:
                    task['status'] = data[2]
                self.delete(index)
                self.create([task.get('title'),task.get('description'),task.get('status'),task.get('created_at')]) 
                return True
                                   
    def search(self,key)-> str:
        for index,task in enumerate(Storage().load()):
            if key in task.get('title'):
                task['index'] = index
                print(TaskResource.make(task))
                        
    def delete(self,index)-> bool:
        storge = Storage()
        data = storge.load()
        if data:
            data.pop(index)
            storge.save(data)
            return True
        else:
            return False
                    
    def create(self,data: list)-> None:
        storeage = Storage()
        data_append = storeage.load()
        data_append.append({"title": data[0],"description": data[1],"status": data[2],"created_at":data[3]})
        storeage.save(data_append)
                    
    def list(self)-> str:
        for index,task in enumerate(Storage().load()):
            task['index'] = index
            print(TaskResource.make(task))
            