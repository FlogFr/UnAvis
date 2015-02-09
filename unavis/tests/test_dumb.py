"""
dumb test to learn the framework
"""

from django.test import TestCase

import logging
logger = logging.getLogger(__name__)


class DumbTestCase(TestCase):
    def setUp(self):
        logger.info('setting up test case')

    def test_dumb_first(self):
        """
        we do a dumb calculation and assert it
        just to test the unit framework
        """
        self.assertEqual(1, 2-1)
