from django.db import models

# Create your models here.
from .utils import code_generator, create_shortcode

class MyUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(MyUrl, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcode(self):
        qs = MyUrl.objects.all()
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            print(q.shortcode)
            new_codes += 1
        return "New codes made: {i}".format(i = new_codes)

class MyUrl(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=20, unique=True, null=False, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = MyUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=="":
            self.shortcode = create_shortcode(self)
        super(MyUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
