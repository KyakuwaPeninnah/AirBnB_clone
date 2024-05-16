#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
import json

class HBNBCommand(cmd.Cmd):
    """This is the command line class inheriting from the cmd"""
    prompt = "(hbnb) "
    

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = arg[0]
        if class_name not in storage.classes:
            print("**class doesn't exist**")
            return
        the_instance = storage.classes[class_name]()
        the_instance.save()


    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if not arg:
            print("**class name is missing**")
            return
        args = arg.split()
        if len(args) < 1:
            print("**class name is missing**")
            return
        class_name = arg[0]
        if args not in storage.classes:
            print("**class doesn't exist**")
            return
        if len(args) < 2:
            print("**instance id missing**")
            return
        instance_id = args[1]
        instance = storage.get(class_name, instance, id)
    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""

    def do_quit(self, arg):
        """This is the quit command documentation"""
        return True
    def do_EOF(self, arg):
        """This is the EOF command that also quits the console"""
        return True

    def empty_line(self):
        """Doesn't do anything when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
