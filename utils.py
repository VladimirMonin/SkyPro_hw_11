import json
from flask import Flask



def load_candidates(filename='candidates.json'):
    """
    Функция читает json с вопросами и возвращает словарь для игры
    :param filename: По умолчанию questions.json
    :return: Словарь
    """
    file = open(filename, encoding='UTF-8')
    candidates = json.load(file)
    file.close()
    return candidates


def get_candidate_by_id(user_id, candidates_list):
    """
    Функция принемает ID пользователя и список юзеров и формирует строку с данным пользователем. Возвращает инфу
    о пользователе или сообщение что кандидат не найден
    :param user_id:
    :return:
    """
    candidate_string = ''
    for candidate in candidates_list:
        if candidate["id"] == int(user_id):
            candidate_string += f'<h1>Имя кандидата - {candidate["name"]}</h1>' \
                                f'<p>Позиция кандидата - {candidate["position"]}</p>\n\n' \
                                f'<img src = "{candidate["picture"]}">\n\n' \
                                f'<p>Навыки: {candidate["skills"]}</p>'

            break
    else:
        candidate_string += f'<h1>Кандидат не найден</h1>'
    return candidate_string

def get_candidate_by_name():
    pass


def get_candidate_by_skill():
    pass


