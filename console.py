#!/usr/bin/python3
'''
Console module, contains the entry point of the command interpreter
'''
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import sys
import inspect
from models.__init__ import storage
import json
from datetime import datetime

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
        '''Creates a new instance of BaseModel, saves it (to the JSON file)'''
        splited_line = input_line.split()
        splited_line_len = len(splited_line)
        if splited_line_len < 1:
            print("** class name missing **")
            return
        else:
            imported_classes = [value[0] for value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]
            if splited_line[0] in imported_classes:
                new_instance = eval(splited_line[0] + "()")
                print((new_instance.__dict__)["id"])
                new_instance.save()
            else:
                print("** class doesn't exist **")

    def do_show(self, input_line):
        '''Prints the string representation of an instance based on the class name and id'''
        splited_line = input_line.split()
        splited_line_len = len(splited_line)
        if splited_line_len < 1:
            print("** class name missing **")
            return
        imported_classes = [value[0] for value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]
        if splited_line[0] not in imported_classes:
            print("** class doesn't exist **")
            return
        if splited_line_len < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        for single_instance in instances:
            getting_id = single_instance.split(".")
            if splited_line[1] == getting_id[1]:
                print(instances[single_instance])
                break
            else:
                print("** no instance found **")
                break

    def do_destroy(self, input_line):
        '''Deletes an instance based on the class name and id (save the change into the JSON file'''
        splited_line = input_line.split()
        splited_line_len = len(splited_line)
        if splited_line_len < 1:
            print("** class name missing **")
            return
        imported_classes = [value[0] for value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]
        if splited_line[0] not in imported_classes:
            print("** class doesn't exist **")
            return
        if splited_line_len < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        for single_instance in instances:
            getting_id = single_instance.split(".")
            if splited_line[1] == getting_id[1]:
                del instances[single_instance]
                storage.save()
                break
            else:
                print("** no instance found **")
                break

    def do_all(self, input_line):
        '''Prints all string representation of all instances based or not on the class name.'''
        splited_line = input_line.split()
        splited_line_len = len(splited_line)
        if splited_line_len < 1:
            print("** class name missing **")
            return
        imported_classes = [value[0] for value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]
        if splited_line[0] not in imported_classes:
            print("** class doesn't exist **")
            return
        else:
            instances = storage.all()
            instances_list = []
            for single_instance in instances:
                instances_list.append(instances[single_instance])
            print(instances_list)

    def do_update(self, input_line):
        '''Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file), only one attribute at a time '''
        splited_line = input_line.split()
        splited_line_len = len(splited_line)
        if splited_line_len < 1:
            print("** class name missing **")
            return
        imported_classes = [value[0] for value in inspect.getmembers(sys.modules[__name__], inspect.isclass)]
        if splited_line[0] not in imported_classes:
            print("** class doesn't exist **")
            return
        if splited_line_len < 2:
            print("** instance id missing **")
            return
        instances = storage.all()
        if instances == {}:
            return
        for single_instance in instances:
            getting_id = single_instance.split(".")
        if splited_line[1] == getting_id[1]:
            obj_reference = splited_line[0] + "." + splited_line[1]
            single_instance = instances[obj_reference]
            cant_update_attributes = ["id", "created_at", "updated_at"]
            if obj_reference in instances.keys():
                if splited_line_len < 3:
                    print("** attribute name missing **")
                elif splited_line_len < 4:
                    print("** value missing **")
                elif splited_line[2] in cant_update_attributes:
                    return
                else:
                    single_instance.__dict__[splited_line[2]] = splited_line[3]
                    single_instance.updated_at = datetime.now()
                    storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
