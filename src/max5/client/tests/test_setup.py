# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from max5.client.testing import MAX5_CLIENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that max5.client is properly installed."""

    layer = MAX5_CLIENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if max5.client is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'max5.client'))

    def test_browserlayer(self):
        """Test that IMax5ClientLayer is registered."""
        from max5.client.interfaces import (
            IMax5ClientLayer)
        from plone.browserlayer import utils
        self.assertIn(IMax5ClientLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MAX5_CLIENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['max5.client'])

    def test_product_uninstalled(self):
        """Test if max5.client is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'max5.client'))

    def test_browserlayer_removed(self):
        """Test that IMax5ClientLayer is removed."""
        from max5.client.interfaces import \
            IMax5ClientLayer
        from plone.browserlayer import utils
        self.assertNotIn(IMax5ClientLayer, utils.registered_layers())
