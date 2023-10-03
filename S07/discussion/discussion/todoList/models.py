from django.db import models

# Create your models here.
#[Section] Models
#Each model is represented by a class that subclass django.db.models.Models.Each model has a number of class variable, each of which represent a database field in the model.
class ToDoItem(models.Model):
    task_name=models.CharField(max_length=50);
    description=models.CharField(max_length=200);
    status=models.CharField(max_length=50, default="pending");
    date_created=models.DateTimeField('date created');
    def __str__(self):
        return self.task_name;