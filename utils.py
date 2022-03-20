import json
from flask import Flask

__candidates = []

def load_candidates(filename='candidates.json'):
    """
    Функция читает json с вопросами и возвращает словарь для игры
    :param filename: По умолчанию questions.json
    :return: Словарь
    """
    global __candidates
    file = open(filename, encoding='UTF-8')
    __candidates = json.load(file)
    file.close()
    return __candidates


def get_candidate_by_id():
    pass


def get_candidate_by_name():
    pass


def get_candidate_by_skill():
    pass


def main():
    load_candidates()

