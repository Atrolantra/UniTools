# UniTools
Repo of scripts, hacks and tools to make various aspects of university easier, faster, and simpler.

Needs Python 2.7.11 but you can probably get away with less.

## folder.py
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

## subject_scraper.py
### About
A script to automatically fetch the synopsis of every unit you have taken. This is useful for students who want to keep a solid record of what the general content and rationale is for the subjects they've done. Having a record like this is also invaluable if a student should ever want to change to a different teaching institution and want to claim credit for past units completed. It is prudent to continuously compile a record like this as you go since sometimes subjects/outlines can be removed from the institution's website for some reason. This script makes this process fast and simple.


### Usage
In the same directory as the script, create a text file named 'ulist.txt'.
In this list enter the unit IDs of the units you want to get a synopsis for, one per line.
For example:
```
INB270
INB104
IFB101
IFB102
```

Then simply run the script and a list of subjects and synopsis' will be created in a text file named 'synopsis list.txt' in the same directory.