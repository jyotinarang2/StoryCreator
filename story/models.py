from django.db import models

# Create your models here.
class Story(models.Model):
    story_text = models.CharField(max_length = 500)
    def __str__(self):
        return self.story_text

#class AudioFile(models.Model):
#    file_name = models.CharField(max_length = 100, blank = False)
#    audio_track = models.FileField()
#    def __str__(self):
#        return  self.file_name

#class ListeningTest(models.Model):
    
