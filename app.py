from flask import Flask, request, render_template
from utils import __candidates, main


main()
app = Flask(__name__)

@app.route('/')
def get_list():
    return render_template('list.html', candidates=__candidates)

app.run(debug=True)

