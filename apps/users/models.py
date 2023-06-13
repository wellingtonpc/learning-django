from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
        upload_to='profile_pictures'
    )
    location = models.CharField(max_length=100)