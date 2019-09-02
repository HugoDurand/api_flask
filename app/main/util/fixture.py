import json, os
import datetime
from app.main import db
from app.main.model.category import Category
from app.main.model.comment import Comment
from app.main.model.video import Video


def get_json():
	path_to_json = 'app/main/fixtures/'
	json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
	json_files.sort()
	for j in json_files:
		with open('app/main/fixtures/'+j) as file:
			sort_data(json.load(file))


def sort_data(data):
	# TODO: Avois nested loops
	for index, d in enumerate(data['data']):
		model = eval(data['model'])()
		for key, value in data['data'][index].items():
			setattr(model, key, value)
			print(getattr(model, key))
		db.session.add(model)
		db.session.commit()