from django.contrib import admin
from .models import *

class NoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Note, NoteAdmin)