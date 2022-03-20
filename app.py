from flask import Flask, request, render_template
from utils import load_candidates

candidates = load_candidates()

app = Flask(__name__)

@app.route('/')
def get_list():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate<x>')
def get_by_id(x):
    return render_template('card.html', candidates=candidates)


app.run(debug=True)

