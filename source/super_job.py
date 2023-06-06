import requests

from config import super_job_key
from iparser import IParser


class SuperJob(IParser):
    _link = 'https://api.superjob.ru/2.0/vacancies/'
    _header_key = {'X-Api-App-Id': super_job_key}

    @classmethod
    def get_requests(cls, key_word: str, salary: int = 100000) -> dict:
        """Searching for specific vacancies"""

        params = {
            'keyword': key_word,
            'no_agreement': 1,
            'payment_from': salary,
        }

        response = requests.get(cls._link, params=params, headers=cls._header_key)

        if response.ok:
            return response.json()
        else:
            raise Exception(f'Requests was not successful | status code: {response.status_code}')
