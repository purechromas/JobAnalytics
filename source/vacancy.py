from ivacancy import IVacancy


class Vacancy(IVacancy):
    def __init__(self, vacancy: dict) -> None:
        self._title = vacancy.get("title")
        self._salary_from = vacancy.get("salary_from")
        self._salary_to = vacancy.get("salary_to")
        self._area = vacancy.get("area")
        self._id = vacancy.get("id")
        self._url = vacancy.get("url")
        self._description = vacancy.get("description")

    def __repr__(self):
        return f'{self}{self._title}{self._url}'

    def __str__(self):
        return self._title

    def __eq__(self, other):
        """EQUAL URL - [NOT EQUAL AUTOMATICALLY WORK]"""
        if isinstance(other, self.__class__):
            return self._url == other._url
        raise TypeError(f'== and != can be use only with exemplar : {self.__class__}')

    def __gt__(self, other):
        """GREATER THAN SALARY_TO - [LESS THAN AUTOMATICALLY WORK]"""
        if isinstance(other, self.__class__):
            return int(self._salary_to) > int(other._salary_to)
        raise TypeError(f'== and != can be use only with exemplar : {self.__class__}')

    @property
    def url(self):
        return self._url
