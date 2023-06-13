from abc import ABC, abstractmethod


class IParser(ABC):
    @classmethod
    @abstractmethod
    def get_request(cls, key_word, salary, page):
        pass

    @classmethod
    @abstractmethod
    def print_beautiful(cls, vacancies):
        pass

    @staticmethod
    @abstractmethod
    def sort_vacancies(vacancies):
        pass

    @classmethod
    @abstractmethod
    def get_vacancy(cls, vacancy_id):
        pass

    @classmethod
    @abstractmethod
    def print_vacancies_found(cls):
        pass
