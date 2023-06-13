def question(qn: str, options: list = None) -> str | int:
    """This function is helping to ask questions user when program starts"""
    if options:
        correct_answer = False
        while not correct_answer:
            answer = input(qn)
            try:
                if int(answer) in options:
                    correct_answer = True
                    return int(answer)
                raise ValueError
            except ValueError:
                print(f'Ожидаетса целое число {options}')
    else:
        return input(qn)
