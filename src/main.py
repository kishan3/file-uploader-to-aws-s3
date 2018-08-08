from constants import URL_TO_CALL, SHEET_NAME
from file_operations import write_list_of_json_data_to_file
from get_file_contents import construct_list_of_json_dict_from_dataframe, get_file_contents
from upload_file_to_aws_s3_bucket import upload_file_to_aws_s3_bucket


def main():
    data = get_file_contents(url=URL_TO_CALL, sheet_name=SHEET_NAME)
    list_of_json = construct_list_of_json_dict_from_dataframe(dataframe=data)
    write_list_of_json_data_to_file(list_of_json=list_of_json)
    upload_file_to_aws_s3_bucket()
    print("Success!")


if __name__ == '__main__':
    main()
