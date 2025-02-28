from model.application import app
from data.users import User, Gender, Hobby
import datetime


def test_complete_and_submit_form():
    user = User(
        first_name='Fedor',
        last_name='Bubnov',
        email='fedor.bubnov_test@gmail.com',
        gender=Gender.MALE,
        phone_number='9990006666',
        date_of_birth=datetime.date(1997, 7, 3),
        subject='Biology',
        hobby=Hobby.SPORTS,
        avatar='avatar.jpg',
        address='Sadovaya, 14',
        state='Haryana',
        city='Karnal')
    app.registration.open()
    app.left_panel.open_simple_registration_form()

    # WHEN
    app.simple_registration.register(user)

    # THEN
    app.simple_registration.should_have_registered(user)
