import re
from django.conf import settings
from waffle.models import Switch

MAINTENANCE_IGNORE_URLS = getattr(settings, 'MAINTENANCE_IGNORE_URLS', ())
IGNORE_URLS = tuple([re.compile(url) for url in MAINTENANCE_IGNORE_URLS])

import logging
logger = logging.getLogger(__name__)


class MaintenanceModeMiddleware(object):
    def process_request(self, request):
        try:
            switch = Switch.objects.get(name='WebsiteUnderMaintenance')
            MAINTENANCE_MODE = switch.active
        except:
            MAINTENANCE_MODE = False
        if not MAINTENANCE_MODE:
            return None

        # Allow access if remote ip is in INTERNAL_IPS
        if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return None

        # Allow access if the user doing the request is logged in and a
        # staff member.
        if hasattr(request, 'user') and request.user.is_staff:
            return None

        # Check if a path is explicitly excluded from maintenance mode
        for url in IGNORE_URLS:
            if url.match(request.path_info):
                return None

        # otherwise add the flag to the request
        request.META['WEBSITE_UNDER_MAINTENANCE'] = True
