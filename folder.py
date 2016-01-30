import os

# Directory path to wherever you have your folder for the semester.
# Eg 'C:\Users\Eric\Google Drive\2016 Sem 1'
folder_directory = r'path_here'
semester_weeks = 14

# Given a path to a folder, returns all folders within.
def get_immediate_subdirectories(directory):
    return [name for name in os.listdir(directory)
            if os.path.isdir(os.path.join(directory, name))]

# Create a subfolder for each week of the semester for each subject folder.
subdirs = get_immediate_subdirectories(folder_directory)
for subdirectory in range(0, len(subdirs) + 1):
    for week in range(1, semester_weeks):
        new_folder = 'Week ' + str(week)
        full_path = folder_directory + '\\' + subdirs[subdirectory] + '\\' + new_folder
        print full_path
        os.makedirs(full_path)

