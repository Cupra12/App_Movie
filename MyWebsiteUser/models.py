from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    my_photo = models.ImageField(null=True, blank=True, upload_to='other/image_user/', default='no_avatar.jpg')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('Home')

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"