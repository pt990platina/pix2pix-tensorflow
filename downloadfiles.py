import os
file_list = os.listdir(r'.')
for file_name in file_list:
    if file_name == 'dataset':
        import shutil
        shutil.rmtree('dataset')


import requests
#url = 'https://www.dropbox.com/s/ejndvtrr8r2lz2d/dataset.zip?dl=1'
url = input('Please input the download link address')
r = requests.get(url)
with open("dataset.zip", "wb") as code:
     code.write(r.content)


import zipfile
import os

file_list = os.listdir(r'.')

for file_name in file_list:
    if os.path.splitext(file_name)[1] == '.zip':
        print('Successfully unzip', file_name)
        file_zip = zipfile.ZipFile(file_name, 'r')
        for file in file_zip.namelist():
            file_zip.extract(file, r'.')
        file_zip.close()
        os.remove(file_name)