import os
import json
from json import JSONDecodeError


class FileManager:
    @classmethod
    def save_scene_number(cls, nr):
        with open('data.json', 'w') as f:
            f.write(json.dumps({'scene_number': nr}))

    @classmethod
    def load_scene_number(cls):
        try:
            with open('data.json', 'r') as f:
                val = f.read()
                val = json.loads(val)['scene_number']
        except FileNotFoundError:
            val = 1
        return val

    @classmethod
    def get_scene_values(cls, nr):
        try:
            with open(f'scene{nr}.json', 'r') as f:
                return json.loads(f.read())
        except FileNotFoundError:
            print(f'scene{nr}.json: not available!')

    @classmethod
    def is_scene_available(cls, current_scene_nr):
        try:
            open(f'scene{current_scene_nr}.json')
            return True
        except FileNotFoundError:
            return False

    @classmethod
    def default_scene_dump(cls, values):
        with open(f'scene{values["nr"]}.json', 'w') as f:
            f.write(json.dumps(values))
