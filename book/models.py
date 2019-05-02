from django.db import models
from django.db.models import Q
from title.models import Title


# Create your models here.

# class BooksQuerySet(models.query.QuerySet):
    # def search_title(self, query):
    #     title_orim = Title.objects.all()
    #     lst =[]
    #     for obj in title_orim:
    #         lup = Q(asin__icontains=obj.asin) & Q(keyword__icontains=query)
    #         title_books = list(self.filter(lup).order_by('-date'))
    #         if len(title_books)>0 and title_books is not None:
    #             lst.append(title_books)
    #     new = []
    #     for i in lst:
    #         for j in i:
    #             new.append(j) 
    #     return new
    
    # def search_publisher(self, query, publisher):
    #     lookup = Q(publisher__icontains=publisher) & Q(keyword__icontains=query)
    #     lst2 = list(self.filter(lookup).order_by('-date'))
    #     return lst2

        

class BooksManager(models.Manager):

    def search_all(self, query):
        lookups = Q(keyword__icontains=query)
        return self.filter(lookups)

    def featured(self, query):
        lookup = Q(publisher__icontains=query)
        return self.filter(lookup)

    def orim(self, query, publisher):
        title_orim = Title.objects.all()
        new = books.objects.none()

        lookup = Q(publisher__icontains=publisher) & Q(keyword__icontains=query)
        lst = self.filter(lookup)

        for obj in title_orim:
            lup = Q(asin__icontains=obj.asin) & Q(keyword__icontains=query)
            title_books = self.filter(lup)
            if len(title_books)>0 and title_books is not None:
                new = new | title_books
        
        new = new | lst

        return new


class books(models.Model):
    
    title = models.CharField(max_length=120, null=True, blank=True)
    author = models.CharField(max_length=120, null=True, blank=True)
    publisher = models.CharField(max_length=120, null=True, blank=True)
    sales_rank = models.CharField(max_length=120, null=True, blank=True)
    page = models.CharField(max_length=120, null=True, blank=True)
    pages = models.CharField(max_length=120, null=True, blank=True)
    position = models.CharField(max_length=120, null=True, blank=True)
    date = models.CharField(max_length=120, null=True, blank=True)
    publication_date = models.CharField(max_length=120, null=True, blank=True)
    asin = models.CharField(max_length=120, null=True, blank=True)
    image = models.CharField(max_length=120, null=True, blank=True)
    keyword = models.CharField(max_length=120, null=True, blank=True)
    objects = BooksManager()

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    