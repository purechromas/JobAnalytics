import requests

from config import super_job_key
from abstract_job_parser import AbstractJobParser


class SuperJob(AbstractJobParser):
    _vacancies = None
    _exemplar = None
    _link = 'https://api.superjob.ru/2.0/vacancies/'
    _header_key = {'X-Api-App-Id': super_job_key}

    def __new__(cls, *args, **kwargs):
        """Singleton"""

        if not cls._exemplar:
            cls._exemplar = super().__new__(cls)
        return cls._exemplar

    @staticmethod
    def _print_vacancies(vacancies: list) -> None:
        """Beautiful print of vacancies in terminal"""

        for vacation in vacancies:
            print(f'ВАКАНЦИЯ ИЗ SUPERJOB\n'
                  f'Должность: {vacation.get("profession")}\n'
                  f'Зарплата от: {vacation.get("payment_from")} руб.\n'
                  f'Зарплата до: {vacation.get("payment_to")} руб.\n'
                  f'Ваканция ID: {vacation.get("id")}\n\n'
                  f'Обязанности: {vacation.get("candidat")}\n\n\n')

    @classmethod
    def get_requests(cls, key_word: str, salary: int, number_vacancies: int) -> list:
        """Searching for specific vacancies"""

        params = {
            'keyword': key_word,
            'no_agreement': 1,
            'payment_from': salary,
        }

        response = requests.get(cls._link, params=params, headers=cls._header_key)

        if response.ok:
            vacancies = response.json()
            cls._vacancies = vacancies.get('objects')[:number_vacancies]
            return vacancies.get('objects')[:number_vacancies]
        else:
            raise Exception(f'Requests was not successful | status code: {response.status_code}')

    def sort_vacancies(self, vacancies: list, from_low_to_high: int) -> list:
        """Sorting the vacancies in specific payment order"""

        sorted_vacancies = sorted(vacancies, key=lambda x: x.get('payment_from'))

        if from_low_to_high == 1:
            self._print_vacancies(sorted_vacancies)
            return sorted_vacancies
        elif from_low_to_high == 2:
            self._print_vacancies(sorted_vacancies[::-1])
            return sorted_vacancies[::-1]
        else:
            raise TypeError

    @classmethod
    def get_vacancy(cls, vacancy_id: str) -> dict:
        for vacancy in cls._vacancies:
            if vacancy.get('id') == int(vacancy_id):
                return vacancy
