from flask import Flask, request, render_template
from utils import load_candidates, get_candidate_by_id

candidates = load_candidates()

app = Flask(__name__)

@app.route('/')
def get_list():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate<id>')
def get_by_id(id):
    get_candidate_by_id(id, candidates)
    return render_template('card.html', candidates=candidates)


app.run(debug=True)

