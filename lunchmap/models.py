from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(verbose_name='Title', max_length=255)
    description = models.TextField(verbose_name='description', blank=True, null=True)
    original_name = models.CharField(verbose_name='original_name',max_length=255, blank=True, null=True)
    filename = models.CharField(verbose_name='filename', max_length=255, blank=True, null=True)
    # author = models.ForeignKey(
    #     'auth.User',
    #     on_delete=models.CASCADE,
    # )
    photo1 = models.ImageField(verbose_name='Picture', blank=True, null=True)
    photo2 = models.FileField(verbose_name='Movie', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lunchmap:detail', kwargs={'pk': self.pk})

# class Shop(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#     author = models.ForeignKey(
#         'auth.User',
#         on_delete=models.CASCADE,
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.PROTECT,
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('lunchmap:detail', kwargs={'pk': self.pk})