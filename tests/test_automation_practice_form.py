import datetime
from model.pages.registration_page import RegistrationPage
from data.users import User, Gender, Hobby, Subject


def test_complete_and_submit_form():
    user = User(
        first_name='Fedor',
        last_name='Bubnov',
        email='fedor.bubnov_test@gmail.com',
        gender=Gender.MALE,
        phone_number='9990006666',
        date_of_birth=datetime.date(1997, 7, 3),
        subjects=[Subject.ENGLISH, Subject.BIOLOGY],
        hobbies=[Hobby.SPORTS, Hobby.MUSIC],
        avatar='avatar.jpg',
        address='Sadovaya, 14',
        state='Haryana',
        city='Karnal')
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.register(user)

    # THEN
    registration_page.should_have_registered(user)
