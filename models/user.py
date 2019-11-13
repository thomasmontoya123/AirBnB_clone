#!/usr/bin/python3
'''User Module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
