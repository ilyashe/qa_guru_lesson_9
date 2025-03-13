import dataclasses
import enum
import datetime
from typing import List


class Gender(enum.Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Hobby(enum.Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


class Subject(enum.Enum):
    ENGLISH = "english"
    CHEMISTRY = "chemistry"
    COMMERCE = "commerce"
    ECONOMICS = "economics"
    BIOLOGY = 'Biology'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    phone_number: str
    date_of_birth: datetime.date
    subjects: List[Subject]
    hobbies: List[Hobby]
    avatar: str
    address: str
    state: str
    city: str

    def formatted_year(self) -> str:
        """Возвращает год как строку."""
        return str(self.date_of_birth.year)

    def formatted_month(self) -> str:
        return self.date_of_birth.strftime("%B")

    def formatted_day(self) -> str:
        return self.date_of_birth.strftime("%d")

    def formatted_hobbies(self)-> str:
        return ', '.join((hobby.value for hobby in self.hobbies))

    def formatted_subjects(self)-> str:
        return ', '.join((subject.value.capitalize() for subject in self.subjects))