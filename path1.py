from pathlib import Path

directory_path = Path('my_test_directory')
print(dir(directory_path))

# check if the directory on tht current diretory exitst

if not directory_path.exists():
    #Create the directory 
    directory_path.mkdir()
    print("Directory is created")
else:
    print(f"{directory_path} alread exists")

# creating path to file
file_path = directory_path / 'src' / 'my_file.txt'

# Reading a file from the python 

with open('test.txt','w') as test_file:
    test_file.write("First line in the file")

with open('test.txt','a') as test_file:
    test_file.write("Second line in the new file \n")
