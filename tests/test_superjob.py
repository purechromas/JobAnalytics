from source.superjobs import SuperJobs


class TestSuperJob:
    super_jobs = SuperJobs()

    def test_sort_vacancies(self, super_jobs_vacancies):
        assert self.super_jobs.sort_vacancies(super_jobs_vacancies)[6]['salary_from'] == 101030
