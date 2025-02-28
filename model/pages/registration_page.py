from selene import browser, have, command
from model import resource


class RegistrationPage:

    @staticmethod
    def open():
        browser.open('/automation-practice-form')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        # browser.driver.execute_script("document.body.style.zoom = '0.5'")

    @staticmethod
    def register(user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element(f'[name=gender][value={user.gender.value}]').perform(command.js.click)
        browser.element('#userNumber').type(user.phone_number)

        browser.element('#dateOfBirthInput').click()
        (browser.element('.react-datepicker__month-select').click().all('option').
         element_by(have.text(user.formatted_month())).click())
        (browser.element('.react-datepicker__year-select').click().all('option').
         element_by(have.text(user.formatted_year())).click())
        browser.element(f'.react-datepicker__day--0{user.formatted_day()}').click()

        browser.element('#subjectsInput').type(user.subject).press_enter()
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(user.hobby.value)).click()

        browser.element('#uploadPicture').set_value(resource.path(user.avatar))

        browser.element('#currentAddress').type(user.address)
        browser.element('#state').click().all('[id^=react-select-3-option]').element_by(have.text(user.state)).click()
        browser.element('#city').click().all('[id^=react-select-4-option]').element_by(have.text(user.city)).click()

        browser.element('#submit').click()

    @staticmethod
    def should_have_registered(user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender.value,
                user.phone_number,
                f'{user.formatted_day()} {user.formatted_month()},{user.formatted_year()}',
                user.subject,
                user.hobby.value,
                user.avatar,
                user.address,
                f'{user.state} {user.city}',
            )
        )
