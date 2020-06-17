
""" you could create all your model classes here.

    however, if you want to stuff them in a subdir, then you can import those classes here instead, and move them whereever.

    the point is that django **must** have a django_app/models.py file where all those classes are accessible (imported or defined) because it expects that rigig hierarchy.
"""



from django_app.modeldir.dude import *
from django_app.modeldir.choice import *
from django_app.modeldir.question import *


