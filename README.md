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
# Install and Run Locally
### For Mac

Download the repository and store in desired location, then in source directory:

* Install homebrew, if you don't already have it
* Install python 3.8.8 with homebrew ```brew install python@3.8.8```
* While a virtual environment is not necessary, it is good practice to use with new projects. Install virtualenv and virtualenvwrapper ```pip install virtualenv virtualenvwrapper```
* Create virtual environment for project ```mkvirtualenv project_name -p /opt/homebrew/opt/python@3.10/bin/python3```
* Install project requirements ```pip install -r requirements.txt```
    
### For Windows

* Install python if you don't already have it(Python 3.8.8)
* Open CMD and navigate to source directory
* Install project requirements ```pip install -r requirements.txt``` 


# Running Local Server and Tests

### Mac
* Open terminal
* Inside the source directory ```python manage.py runserver```
* App is now running locally on localhost
* For tests: ```python manage.py test manager```

### Windows
* Open CMD
* Inside the source directory ```py manage.py runserver```
* * For tests: ```py manage.py test manager```
* App is now running locally on localhost
* For tests: ```python manage.py test manager```

# Running Tests
If you'd like to run test cases locally
* 

A set of instructions to run service locally, for example:
mac (service)

python manage.py runserver

windows (service)

py manage.py runserver
