import pandas as pd

from constants import URL_TO_CALL
from upload_file_to_aws_s3_bucket import upload_file_to_aws_s3_bucket
from file_operations import write_list_of_json_data_to_file


def get_file_contents(url, sheet_name):
    data = pd.read_excel(url, sheet_name=sheet_name)
    return data


def construct_list_of_json_dict_from_dataframe(dataframe):
    json_list = []
    for index, row in dataframe.iterrows():
        json_dict = {}
        for coulmn in dataframe.columns:
            json_dict[coulmn] = row[coulmn]
        json_list.append(json_dict)
    return json_list


if __name__ == '__main__':
    data = get_file_contents(url=URL_TO_CALL, sheet_name="MICs List by CC")
    list_of_json = construct_list_of_json_dict_from_dataframe(dataframe=data)
    write_list_of_json_data_to_file(list_of_json=list_of_json)
    upload_file_to_aws_s3_bucket()
    print("Success!")
