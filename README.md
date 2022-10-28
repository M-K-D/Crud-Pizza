# Crud-Pizza
A simple Django web application that allows users to manages pizza toppings, as well as pizza recipes. Please note that this is an example web application that anyone could access currently; If you visit the live application, please do not enter any kind of sensitive or personal information.

This application is live and deployed at: http://mkd-crud.herokuapp.com/

If you'd like to download and run this project locally, please see below.

# Install Locally
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
* Open terminal and navigate to source directory
* For running local server: ```python manage.py runserver```
* For tests: ```python manage.py test manager```

### Windows
* Open CMD and navigate to source directory
* For running local server: ```py manage.py runserver```
* For tests: ```py manage.py test manager```

Once the server is running, the app will be available in your browser at ```localhost```

