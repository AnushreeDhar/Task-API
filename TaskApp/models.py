from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.OneToOneField(User)
    task_name = models.CharField(max_length=20)
    task_desc = models.TextField(max_length=200)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Images/',  default='Images/None/No-img.jpg')
    doc = models.FileField(upload_to='Docs/', default='Doc/None/No-doc.pdf')

    
    def __str__(self):
        return  "%s" % self.task_name

    
