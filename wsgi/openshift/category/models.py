from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pagemodel import Page
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Hello(CMSPlugin):
    guest_name = models.CharField(max_length=50, default='Guest')

class ExtendedPage(models.Model):
    page = models.ForeignKey(Page, unique=True, verbose_name=_("Page"), editable=False, related_name='extended_fields')
    pagecategory = models.ForeignKey('Category')

class CategoryExtension(PageExtension):
    page_categories = models.ManyToManyField('Category', blank=True, null=True)

    def copy_relations(self, oldinstance, language):
        for page_category in oldinstance.page_categories.all():
            page_category.pk = None
            page_category.CategoryExtension = self
            page_category.save()

class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')

extension_pool.register(CategoryExtension)
extension_pool.register(IconExtension)
