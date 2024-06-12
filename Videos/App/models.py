from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,FileExtensionValidator
# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Dars nomi')
    video = models.FileField(upload_to='lesson/', verbose_name='dars nomi',
                             validators=[FileExtensionValidator(allowed_extensions=['mp4','mov'])],
                             help_text='Video yuklang')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name