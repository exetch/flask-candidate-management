from flask import Flask, render_template, request, redirect, url_for
from utils import load_candidates, get_by_pk, get_by_skill, update_candidate, \
    get_all, get_all_skills, save_candidate, \
    generate_pk, search_candidates_by_criteria

app = Flask(__name__)



@app.route('/')
def index():
    candidates = load_candidates()
    return render_template('index.html', candidates=candidates)



@app.route('/candidate/<int:pk>')
def candidate_details(pk):
    candidate = get_by_pk(pk)
    return render_template('candidate.html', candidate=candidate)


@app.route('/skills/<skill>')
def skill_search(skill):
    candidates = get_by_skill(skill)
    return render_template('skill_search.html', candidates=candidates)


@app.route('/candidate/edit/<int:pk>', methods=['GET', 'POST'])
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
    return render_template('candidates.html', candidates=candidates)


@app.route('/skills')
def skill_list():
    skills = get_all_skills()
    return render_template('skills.html', skills=skills)


@app.route('/add', methods=['GET', 'POST'])
def add_candidate():
    if request.method == 'POST':
        candidate = {
            'pk': generate_pk(),
            'name': request.form['name'],
            'position': request.form['position'],
            'skills': request.form['skills'],
            'picture': 'https://picsum.photos/200',
            'gender': request.form['gender'],
            'age': int(request.form['age'])
        }
        save_candidate(candidate)
        return redirect(url_for('index'))
    return render_template('add_candidate.html')


@app.route('/search_candidates', methods=['GET', 'POST'])
def search_candidates():
    if request.method == 'POST':
        query = {
            'name': request.form.get('name'),
            'position': request.form.get('position'),
            'age_min': request.form.get('age_min'),
            'age_max': request.form.get('age_max'),
            'gender': request.form.get('gender'),
            'skills': request.form.get('skills')
        }
        results = search_candidates_by_criteria(query)
        return render_template('search.html', results=results)
    return render_template('search.html')





if __name__ == '__main__':
    app.run()
