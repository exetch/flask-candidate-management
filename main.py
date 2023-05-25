from flask import Flask, render_template
from utils import load_candidates, get_by_pk, get_by_skill

app = Flask(__name__)


# Главная страница
@app.route('/')
def home():
    candidates = load_candidates()
    return render_template('index.html', candidates=candidates)


# Страница кандидата по pk
@app.route('/candidate/<int:pk>')
def candidate_details(pk):
    candidate = get_by_pk(pk)
    if candidate:
        return render_template('candidate.html', candidate=candidate)
    else:
        return "Кандидат не найден."


# Страница поиска по навыку
@app.route('/skills/<string:skill>')
def skill_search(skill):
    candidates = get_by_skill(skill)
    return render_template('skill_search.html', candidates=candidates)


if __name__ == '__main__':
    app.run()
