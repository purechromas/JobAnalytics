from source.hh import HH
from source.super_job import SuperJob
from source.vacancy import Vacancy
from source.job_saver import JobSaver
from utils import normal_question, optional_question

hh = HH()
sj = SuperJob()
js = JobSaver()


def main():
    site: int = optional_question('Какой сервис вы предпочитаете для поиска работы?\n1.HH\n2.Superjob\n', options=[1, 2])
    key_word: str = normal_question('Напишите ключевое слово по поиску вакансии.\n')
    salary: int = int(normal_question('Выберите заплату от:\n'))
    number_vacancies: int = optional_question('Сколько вакансии вы хотите, чтобы мы показали?\n5\n20\n', options=[5, 20])
    sort_by: int = optional_question('Выберите сортировка по:\n1.По возрастанию зарплаты\n2.По убыванию зарплат\n', options=[1, 2])

    if site == 1:
        vacancies = hh.get_requests(key_word=key_word, salary=salary, number_vacancies=number_vacancies)
        hh.sort_vacancies(vacancies=vacancies, from_low_to_high=sort_by)
    else:
        vacancies = sj.get_requests(key_word=key_word, salary=salary, number_vacancies=number_vacancies)
        sj.sort_vacancies(vacancies=vacancies, from_low_to_high=sort_by)

    like: int = optional_question('Есть ли вакансия, которая вам понравилась?\n1.Да\n2.Нет\n', [1, 2])

    if site == 1:
        if like == 1:
            vacancy_id: str = normal_question('Напите ID вакансия:\n')
            vacancy = hh.get_vacancy(vacancy_id=vacancy_id)
            exemplar = Vacancy(vacancy, 'hh')
            print(repr(exemplar))
            exemplar.requirement()
            save: int = optional_question('Хотите сохранить ето ваканция в файл?\n1.Да\n2.Нет\n', [1, 2])
            if save == 1:
                type_file: int = optional_question(
                    'В каком формате вы хотите, чтобы мы сохранили файл?\n1.JSON\n2.CSV\n', [1, 2])
                if type_file == 1:
                    js.save_json(vacancy)
                else:
                    js.save_csv(vacancy)
    else:
        if like == 1:
            vacancy_id: str = normal_question('Напите ID вакансия:\n')
            vacancy = sj.get_vacancy(vacancy_id=vacancy_id)
            exemplar = Vacancy(vacancy, 'superjob')
            print(exemplar)
            save: int = optional_question('Хотите сохранить ето ваканция в файл?\n1.Да\n2.Нет\n', [1, 2])
            if save == 1:
                type_file: int = optional_question(
                    'В каком формате вы хотите, чтобы мы сохранили файл?\n1.JSON\n2.CSV\n', [1, 2])
                if type_file == 1:
                    js.save_json(vacancy)
                else:
                    js.save_csv(vacancy)


if __name__ == '__main__':
    main()
