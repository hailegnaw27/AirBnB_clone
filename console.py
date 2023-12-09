#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a newline for better formatting
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_help(self, arg):
        """Help command to display available commands"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """
        creates a new model
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            print(storage.all().get(key, "** no instance found **"))
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objects = storage.all()
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            print("** instance id missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        objects_list = []
        all_objects = storage.all()
        args = arg.split()
        if not args or args[0] == "":
            for obj in all_objects.values():
                objects_list.append(str(obj))
        else:
            try:
                class_name = args[0]
                for key, obj in all_objects.items():
                    if class_name == obj.__class__.__name__:
                        objects_list.append(str(obj))
                if len(objects_list) == 0:
                    raise KeyError
                else:
                    print(objects_list)
            except KeyError:
                print("** class doesn't exist **")
    def do_count(self, arg):
        """
        Retrieves the number of instances of a class
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in storage.classes:
            print("** class doesn't exist **")
            return

            count = 0
        for key in storage.all():
            if key.split('.')[0] == cls_name:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute
        """
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objects = storage.all()
            if key not in all_objects:
                print("** no instance found **")
                return

            obj = all_objects[key]

            if len(args) < 3:
                print("** attribute name missing **")
                return

            attr_name = args[2]

            if len(args) < 4:
                print("** value missing **")
                return

            attr_value = args[3]

            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, attr_type(attr_value))
                obj.save()  # Call save after updating the attribute
            else:
                print("** attribute doesn't exist **")

        except IndexError:
            print("** instance id missing **")

        except IndexError:
            print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

