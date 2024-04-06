from abc import ABC, abstractmethod
import uuid
from datetime import datetime

class BaseEntity(ABC):
    def __init__(self):
        self.Id = uuid.uuid4()
        self.CreatedData = datetime.now()
        self.DateOfBirth = None

    def __eq__(self, other):
        if isinstance(other, BaseEntity):
            return self.Id == other.Id
        return NotImplemented

    def __hash__(self):
        return hash(self.Id)
