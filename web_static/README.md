# --- AirBnB clone - Web static ---

# Background context
-------------
**Web static, what?**
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

**Learning objectives**
-------------
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- General
- What is HTML
- How to create an HTML page
- What is a markup language
- What is the DOM
- What is an element / tag
- What is an attribute
- How does the browser load a webpage
- What is CSS
- How to add style to an element
- What is a class
- What is a selector
- How to compute CSS Specificity Value
- What are Box properties in CSS

**Requirements**
-------------
**General**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be W3C compliant and validate with W3C-Validator
- All your CSS files should be in styles folder
- All your images should be in images folder
- You are not allowed to use !important and id (#... in the CSS file)
- You are not allowed to use tags img, embed and iframe
- You are not allowed to use Javascript
- Current screenshots have been done on Chrome 56 or more.
- No cross browsers
- You have to follow all requirements but some margin/padding are missing - you should try to fit as much as you can to screenshots

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
