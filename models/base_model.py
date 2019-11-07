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

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        args_len = len(args)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if args_len == 0:
            for key, value in kwargs.items():
                if key == "created_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

    def __str__(self):
        return "[{}] ({}) {}".format(BaseModel.__name__,
                                     self.id, self.__dict__)

    def save(self):
        self.update_at = datetime.now()

    def to_dict(self):
        dict_to_return = self.__dict__
        dict_to_return["__class__"] = BaseModel.__name__
        dict_to_return["created_at"] = str(datetime.isoformat(self.created_at))
        dict_to_return["updated_at"] = str(datetime.isoformat(self.updated_at))
        return dict_to_return
