# NOTE: In this file, we are going to create a variable, and call it 'urlpatterns'.
# This variable needs to be set to a list, per Django's requirements! This is just
# what Django expects from us here.

# In this list, we need to add objects that map url endpoints to our view functions.
# To make that happen, we need to use the 'path' function, which needs to be imported
# from 'django.urls':
from django.urls import path
from . import views

# When using the 'path' function, our first parameter passed will be an empty string.
# That empty string represents the ROOT of our app. For example, we will have end-
# points that look like this:

# movies/
# movies/1  <-- the '1' here represents a given movie's ID
# movies/1/details

# We should be designing apps from the perspective of OTHER DEVELOPERS. They need to
# be designed for REUSABILITY - so, we shouldn't care what the 'prefix' (movies) is.
# If another developer wants to download this app from PyPI.org some day, they should
# be able to easily drop it in to their Django project and keep pushing. So, that's
# why we should use 'RELATIVE URL PATHS' as opposed to 'absolute url paths'.

# As a second argument, we should pass our 'views' function. For this to happen, we need
# to import it from our 'views' module, which is in this same directory. Check up at
# {line 9} for the proper way to import it (via Django's req. conventions). It's a bit
# different from pure python convention, so pay attention!

# This process of mapping url endpoints to paths is called 'URL Configuration', and
# every app should have one! This variable is set to a list - that is KEY! That list
# can have MULTIPLE paths within, just remember to separate with commas!
urlpatterns = [
    path('', views.index, name='index')
    # NOTE: I'm not calling this function! Django will handle all that!
    # Also, as a best practice, a name should be given, and passed as
    # a third argument (notice, it's a keyword argument!)
]
