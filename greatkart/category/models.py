from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50,unique=True)
    slug = models.CharField(max_length=50,unique=True) # url of category
    description = models.TextField(max_length=255 ,blank = True)  # product description
    cat_image = models.ImageField(upload_to='photos/categories',blank=True) 
    # we need pillow library so install it

    class Meta:
        verbose_name='category'
        verbose_name_plural= 'categories'   #for admin panel

    def get_url(self):
        return reverse("products_by_category",args=[self.slug])
#url name in urls.py
    
    def __str__(self):
        return self.category_name
   
