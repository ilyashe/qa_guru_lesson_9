import dataclasses
import enum


class Gender(enum.Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Hobby(enum.Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    hobby: Hobby
    avatar: str
    address: str
    state: str
    city: str
