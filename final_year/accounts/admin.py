from django.contrib import admin
from .models import Faculty
from .models import Title
from .models import Lecture

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Title)
admin.site.register(Lecture)