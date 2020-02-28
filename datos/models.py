from django.db import models

# Create your models here.
class Dato(models.Model):
    titulo = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    chrono = models.BigIntegerField()
    value = models.FloatField()
    quality = models.SmallIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    
    def __str__(self):
        return self.titulo

    def snippet(self):
        return self.name[:50] + '...'