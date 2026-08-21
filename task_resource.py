
class TaskResource():
    
    @staticmethod
    def make(data):
        return f"\nid: {data.get('index')}. title: {data.get('title')}. description: {data.get('description')}. status: {data.get('status')}. created_at: {data.get('created_at')}"
                