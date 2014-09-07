"""
help and tools for the sitemaps
"""

from django.contrib.sitemaps import FlatPageSitemap

class CustomFlatPageSitemap(FlatPageSitemap):
    def location(self, obj):
        return "{}{}".format("/page", obj.get_absolute_url())
