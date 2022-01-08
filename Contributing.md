### Dependencies & USER INSTRUCTIONS :

Dependencies are added to the `requirements.txt` file.

Usage of virtualenv is highly recommended. Please use the following steps to install this django project.

Use the following steps (requires a terminal) to set up the project

### Cloning

(this will make a folder for the project be in the outter folder where you want it placed)

> git clone url

> Navigate into this new folder

> ls (you see requirements.txt and not settings.py)

> touch .env

> Navigate into folder named the same as outer folder

> ls (you see settings.py and not requirements)

> touch local_settings.py

> .. (back to requirements)

> Code . Or open in editor

### Add requirements

Fill in the 2 files both should be light grey and not be tracked by git

Install virtualenv if it's not installed before

> $ pip3 install virtualenv

> virtualenv venv

> source venv/bin/activate

> pip3 install -r requirements.txt

You should now be able to test locally

### Branching

Create/Switch to branch and work on it there..

> (gco/git checkout) FrontEnd

Make and edit and Test locally

add, commit, & Push to that branch

> git push origin FrontEnd/Development/Fixes

Switch to master, merge, and push

> (gcm/git checkout master)

> (gm/git merge) FrontEnd/Development/Fixes

> (gp/git push)

Repeat branching and update your team and progress tracker
