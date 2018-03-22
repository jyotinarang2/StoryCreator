from django.contrib import admin
from django import forms
from django.forms import ModelForm
from .models import Story
# Register your models here.
list_display = (..., 'audio_file_player', ...)
actions = ['custom_delete_selected']


        
def custom_delete_selected(self, request, queryset):
    #custom delete code
    n = queryset.count()
    for i in queryset:
        if i.audio_file:
            if os.path.exists(i.audio_file.path):
                os.remove(i.audio_file.path)
        i.delete()
    self.message_user(request, _("Successfully deleted %d audio files.") % n)
custom_delete_selected.short_description = "Delete selected items"

def get_actions(self, request):
    actions = super(AudioFileAdmin, self).get_actions(request)
    del actions['delete_selected']
    return actions

admin.site.register(Story)
#admin.site.register(AudioFile)
