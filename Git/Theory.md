# Git Theory

**Stages of project changes**

Untracked -> Modified -> Staged -> Committed

**Git ignore**

To ignore changes to the chosen files, put them in the .gitignore file

/index.html

directory/index.html

directory/*               Ignores all files in the directory

directory/*.py            Ignores all .py files in the directory

Cached files will still be tracked

**git rm -r --cached**    Removes caching, but not the files

## Merging

Switch to master branch to merge branches

Fast Forward merge: merges 2 branches if there is no conflict

3-way merge: Merging the feature branch after someone else has merged their branch
             with the master branch
             Triggered by the same command, conflicts are checked - if none are found,
             branches are merged as a new commit
             In case of a conflict, the different commit changes will be shown inside of the
             conflicting files
             Choose the correct one, then stage and commit the final project state, branches will be merged

## Rebase

Used to integrate changes from one branch into another

A process of moving or combining a sequence of commits to a new base commit

## Contributing

Fork copies a repository to a new repository on GitHub, then it can be cloned
to the local machine with **git clone <link>** command

Commit and push changes on the forked project to GitHub, then go to the original
repository and select 'New pull request'
Changes will be compared, and if no conflicts are found, there will be an option
to send the pull request

This pull request can then be reviewed by the original project's owner, and ultimately
the branches can be merged by them
If the pull request contains conflicts, the project owner can resolve them as usual,
then merge the branches

## Collaborations

Add a user as a collaborator in the repository settings
The invite will be sent via email to be confirmed

As a collaborator, there is no need to fork the repository
Instead, simply clone it

Usually, the master branch is protected by the rules defined in the project settings on GitHub
If the master branch is protected against commits, create a separate branch and commit the changes
to it instead
Then, create a pull request for the project owner to merge the new branch with the master branch
