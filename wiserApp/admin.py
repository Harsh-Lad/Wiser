from django.contrib import admin
from .models import *
# Register your models here.

class MoodAdmin(admin.ModelAdmin):
    list_display = ('user','mood', 'date_added')
    list_filter = ('user', 'mood', 'date_added')
    search_fields = ('user', 'mood', 'date_added')

admin.site.register(Mood , MoodAdmin)

class AssigmentAdmin(admin.ModelAdmin):
    list_display = ('assignmentName','user', 'date_added')
    list_filter = ('user', 'date_added')
    search_fields = ('assignmentName','user', 'date_added')

admin.site.register(Assignemnt, AssigmentAdmin)


class NotesAdmin(admin.ModelAdmin):
    list_display = ('noteName','user', 'date_added')
    list_filter = ('user', 'date_added')
    search_fields = ('noteName','user',  'date_added')

admin.site.register(Notes, NotesAdmin)

class JournalAdmin(admin.ModelAdmin):
    list_display = ('journalName','user', 'date_added')
    list_filter = ('user', 'date_added')
    search_fields = ('journalName','user', 'date_added')

admin.site.register(Journal, JournalAdmin)