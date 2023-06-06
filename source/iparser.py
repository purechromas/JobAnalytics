from abc import ABC, abstractmethod


class IParser(ABC):
    @abstractmethod
    def get_requests(self, key_word: str, salary: int) -> dict:
        pass
