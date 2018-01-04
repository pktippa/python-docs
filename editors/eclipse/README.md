# Eclipse for Python Editor

## Importing Project in PyDev - Eclipse

* Clone the original or forked repo.

```sh
$ git clone https://github.com/pktippa/he-brainwaves-17-1.git
```

* Change the perspective to PyDev. Window -> Perspective -> Open Perspective -> Other -> (select) PyDev and Open
* In Eclipse, File -> Import -> Git -> Projects From Git -> Existing Local Repository -> 

If the repo not show, click on 'Add' and then browse to clone repo.

* After sucessfully imported the project, To configure as PyDev Project. Right Click on Project -> PyDev -> Set as PyDev Project.

* If there are any errors while resolving the Python interpreter.(May happen if the Python is installed from Anaconda)

Go to Window -> Preferences -> PyDev -> Interpreters -> Python Interpreter -> If interpreter shows error or no interpreter is present.

Click on Add -> Browse to Anaconda installed folder and point to python (exe for Windows) interpreter and add. This will load the libraries also, click on Save, Apply and Close.

It will take some time since it has to load all the resources into cache.