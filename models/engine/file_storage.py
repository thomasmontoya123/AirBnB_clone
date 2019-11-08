#!/usr/bin/python3
'''
File storage module
'''
import json
from datetime import datetime


class FileStorage():
    '''
    Serialization-deserialization
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        Returns the dictionary __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key <obj class name>.id
        '''
        new_directory = obj.__dict__
        new_directory["created_at"] = datetime.isoformat(new_directory["created_at"])
        new_directory["updated_at"] = datetime.isoformat(new_directory["updated_at"])
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = new_directory   

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path)
        '''
        with open(self.__file_path, "w", encoding='utf-8') as f:
            opened = self.__objects
            f.write(json.dumps(opened))

    def reload(self):
        '''
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        '''
        try:
            with open(self.__file_path,  encoding='utf-8') as f:
                readed = f.read()
                self.__objects = json.loads(readed)
        except Exception:
            pass
