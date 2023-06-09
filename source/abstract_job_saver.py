from abc import ABC, abstractmethod


class AbstractJobSaver(ABC):
    @staticmethod
    @abstractmethod
    def save_json(self):
        pass

    @staticmethod
    @abstractmethod
    def save_csv(self):
        pass
