from abc import ABC, abstractmethod


class ISaver(ABC):

    @staticmethod
    @abstractmethod
    def save_json(vacancy):
        pass

    @staticmethod
    @abstractmethod
    def save_csv(vacancy):
        pass
