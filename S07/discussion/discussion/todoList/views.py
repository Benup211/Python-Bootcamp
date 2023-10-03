from django.shortcuts import render
#The from keyword allows importing of necessary classes,methods and other items needed in our application from the "django.http" package with import keyword defines what are we importing from the package.
#Where in the HttpResponse module will allow us to send response to our user/client
from django.http import HttpResponse
# Create your views here.
from .models import ToDoItem

def index(request):
    todoitem_list=ToDoItem.objects.all();
    output = ', '.join([todoitem.task_name for todoitem in todoitem_list]);
    return HttpResponse(output);