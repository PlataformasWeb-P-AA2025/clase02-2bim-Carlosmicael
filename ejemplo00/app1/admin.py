from django.contrib import admin

# Register your models here.

from .models import Estudiante
from .models import Ciudad


admin.site.register(Estudiante)
admin.site.register(Ciudad)