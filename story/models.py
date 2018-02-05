from django.db import models

# Create your models here.
class Story(models.Model):
    story_text = models.CharField(max_length = 500)

class AudioFile(models.Model):
    audio_track = models.FileField()
