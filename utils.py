import json

def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_all():
    candidates = load_candidates()
    names = [candidate['name'] for candidate in candidates]
    return names

def get_by_pk(pk):
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return None

def get_by_skill(skill_name):
    candidates = load_candidates()
    filtered_candidates = [candidate for candidate in candidates if skill_name.lower() in candidate['skills'].lower()]
    return filtered_candidates
