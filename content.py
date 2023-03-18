import os

# get the path of the current working folder
current_dir = os.getcwd()

# get a list of all files in the current folder
files = os.listdir(current_dir)

# create a new text file to write the list of files
with open("file_list.txt", "w") as file:
    # write each file name to the text file
    for f in files:
        file.write(f + "\n")