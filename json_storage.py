import json

class JsonStorage():
    
    def __init__(self, path: str = 'data/data.json'):
        self.path = path
        
    def load(self):
        with open(self.path,'r') as file:
            return json.load(file)
    
    def save(self, data):
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)            
        