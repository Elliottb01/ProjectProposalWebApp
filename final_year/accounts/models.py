
from pickle import TRUE
from tokenize import Number
from unicodedata import name
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Title(models.Model):
    id = models.BigIntegerField(primary_key=True)
    honorific = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'title'

    def __str__(self):
        return self.honorific

class Faculty(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fac_name = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'faculty'

    def __str__(self):
        return self.fac_name

class Lecture(models.Model):
    id = models.BigAutoField(primary_key=True)
    profilepic = models.ImageField(null=True, blank=True, upload_to="images/")
    title = models.ForeignKey('Title', models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.
    last_name = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.
    office= models.CharField(blank=True, null=True, max_length=100)
    email = models.CharField(blank=True, null=True, max_length=100)  # This field type is a guess.
    number = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.
    faculty = models.ForeignKey('Faculty', models.DO_NOTHING, blank=True, null=True)
    lec_description = models.TextField(blank=True)
    user_account = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'lecture'

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        elif self.last_name:
            return self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return 'Name not present'

@receiver(post_save, sender=User)
def create_lecture(sender, instance, created, **kwargs):
    if created:
       Lecture.objects.create(user_account=instance)

@receiver(post_save, sender=User)
def save_lecture(sender, instance, **kwargs):
    instance.lecture.save()
