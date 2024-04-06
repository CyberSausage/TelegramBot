from Domen.Primitivies.Gender import Gender
from Domen.ValueObjects.FullName import FullName
from Domen.Primitivies.ValidationMessages import ValidationMessages
from Domen.Entities.BaseEntity import BaseEntity
from datetime import datetime
from typing import Union
import re

class Pers(BaseEntity):
    def __init__(self, fullName: FullName, birthDay: Union[datetime, None] = None, gender=None, phoneNumber: str = "", telegram: str = ""):
        super().__init__()
        self.FullName = fullName
        self.BirthDay = self.validate_BirthDay(birthDay)
        self.Gender = self.validate_Gender(gender)
        self.PhoneNumber = self.validate_PhoneNumber(phoneNumber)
        self.Telegram = self.validate_Telegram(telegram)

    @staticmethod
    def validate_BirthDay(birthDay: datetime) -> datetime:
        if not birthDay:
            raise ValueError(ValidationMessages.NullOrEmpty("BirthDay"))

        if birthDay >= datetime.now():
            raise ValueError("Вы ещё не родились")

        if not birthDay.year <= 150:
            raise ValueError("Возраст не может превышать 150 лет")

        return birthDay

    @staticmethod
    def validate_Gender(gender: int) -> int:
        if not gender == Gender.Undefined and not gender == Gender.Man and not gender == Gender.Woman:
            raise ValueError("Гендер не найден")

        return gender

    @staticmethod
    def validate_Telegram(telegram: str) -> str:
        if not telegram:
            raise ValueError(ValidationMessages.NullOrEmpty("Telegram"))

        if not re.match(r'^@[a-zA-Z0-9]{1,20}$', telegram):
            raise ValueError("Ник должен содержать: \"@\" и не превышать 20 символов")

        return telegram

    @staticmethod
    def validate_PhoneNumber(phoneNumber: str) -> str:
        if not phoneNumber:
            raise ValueError(ValidationMessages.NullOrEmpty("PhoneNumber"))

        if not re.match(r'^\+37377[4-9]{5}$', phoneNumber):
            raise ValueError("Телефон должен содержать: \"+37377\" и не превышать 12 символов")

        return phoneNumber

    @property
    def Age(self) -> int:
        return datetime.now().year - self.BirthDay.year
