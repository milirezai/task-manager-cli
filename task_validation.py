from exception import TaskException

class TaskValidation():
    
    def __init__(self, task):
        self.task = task
        
    def validate(self):
        if self.task.get('title'):
            self.title_validate(self.task.get('title'))
        if self.task.get('description'):
            self.description_validate(self.task.get('description'))
        if self.task.get('status'):
            self.status_validate(self.task.get('status'))
                        
    def title_validate(self, title: str):
        if title is None or len(title) < 2:
            raise TaskException('title is not leng')
                            
    def description_validate(self, description: str):
        if description is None or len(description) < 5 or len(description) > 30:
            raise TaskException('description is not leng')
    
    def status_validate(self, status: str):
        if status not in ['uncompleted','completed']:
            raise TaskException('status invalid')
    