# Introduction to git and GitHub

<!-- fg=white bg=black -->

by _Kai_ and _Jannik_ 

```bash
$ git
```

---

## What is git?

- Version control system based on fancy math graph theory

> **Track Changes on steroids**

## What is git?

### Concepts

- commits
- branches

```
o <-- o <-- o <-- o
            ^
             \
              --- o <-- o
```

- merging

```
o <-- o <-- o <-- o <---- o
            ^            /
             \          v
              --- o <-- o
```

---

## Why should you use git?

- reproducibility
- collaboration
- fearless experimentation

---

## How do you use git?

https://missing.csail.mit.edu/2020/version-control/

---

## How do you use git?

### Basics

`git help <command>`: get help for a git command
`git init`: creates a new git repo, with data stored in the .git directory
`git status`: tells you what’s going on
`git add <filename>`: adds files to staging area
`git commit`: creates a new commit
`git log`: shows a flattened log of history
`git log --all --graph --decorate`: visualizes history as a DAG
`git diff <filename>`: show changes you made relative to the staging area
`git diff <revision> <filename>:` shows differences in a file between snapshots
`git checkout <revision>`: updates HEAD and current branch

---

## How do you use git?

### Branching and merging

`git branch`: shows branches
`git branch <name>`: creates a branch
`git checkout -b <name>`: creates a branch and switches to it
same as `git branch <name>`; `git checkout <name>`
`git merge <revision>`: merges into current branch
`git mergetool`: use a fancy tool to help resolve merge conflicts
`git rebase`: rebase set of patches onto a new base

---

## How do you use git?

### Remotes

`git remote`: list remotes
`git remote add <name> <url>`: add a remote
`git push <remote> <local branch>:<remote branch>`: send objects to remote, and update remote reference
`git branch --set-upstream-to=<remote>/<remote branch>`: set up correspondence between local and remote branch
`git fetch`: retrieve objects/references from a remote
`git pull`: same as git fetch; git merge
`git clone`: download repository from remote

---

## How do you use git?

### Undo

`git commit --amend`: edit a commit’s contents/message
`git reset HEAD <file>`: unstage a file
`git checkout -- <file>`: discard changes

---

## How do you use git?

### Advanced

`git config`: Git is highly customizable
`git clone --depth=1`: shallow clone, without entire version history
`git add -p`: interactive staging
`git rebase -i`: interactive rebasing
`git blame`: show who last edited which line
`git stash`: temporarily remove modifications to working directory
`git bisect`: binary search history (e.g. for regressions)
`.gitignore`: specify intentionally untracked files to ignore

---

## Git can be hard...

https://xkcd.com/1597

---

<!-- fg=white bg=black -->

## Collaborating with GitHub

---

<!-- effect=fireworks -->

## Collaborating with GitHub

Demo time!

---





