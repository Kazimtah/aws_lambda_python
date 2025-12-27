import os 

directory_path = 'my_test_directory'

if  not os.path.exists(directory_path):
    # create a directory 
    os.mkdir(directory_path)
else:
    print(f"The directory by the name of {directory_path} exists")
# creating path to the file
file_path = os.path.join(directory_path, 'my_file.txt')
 
print('File Path:', file_path )

#Getting parent directory
parent_directory = os.path.dirname(file_path)
print('Parent Directory:', parent_directory)

# Checking if the file is file or a directory 

is_file = os.path.isfile(file_path)
print("File Paht is :", is_file)
is_directory = os.path.isdir(directory_path)
print("Is directory:", is_directory)


# listing file directory 
dir_files = os.listdir(directory_path)
print(dir_files)
print(f" file in the directory is {directory_path}")
for file in dir_files:
    print(file)

#removing the directory
if os.path.exists(directory_path):
    os.rmdir(directory_path)
    print("the directory is removed")

