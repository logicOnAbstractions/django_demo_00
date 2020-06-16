from django.db import models

# Create your models here.

class Question(models.Model):
    """ a model for django, which will define the DB schema.
        * **class** attributes are db schema columns
    """

    question_text       = models.CharField(max_length=200, default='hit me')              # mand. args max_length
    pub_date            = models.DateTimeField('date published')

class Choice(models.Model):
    question            = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text         = models.CharField(max_length=200, default='option 1')
    votes               = models.IntegerField(default=0)