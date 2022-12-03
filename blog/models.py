from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=100, verbose_name='title')
    pub_date = models.DateField(auto_now=True, verbose_name='pub_date')
    text = models.TextField(verbose_name='text')
