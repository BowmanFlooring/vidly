"""vidly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Here, notice that Django has already set up an url endpoint. Anything that starts with
# 'admin' gets mapped to 'admin.site.urls'. This is done for every Django project auto-
# matically, and it means that all Django projects come with an admin panel. Nice!
# We need to add to this, though! Let's add another configuration for 'movies/'. So, let's
# add a new path object - We're going to tell our 'Vidly' app that ANY path that starts with
# 'movies/' should be handed off to the URL configuration in the 'movies' app.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls'))  # <-- OUR ADDED LINE!
]
