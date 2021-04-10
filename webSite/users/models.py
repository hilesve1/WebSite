from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', upload_to='user_images', default='default.png')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

        #Чтоб обрезать изображение
    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)


    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайл'
