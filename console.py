#!/usr/bin/env python3
'''
Console module, contains the entry point of the command interpreter
'''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage
import json
from datetime import datetime
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

allowed_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    '''
    Console class, containing console methods and attrs
    '''
    prompt = '(hbnb) '

    def do_quit(self, input_line):
        '''Quit command to exit the program'''
        exit()

    def do_EOF(self, input_line):
        '''EOF close the console'''
        return True

    def emptyline(self):
        pass

    def do_create(self, input_line):
        '''Creates a new instance of an allowed Class and
        saves it (to the file.JSON file)'''

        splited_input = input_line.split()
        splited_input_len = len(splited_input)

        if splited_input_len < 1:
            print("** class name missing **")
            return

        else:
            if splited_input[0] in allowed_classes:
                new_instance = eval(splited_input[0] + "()")
                print((new_instance.__dict__)["id"])
                new_instance.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, input_line):
        '''Prints the string representation of
        an instance based on the class name and id'''

        splited_input = input_line.split()
        splited_input_len = len(splited_input)

        if splited_input_len < 1:
            print("** class name missing **")
            return

        if splited_input[0] not in allowed_classes:
            print("** class doesn't exist **")
            return

        if splited_input_len < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        obj_reference = splited_input[0] + "." + splited_input[1]

        if obj_reference in instances.keys():
            print(instances[obj_reference])
        else:
            print("** no instance found **")

    def do_destroy(self, input_line):
        '''Deletes an instance based on the class
        name and id (save the change into the JSON file'''

        splited_input = input_line.split()
        splited_input_len = len(splited_input)
        if splited_input_len < 1:
            print("** class name missing **")
            return

        if splited_input[0] not in allowed_classes:
            print("** class doesn't exist **")
            return

        if splited_input_len < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        obj_reference = splited_input[0] + "." + splited_input[1]

        if obj_reference in instances.keys():
            del instances[obj_reference]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, input_line):
        '''Prints all string representation of
        all instances based or not on the class name.'''

        splited_input = input_line.split()
        splited_input_len = len(splited_input)

        if splited_input_len < 1:
            print("** class name missing **")
            return

        if splited_input[0] not in allowed_classes:
            print("** class doesn't exist **")
            return

        else:
            instances = storage.all()
            instances_list = []

            for single_instance in instances:
                instances_list.append(instances[single_instance])
            print(instances_list)

    def do_update(self, input_line):
        '''Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file),
        only one attribute at a time '''

        splited_input = input_line.split()
        splited_input_len = len(splited_input)

        if splited_input_len < 1:
            print("** class name missing **")
            return

        if splited_input[0] not in allowed_classes:
            print("** class doesn't exist **")
            return

        if splited_input_len < 2:
            print("** instance id missing **")
            return

        instances = storage.all()
        obj_reference = splited_input[0] + "." + splited_input[1]

        if obj_reference in instances.keys():
            single_instance = instances[obj_reference]
            cant_update_attributes = ["id", "created_at", "updated_at"]
            if splited_input_len < 3:
                print("** attribute name missing **")
                return

            elif splited_input_len < 4:
                print("** value missing **")
                return

            elif splited_input[2] in cant_update_attributes:
                return

            else:
                single_instance.__dict__[splited_input[2]] = splited_input[3]
                single_instance.updated_at = datetime.now()
                storage.save()
        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
