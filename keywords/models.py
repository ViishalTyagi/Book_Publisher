from django.db import models
from django.db.models import Q


# Create your models here.

class KeywordsManager(models.Manager):

    def search(self, query):
        lookups = Q(keyword__icontains=query)
        list = self.filter(lookups)
        if len(list)>0:
            return True
        return False


class keyword(models.Model):
    keyword = models.CharField(max_length=120, blank=True, null=True)
    objects = KeywordsManager()