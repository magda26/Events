from django.db import models
from django.contrib.auth.models import User

CAT_OPTIONS = [
    ('CF', 'Conferencia'),
    ('SE', 'Seminario'),
    ('CG', 'Congreso'),
    ('CR', 'Curso')
    ]

class Event(models.Model):
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_category = models.CharField(choices=CAT_OPTIONS,max_length=10)
    event_place = models.CharField(max_length=30)
    event_address =  models.CharField(max_length=100)
    event_initial_date = models.DateField()
    event_final_date = models.DateField()
    event_type =  models.BooleanField(default=True)
    thumbnail = models.ImageField(upload_to='thumbnail_image')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
