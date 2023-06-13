import requests

from iparser import IParser
# im using .env file witch you need to make and add there your own super_job_key - https://api.superjob.ru/?from_refresh=1
from config import super_job_key


class SuperJobs(IParser):
    __exemplar = None
    __vacancies_found = None
    __vacancies = []
    __url = "https://api.superjob.ru/2.0/vacancies/"
    __header_key = {"X-Api-App-Id": super_job_key}

    def __new__(cls, *args, **kwargs):
        """Singleton"""
        if not cls.__exemplar:
            cls.__exemplar = super().__new__(cls)
        return cls.__exemplar

    @classmethod
    def get_request(cls, key_word: str, salary: int, page: int = 0) -> list:
        """Parsing vacancies from hh.ru and returning list of vacancies"""
        params = {
            "keyword": key_word,
            "no_agreement": 1,
            "payment_from": salary,
            "page": page
        }

        response = requests.get(url=cls.__url, params=params, headers=cls.__header_key)

        if response.ok:
            vacancies = response.json()
            cls.__vacancies_found = vacancies.get("total")
            filtered_vacancies = cls.__filter_vacancies(vacancies.get('objects'))
            validated_vacancies = cls.__validate_vacancies(filtered_vacancies)
            for vacancy in validated_vacancies:
                cls.__vacancies.append(vacancy)
            return validated_vacancies
        else:
            raise Exception(f"Requests was not successful | status code: {response.status_code}")

    @staticmethod
    def __filter_vacancies(vacancies: list) -> list:
        """Filtering vacancies by RUB, only with salary_from and salary_to"""
        first_filter = [vacancy for vacancy in vacancies if vacancy.get("currency") == "rub"]
        second_filter = [vacancy for vacancy in first_filter if vacancy.get("payment_from")]
        return [vacancy for vacancy in second_filter if vacancy.get("payment_to")]

    @staticmethod
    def __validate_vacancies(vacancies: list) -> list:
        """Rewriting the vacancies so we can use them easier"""
        validated_vacancies = []
        for vacancy in vacancies:
            _ = {
                "id": vacancy.get("id"),
                "title": vacancy.get("profession"),
                "url": vacancy.get("link"),
                "salary_from": vacancy.get("payment_from"),
                "salary_to": vacancy.get("payment_to"),
                "description": "".join(line for line in vacancy.get("candidat").replace("•", "").split("\n")),
                "area": vacancy.get("town").get("title"),
            }
            validated_vacancies.append(_)
        return validated_vacancies

    @staticmethod
    def sort_vacancies(vacancies: list) -> list:
        """Sorting the vacancies by salary_from"""
        return sorted(vacancies, key=lambda x: x.get("salary_from"))

    @classmethod
    def get_vacancy(cls, vacancy_id: str) -> dict:
        """Searching for vacancy in vacancies by ID and returning it"""
        _ = [vacancy for vacancy in cls.__vacancies if int(vacancy_id) == vacancy.get("id")]
        return _[0]

    @classmethod
    def print_beautiful(cls, vacancies: list) -> None:
        """Printing all vacancies in a more beautiful way"""
        for vacancy in vacancies:
            print(f'ВАКАНСИЯ ИЗ SUPERJOBS\n'
                  f'Должность: {vacancy.get("title")}\n'
                  f'Зарплата от: {vacancy.get("salary_from")} руб.\n'
                  f'Зарплата до: {vacancy.get("salary_to")} руб.\n'
                  f'Город: {vacancy.get("area")}\n'
                  f'Вакансия ID: {vacancy.get("id")}\n'
                  f'Вакансия URL: {vacancy.get("url")}\n\n'
                  f'Описание: {vacancy.get("description")[:400]}...\n\n\n')

    @classmethod
    def print_vacancies_found(cls) -> None:
        """Printing all vacancies witch where found after get_request"""
        print(f'\nНАЙДЕНЫ {cls.__vacancies_found} ВАКАНСИИ!\n')
