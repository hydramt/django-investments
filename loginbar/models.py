from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.


class mapping(models.Model):
      created = models.DateTimeField(auto_now_add=True)
      modified = models.DateTimeField(auto_now=True)
      uri = models.CharField(max_length=1000)
      text = models.CharField(max_length=50)
      enabled = models.BooleanField(default=True)

      def __str__(self):
         return '%s uri: %s text: %s' % (self.enabled, self.uri, self.text)
