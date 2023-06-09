def normal_question(question: str) -> str:
    return input(question)


def optional_question(question: str, options: list) -> int:
    correct_answer = False
    while not correct_answer:
        answer = input(question)
        try:
            if int(answer) in options:
                correct_answer = True
                return int(answer)
        except ValueError:
            print(f'Ожидаетса целое число {options}')
