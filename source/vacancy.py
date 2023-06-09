from abstract_vacancy import AbstractVacancy


class Vacancy(AbstractVacancy):
    def __init__(self, vacancy: dict, site: str):
        if site == 'hh':
            self._job_title = vacancy.get('name')
            self._salary_from = vacancy.get('salary').get('from')
            self._salary_to = vacancy.get('salary').get('to')
            self._vacation_id = vacancy.get('id')
            self._requirement = vacancy.get('snippet').get('requirement')
            self._responsibility = vacancy.get('snippet').get('responsibility')
            self._experience = vacancy.get('experience').get('name')
            self._area = vacancy.get('area').get('name')
            self._url = vacancy.get('alternate_url')
        elif site == 'superjob':
            self._job_title = vacancy.get('profession')
            self._salary_from = vacancy.get('payment_from')
            self._salary_to = vacancy.get('payment_to')
            self._vacation_id = vacancy.get('id')
            self._requirement = vacancy.get('candidat')
            self._responsibility = vacancy.get
            self._experience = vacancy.get('experience').get('title')
            self._area = vacancy.get('town').get('title')
            self._url = vacancy.get('link')
        else:
            raise TypeError('Site must be str: hh or superjob')

    def __repr__(self):
        return f'{self}{self._job_title}{self._url}'

    def __str__(self):
        return f'{self._job_title}'

    def __eq__(self, other):  # EQUAL|NOT EQUAL automatically work
        """Returning is vacancies urls are the same"""
        if isinstance(other, self.__class__):
            return self._url == other._url
        raise TypeError(f'Equal (== | !=) can be use only with exemplar class -> {self.__class__}')

    def __gt__(self, other):  # GREATER THAN|LESS THAN automatically work
        """Returning is vacation salary_from is GREATER THAN other vacation salary_from"""
        if isinstance(other, self.__class__):
            try:
                return int(self._salary_to) > int(other._salary_to)
            except TypeError:
                raise TypeError('There is no information about the salaries')
        raise TypeError(f'Greater than (> | <) can be use only with exemplar class -> {self.__class__}')

    @property
    def requirement(self):
        """Returning requirements for this job"""
        return self._requirement
