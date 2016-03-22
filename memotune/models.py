from django.db import models
from django.contrib.auth.models import User

    
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    join_data = models.DateField()
    high_score = models.IntegerField(default=0)
    
    
    def __unicode__(self):
        return self.user.username