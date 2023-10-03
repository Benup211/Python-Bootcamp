from django.urls import path
from . import views

#The path() function can recieve for arguments
#We'll only focus on the two arguments that are required, which are the "route" and view, and the third argument name which aloows us to make global changes to the url patterns of your project while only th=ouching a single file.
urlpatterns=[
    path('',views.index,name='index')
]