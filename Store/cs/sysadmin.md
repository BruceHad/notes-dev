

# Linux Overview

The operating system consists of a kernal and some system programs. The kernel is the heart of the computer, providing the basic services from which all other services are built. The computer hardware is accessed via the kernel. These kernel tools are accessed via _system calls_. System programs run on top of the kernel and build out the full operating system.

Compilers can be built into the operating system (e.g the [GCC](https://en.wikipedia.org/wiki/GNU_Compiler_Collection) on linux). 


## Files and Access

Files are central to Unix. Folders are files, devices are files, commands are files. Linux access is largely controlled by file access.

Files have two owners, the Group and the Owner. Permissions can be set for Owner, Group or Other (basically anyone else), which allows for flexible and fairly fine grained control of access to files, although other options are available such as ACL ([access control list](https://en.wikipedia.org/wiki/Access_control_list)) for more complex situations.

By default, the person who has created a file will be set as the Owner and that person's primary Group is set as the Group owner. These can be changed using the  CHOWN or CHGRP commands. Linux can also be set up to set the Group to the Group of the containing folder (BSD style).

    chown bruce file1

You can also change the Owner and Group at the same time, and use the Recursive option to change all files under a specific folder.

    chown bruce:admin /path/to/folder/

All of the files on a system have permissions that allow or prevent others from viewing, modifying or executing. The super user "root" has the ability to access any file on the system.

There are three levels of actions that can be controlled by a files permissions: Read, Write and Execute. Read and Write allow the user/group to Read or Edit the file, while execute allows the file to be run as a program. Folders (files of type 'directory') are slightly different. Read allows the folder to be view (i.e. LS), Write allows the contents of the folder to be deleted or files added and Execute allows the user/group to open the folder (e.g. CD to it). Folder must have execute permissions to work as folders.

On the command line, a files permissions are represented by 10 bits of information. e.g:

    -rwxr--r--

The first bit represents the file type:

* regular (-)
* directory (d)
* character special (c)
* block special (b)
* fifo (p)
* symbolic link (l)
* socket (s)

The following 9 bits show the three (Read, Write or Execute) flags for the File Owner, File Group or Other respectively. So in the above example, it is a regular file where the owner has Read/Write/Execute priviledges, but the others have only Read.

Alternatively, the permissions can be shown/set numerically. In this case, the permissions are set by three values, one for Owner, Group or Other. The values are determined by the sum of the values:

* Read - 4
* Write - 2
* Execute - 1

For example, read/write can be represent by the number 6 and Read/Write/Execute is 7. Note: 0 means no permissions (equivalent to ---).

## Changing File Permissions

The files permission can be changed using the CHMOD command (stands for Change Mode).

    chmod {options} filename

Options are:

u - owner
g - group
o - other
a - all (same as ugo)
x - execute
w - write
r - read
+ - add
- - remove
= - set

For example:

    chmod o+rw file1

This will add Read and Write access for Others.

    chmod 666 file1

This will set Read and Write access to all.

To change the file permissions recursively (i.e. all the files contained in a specified folder) you can add the -R options.

For example:
    
    chmod 666 -R path/to/folder/ 

# Documentation

A man page (short for manual page) is a form of online software documentation usually found on a Unix or Unix-like operating system. Topics covered include computer programs (including library and system calls), formal standards and conventions, and even abstract concepts. A user may invoke a man page by issuing the man command.

	man <command_name>

[Linux man pages can be found here](http://linux.die.net/man/). They are usually formed into 8 sections:

1 	General commands
2 	System calls
3 	Library functions, covering in particular the C standard library
4 	Special files (usually devices, those found in /dev) and drivers
5 	File formats and conventions
6 	Games and screensavers
7 	Miscellanea
8 	System administration commands and daemons

Sections for the same command can sometimes be found in multiple sections.

The [apropos command](http://www.linfo.org/apropos.html) can be used to list contents and search keywords in the man pages.

# Linux Applications

## Burning CDs

Wodim is a handy, command line tool for burning CDs. Not sure how widely supported it is, but appears to be on Ubuntu by default.

First, type 

	wodim --devices 

in order to get the identifier for your device.

Then, type the following to actually burn an iso image:

	wodim dev=/dev/scXX -v systemrescuecd-x86-x.y.z.iso    

For instance:

wodim dev=/dev/sr0 speed=8 -v sysresccd-x.y.z.iso

Lots of options to investigate.

## MD5Sum

The program md5sum is designed to verify data integrity using the MD5 (Message-Digest algorithm 5) 128-bit cryptographic hash. MD5 hashes used properly can confirm both file integrity and authenticity.

First open a terminal and go to the correct directory to check a downloaded iso file:

	ubuntu@ubuntu-desktop:~$ cd Downloads

Then run the following command from within the download directory.

	md5sum ubuntu-11.10-dvd-i386.iso

md5sum should then print out a single line after calculating the hash:

	8044d756b7f00b695ab8dce07dce43e5 ubuntu-11.10-dvd-i386.iso

Compare the hash (the alphanumeric string on left) that your machine calculated with the corresponding hash.

# Links 

A link is a mechanism that allows several filenames (actually, directory entries) to refer to a single file on disk. There are two kinds of links: hard links and symbolic or soft links. A hard link associates two (or more) filenames with the same inode. Hard links are separate directory entries that all share the same disk data blocks. For example, the command:

    $ ln index hlink

This creates an entry in the current directory named hlink with the same inode number as index, and the link count in the corresponding inode is increased by 1. Hard links may not span filesystems, because inode numbers are unique only within a filesystem. In addition, hard links should be used only for files and not for directories, and correctly implemented versions of ln won't let you create the latter.

Symbolic links, on the other hand, are pointer files that refer to a different file or directory elsewhere in the filesystem. Symbolic links may span filesystems, because they point to a Unix pathname, not to a specific inode.

Symbolic links are created with the -s option to ln .

## Symbolic Link (SymLink)

A symbolic link (also symlink or soft link) is a special type of file that contains a reference to another file or directory in the form of an absolute or relative path and that affects pathname resolution. 

SymLinks are present in most Unix-like and also Windows operating systems.

Symbolic links operate transparently for most operations: programs which read or write to files named by a symbolic link will behave as if operating directly on the target file. However, programs that need to handle symbolic links specially (e.g., backup utilities) may identify and manipulate them directly.

A symbolic link contains a text string that is automatically interpreted and followed by the operating system as a path to another file or directory. This other file or directory is called the "target". The symbolic link is a second file that exists independently of its target. 

If a symbolic link is deleted, its target remains unaffected. 

If a symbolic link points to a target, and sometime later that target is moved, renamed or deleted, the symbolic link is not automatically updated or deleted, but continues to exist and still points to the old target, now a non-existing location or file.

Symbolic links may point to any file or directory irrespective of the volumes on which the source and destination reside.

In POSIX-compliant operating systems, symbolic links are created with the symlink()[2] system call. The ln shell command normally uses the link()[3] system call, which creates a hard link. When the ln -s flag is specified, the symlink() system call is used instead, creating a symbolic link.

In linux, the following command creates a symbolic link at the command-line interface (shell):

	ln -s source_file link_name

source_file is the relative or absolute path to which the symlink should point. Usually the target will exist, although symbolic links may be created to non-existent targets. link_name is the desired name of the symbolic link.

Symbolic Links can be removed using the unlink command.

	unlink link_name
	
# Performance

https://sites.google.com/site/easylinuxtipsproject/bugs

Tried fixing the 'swappiness value' to see if it speeds things up. Didn't seem to make a difference.

    cat /proc/sys/vm/swappiness
    sudo gedit /etc/sysctl.conf
    
# Disk Space

# Aliases

You can alias commonly used commands.

    alias newcommand='yourcommand -arguments'

e.g. I often use ls -l to list the contents of a directory in long form. It would be quicker presumably to have.

    alias ls='ls -l'

Try 

    compgen -a

to list all available aliases.
