#!/usr/bin/python3
"""Command Interpreter module"""


from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.user import User
from models import storage
from models.base_model import BaseModel
import shlex
import cmd


class HBNBCommand(cmd.Cmd):
    """Class for the command line interpreter"""

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place",
               "State", "City", "Review", "Amenity"]

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
            storage.save()
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

    def default(self, arg):
        """ retrieve all instances of a class by
        using: <class name>.all()
        """
        if ".all()" in arg:
            class_name = arg.split('.all()')[0]
            if class_name in self.classes:
                self.do_all(class_name)
            else:
                print("** class doesn't exist **")
        elif ".count()" in arg:
            class_name = arg.split('.count()')[0]
            if class_name in self.classes:
                self.do_count(class_name)
            else:
                print("** class doesn't exist **")
        elif ".show(" in arg:
            class_name, id_part = arg.split('.show(')
            required_id = id_part[:-1]
            if class_name in self.classes:
                self.do_show("{} {}".format(class_name, required_id))
            else:
                print("** class doesn't exist **")
        elif ".destroy(" in arg:
            class_name, id_part = arg.split('.destroy(')
            required_id = id_part[:-1]
            if class_name in self.classes:
                self.do_destroy(f"{class_name} {required_id}")
            else:
                print("** class doesn't exist **")
        elif ".update(" in arg:
            class_name, rest_part = arg.split('.update(')
            rest_part = rest_part.rstrip(")")
            parts = rest_part.split(",")
            instance_id = parts[0].strip('"')
            attr_name = parts[1].strip('"')
            attr_value = parts[2].strip('"')
            if class_name in self.classes:
                self.do_update("{} {} {} {}".format(
                    class_name, instance_id, attr_name, attr_value))
            else:
                print("** class doesn't exist **")
        else:
            print("***Unknown syntax:{}".format(arg))

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
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

    def do_count(self, arg):
        """Retrieves number of objects based on class name"""
        count = 0
        for key, value in storage.all().items():
            if arg == key.split(".")[0]:
                count += 1
        print(count)

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
