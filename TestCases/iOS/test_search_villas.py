import pytest

from Page_Actions.Android.OnboardScreen import OnboardScreen
from TestCases.BaseTest import BaseTest
from Utilities import dataProvider
from Utilities.scroll_util import ScrollUtil


class Test_SearchVilla(BaseTest):

    @pytest.mark.parametrize("city,hotel", dataProvider.get_data("VillaTest"))
    def test_searchVilla(self,city,hotel):
        home = OnboardScreen(self.driver)
        home.gotoVillas().searchVilla(city)
        ScrollUtil.scrollToTextByAndroidUIAutomator(hotel, self.driver)