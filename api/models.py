from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

CAT_OPTIONS = [
    ('CONFERENCE', 'Conferencia'),
    ('SEMINAR', 'Seminario'),
    ('CONGRESS', 'Congreso'),
    ('COURSE', 'Curso')
    ]

VIR_OPTIONS = [
    ('VIRTUAL', 'Virtual'),
    ('PRESENCIAL', 'Presencial')
    ]

class Event(models.Model):
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_category = models.CharField(choices=CAT_OPTIONS,max_length=10)
    event_place = models.CharField(max_length=30)
    event_address =  models.CharField(max_length=100)
    event_initial_date = models.DateField()
    event_final_date = models.DateField()
    event_type =  models.CharField(choices=VIR_OPTIONS,max_length=10)
    thumbnail = models.ImageField(upload_to='thumbnail_image',default='default-thumbnail.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add = True, editable=False )

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
