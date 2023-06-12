Source: https://learn.microsoft.com/en-us/training/paths/django-create-data-driven-websites/    

* A Python web framework - Django is suitable for both front-end and back-end web development
* Powerful when working with a data-driven application, where the main goal is to provide a front end to a database
* Flexibility and security -great out-of-the-box security
* A route tells Django what function to execute if the user makes a request
* Views are functions or classes that execute code and return HTML or other types of responses, such as a 404 error

Commands
* django-admin startproject <project_name> .
* python manage.py runserver
* python manage.py startapp <app_name>

# Models and Data
* Django is focused on data-driven applications, so it provides its own object-relational mapper (ORM).
* https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types  
* The Django ORM allows you to create and update the database itself through a process known as migrations.

# Commands
* python manage.py makemigrations
* python manage.py sqlmigrate <app_label> <migration_name>
* python manage.py showmigrations
* python manage.py migrate <app_label> <migration_name>