# Course Roast Board

## Description

This Project is a purpose of learning Django framework as a backend, developed in a virtual environment and deployed in the free AWS EC2 instance linking to the domain name `golyy.org`

- Frontend
    > HTML
    > bootstrap 4
    > jQuery

- Backend
    > Django

- Deployment
    > Gunicorn
    > Nginx
    > AWS ubuntu@EC2

## Importance
- This project demo is currently under development, many features are not yet to be done.
- All the data are fake, and may be not related to course roasting, just for testing purpose.

## Commit Changes to the project
simply run the script `golyyUD.sh`


## Development Steps
- Get Started
    - Installation, env setup
        - prepare VM
        > ```sudo apt-get install python3-venv```
        > ```python3 -m venv venv```
        > ```source env/bin/activate```
        - setup required libs
        > ```pip install -r requirements.txt```
    - Starting a new project
        > - ``` django-admin startproject [porjectName]```
        > - "manage.py": shortcut to use the django-admin command-line utility. We use it to run dev server, tests, create migrations and much more
        > - "\__init__.py": it is an empty file which tells django this folder is a Python package
        > - "settings.py": contains all projects configuration.
        > - "urls.py": responsible for mapping the routes and paths in the project. For example, if you want to show something in the URL ```/about/```, you have to map it here first.
        > - "wsgi.py": a simple gateway interface for deployment.


        Django comes with a simple web server so that we dont have to install anything to run the project locally during the dev. Command is ``` Python manage.py runserver```

        - Important concepts
            - app: is a web application that does something. An app usually is composed of a set of models(DB tables), views, templates, tests
            - project: is a collection of configurations and apps.

        - Starting an app
            - Note: should in the same dir where manage.py exists
            - ```django-admin startapp [appName]```
            - "migrations/": here django stores files to kkep track of the changes created in "models.py", so to keep synchronization of DB and "models.py"
            - "admin.py": a configuration file for a built-in django app called Django Admin
            - "apps.py": a configuration file for app itself
            - "models.py": where we define entities of web application. It is automatically translated into DB table by Django
            - "tests.py": is used to write unit tests for the app
            - "views.py": where we handle the request/response cycle of web app
        - Configure project to use the app
            - Go to ```INSTALLED_APPS``` in "settings.py" and append the app to it
            - write view func in "views.py"
            - tell django when to serve this view, add ```url()``` in "urls.py"
            - run the app

- Fundamentals
    - project development process
        - Use Case Diag
        - Class Diag(ER Diag)
        - views
        - templates engine
        - static files setup
            - taking the advantages of bootstrap 4 library for css stylesheet
        - create admin
            - django admin is ready configured with built-in listed in INSTALLED_APPS
            - good for content-driven web app
            - this is an admin interface in replacement of using (```python manage.py shell```) to add new boards
            - create admin account by command (```python manage.py createsuperuser```) to manage the web app
            - after creating admin account, go to URL: ```http://127.0.0.1:8000/admin/``` to the login page
            - use username and password to log into the administration interface 

- Advanced Topics
    - URLs
        - adding new pages:
            > - add url() in urlpatterns in urls.py
            > - add corresponding views function in views.py
            > - add corresponding html file in templates
            > - write unit tests in tests.py
                > - new page, new test class
                > - reminder: need to import url name
        - URL routing:
            > - add unit tests
            > - add links in html file using the ```{% url [urlName] [arbitrary num of args]%}```
        - Reusable Templates
            > - create a master page with the base stuff
    - Forms
        - reusable form

- Authentication
    - user account related stuff
    - start an app for this part
        > ```django-admin startapp accounts```
        > add email feild in login
        > custmize backgroud of accounts
            >  https://www.toptal.com/designers/subtlepatterns/ choose a nice pattern and download the image or choose a image you like somewhere else
            > place it in the `static/img`
            > apply it in `accounts.css` 
        > add logout
    - Displaying Menu For Authenticated Users
        - add dropdown menu with logout link for logged users
            - Bootstrap 4 dropdown component needs jQuery to work
                > https://jquery.com/download/ download the compressed, production jQuery newest version
            - Bootstrap 4 also needs a library called Popper to work
                > https://popper.js.org/ download the latest version
                > Inside the `popper.js-1.12.5` folder, go to `dist/umd` and copy the file `popper.min.js` to our `js` folder
            - copy the `bootstrap.min.js` file to our js folder as well
    - add login functionality
        - link logic: `urls.py` $\rightarrow$ configure `LOGIN_REDIRECT_URL = 'home'` in `settings.py` $\rightarrow$ link `url` in `href` of `login` `a` tag $\rightarrow$ create `login.html`
        - link `signup` and `login` by adding `url` in `href`
    - Creating Custom Template Tags

## Reference

>This project is based on [Vitor Freitas's](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html) Dajngo tutorial, and custmized a little bit.