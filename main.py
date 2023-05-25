from flask import Flask, render_template, request, redirect, url_for
from utils import load_candidates, get_by_pk, get_by_skill, update_candidate, get_all, get_all_skills


app = Flask(__name__)


# Главная страница
@app.route('/')
def home():
    candidates = load_candidates()
    return render_template('index.html', candidates=candidates)


# Страница кандидата по pk
@app.route('/candidates/<pk>')
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
        # Получите данные из формы редактирования и обновите информацию о кандидате
        # с помощью функции update_candidate(pk, data) из utils.py
        data = request.form  # Получение данных из формы редактирования

        # Обновление информации о кандидате с помощью функции update_candidate(pk, data)
        update_candidate(pk, data)
        # Перенаправьте пользователя на страницу с подробной информацией о кандидате
        return redirect(url_for('candidate_details', pk=pk))

    else:
        # Получите данные кандидата по pk с помощью функции get_by_pk(pk) из utils.py
        candidate = get_by_pk(pk)
        # Отобразите форму редактирования с текущими данными кандидата
        return render_template('edit_candidate.html', candidate=candidate)

@app.route('/candidates')
def candidates():
    candidates = get_all()  # Получение списка всех кандидатов
    return render_template('candidate_list.html', candidates=candidates)



@app.route('/skills')
def skills():
    all_skills = get_all_skills()  # Получение списка всех навыков
    return render_template('skill_list.html', skills=all_skills)



if __name__ == '__main__':
    app.run()
