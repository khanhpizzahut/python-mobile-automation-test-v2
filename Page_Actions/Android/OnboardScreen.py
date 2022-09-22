from Page_Actions.BasePage import BasePage
from Page_Actions.Android.Elements import *


class OnboardScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def changeCountry_UK(self):
        self.click(Onboard_Screen.icon_country)
        self.click(Onboard_Screen.option_country_uk)
        self.click(Onboard_Screen.btn_select_country)

    def changeCountry_IN(self):
        self.click(Onboard_Screen.icon_country)
        self.click(Onboard_Screen.option_country_in)
        self.click(Onboard_Screen.btn_select_country)

    def login(self):
        self.click(Onboard_Screen.btn_signin_register)

    def continue_as_guest(self):
        self.click(Onboard_Screen.btn_continue_guest)
