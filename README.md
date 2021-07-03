# git-intro

Introduction to git and GitHub

## Presentation

Run the following code to render the presention in the terminal:

```bash
pip install -r requirements.txt
cd presentation
present intro.md
```

## Notes

Things to mention / show:

- Setting up ssh with git and GitHub,
- Talk about git `config --global`
  - `pull.rebase`
  - `init.defaultBranch`
  - `user.name`
  - `user.email`
- Using git with other tools: **vs code extension**(s), **GitHub Desktop**

Demonstrate:

- "This code doesn't run as expected": **GitHub Issues**
- "Indeed, I can fix it": **git branches**
- "This is what I did, can you include it in the main code?": **Pull Request**
- "Let me review those fixes": **code review**
- "Looks good now, ready to": **Merge**

Show:

- This works across repositories as well: **forks** and ***Pull Requests** for contributing to Open Source Software
- e.g. <https://github.com/rstudio/rmarkdown/pull/1996>

## Resources

- Comprehensive and complete: <https://git-scm.com/book/en/v2>
- Cheat Sheet (list): <https://training.github.com/downloads/github-git-cheat-sheet/>
- Cheat Sheet (graphical): <https://ndpsoftware.com/git-cheatsheet.html#loc=stash;>
- 1 hour lecture, very good to _understand_ what happens behind the scenes: <https://missing.csail.mit.edu/2020/version-control/>
- Summary of a python project structure: <https://github.com/yngvem/python-project-structure>
