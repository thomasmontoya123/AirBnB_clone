#/usr/bin/python3
import json

class FileStorage()
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects

    
    def new(self, obj):
        self.__objects['{} {}'.format(type(obj).__name, obj.id)] = obj.__dict__
    
    def save(self):
        
        pass
    
    def reload(self):
        pass

    