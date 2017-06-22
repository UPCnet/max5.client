# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import max5.client


class Max5ClientLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=max5.client)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'max5.client:default')


MAX5_CLIENT_FIXTURE = Max5ClientLayer()


MAX5_CLIENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MAX5_CLIENT_FIXTURE,),
    name='Max5ClientLayer:IntegrationTesting'
)


MAX5_CLIENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MAX5_CLIENT_FIXTURE,),
    name='Max5ClientLayer:FunctionalTesting'
)


MAX5_CLIENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MAX5_CLIENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='Max5ClientLayer:AcceptanceTesting'
)
