from source.hh import HH


class TestHH:
    hh = HH()

    def test_sort_vacancies(self, hh_vacancies):
        assert self.hh.sort_vacancies(hh_vacancies)[0]['salary_from'] == 30000
