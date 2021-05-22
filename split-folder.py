import os

print("""
Welcome!

This program will help you split big directories with many files (10.000+) into smaller \
    subfolders.
Since opening big folders can crash your computer, this program is meant to be run \
    in the parent directory the actual folder you want to clean up.

You will soon be asked:
1) Which folder do you want to split?
2) How many sub-folders would you like to split them into?
3) Y/N confirmation on weither to procede.
-------------------------------------------------------
""")
dirs = [f for f in os.listdir('.') if os.path.isdir(f)]

print(f'Found the following directories: ')
for d in dirs: print(d)

target_dir = input(f'Which directory would you like to split?\n')
print(f'Preparing to split {target_dir}...')

try:
    files = os.listdir(target_dir)
except FileNotFoundError as e:
    print(e)
    print('Either you typed something wrong or you entered a folder name with spaces.')
    print('This program is unable to handle folder names with spaces, please rename \
        folder to something without spaces')
    raise SystemExit('Exiting program...')

num_files = len(files)
files_per_folder = int(input(f'{target_dir} contains {num_files} files, how many \
    files per folder?'))

num_folders = int(num_files / files_per_folder)

print(f'This will create {num_folders} folders')

if not 'Y' == input('Continue? (Y/N)').strip().upper():
    raise SystemExit('Exiting program...')

def create_folders(num):
    # Creates the folders the files will be put in
    sub_folders = []
    for i in range(1, num+1):
        os.mkdir(str(i))
        sub_folders.append(str(i))
    return sub_folders

def move_file(fname, folder):
    # Moves the file into the folder
    print(f'Moving {fname} into {folder}')
    os.rename(fname,os.path.join(folder,fname))

os.chdir(target_dir)

create_folders(num_folders)

count_current_folder = 0
total_count = 0
current_folder = 1

for f in files:
    folder_name = str(current_folder)
    move_file(f,folder_name)
    count_current_folder += 1
    if count_current_folder == files_per_folder:
        current_folder += 1
        count_current_folder = 0

print(f'Finished moving {total_count} files.')

    








