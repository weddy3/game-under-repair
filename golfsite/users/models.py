from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"
    

    def save(self):
        # runs parent classes save method
        super().save()
        # want to scale down potential large uploaded images
        uploaded_profile_picture = Image.open(self.image.path)

        if uploaded_profile_picture.height > 300 or uploaded_profile_picture.width > 300:
            output_size = (300,300)
            uploaded_profile_picture.thumbnail(output_size)
            uploaded_profile_picture.save(self.image.path)