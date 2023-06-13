from source.vacancy import Vacancy


class TestVacancy:
    def test_vacancy(self, vacancy1, vacancy2):
        vcy1 = Vacancy(vacancy1)
        vcy2 = Vacancy(vacancy2)

        assert (vcy1 == vcy2) is True
        assert (vcy1 > vcy1) is False
        assert str(vcy1) == 'Ведущий системный администратор'
        assert vcy2.url == 'https://www.superjob.ru/vakansii/veduschij-sistemnyj-administrator-46276186.html'
