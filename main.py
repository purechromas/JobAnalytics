from hh import HH
from superjobs import SuperJobs
from vacancy import Vacancy
from saver import Saver
from utils import question

hh = HH()
super_job = SuperJobs()
saver = Saver()

site: int = question("Какой сервис вы предпочитаете для поиска работы?\n1.HH\n2.Superjob\n", options=[1, 2])
key_word: str = question("Напишите ключевое слово по поиску вакансии.\n")
salary: str = question("Выберите заплату от:\n")

if site == 1:  # Request is going on HH
    vacancies = hh.get_request(key_word=key_word, salary=int(salary), page=0)
    hh.print_vacancies_found()
    sorted_vacancies = hh.sort_vacancies(vacancies)
    hh.print_beautiful(sorted_vacancies)
else:  # Request is going on Super_jobs
    vacancies = super_job.get_request(key_word=key_word, salary=int(salary), page=0)
    super_job.print_vacancies_found()
    sorted_vacancies = super_job.sort_vacancies(vacancies)
    super_job.print_beautiful(sorted_vacancies)

page = 1

while True:
    answer = question("Хатите ли проити на следвашую страницу?\n1.Да\n2.Нет\n", options=[1, 2])
    if answer == 2:
        break
    else:
        if site == 1:
            vacancies = hh.get_request(key_word=key_word, salary=int(salary), page=page)
            sorted_vacancies = hh.sort_vacancies(vacancies)
            hh.print_beautiful(sorted_vacancies)
            page += 1
        else:
            vacancies = super_job.get_request(key_word=key_word, salary=int(salary), page=page)
            sorted_vacancies = super_job.sort_vacancies(vacancies)
            super_job.print_beautiful(sorted_vacancies)
            page += 1

like: int = question("Есть ли вакансия, которая вам понравилась?\n1.Да\n2.Нет\n", options=[1, 2])

if like == 1:
    vacancy_id: str = question("Напите ID вакансия:\n")
    if site == 1:  # Making exemplar Vacancy class with vacancy ID
        vacancy_hh = hh.get_vacancy(vacancy_id)
        liked_vacancy = Vacancy(vacancy_hh)
        save: int = question("Хотите сохранить ето ваканция в файл?\n1.Да\n2.Нет\n", options=[1, 2])
        if save == 1:
            type_file: int = question("В каком формате вы хотите, чтобы мы сохранили файл?\n1.JSON\n2.CSV\n", options=[1, 2])
            if type_file == 1:  # Saving the vacancy in file
                saver.save_json(vacancy_hh)
            else:
                saver.save_csv(vacancy_hh)
    else:
        vacancy_sj = super_job.get_vacancy(vacancy_id)
        liked_vacancy = Vacancy(vacancy_sj)
        save: int = question("Хотите сохранить ето ваканция в файл?\n1.Да\n2.Нет\n", [1, 2])
        if save == 1:
            type_file: int = question("В каком формате вы хотите, чтобы мы сохранили файл?\n1.JSON\n2.CSV\n", options=[1, 2])
            if type_file == 1:  # Saving the vacancy in file
                saver.save_json(vacancy_sj)
            else:
                saver.save_csv(vacancy_sj)
