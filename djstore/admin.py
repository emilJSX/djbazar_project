# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['name','price','date']
    list_display_links = ['name','price']
    readonly_fields = ['image_tag']

class TopProductAdmin(admin.ModelAdmin):
    
    list_display = ['name','price','date']
    list_display_links = ['name','price']

class CategoryAdmin(TranslatableAdmin):
    list_display = ['title']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Topproduct,TopProductAdmin)
admin.site.register(Banertop)
admin.site.register(Banerleft)
admin.site.register(Banerright)
