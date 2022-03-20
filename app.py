from flask import Flask, request, render_template
from utils import load_candidates, get_candidate_by_id, get_candidate_by_name

candidates = load_candidates()
app = Flask(__name__)

@app.route('/')
def get_list():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def get_by_id(id):
    candidates_dict = get_candidate_by_id(id, candidates)
    return render_template('card.html', candidate=candidates_dict)

@app.route('/search/<candidate_name>')
def get_by_name(candidate_name):
    find_candidates = get_candidate_by_name(candidate_name, candidates)
    return render_template('search.html', candidates=find_candidates, candidates_len = len(find_candidates))


app.run(debug=True)

