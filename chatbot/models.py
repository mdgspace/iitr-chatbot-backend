from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class Links(models.Model):
    link_name = models.CharField(max_length = 60)
    url = models.URLField(max_length = 200)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return (self.link_name)

    class Meta:
        ordering = ['link_name']


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    links = GenericRelation(Links)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_category',
        blank=True)
    links = GenericRelation(Links)

    def category_name(self):
        return self.category.category_name

    def __str__(self):
       return self.sub_category_name




