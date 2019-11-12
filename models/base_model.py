#!/usr/bin/python3
'''
Base model module
'''
import uuid
import models
from datetime import datetime


def isotime(datestring):
    '''
    isotime function
    '''
    datestring = str(datestring)
    return datestring.replace('T', " ")


def fromisoformat(datestring):
    '''
    fromisoformat function
    '''
    format_date = '%Y-%m-%d %H:%M:%S.%f'
    return datetime.strptime(isotime(datestring), format_date)


class BaseModel:
    '''
    Base model class:
    Defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def __repr__(self):
        '''return a string representation'''
        return self.__str__()

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_to_return = dict(self.__dict__)
        dict_to_return["__class__"] = str(type(self).__name__)
        dict_to_return["created_at"] = self.created_at.isoformat()
        dict_to_return["updated_at"] = self.updated_at.isoformat()
        return dict_to_return
