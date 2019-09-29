# Django tutorial --- from zero to deloyment


This repository is a learning practice following [Vitor Freitas's](https://simpleisbetterthancomplex.com/series/2017/09/11/a-complete-beginners-guide-to-django-part-2.html) tutorial, related links refering to https://github.com/sibtc/django-beginners-guide/tree/v0.1-lw

1. Development

- Get Started
    - Installation, env setup
    - Starting a new project
        > - ``` django-admin startproject [porjectName]```
        > - "manage.py": shortcut to use the django-admin command-line utility. We use it to run dev server, tests, create migrations and much more
        > - "__init__.py": it is an empty file which tells django this folder is a Python package
        > - "settings.py": contains all projects configuration.
        > - "urls.py": responsible for mapping the routes and paths in the project. For example, if you want to show something in the URL ```/about/```, you have to map it here first.
        > - "wsgi.py": a simple gateway interface for deployment.


        Django comes with a simple web server so that we dont have to install anything to run the project locally during the dev. Command is ``` Python manage.py runserver```

        - Important concepts
            - app: is a web application that does something. An app usually is composed of a set of models(DB tables), views, templates, tests
            - project: is a collection of configurations and apps.
        - Starting an app
            - 
    - Hello World app

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
