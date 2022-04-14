from django.contrib import admin

from .models import Project
from .models import Conceptual
from .models import Programming
from .models import Technical
from .models import Status
from .models import Subjects
from .models import Skill


# Register your models here.
admin.site.register(Project)
admin.site.register(Conceptual)
admin.site.register(Programming)
admin.site.register(Technical)
admin.site.register(Status)
admin.site.register(Subjects)
admin.site.register(Skill)
