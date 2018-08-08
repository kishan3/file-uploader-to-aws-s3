import json
import os


def get_file_path(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path = os.path.join(dir_path, file_name)
    return path


def write_list_of_json_data_to_file(list_of_json):
    path = get_file_path("mics_list_by_cc.json")
    with open(path, 'w') as fout:
        json.dump(list_of_json, fout)
