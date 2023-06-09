import requests

from abstract_job_parser import AbstractJobParser


class HH(AbstractJobParser):
    _exemplar = None
    _vacancies = None
    _link = 'https://api.hh.ru/vacancies'

    def __new__(cls, *args, **kwargs):
        """Singleton"""

        if not cls._exemplar:
            cls._exemplar = super().__new__(cls)
        return cls._exemplar

    @staticmethod
    def _print_vacancies(vacancies: list) -> None:
        for vacancy in vacancies:
            print(f'ВАКАНЦИЯ ИЗ HH\n'
                  f'Должность: {vacancy.get("name")}\n'
                  f'Зарплата от: {vacancy.get("salary").get("from")} {vacancy.get("salary").get("currency")}\n'
                  f'Зарплата до: {vacancy.get("salary").get("to")} {vacancy.get("salary").get("currency")}\n'
                  f'Ваканция ID: {vacancy.get("id")}\n\n'
                  f'Обязанности: {vacancy.get("snippet").get("requirement")}\n'
                  f'Ответственность: {vacancy.get("snippet").get("responsibility")}\n\n\n')

    @classmethod
    def get_requests(cls, key_word: str, salary: int, number_vacancies: int) -> list:
        """Searching for specific vacancies"""

        params = {
            'text': key_word,
            'only_with_salary': True,
            'salary': salary,
        }

        response = requests.get(cls._link, params=params)

        if response.ok:
            vacancies = response.json()
            cls._vacancies = vacancies.get('items')[:number_vacancies]
            return vacancies.get('items')[:number_vacancies]
        else:
            raise Exception(f'Requests was not successful | status code: {response.status_code}')

    def sort_vacancies(self, vacancies: list, from_low_to_high: int) -> list:
        """Sorting the vacancies in specific payment order"""

        sorted_vacancies = sorted(vacancies,
                                  key=lambda x: x.get('salary').get('from') if x.get('salary').get(
                                      'from') is not None else float('-inf'))  # chatGPT helped with float('-inf')

        if from_low_to_high == 1:
            self._print_vacancies(sorted_vacancies)
            return sorted_vacancies
        elif from_low_to_high == 2:
            self._print_vacancies(sorted_vacancies[::-1])
            return sorted_vacancies[::-1]

    @classmethod
    def get_vacancy(cls, vacancy_id: int | str) -> dict:
        for vacancy in cls._vacancies:
            if vacancy.get('id') == str(vacancy_id):
                return vacancy
