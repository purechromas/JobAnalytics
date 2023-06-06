import requests

from iparser import IParser


class HH(IParser):
    _exemplar = None
    _link = 'https://api.hh.ru/vacancies'

    def __new__(cls, *args, **kwargs):
        """Singleton"""

        if not cls._exemplar:
            cls._exemplar = super().__new__(cls)
        return cls._exemplar

    @classmethod
    def get_requests(cls, key_word: str, salary: int = 100000) -> dict:
        """Searching for specific vacancies"""

        params = {
            'text': key_word,
            'only_with_salary': True,
            'salary': salary,
        }

        response = requests.get(cls._link, params=params)

        if response.ok:
            return response.json()
        else:
            raise Exception(f'Requests was not successful | status code: {response.status_code}')
