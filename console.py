#!/usr/bin/python3
"""Command Interpreter module"""

from models import storage
from models.base_model import BaseModel
import shlex
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command line interpreter"""

    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quits the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a BaseModel,
        saves it (to the JSON file) and prints the id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """ Prints the string representation of
        an instance based on the class name and id
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                print(objects[key])

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name
        """
        args = shlex.split(arg)

        objects = storage.all()

        if len(args) == 0:
            for obj in objects.values():
                print(str(obj))
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.startswith(args[0]):
                    print(str(value))

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in objects:
                print("** no instance found **")
            else:
                del objects[key]
                storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        """
        args = shlex.split(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                try:
                    attr_value = eval(attr_value)
                except ValueError:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

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
