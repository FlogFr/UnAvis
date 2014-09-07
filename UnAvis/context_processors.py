"""
this context processors aims to
generate the menu for example
"""

from UnAvis.tools.menu import get_menu

import logging
logger = logging.getLogger(__name__)


def menu(request):
    return get_menu(request)
