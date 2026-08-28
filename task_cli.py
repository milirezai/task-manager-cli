from task_service import TaskService
from utility import create_task,update_task


class TaskCli():
    
    def __init__(self, data):
        if data not in [1,2,3,4,5,6,7,8]:
            self._close()
        self.run(data) 
                    
    def run(self,data):
        match(data):
            case 1:
                return self.create()
            case 2:
                return self.all()
            case 3:
                return self.search()
            case 4:
                return self.update()
            case 5:
                return self.completed()
            case 6:
                return self.uncompleted()
            case 7:
                return self.delete()
            case 8:
                return self.close()
                
    def create(self):
            print('\ncreate a new task:')
            task_data = create_task()
            TaskService(task_data).create()
            print('\ncreate a new task successfull')
        
    def all(self):
            print('\nlist all tasks:')
            TaskService().all()
    
    def search(self):
            print('\nsearch a task:')
            key = input('title task? ')
            TaskService(key).search()
                  
    def update(self):
            print('\nupdate a task:')
            task_data = update_task()
            TaskService(task_data).update()
            print('\nupdate a  task successfull')
   
    def completed(self):
            id = int(input('completed task? '))
            TaskService(id).completed()
            print('\ncompleted a task successfull') 

    def uncompleted(self):
            id = int(input('uncompleted task? '))
            TaskService(id).uncompleted()
            print('\nuncompleted a task successfull') 
            
    def delete(self):
            print('\ndelete a task:')
            id = int(input('delete task? '))
            TaskService(id).delete()
            print('\ndelete a task successfull') 
      
    def close(self):
            print('app closed')
            exit()
 