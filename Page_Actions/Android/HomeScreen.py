from Page_Actions.BasePage import BasePage
from Page_Actions.Android.Elements import *


class HomeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

# Not allow location
    def localiseDelivery(self):
        self.click("option_delivery_ID")
        try:
            self.click("premission_location_btn_close_ID")
        except:
            self.click("location_not_allow_first_time_ID")

    def localiseTakeaway(self):
        self.click("option_takeaway_ID")
        try:
            self.click("premission_location_btn_close_ID")
        except:
            self.click("location_not_allow_first_time_ID")

# Check deals
    def viewDeals(self):
        self.click(Home_Screen.txtview_deals)

