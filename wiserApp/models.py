from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Mood(models.Model):
    mood = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mood

class Assignemnt(models.Model):
    assignmentName = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigmentFile = models.FileField(upload_to='assignments/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assignmentName

class Notes(models.Model):
    noteName = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    noteFile = models.FileField(upload_to='notes/')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.noteName

class Journal(models.Model):
    journalName = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    journalFile = RichTextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.journalName



