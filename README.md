# 0x00. AirBnB clone - The console
---
<img align="center" src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png"  width="100%"/>

## Welcome to the AirBnB clone project! (The Holberton B&B)

---
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
## What’s a command interpreter?
Do you remember the linux Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

## Build:
* Build using python 3.4
* Pep8 codestyle
* Tested with unnitest module(Use this command to test: ```sh python3 -m unittest discover tests ```)
## Execution:
work like this in interactive mode:

```sh
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also works in non-interactive mode:

```sh
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
Authors:
* **Thomas Montoya** - *Initial Work and Documentación* - [Thomasmontoya123](https://github.com/thomasmontoya123)
* **Jonathan Cardenas** - *Initial Work and Documentación* - [guxal](https://github.com/guxal)