from django.contrib import admin
from category.models import Category
# Register your models here.
from models import ExtendedPage
from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page
from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from .models import CategoryExtension,IconExtension


class CategoryExtensionAdmin(PageExtensionAdmin):
    pass

class IconExtensionAdmin(PageExtensionAdmin):
    pass

admin.site.register(Category)
admin.site.register(CategoryExtension, CategoryExtensionAdmin)
admin.site.register(IconExtension, IconExtensionAdmin)

