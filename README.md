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

# Change #3
Now there are two files which are for the carrigan and octoprime tires. There is also
the "tires.py" file which serves as the parent class of the previous two tires files.
Furthermore, adjustments were made within the "car_factory.py" file to also use the new
tires files. The "test_car.py" files still create the cars to test if there are any
errors with this new addition of tires. In addition, there is a new unit case which test
these two new tires individually instead of creating 20 new test cases in total when
combining with the previous test cases.