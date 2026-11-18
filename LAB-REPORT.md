# Lab Report - Student Task Manager (CSC418, Lab Assignment 4)

## 1. Git vs GitHub; add, commit, push
Git is the version control tool that runs on my computer and records the
history of my files. GitHub is a website that hosts Git repositories online
and adds teamwork features such as Issues, Pull Requests and Actions.
`git add` puts changes into the staging area, `git commit` saves the staged
changes as a snapshot with a message, and `git push` uploads my commits to
the remote repository on GitHub.

## 2. Branches, Pull Requests and merge conflicts
Branches let me build a feature separately without breaking `main`. A Pull
Request asks for my branch to be merged and gives others a place to review the
changed files and comment before merging. A merge conflict happens when two
branches change the same lines of the same file and Git cannot decide which
change to keep.

## 3. fetch vs pull; merge vs rebase
`git fetch` only downloads new commits from the remote and does not change my
working files. `git pull` is fetch followed by a merge into the current branch.
`git merge` joins two branches and keeps both histories with a merge commit,
while `git rebase` replays my commits on top of another branch to make the
history a straight line (it rewrites those commits).

## 4. GitHub Issues and Actions
Issues track bugs, features and documentation tasks so everyone sees what must
be done and who is doing it. Actions run automated workflows, such as the unit
tests on every push and pull request, so mistakes are found early.

## 5. A difficulty I faced
My first merge conflict in README.md confused me because Git stopped halfway
through the merge. I solved it by reading the conflict markers (<<<<<<<,
=======, >>>>>>>), keeping the right lines, removing the markers, then running
`git add` and `git commit` to finish the merge.
