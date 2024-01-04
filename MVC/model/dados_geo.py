import json


class DadosGeo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        
    def carregar_dados(self):
        with open(self.file_path, 'r') as file:
            self.data = json.load(file)
            
    def get_dados(self):
        return self.data
    
    
