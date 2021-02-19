# --- AirBnB_clone ---

![alt text](https://miro.medium.com/max/2400/0*NChTo-XqLOxLabIW)

**Welcome to our AirBnB clone project! (The Holberton B&B)**

**General**
-------------
As a first step we were asked to write a command interpreter to manage our AirBnB objects. This is the first step towards building our first complete web application: the AirBnB clone. This first step was very important because you will use what we created during this project with all the other projects below: HTML / CSS templates, database storage, API, front-end integration ...

The tasks we carried out were:

Create a main class (called BaseModel) that takes care of the initialization, serialization, and deserialization of new instances.
We create a simple serialization / deserialization flow: Instance <-> Dictionary <-> JSON String <-> file
We create all the classes used for AirBnB (user, state, city, place ...) that all inherit from BaseModel
We create a storage engine to be able to save data.
We create all the unit tests to validate all our classes and storage engine.

**What’s a command interpreter?**
-------------
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

   - Create a new object (ex: a new User or a new Place)
   - Retrieve an object from a file, a database etc…
   - Do operations on objects (count, compute stats, etc…)
   - Update attributes of an object
   - Destroy an object

**How to use the interpreter?**
-------------
Usage in interactive mode:
```
$ ./console.py
```
This: displays a message:
```
(hbnb)
```
and waits for the user to type a command. A command line always ends with a new line. The prompt is displayed again each time a command is executed.

and in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
Here is a simple example of how to use our console
```
(hbnb) create BaseModel
de2630a8-7556-4e6d-8b55-8b0a4ba8082d
(hbnb) show BaseModel de2630a8-7556-4e6d-8b55-8b0a4ba8082d
[BaseModel] (de2630a8-7556-4e6d-8b55-8b0a4ba8082d) {'updated_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 756946), 'created_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 75683\
6), 'id': 'de2630a8-7556-4e6d-8b55-8b0a4ba8082d'}
(hbnb) quit
```

# Files and folders
- models
    - engine
        - __init__.py
        - file_storage.py
    - __init__.py
    - amenity.py
    - base_model.py
    - city.py
    - place.py
    - review.py
    - state.py
    - user.py
    - tests
        - __init__.py
        - test_models
            - __init__.py
            - test_amenity.py
            - test_base_model.py
            - test_city.py
            - test_file_storage.py
            - test_place.py
            - test_review.py
            - test_state.py
            - test_user.py
- console.py
- README.md
- AUTHORS
- airbnbimage.png

# Requirements
-------------
**Python Scripts**
   - Allowed editors: vi, vim, emacs
   - All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
   - All your files should end with a new line
   - The first line of all your files should be exactly #!/usr/bin/python3
   - A README.md file, at the root of the folder of the project, is mandatory
   - Your code should use the PEP 8 style (version 1.7 or more)
   - All your files must be executable
   - The length of your files will be tested using wc
   - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
   - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
   - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
   - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

**Python Unitests**
   - Allowed editors: vi, vim, emacs
   - All your files should end with a new line
   - All your test files should be inside a folder tests
   - You have to use the unittest module
   - All your test files should be python files (extension: .py)
   - All your test files and folders should start by test_
   - Your file organization in the tests folder should be the same as your project
   - e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
   - e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
   - All your tests should be executed by using this command: python3 -m unittest discover tests
   - You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
   - All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
   - All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
   - All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
   - We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# Authors
Made by [Cecilia Giudice](https://github.com/ChechG)
and [Tadeo Grach](https://github.com/tadeograch)
to Holberton School 2021
