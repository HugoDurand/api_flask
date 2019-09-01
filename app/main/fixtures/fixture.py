import json, os
from app.main import db


def get_json():
    path_to_json = 'app/main/fixtures/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    for j in json_files:
        with open('app/main/fixtures/'+j) as file:
            data = json.load(file)
        return sort_data(data)


def sort_data(data):
    # TODO: Avois nested loops
    for index, d in enumerate(data['data']):
        for key, value in data['data'][index].items():
            model = data['model'](
                key=value,
            )
            db.session.add(model)
            db.session.commit()
