from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def get_list():
    candidates = ['Вася', 'Петя']
    return render_template('list.html', candidates=candidates)

app.run()

