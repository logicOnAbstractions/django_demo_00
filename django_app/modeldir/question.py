from django.db import models

class Question(models.Model):
    """ a model for django, which will define the DB schema.
        * **class** attributes are db schema columns
    """

    question_text       = models.CharField(max_length=200, default='hit me')              # mand. args max_length
    pub_date            = models.DateTimeField('date published')