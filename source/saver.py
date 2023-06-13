import csv
import json

from isaver import ISaver


class Saver(ISaver):
    _exemplar = None

    def __new__(cls, *args, **kwargs):
        """Singleton"""

        if not cls._exemplar:
            cls._exemplar = super().__new__(cls)
        return cls._exemplar

    @staticmethod
    def save_json(vacancy: dict) -> None:
        """Saving the vacancy in a csv file with name 'vacancy.json' in a main folder"""
        with open('vacancy.json', 'w', encoding='utf-8') as file:
            json.dump(vacancy, file)

    @staticmethod
    def save_csv(vacancy: dict) -> None:
        with open("vacancy.csv", 'w', encoding='utf-8') as csvfile:
            """Saving the vacancy in a csv file with name 'vacancy.csv' in a main folder"""
            writer = csv.writer(csvfile)
            for key, value in vacancy.items():
                writer.writerow([key, value])
