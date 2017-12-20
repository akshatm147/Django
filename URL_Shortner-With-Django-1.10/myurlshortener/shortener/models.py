from django.db import models

# Create your models here.
from .utils import code_generator, create_shortcode

class MyUrl(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=20, unique=True, null=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=="":
            self.shortcode = create_shortcode(self)
        super(MyUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
