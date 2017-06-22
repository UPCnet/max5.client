# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from base5.core.testing import BASE5_CORE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that base5.core is properly installed."""

    layer = BASE5_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if base5.core is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'base5.core'))

    def test_browserlayer(self):
        """Test that IBase5CoreLayer is registered."""
        from base5.core.interfaces import (
            IBase5CoreLayer)
        from plone.browserlayer import utils
        self.assertIn(IBase5CoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = BASE5_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['base5.core'])

    def test_product_uninstalled(self):
        """Test if base5.core is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'base5.core'))

    def test_browserlayer_removed(self):
        """Test that IBase5CoreLayer is removed."""
        from base5.core.interfaces import \
            IBase5CoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(IBase5CoreLayer, utils.registered_layers())
