import csv
import json

from abstract_job_saver import AbstractJobSaver


class JobSaver(AbstractJobSaver):
    _exemplar = None

    def __new__(cls, *args, **kwargs):
        """Singleton"""

        if not cls._exemplar:
            cls._exemplar = super().__new__(cls)
        return cls._exemplar

    @staticmethod
    def save_json(vacancy: dict):
        with open('vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(vacancy, file)

    @staticmethod
    def save_csv(vacancy: dict):
        with open("vacancies.csv", 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in vacancy.items():
                writer.writerow([key, value])
