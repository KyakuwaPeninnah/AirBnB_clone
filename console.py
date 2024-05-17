#!/usr/bin/python3
"""Command Interpreter module"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command line interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_EOF(self, arg):
        """Ends the file with Ctrl+D"""
        print()
        return True

    def help_quit(self):
        """Exits the program """
        print("Quit command to exit the program")

    def emptyline(self):
        """Does nothing on empty input line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
