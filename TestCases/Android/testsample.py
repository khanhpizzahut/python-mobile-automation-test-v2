import unittest

from Page_Actions.Android.Elements import *
from Page_Actions.Android.OnboardScreen import OnboardScreen
from TestCases.BaseTest import BaseTest


class testSample(BaseTest, unittest.TestCase):
    def test_001_2126_tc0(self):
        onboard = OnboardScreen(self.driver)
        onboard.changeCountry_UK()
        onboard.verifyTextview(Onboard_Screen.btn_signin_register,"Sign in or Register")
    def test_002_2137_tc1(self):
        onboard = OnboardScreen(self.driver)
        onboard.changeCountry_IN()
        onboard.login()
        assert 1 == 2





