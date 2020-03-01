# Git Commands

**git --version**         Checks if Git is installed and if so, which version

**git init**              Initializes a Git folder

**git status**            Branch/Folder overview

**git log**               Shows history of commits

**git log --oneline**     Same, but nicer formatting

**git show HEAD~1**       Shows details of commit with index 1


**git add file.py**       Stages a file

**git commit -am "Text"**

## Undo

**git checkout file.py**  Undoes changes on a modified file

**git checkout**          Undoes changes on all modified files

**git checkout <id>**     Goes to the state at commit with specified id

**git checkout master**   Goes back to the original pre-checkout state


**git revert <id>**         Creates a new commit that puts the project into
                            the state it was in after commit with specified id                    
                            This will not remove commits from the history,
                            just create a new one on top of the existing ones

**git reset .**             Unstages changes

**git reset --mixed <id>**  Default. Removes commits up until the specified one
                            Changes from the removes commit will be unstaged

**git reset --soft <id>**   Same, but changes are staged

**git reset --hard <id>**   Removes commits and all changes

## GitHub & Branches

**git remote add origin <link>**  Connects local git repository to an online GitHub repository

**git pull origin master**        Mirrors online changes to the local repository

OR

**git branch --set-upstream-to=origin/master master** + **git pull**


**git branch feature**        Creates a new branch named 'feature'

**git branch**                Lists all active branches

**git checkout feature**      Switches currently used branch

**git checkout -b feature**   Creates a new branch and switches to it

**git branch -D feature**     Deletes the specified branch

**git push origin feature**   Mirrors changes on the feature branch to local repository

**git pull origin feature**

## Merge & Rebase

**git merge feature**               Master branch catches up to the feature branch

**git merge --abort**               Stops merging, removes conflicts, returns both branches
                                    to their pre-merge state
                        
**git rebase master**   Feature branch catches up to the changes on the master branch

## Contributing & Collaboration

**git clone <link>**      Clone an existing GitHub repository onto the local machine
