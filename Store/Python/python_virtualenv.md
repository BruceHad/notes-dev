# Python - Virtual Environment

A virtual environment is an isolated working copy of python that lets you work on a project without affecting other python projects. e.g. you can work on a different version of python, or import a different set of libraries without worrying about conflicts.

_virtualenv_ is the tool used to create these VEs. virtualenv can be installed with Pip.

    $virtualenv new_folder 

This creates a new virtual environment, placing it in the named folder.

    $source new_folder/bin/activate

This activates the new folder, effectively changing your $PATH variable. I will also update your CL prompt to show which VE you are working in.

    $deactivate

This de-activates the VE and returns you to core python. To delete a VE you just have to delete the folder.


## virtualenvwrapper

The wrapper is a set of commands that make it easier to manage lots of virtual environments. Not sure I need that just now.

