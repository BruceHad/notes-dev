# Linux Path Variable

http://www.linfo.org/path_env_var.html

The PATH is an environmental variable in *nix like systems that tells the shell which directories to search for _executable_ files. Make is convenient to run programs.

A user's PATH consists of a series of colon-separated _absolute_ paths stored in plain text files. Whenever a user types a command (that's not built into the shell) the shell searches through those directories until it finds a matching executable.

A list of environment variables (including PATH) can be shown with the env command.

    env

The PATH can be shown in a couple of ways.

    env | grep PATH
    echo $PATH

Each user can have different PATH.

Path variables can be changed for the _current_ session or permanently.

    PATH="/usr/sbin:$PATH"

This update the current session, where _directory_ is the full path. 

    export PATH=$PATH:/usr/sbin

Does the same thing.

A permanent change can be added to a user's bash profile. In Ubuntu this is called .profile.

    gedit ~/.profile

To add a directory named /usr/test to a user's PATH variable, it should be appended with a text editor to the line that begins with PATH so that the line reads something like PATH=$PATH:$HOME/bin:/usr/test. It is important that each absolute path be directly (i.e., with no intervening spaces) preceded by a colon. 

Alternatively, you can add export commands to the .profile.

There is also the environment file.

    gedit /etc/environment

Or the profile file:

    gedit /etc/profile

Or the bashrc file

    gedit ~/.bashrc

To reload .profile after any changes just type:

    . ~/.profile

