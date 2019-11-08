#!/usr/bin/python3
'''
Console module, contains the entry point of the command interpreter
'''
import cmd


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


def main():
    HBNBCommand().cmdloop()

main()
