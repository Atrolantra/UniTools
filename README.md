# UniTools
Repo of scripts, hacks and tools to make various aspects of university easier, faster, and simpler.

Needs Python 2.7.11 but you can probably get away with less.

## Folder.py
### About
A script to automatically create a folder for each week of semester given a folder for that semester that contains a folder for each subject being taken.

This is what your directory should look like before running the script.
```
├── 2016 Semester 1
|	├── Algorithms
|	├── Software
|	├── Contracts
|	├── Property law
```

After running the script on the directory this is what it becomes. One folder is made for each week in the semester.
```
├── 2016 Semester 1
|	├── Algorithms
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
|	├── Software
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
|	├── Contracts
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
|	├── Property law
|	|	├── Week 1
|	|	├── Week 2
|	|	├── Week 3
|	|	├── ...
```

### Usage
Set the folder_directory variable to whatever the directory of your semester top level folder is. 
For example, `C:\Users\Eric\Google Drive\2016 Sem 1`

Set the semester_weeks variable to however many weeks there are in the semester. 
For example, `14`