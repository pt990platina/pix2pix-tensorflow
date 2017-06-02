import os, zipfile

source_dir, output_filename = 'dataset_test', 'dataset_test.zip'

zipf = zipfile.ZipFile(output_filename, 'w')
pre_len = len(os.path.dirname(source_dir))
for parent, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        pathfile = os.path.join(parent, filename)
        arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
        zipf.write(pathfile, arcname)
zipf.close()
 