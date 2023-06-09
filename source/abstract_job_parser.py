from abc import ABC, abstractmethod


class AbstractJobParser(ABC):
    @abstractmethod
    def get_requests(self, key_word: str, salary: int, number_vacancies: int) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def _print_vacancies(vacancies: dict):
        pass
