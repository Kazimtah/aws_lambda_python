from zipfile import ZipFile
from pathlib import Path


my_directory = Path('my-files')
if not my_directory.exists(): 
    my_directory.mkdir()


with open('my-files/first.txt', 'w') as file:
    file.write("this the first file\n")

with open('my-files/second.txt','w') as file:
    file.write("The second file \n")

with ZipFile('myfile.zip', mode = 'w') as zip_file:
    for file in my_directory.iterdir():
        print(file)
        zip_file.write(file)
