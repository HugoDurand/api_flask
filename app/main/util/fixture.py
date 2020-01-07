import json, os

from ..service.category_service import new_category
from ..service.comment_service import new_comment
from ..service.video_service import new_video

from ..model.category import Category
from ..model.comment import Comment
from ..model.video import Video

model_create_functions = {
	'Category': new_category,
	'Comment': new_comment,
	'Video': new_video
}


def get_json():
	path_to_json = 'app/main/fixtures/'
	json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
	json_files.sort()
	for j in json_files:
		with open('app/main/fixtures/'+j) as file:
			sort_data(json.load(file))


def sort_data(data):
	for index, d in enumerate(data['data']):
		model = eval(data['model'])()
		function = globals()["new_"+str(type(model).__name__.lower())]
		function(d)
