# In Django, we have this package - 'django.db'. Within that package, we have a
# module colled 'models'. In that module, we have a class called 'Models". To
# import it into this file, here's what the import statement would look like:
from movies.apps import MoviesConfig
from django.db import models
# This package encapsulates ALL THINGS necessary for working with databases.

# Let's also import django's 'timezone' class, so we can have our app assign
# a 'date_created' tag to every movie - and that tag should be current, no
# matter where the user that created the entry is located:
from django.utils import timezone

# Create your models here.

# NOTE: ****SOMETHING TO REMEMBER FOR NOW, LATER, AND FOREVER****

# By creating this class, and then also deriving it from the 'Model' class from
# within the 'models' module, our class will inherit ALL the functionality of
# 'Model' class. Therefore, we won't have to write any of that code! It's simply
# built right in to our 'Genre' class! (In this specific case, we won't have to
# write any of the code to store 'Genre' objects in a database).


class Genre(models.Model):
    name = models.CharField(max_length=255)
    # This states that the 'Genre' class will have a name consisting of
    # characters, and will also be NO LONGER than 255 characters. This
    # is a form of hacker-prevention. That way, hackers can't just spawn
    # the shit out of a name-generator and throw it on our database.

    # These two lines make sure the genre gets displayed as it's
    # actual string representation.
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    # Now, we need to create a relationship between 'Movie' and 'Genre'.
    #============ every movie must be in a certain genre! ============#
    # The next line esentially ties this class to the 'Genre' class, and
    # also tells Django that, if a given genre gets deleted, then all of
    # the movies within that genre must also be deleted (cascading) -
    # the second argument (on_delete) MUST be a keyword argument!
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


# Up to this point, we have now defined the two model classes (Movie, Genre)
# within the 'movies' app. The next step would be to tell Django to scynchronize
# our database with the models we have defined within this app!

# NOTE
# * the two model classes (Movie, Genre) above can ALWAYS be modified to our
# * liking! They don't have to stay as they exist presently! Any NEW CLASSES
# * that we may want to add should go BELOW this NOTE paragraph. Also, those
# * two classes can always be viewed as 'template' classes. The comments are
# * there for a reason! Also, because I've inserted an '__init__.py' file in
# * this directory, it can be uploaded to the pypi.org repository and pulled
# * back down locally - to be used with a different project at a later date.
