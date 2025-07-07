import csv
from django.core.exceptions import ValidationError
    
class DataLoader:
    fileRoot = ""
    file = ""
    decoded_file = ""
    
    def __init__(self, file):
        self.file = file
        
    def loadData(self):
        reader = csv.reader(self.decoded_file.splitlines())
        return list(reader)
            
    def validate(self):
        try:
            self.decoded_file = self.file.read().decode('utf-8')
            csv.Sniffer().sniff(self.decoded_file)
            
            return True
        except Exception as e:
            #raise ValidationError("El archivo no es un CSV válido.") from e
            return None