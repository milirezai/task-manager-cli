from task import Task
from datetime import datetime

class App():
    
    def __init__(self, input):
        if input not in [1,2,3,4,5,6,7]:
            self._close()
        self.input = input
        
    def run(self):
        match(self.input):
            case 1:
                return self._create()
            case 2:
                return self._list()
            case 3:
                return self._search()
            case 4:
                return self._update()
            case 5:
                return self._completed()
            case 6:
                return self._delete()
            case 7:
                return self._close()
                
    def _create(self):
            print('\ncreate a new task:')
            taskName = input('task name? ')
            taskDescription = input('task description? ')
            taskStatus = 'uncompleted'    
            taskCreateTime = datetime.now().date().isoformat()
            taskData = [taskName,taskDescription,taskStatus,taskCreateTime]
            Task().create(taskData)
            print('task create successful')
        
    def _list(self):
            print('\nlist all tasks:')
            return Task().list()
    
    def _search(self):
            print('\nsearch a task:')
            key = input('title task? ')
            result = Task().search(key)
            return result         
                   
    def _update(self):
            print('\nupdate a task:')
            taskId = int(input('task id? '))
            taskName = input('task name? ')
            taskDescription = input('task description? ')
            taskStatus = input('task status? ')
            taskCreateTime = datetime.now().date().isoformat()
            task = [taskName,taskDescription,taskStatus,taskCreateTime]
            result = Task().update(id= taskId, data= task)
            print('task update successful' if result else 'no task for update')
    
    def _completed(self):
            print('\ncompleted a task:')
            taskId = int(input('task id? '))
            task = ['', '', 'completed', datetime.now().date().isoformat()]
            Task().update(self= Task,id= taskId, data= task)
            print('task completed successful')
    
    def _delete(self):
            print('\ndelete a task:')
            index = int(input('delete task? '))
            delete = Task().delete(index)
            print('delete task successful' if delete else 'no task for delete')
    
    def _close(self):
            print('app closed')
            exit()