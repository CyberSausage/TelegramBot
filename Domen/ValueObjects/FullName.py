from Domen.ValueObjects.BaseValueObjects import BaseValueObjects
from Domen.Primitivies.ValidationMessages import ValidationMessages
import re

class FullName(BaseValueObjects):
    def __init__(self, firstName: str, lastName: str):
        self.FirstName, self.LastName = self.validate_full_name(firstName, lastName)

    @staticmethod
    def validate_full_name(frstName, lstName: str) -> str:
        if not frstName or not lstName:
            raise ValueError(ValidationMessages.NullOrEmpty("FullName"))

        if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s]+$', frstName + lstName):
            raise ValueError("Полное имя должно содержать только русские или английские буквы")

        return frstName, lstName