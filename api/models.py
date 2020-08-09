from django.db import models
from django.contrib.auth.models import User

CAT_OPTIONS = [
    ('CF', 'Conferencia'),
    ('SE', 'Seminario'),
    ('CG', 'Congreso'),
    ('CR', 'Curso')
    ]

class Event(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(choices=CAT_OPTIONS)
    place = models.CharField(max_length=30)
    address =  models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    virtual =  models.BooleanField(default=True)
    created_date = models.DateField()
    user = models.ForeignKey(User)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
