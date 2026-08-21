import json

class Storage():
    
    def __init__(self, path: str ='storage/data.json'):
        self.path = path
            
    def load(self):
        with open(self.path, 'r') as file:
            return json.load(file)
    
    def save(self, data: list):
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)
       