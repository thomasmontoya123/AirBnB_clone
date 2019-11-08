#!/usr/bin/python3
'''
Console module, contains the entry point of the command interpreter
'''
import cmd
<<<<<<< HEAD
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
=======
>>>>>>> e463916b8ed6643601307961fdbd6f4b7ee497b7


class HBNBCommand(cmd.Cmd):
    '''
    Console class, containing console methods and attrs
    '''
    prompt = '(hbnb) '

    def do_quit(self, line):
        '''Quit command to exit the program'''
        exit()

    def do_EOF(self, line):
        '''EOF close the console'''
        return True

    def emptyline(self):
        pass

<<<<<<< HEAD
    def do_create(self, line):
        '''Creates a new instance of BaseModel, saves it (to the JSON file)'''
        if len(line) < 2:
            print("** class name missing **")
            return
        else:
            splited = line.split()
            try:
                new_instance = eval(splited[0] + "()")
                print((new_instance.__dict__)["id"])
                new_instance.save()
            except Exception:
                print("** class doesn't exist **")

    def do_show(self):
        '''Prints the string representation of an instance based on the class name and id'''
        pass

    def do_destroy(self):
        '''Deletes an instance based on the class name and id (save the change into the JSON file'''

    def do_all(self, line):
        '''Prints all string representation of all instances based or not on the class name.'''
        pass

    def do_update(self, class_name, id):
        '''Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) '''
        pass