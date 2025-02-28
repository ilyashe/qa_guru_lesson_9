from selene import browser, have


class SimpleUserRegistrationPage:

    @staticmethod
    def open():
        browser.open('/text-box')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        # browser.driver.execute_script("document.body.style.zoom = '0.5'")

    @staticmethod
    def register(user):
        browser.element('#userName').type(f'{user.first_name} {user.last_name}')
        browser.element('#userEmail').type(user.email)
        browser.element('#currentAddress').type(user.address)
        browser.element('#permanentAddress').type(user.address)

        browser.element('#submit').click()

    @staticmethod
    def should_have_registered(user):
        browser.element('#name').should(have.text(f'{user.first_name} {user.last_name}'))
        browser.element('#email').should(have.text(user.email))
        browser.element('p#currentAddress').should(have.text(user.address))
        browser.element('p#permanentAddress').should(have.text(user.address))
