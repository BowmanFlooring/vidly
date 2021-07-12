from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# This first function, which I've called 'index', could actually be called anything.
# It's name is arbitrary. However, usually this 'main' view function is called 'index',
# because it represents the main page of the app. 'Index' is used quite universally
# in the coding community, so I'm going to stick to that naming convention for now.

'''
NOTE:
  * ALL VIEW FUNCTIONS SHOULD TAKE THE 'request' PARAMETER!!!! 
  * again, the name is arbitrary, but the object that is passed 
  * to this function is an http request object! We will NOT
  * call this function, Django takes care of it for us!! So, when
  * we send an http request endpoint, Django - based on some
  * configuration - will figure out what view function should be called.

  * Also, aside from all functions taking the 'request' parameter, they
  * should all return an http RESPONSE as well. (check {line 1})
'''


def index(request):
    return HttpResponse("""
    Hello, world! This is a test.
    My name is Dakota Bowman, and I own Bowman Flooring Company.
    Today is Sunday, July 11th, at approximately 3:20am.
    
    This is the first of many tests, insterted into an
    'HttpResponse' object. That object, which is the name of
    the class,  was imported from the 'django.http' module.

    Thanks! Happy coding...
    """)
# Now, we need to map this function to a URL! To do that, we need to create a new file
# called 'urls.py' inside of the 'movies' folder. By convention, the name of the file
# should be 'urls.py', so again, I'm sticking with conventional knowledge here.
