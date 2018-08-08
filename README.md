# Download-Store-Read-Upload file to AWS S3 bucket

Read xsl file and store it as json. After that we upload that file to AWS S3 bucket.
1. Download the xlsx from - https://www.iso20022.org/sites/default/files/ISO10383_MIC/ISO10383_MIC.xls
2. Store the xlsx
3. Read the tab titled "MICs List by CC"
4. Create a list of dict containing all rows (except row 1). The values in row 1 would be the keys for in each dict.
5. Store the list from step 4) as a .json file in an AWS S3 bucket

## setup

  Install virtualenvwrapper. (http://virtualenvwrapper.readthedocs.io/en/latest/)

  Make a virtual environment using:

      mkvirtualenv file_uploader -p /usr/bin/python3

  Install requirements:

      pip install -r requirements.txt

  Usage:

      python src/main.py

## python version
    Python 3.6.5
