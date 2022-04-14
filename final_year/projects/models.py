from __future__ import unicode_literals
from asyncio.windows_events import NULL
import encodings
from optparse import Values
from pickle import TRUE
from tkinter import CASCADE
from tokenize import Number
from unicodedata import name
from xml.parsers.expat import model
import django
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import Lecture
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
import string
import random
from django.urls import reverse



class Skill(models.Model):
    skill_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'skill'

    def __str__(self):
        return self.skill_name


class Subjects(models.Model):
    subjects_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'subjects'


    def __str__(self):
        return self.subjects_name


class Status(models.Model):
    id = models.BigIntegerField(primary_key=True)
    status_name = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'status'
    
    def __str__(self):
        return self.status_name

class Technical(models.Model):
    id = models.BigIntegerField(primary_key=True)
    technical_dif = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'technical'

    def __str__(self):
        return self.technical_dif

class Programming(models.Model):
    id = models.BigIntegerField(primary_key=True)
    programming_dif = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'programming'

    def __str__(self):
        return self.programming_dif

class Conceptual(models.Model):
    id = models.BigIntegerField(primary_key=True)
    conceptual_dif = models.CharField(blank=True, null=True, max_length=50)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'conceptual'

    def __str__(self):
        return self.conceptual_dif

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    date = models.DateTimeField(null=True, default= timezone.now)
    lecture = models.ForeignKey(Lecture, models.DO_NOTHING, blank=True, )
    lecture2 = models.ForeignKey(User,on_delete=models.CASCADE)
    conceptual = models.ForeignKey(Conceptual, models.DO_NOTHING,  )
    technical = models.ForeignKey('Technical', models.DO_NOTHING,  )
    programming = models.ForeignKey(Programming, models.DO_NOTHING,  )
    status = models.ForeignKey('Status', models.DO_NOTHING, blank=True, null=True)
    Skill = models.ManyToManyField(Skill, blank=True, related_name= 'pskills')
    subject = models.ManyToManyField(Subjects, blank=True, related_name='psubjects')

    class Meta:
        managed = True
        db_table = 'project'
    #sets p_skill to the information from skill field using query set flter()
    def p_skill(self):
        return self.Skill.filter()
    #sets p_subject to the information from skill field using query set flter()
    def p_subject(self):
        return self.subject.filter()

    #return the string of project as title in admin area
    def __str__(self):
        return self.title

    #create snippet of description to display 200 characters long
    def snippet(self):
        return self.description[:200] + '...'

    def get_absolute_url(self):
        return reverse('projects:list')


    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        super(Project, self).save(*args, **kwargs)

    def generate_slug(self, save_to_obj=False, add_random_suffix=True):
       # `add_random_suffix ` is to make sure that slug field has unique value.
        #using django slugify to turn title into slug. ie add - where spaces would be, and assign it to variable
        generated_slug = slugify(self.title)

        # Generate random suffix here, that is 5 long
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(10)
            ])
            generated_slug += '-%s' % random_suffix
            #add random suffix to generated slug variable

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])
        #save generated slug to slug fild by calling above save function
        return generated_slug








