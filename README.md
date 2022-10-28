# Crud-Pizza
A simple Django web application that manages pizza toppings, as well as pizza recipes. 

This application is live and deployed at: 

If you'd like to download and run this project locally, please see below.

# Run Locally 
Download project files and save them to your desired location. 

From here, open your terminal/command line and navigate to the root of the project directory. 

Before moving forward, you'll need to ensure that you have Python and all of the required dependencies installed to successfully build and run the application. Python 3.10.8 is the recommended version for this application, but older version of Python 3 might work as well. Once you have verified a working version of Python, use pip to install all dependencies found in 'insert requirements.txt'
NOTE: Whitenoise is not necessary for running locally

After all dependencies are installed, you can now start the local web server: python manage.py runserver

COPY AND MODIFY THIS AT A LATER POINT -----------------------------------------------------------------------------------------
# Install and Build Locally
### Mac

Download the repository and store in desired location, then:

    * Install homebrew, if you don't already have it
    * install python 3.10 using homebrew brew install python@3.10
    install virtualenv and virtualenvwrapper pip install virtualenv virtualenvwrapper
    create virtual environment for project mkvirtualenv project_name -p /opt/homebrew/opt/python@3.10/bin/python3
    install project requirements pip install -r requirements.txt

known issues and fixes

If your system python does not include pip, you will need to make sure pip is installed :

python -m ensurepip # if your system python is at least 3.4

If your system python isn't at least 3.4, you will need to use your system package manager to install pip.
windows

In this source directory:

    install python
    open project in pycharm
    set interpreter installed python 3.10
    open shell
    install project requirements pip install -r requirements.txt

Run tests locally

A set of instructions to run tests locally, for example:

pytest

Run service locally

A set of instructions to run service locally, for example:
mac (service)

python manage.py runserver

windows (service)

py manage.py runserver
