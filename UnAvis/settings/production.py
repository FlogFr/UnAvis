"""
Django production settings for 1Avis project.
"""

from UnAvis.settings.defaults import DefaultConfiguration
import os
import dj_database_url


class ProductionConfiguration(DefaultConfiguration):
    ALLOWED_HOSTS = ['.1avis.fr',
                     '127.0.0.1',
                     '.localhost']
