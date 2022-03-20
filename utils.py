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
    for candidate in candidates_list:
        if candidate["id"] == int(user_id):
            candidate_dict = {
                'name': candidate["name"],
                'position': candidate["position"],
                'picture': candidate["picture"],
                'skills': candidate["skills"],
            }
    return candidate_dict

def get_candidate_by_name(user_name, candidates_list):
    find_list = []
    for candidate in candidates_list:
        if user_name.lower() in candidate['name'].lower():
            find_list.append(candidate)
    return find_list


def get_candidate_by_skill(skill, candidates_list):
    find_list = []
    for candidate in candidates_list:
        skill_list = candidate['skills'].lower().split(', ')
        if skill.lower() in skill_list:
            find_list.append(candidate)
    return find_list


