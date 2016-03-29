#Git & Github

[Version Control][4] manages changes to documents and files. This can be complicated, especially when there are a large number of people working on the same project/files. There is software to help manage Version Control. 

Git is a distributed VCS that tracks software revisions and allows many developers to work on a given project without necessarily being connected to a common network.

[GitHub][3] is a web-based hosting service for software development projects that use the Git revision control system. So you can host/backup the project files online. It also adds social features that let you track other projects/developers.

# Git Notes

## Initial Set Up

Install git locally and set up username and email address.

git config --global user.name "Your Name Here"
git config --global user.email "your_email@youremail.com"

Note, if using Github, email addresses should match.

## Init

Create a new folder to hold all project documents and start work on your project. Once you have some intial documents (e.g. a README) cd to the folder then:

    git init        -- set up the git files in the folder.
    git add .       -- adds all files in the folder, or
    git add README index.html   -- add individual file.
    git commit      -- commits all changes to the project.
    git status      -- tells you the status of the project.

## Commit Messages

When committing you will be prompted to set a commit message. The commit message should be made up of:

Single line description (50 chars)
---- blank line ----
Detailed description, including reason for change etc. Imperative present tense recommended. Can have multiple paragraphs and use bullets.

## Iggy

There will be files in the folder that you don't want tracked. e.g. backups, binaries etc. Simply create a .gitignore file in the root directory. In the file list the files you want to ignore, or use wildcards. e.g. '*~' will ignore all files with a tilde at the end (backups).

    git add .gitignore
    git commit
    git status

The ingored files should no longer be tracked.

## Git Workflow (Simple)

Recommended that you make small changes and commit regularly, so that each change can be described in a single sentence.

    git add .
    git commit

## Review Changes

    git log
    git log n3          -- review last 3 commits
    git log --stat --summary
    git diff            -- view changes that haven't been committed yet.
    git log --pretty    --online

This command prints out a history of commits and their ids. You can use their ids to compare versions.
    
    git diff 8fef..c6e7

Note you don't need the full id numbers.

    git diff HEAD^..HEAD    -- view the last change

## Reverting Changes

    git reset --hard        -- throw away changes since last commit.
    git checkout myfile.txt -- throw away changes to myfile since last commit.
    git commit --amend      -- change the commit message
    git reset --soft HEAD^  -- reset the last commit (incase you missed a file).



## The Repository

The simplest system just consists of a single repository. Users can 'check out a working copy' of any files that need to be updated. They can then 'commit the changes' back to the repository.

A more complex system may consist of multiple users, each with a local repository (a copy of the central, shared repository). The user works on the local repository (checking out and committing changes). Once the user has finished their work on the local repository, the changes can be 'pushed' to the central repository.

## Branches

Branches are seperate working directories that allow new features to be worked on without affecting the master branch.

Branches can be worked on an tested independantly. Once the work is complete it can be merged with the master branch. It should also be easy to update the branch from the master, to ensure that the latest code is being used.

## Kicking Off A Project

Create a repo on github.

Follow the direction on Github:
	1. Create directory.
	2. Move to directory.
	3. 'git init' - This creates a new folder in the directory called .git.
	4. Create your new files in that folder. For example, README.
	5. 'git add .' to stage your new files.
	6. Commit all your changes (git commit -m 'Commit comment')
	7. Push your changes to the repo.
	
## Git Workflow

This is the suggested workflow when using Git.

Since I am using Github (almost like a backup) I will have two (or more) clones of the system, one on Github and one local.

1. Clone Master Locally

To clone the remote repository to get a working repository on my local machine:

    git clone git://github.com/<project>

This command clones the requested project locally. It keeps the address of the original project and aliases it as 'origin' to make it easy to push changes back up to the original.

This can be considered the Master branch. Each project has a master branch. This is the branch that is/can be deployed to live so should be a fully working and tested version of the system. It's always safe to create a new branch from Master.

2. Create Working Branch

When working on a feature, create a branch off Master. 

    git branch mybranchname
    git checkout mybranchname

We can then make changes to the project. Then we need to 'stage' those changes. We do this by adding the files to the project.

    git add -A .

This command adds a changed file to the project. If you make further changes before committing, you need to add the file again. You could also all all files from the current working directory:

A couple of handy commands: <code>git status</code> shows the current status of the repository and <code>git dif --cached</code> shows a differential view of the staged changes.

Fourth, we have to commit those changes to the local branch. 

	git commit -m 'Commit comment'

Finally, the changes can be pushed back to shared repository.

	git push <repository> <branch>

e.g.

    git push origin master
    or git push origin mybranchname
 

### 3. Merge Into Master

Once feature is complete and fully tested, merge back into master.

    git checkout master
    git merge mybranchname

Then you can delete the completed branch.

    git branch -d mybranchname

### 4. Immediately Deploy

Since the Master branch is the live version, it can be deployed to live immediately.

## Ignore

A global .gitignore file can also be used by adding one to your global git config. For example, you might create the file ~/.gitignore_global and add some rules to it. To add this to your config, run 

    git config --global core.excludesfile ~/.gitignore_global
	
My file contains the recommended list from here: http://help.github.com/ignore-files/ plus *~ to ignore any backup system files.

-------------

[1]: http://hoth.entp.com/output/git_for_designers.html "Git for Designers"
[2]: http://scottchacon.com/2011/08/31/github-flow.html "Github Flow"
[3]: http://en.wikipedia.org/wiki/Github "Github on Wikipedia"
[4]: http://en.wikipedia.org/wiki/Revision_control "Revision Control on Wikipedia"
[5]: http://wiki.spheredev.org/Git_for_the_lazy "Git for the Lazy"

