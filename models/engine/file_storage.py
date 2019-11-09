#!/usr/bin/python3
'''
File storage module
'''
import json
from models.base_model import BaseModel
from models.user import User


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
        if obj:
            keyid = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[keyid] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file (path: __file_path)
        '''
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding='UTF-8') as f:
            json.dump(my_dict, f)

    def reload(self):
        '''
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        '''
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                for key, value in (json.load(f)).items():         
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
