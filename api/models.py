from django.db import models
from django.conf import settings
from django_userforeignkey.models.fields import UserForeignKey
from django.utils import timezone
import uuid
from datetime import date


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


def get_path_class(instance, filename):
    extension = os.path.splitext(filename)[1][1:]
    class_directory = instance.__class__.__name__
    path = os.path.join(class_directory)
    filename = '{}.{}'.format(date.today().strftime("%Y-%m-%d") + "_" + uuid4().hex, extension)
    return os.path.join(path, filename)

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event_name = models.CharField(max_length=100, null=False, blank=False)
    event_category = models.CharField(choices=CAT_OPTIONS,max_length=10)
    event_place = models.CharField(max_length=30)
    event_address =  models.CharField(max_length=100)
    event_initial_date = models.DateField()
    event_final_date = models.DateField()
    event_type =  models.CharField(choices=VIR_OPTIONS,max_length=10)
    thumbnail = models.ImageField(upload_to='thumbnail_image',default='default-thumbnail.jpg')
    user = UserForeignKey(auto_user_add=True)
    creation_date = models.DateTimeField(auto_now_add = True, editable=False )

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
