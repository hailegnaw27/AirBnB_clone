#!/usr/bin/python3
"""
Entry point of the command interpreter
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Quit command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing when the user inputs an empty line
        """
        pass
    def do_create(self, arg):
        """
        Create a new instance of BaseModel or User, saves it (to the JSON file)
        and prints the id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in storage.classes:
            print("** class doesn't exist **")
            return

        obj_dict = {}
        for pair in args[1:]:
            key_val = pair.split('=')
            if len(key_val) == 2:
                key, val = key_val[0], key_val[1]
                if val[0] == '"' and val[-1] == '"':
                    val = val[1:-1]
                elif '.' in val:
                    try:
                        val = float(val)
                    except ValueError:
                        pass
                else:
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                obj_dict.update({key: val})

        obj = eval(cls_name)(**obj_dict)
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = '{}.{}'.format(cls_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        print(instance)
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = '{}.{}'.format(cls_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        storage.all().pop(key)
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all instances based on the class name
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in storage.classes:
            print("** class doesn't exist **")
            return

        all_instances = []
        for key in storage.all():
            if key.split('.')[0] == cls_name:
                all_instances.append(str(storage.all()[key]))
            print(all_instances)


    def do_update(self, arg):
        """
        Updates an instance based on the class name and id using a dictionary representation of the attributes
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        cls_name = args[0]
        if cls_name not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = '{}.{}'.format(cls_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** dictionary missing **")
            return

        try:
            attributes_dict = ast.literal_eval(args[2])
        except ValueError:
            print("** invalid dictionary **")
            return

        instance = storage.all().get(key)
    
        for attr, value in attributes_dict.items():
            setattr(instance, attr, value)

        instance.save()

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
