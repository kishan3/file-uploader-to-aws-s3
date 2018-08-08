import pandas as pd

from file_operations import write_list_of_json_data_to_file


def get_file_contents(url, sheet_name):
    data = pd.read_excel(url, sheet_name=sheet_name)
    return data


def construct_list_of_json_dict_from_dataframe(dataframe):
    list_of_json = []
    for index, row in dataframe.iterrows():
        json_dict = {}
        for coulmn in dataframe.columns:
            json_dict[coulmn] = row[coulmn]
        list_of_json.append(json_dict)
    return list_of_json


def upload_json_file_to_aws_s3_bucket():
    # upload file
    return


if __name__ == '__main__':
    url = "https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls"
    data = get_file_contents(url=url, sheet_name="MICs List by CC")
    list_of_json = construct_list_of_json_dict_from_dataframe(dataframe=data)
    import ipdb
    ipdb.set_trace()
    write_list_of_json_data_to_file(list_of_json=list_of_json)
    upload_json_file_to_aws_s3_bucket()
    print("Success!")
