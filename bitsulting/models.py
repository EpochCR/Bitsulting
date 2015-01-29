from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django import forms
from django.template.defaultfilters import slugify

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256, unique=True)
    author = models.ForeignKey(User)
    slug = models.SlugField(max_length=256, unique=True)
    body = models.TextField(unique=True, blank=False)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('bitsulting.Category')
    bitcoinAddress = models.CharField(max_length=35)
    reward_value = models.CharField(default='0.00001000', blank=False, max_length=17)
    active = forms.BooleanField(initial=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('q', None, { 'slug': self.slug })

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Question, self).save(*args, **kwargs)

#Responses that contain the address that need no login
class Response(models.Model):
    bitcoinAddress = models.CharField(max_length=35)
    text = models.TextField()
    question = models.ForeignKey(Question)
    created_on = models.DateTimeField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return self.text

class Category(models.Model):
    title = models.CharField(max_length=256, db_index=True)
    slug = models.SlugField(max_length=256, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('c', None, { 'slug': self.slug })