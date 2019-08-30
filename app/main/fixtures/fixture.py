import json
from pprint import pprint


def get_json():
    with open('app/main/fixtures/fixtures.json') as f:
        data = json.load(f)
        pprint(data)
