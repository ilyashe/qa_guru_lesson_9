from model.pages.registration_page import RegistrationPage
from model.components.left_panel import LeftPanel
from model.pages.simple_registration_page import SimpleUserRegistrationPage


class Application:
    def __init__(self):
        self.registration = RegistrationPage()
        self.simple_registration = SimpleUserRegistrationPage()
        self.left_panel = LeftPanel()


app = Application()
