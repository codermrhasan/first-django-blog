from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField('Upload your profile picture',default='profile_pics/defaultpropic.jpg', upload_to='profile_pics/')
    blog_banner = models.ImageField(default='blog_banner_pics/default_blog_banner1.jpg', upload_to='blog_banner_pics/')
    blog_description = models.TextField(max_length=124, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

