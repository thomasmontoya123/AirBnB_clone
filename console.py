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

allowed_classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]


class HBNBCommand(cmd.Cmd):
    '''
    Console class, containing console methods and attrs
    '''
    prompt = '(hbnb) '

    def do_quit(self, input_line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, input_line):
        '''EOF close the console'''
        return True

    def emptyline(self):
        '''Empty line'''
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

    def do_all(self, input_line, flag=True):
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

            for single_instance in instances.keys():
                if single_instance.split('.')[0] == splited_input[0]:
                    instances_list.append(instances[single_instance].__str__())

            if flag is True:
                print(instances_list)

            else:
                return(len(instances_list))

    def do_update(self, input_line):
        '''Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file),
        only one attribute at a time)'''

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

    def default(self, input_line):
        '''Method called on an input line when
        the command prefix is not recognized'''

        splited_input = input_line.split('.')

        if splited_input[1] == "all()":
            HBNBCommand.do_all(self, splited_input[0], True)
            return

        elif splited_input[1] == "count()":
            instance_counter = HBNBCommand.do_all(self,
                                                  splited_input[0], False)
            print(instance_counter)
            return

        elif "show" in splited_input[1]:
            id_from_input_line = splited_input[1].split('(')
            id_from_input_line = id_from_input_line[1][1:-2]
            argument_to_pass = splited_input[0] + " " + id_from_input_line
            HBNBCommand.do_show(self, argument_to_pass)
            return

        elif "destroy" in splited_input[1]:
            id_from_input_line = splited_input[1].split('(')
            id_from_input_line = id_from_input_line[1][1:-2]
            argument_to_pass = splited_input[0] + " " + id_from_input_line
            HBNBCommand.do_destroy(self, argument_to_pass)
            return

        elif ("update") in splited_input[1]:
            '''After the fisrst dot'''
            args_from_input_line = splited_input[1].split('(')
            args_from_input_line = args_from_input_line[1][1:-2]
            argument_to_pass = splited_input[0] + " " + args_from_input_line
            '''clean the line removing unncesary signs'''
            argument_to_pass = argument_to_pass.replace(',', "")
            argument_to_pass = argument_to_pass.replace('"', "")
            '''check if we have a dir in the line'''
            dict_checker = args_from_input_line.split(',')
            '''just the object id'''
            object_id = dict_checker[0].replace('"', "")
            if "{" in dict_checker[1]:
                '''get everithing inside the dir '''
                dict_to_pass = dict_checker[1:]
                index = 0
                for i in range(len(dict_to_pass)):
                    argumen_from_dict = dict_to_pass[index]
                    argumen_from_dict = argumen_from_dict.replace("{", "")
                    argumen_from_dict = argumen_from_dict.replace("'", "")
                    argumen_from_dict = argumen_from_dict.replace('"', "")
                    argumen_from_dict = argumen_from_dict.replace(":", "")
                    '''clean the keys and the values'''
                    argumen_from_dict = (splited_input[0] + " " +
                                         object_id + argumen_from_dict)
                    '''join all the line to give to the function,
                    Class Id key value'''
                    HBNBCommand.do_update(self, argumen_from_dict)
                    index += 1
            else:
                HBNBCommand.do_update(self, argument_to_pass)

        elif ("{}") in splited_input[1]:
            print("yes")

        else:
            print("*** Unknown syntax: {}".format(input_line))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
