from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.CharField(max_length=10)
    lte_exists = models.CharField(max_length=5)
    slug = models.SlugField()
