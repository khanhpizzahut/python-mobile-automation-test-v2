import time

from Page_Actions.Android.OnboardScreen import OnboardScreen
from TestCases.BaseTest import BaseTest


class Test_SearchHotel(BaseTest):

    # @pytest.mark.parametrize("city", dataProvider.get_data("SearchTest"))
    # def test_searchHotel(self,city):
    #     home = HomeScreen(self.driver)
    #     home.gotoHotels().searchHotel(city)

    def test_vaologin(self):
        home = OnboardScreen(self.driver)
        home.login()
        time.sleep(20)