from flask import Flask, render_template, request
from vsearch import search_for_letters


app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your result:'
    results = str(search_for_letters(phrase, letters))
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_title=title, the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the search_for_letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)