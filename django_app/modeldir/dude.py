from django.db import models

# Create your models here.

class Dude(models.Model):

    """ just a dude
    """
    first_name       = models.CharField(max_length=200, default='john')              # mand. args max_length
    last_name        = models.CharField(max_length=200, default='smith')


    def __repr__(self):
        return f"{self.first_name} {self.last_name}"