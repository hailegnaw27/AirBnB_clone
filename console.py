#!/usr/bin/python3
"""
Module documentation goes here
"""

import cmd
import json
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            key = args[0] + "." + args[1]
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instances = models.storage.all()
            key = args[0] + "." + args[1]
            if key in instances:
                del instances[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances"""
        args = arg.split()
        instances = models.storage.all()
        if len(args) == 0:
            print([str(instance) for instance in instances.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            filtered_instances = [str(instance) for instance in instances.values()
                                  if type(instance).__name__ == args[0]]
            print(filtered_instances)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
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
            instances = models.storage.all()
            key = args[0] + "." + args[1]
            if key in instances:
                instance = instances[key]
                attribute_name = args[2]
                attribute_value = args[3].strip("\"'")
                setattr(instance, attribute_name, attribute_value)
                instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

