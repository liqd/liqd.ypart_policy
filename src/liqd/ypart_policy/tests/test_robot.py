from  liqd.ypart_policy.testing import LIQD_YPART_POLICY_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=LIQD_YPART_POLICY_FUNCTIONAL_TESTING)
    ])
    return suite