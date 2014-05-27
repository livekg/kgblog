from django.contrib import admin
from category.models import Category
# Register your models here.
from models import ExtendedPage
from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page
from django.contrib import admin
from models import Category
from cms.extensions import PageExtensionAdmin

from .models import CategoryExtension,IconExtension

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'pub_date')
    pass

class CategoryExtensionAdmin(PageExtensionAdmin):
    list_display = ('page_category',)
    pass

class IconExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryExtension, CategoryExtensionAdmin)
admin.site.register(IconExtension, IconExtensionAdmin)

