# Starter Repo
This repo has everything you need to get started on the program, good luck!


# Change #1
The python files that were once in the "Model" folder has been relocated to a
new folder named "Deprecated". This is because of the possibility that those
files may come into use in the future.

# Change #2
When executing the "test_car.py" file, you must be in the parent directory and
execute the command "python -m test.test_car" in the command line.
This is because the "test_car.py" file is accessing file from the parent (or root)
directory, but "test_car.py" is in the child directory (in this case, the folder
"test"). But the command shown before will allow the "test_car.py" file to directly
access the root directory to then access the necessary file.

Also, the "Deprecated" folder is removed, as it should no longer be needed