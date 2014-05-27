from django import template
from cms.models.pagemodel import Page
from category.models import CategoryExtension
register = template.Library()

def cms_latest_news():
    categoryExtensions = CategoryExtension.objects.filter(page_category__category_name='News')
    filterCatExt = categoryExtensions.exclude(public_extension_id=None).distinct()
    cms_pages = Page.objects.filter(categoryextension__in=filterCatExt.values_list('id')).distinct()
    return {'cms_pages': cms_pages}

register.inclusion_tag('latest_news.html')(cms_latest_news)