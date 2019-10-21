from __future__ import unicode_literals
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.core.files.base import ContentFile
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
# Create your models here.


THUMB_SIZE = (920,760)


class Category(TranslatableModel):
    image = models.ImageField(upload_to='media/category',null=True)
    
    translations = TranslatedFields(
        title = models.CharField(_("Başlıq"), max_length=200)
    )
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # category idsine gore ayrica seyfe (complete)
        return reverse("category-detail", kwargs={"pk": self.pk})
        
        #Mehsullar
class Product(models.Model):
    name = models.CharField(max_length=20,verbose_name=_("Ad"))
    price = models.IntegerField(verbose_name=_("Qiymət"))
    number = models.IntegerField()
    description = models.CharField(max_length=255,verbose_name=_("Haqqında"))
    img = models.ImageField(upload_to='media/product',verbose_name=_("Şəkil"))
    category = models.ForeignKey(to='Category',related_name='products',on_delete=models.CASCADE,null=True,verbose_name=_("Kateqoriyalar"))
    date = models.DateTimeField(default=timezone.now,verbose_name="Tarix")
    is_active = models.BooleanField(default=False)
    
   
    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe(f'<img src="{self.img.url}" width="300" height="300" />')
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

        #Top Mehsullar
class Topproduct(models.Model):
    name = models.CharField(max_length=20,verbose_name="Ad")
    price = models.IntegerField(verbose_name="Qiymət")
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=255,verbose_name="Haqqında")
    img = models.ImageField(upload_to='media/topproducts',verbose_name="Şəkil")
    category = models.ForeignKey('Category',related_name='topproducts',on_delete=models.CASCADE,null=True,verbose_name="Kategoriyalar")
    date = models.DateTimeField(default=timezone.now,verbose_name="Tarix")

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20,verbose_name=_("Ad"))
    email = models.EmailField(max_length=25,verbose_name=_("Email"))
    subject = models.CharField(max_length=50,verbose_name=_("Mövzu"))
    message = models.TextField(max_length=255,verbose_name=_("Mesaj"))

    def __str__(self):
        return self.name 


class Banertop(models.Model): 
    banner_top = models.ImageField(upload_to='media/banerstop')



class Banerleft(models.Model):
    banner_left = models.ImageField(upload_to='media/bannersleft')



class Banerright(models.Model):
    banner_right = models.ImageField(upload_to='media/bannersright')
