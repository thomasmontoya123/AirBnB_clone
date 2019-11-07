#!/usr/bin/python3
'''
Base model module
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    Base model class:
    Defines all common attributes/methods for other classes
    '''

    def __init__(self, id=None, created_at=None, update_at=None):
        if id is None:
            self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        dict_to_return = self.__dict__
        dict_to_return["__class__"] = BaseModel.__name__
        dict_to_return["created_at"] = str(datetime.isoformat(self.created_at))
        dict_to_return["update_at"] = str(datetime.isoformat(self.update_at))
        return dict_to_return
