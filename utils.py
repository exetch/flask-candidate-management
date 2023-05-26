import json
import re


def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_all():
    candidates = load_candidates()
    return candidates


def get_all_skills():
    all_skills = set()
    candidates = load_candidates()
    for candidate in candidates:
        candidate_skills = candidate.get('skills', '').split(', ')
        all_skills.update(candidate_skills)
    return sorted(all_skills)


def get_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return None


def get_by_skill(skill_name):
    candidates = load_candidates()
    filtered_candidates = [candidate for candidate in candidates if
                           skill_name.lower() in candidate['skills'].lower().split(', ')]
    return filtered_candidates


import json


def update_candidate(pk, data):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            # Обновление данных кандидата
            candidate['name'] = data['name']
            candidate['position'] = data['position']
            candidate['skills'] = data['skills']
            candidate['age'] = int(data['age'])
            break

    with open('candidates.json', 'w', encoding='utf-8') as file:
        json.dump(candidates, file, indent=2, ensure_ascii=False)


def save_candidate(candidate):
    data = load_candidates()
    data.append(candidate)
    with open('candidates.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def generate_pk():
    data = load_candidates()
    max_pk = max(data, key=lambda candidate: candidate['pk'])['pk']
    new_pk = max_pk + 1
    return new_pk


def search_candidates_by_criteria(query):
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)

    results = []
    for candidate in candidates:
        if query['name'] and not re.search(fr'\b{re.escape(query["name"])}\b', candidate['name'], flags=re.IGNORECASE):
            continue
        if query['position'] and not re.search(fr'\b{re.escape(query["position"])}\b', candidate['position'], flags=re.IGNORECASE):
            continue
        if query['age_min'] and candidate['age'] < int(query['age_min']):
            continue
        if query['age_max'] and candidate['age'] > int(query['age_max']):
            continue
        if query['gender'] and not re.search(fr'\b{re.escape(query["gender"])}\b', candidate['gender'], flags=re.IGNORECASE):
            continue
        if query['skills']:
            required_skills = re.split(r',\s*|\s+', query['skills'])
            candidate_skills = re.split(r',\s*|\s+', candidate['skills'])
            if not all(skill.lower() in candidate_skills for skill in required_skills):
                continue
        results.append(candidate)

    return results

