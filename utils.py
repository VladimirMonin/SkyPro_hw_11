import json
from flask import Flask

def load_candidates(filename='candidates.json'):
    """
    Функция читает json с вопросами и возвращает словарь для игры
    :param filename: По умолчанию questions.json
    :return: Словарь
    """
    file = open(filename, encoding='UTF-8')
    candidates_list = json.load(file)
    file.close()
    return candidates_list


def get_candidate_by_id():
    pass


def get_candidate_by_name():
    pass


def get_candidate_by_skill():
    pass


# ЗАГРУЗКА ВОПРОСОВ в список
candidates_list = load_candidates()

# ЗАПУСК ПРИЛОЖЕНИЯ ФЛАСК
app = Flask(__name__)

@app.route("/")
def page_index():
    all_candidates = candidates_list
    return f"<pre>{all_candidates}<pre>"

app.run()