#!/usr/bin/python3
""" console time """
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
 
class HBNBCommand(cmd.Cmd):
    """ class of console commands """
    prompt = "(hbnb) "
 
    def do_EOF(self, args):
        """ exit the program """
        print()
        return True
 
    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """ Nothing going on """
        pass
 
    def do_create(self, args):
        """ Creates instances of class """
        if not args:
            print("** class name missing **")
        elif args != self.__class__.__name__:
            print("** class doesn't exist **")
        else:
            new = self.__class__.__name__.__init__()
            print(new.id)
            new.save()
 
    def do_show(self, args):
        """ Str representation of instances """
        i = args.split()
        if not args:
            print("** class name missing **")
            return
        elif i[0] != self.__class__.__name__:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        key_search = "{}.{}".format(i[0], i[1])
        if key_search not in storage.all().keys():
            print("** no instance found **")
        else:
            new_obj = storage.all()
            print("[{}] ({}) {}".format(i[0], i[1], new_obj[key_search]))
 
    def do_destroy(self, args):
        """ Deletes instances based on ID """
        i = args.split()
        if not args:
            print("** class name missing **")
            return
        elif i[0] != self.__class__.__name__:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        key_search = "{}.{}".format(i[0], i[1])
        if key_search not in storage.all().keys():
            print("** no instance found **")
        else:
            new_obj = storage.all()
            del new_obj[key_search]
            with open("file.json", mode='r') as my_file:
                json_data = json.load(my_file)
                del json_data[key_search]
            with open("file.json", mode='w') as my_f:
                my_f.write(json.dumps(json_data))
 
    def do_all(self, args):
        """ Prints all the str representation of the instances """
        list_obj=[]
        new_obj = storage.all()
        if args and args != self.__class__.__name__:
            print("** class doesn't exist **")
            return
        for key, value in new_obj.items():
            list_obj.append(str(key) + " " + str(value))
        print((list_obj))
    
    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding or updating attribute """
        i = args.split()
        if not args:
            print("** class name missing **")
            return
        elif i[0] != self.__class__.__name__:
            print("** class doesn't exist **")
            return
        elif len(i) == 1:
            print("** instance id missing **")
            return
        key_search = "{}.{}".format(i[0], i[1])
        if key_search not in storage.all().keys():
            print("** no instance found **")
            return
        if len(i) == 2:
            print("** attribute name missing **")
            return
        if len(i) == 3:
            print("** value missing **")
            return
        for key, value in storage.all().items():
            if key == key_search:
                for key2 in value.keys():
                    if key2 == i[2]:
                        value[key2] = i[3]
                        return
                value[i[2]] = i[3]
                return

if __name__ == "__main__":
    HBNBCommand().cmdloop()