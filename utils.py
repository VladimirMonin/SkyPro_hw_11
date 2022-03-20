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


def get_candidate_by_id():
    pass


def get_candidate_by_name():
    pass


def get_candidate_by_skill():
    pass


