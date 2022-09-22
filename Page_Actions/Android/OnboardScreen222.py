from Page_Actions.BasePage import BasePage
from Page_Actions.Android.HotelScreen import HotelScreen
from Page_Actions.Android.VillasScreen import VillasScreen


class OnboardScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def changeCountry_UK(self):
        self.click("icon_country_ID")
        self.click("option_country_uk_XPATH")
        self.click("btn_select_country_ID")

    def login(self):
        self.click("btn_signin_register_ID")

    def continue_as_guest(self):
        self.click("btn_continue_guset_ID")

    def nhapemai(self):
        self.type("textfield_email_ID","khanh@gmail.com")
    def gotoHotels(self):
        self.click("hotels_ID")
        return HotelScreen(self.driver)

    def gotoVillas(self):
        self.click("villas_XPATH")
        return VillasScreen(self.driver)

    def gotoFlights(self):
        pass

    def gotoTrains(self):
        pass
