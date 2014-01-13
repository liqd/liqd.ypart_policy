from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class Liqdypart_PolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import liqd.ypart_policy
        xmlconfig.file(
            'configure.zcml',
            liqd.ypart_policy,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'liqd.ypart_policy:default')

LIQD_YPART_POLICY_FIXTURE = Liqdypart_PolicyLayer()
LIQD_YPART_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LIQD_YPART_POLICY_FIXTURE,),
    name="Liqdypart_PolicyLayer:Integration"
)
LIQD_YPART_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LIQD_YPART_POLICY_FIXTURE, z2.ZSERVER_FIXTURE),
    name="Liqdypart_PolicyLayer:Functional"
)
