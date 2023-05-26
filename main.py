from flask import Flask, render_template, request, redirect, url_for
from utils import load_candidates, get_by_pk, get_by_skill, update_candidate, get_all, get_all_skills

app = Flask(__name__)
print(get_all_skills())
print(get_all())


# Главная страница
@app.route('/')
def home():
    candidates = load_candidates()
    return render_template('index.html', candidates=candidates)


# Страница кандидата по pk
@app.route('/candidate/<pk>')
def candidate_details(pk):
    candidate = get_by_pk(pk)  # Получение данных кандидата по pk
    return render_template('candidate.html', candidate=candidate)


# Страница поиска по навыку
@app.route('/skills/<skill>')
def skill_search(skill):
    candidates = get_by_skill(skill)  # Получение списка кандидатов по навыку
    return render_template('skill_search.html', candidates=candidates)


@app.route('/candidates/edit/<int:pk>', methods=['GET', 'POST'])
def edit_candidate(pk):
    if request.method == 'POST':
        data = request.form
        update_candidate(pk, data)
        return redirect(url_for('candidate_details', pk=pk))

    else:
        candidate = get_by_pk(pk)
        return render_template('edit_candidate.html', candidate=candidate)


@app.route('/candidates')
def candidates():
    candidates = get_all()
    return render_template('candidate.html', candidates=candidates)


@app.route('/skills')
def skills():
    all_skills = get_all_skills()
    return render_template('skills.html', skills=all_skills)


if __name__ == '__main__':
    app.run()
