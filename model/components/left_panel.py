from selene import browser, have


class LeftPanel:

    def open(self, menu_block, sub_menu):
        (browser.all('.element-group').element_by(have.text(menu_block)).click()
         .all('li').element_by(have.text(sub_menu)).click())
        return self

    def open_simple_registration_form(self):
        return self.open('Elements', 'Text Box')
