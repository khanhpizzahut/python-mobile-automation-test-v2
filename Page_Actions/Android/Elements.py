from appium.webdriver.common.mobileby import MobileBy

class Home_Screen():
    txtview_hello = (MobileBy.ID,"tvHello")
    op_delivery = (MobileBy.ID,"tvDelivery")
    op_takeaway = (MobileBy.ID, "tvCollection")
    txtview_deals = (MobileBy.ID,"tvHotDealViewMenu")

class Onboard_Screen():
    icon_country = (MobileBy.ID, "view_change_country")
    btn_signin_register = (MobileBy.ID, "btnSignIn")
    btn_continue_guest = (MobileBy.ID, "btnContinueAsGuest")
    # Change Country
    option_country_uk = (MobileBy.XPATH,"// android.widget.TextView[ @ text = 'United Kingdom']")
    option_country_in = (MobileBy.XPATH,"// android.widget.TextView[ @ text = 'India']")
    btn_select_country = (MobileBy.ID, "btn_select_country")