###

#  <--django-admin startproject <projectName>-->

###
#the outer discussion/ is our root directory of our project.It will contain all the necessary files and folder for the django application
#manage.py:A command-line utility that lets you interact with this django project in various ways
#the inner discussion/ directory is the actual python package inside our project.Its name is python package name you'll need to use import anything inside it.
#__init__.py:An empty file that tells this directory should be considered a python package
#settings.py:contain application configuration
#urls.py:In the urls.py files, the url declaration for this django project;"table of contents" of your Django powered site.
#asgi.py: An entry-point for ASGI compatible web servers to serve your project
#wsgi.py:An entry point for WSGI-comatible webserver to serve our project

#to run our application/project we should execute this command:
####

##<--python manage.py runserver-->//inside directory of manage.py

####

#Inside our project, we can actually create application
#To do that we need to use this command
###

#<--python manage.py startapp <appname> -->

###
#reminder:Make sure that before the command is executed, you should be at the root folder where the manager.py file is located at.
#In the context of Django, an app and a project has different meaningd unlike in other programming languages. An App is a "web application that does somethings" -eg a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website.abs
#A project can contain multiple apps,An app can be in multiple projects


# <--from django.http import HttpResponse--> in views.py of todolist
# <---def index(request):
    # return HttpResponse("Hello from the views.py file")---->

#By running makemigration, you're telling Django that you've made some changes to your model or add a model and that you'd like the changes to be stored as a migration
#python manage.py makemigrations todoList