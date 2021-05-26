import os

# modes
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# read a file
f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "r")

# only parts of the file
print(f.read(5))

# read only one line
print(f.readline())
print(f.readline())  # read another line

# loop through file
for x in f:
    print(x)

# close a file
# Note: You should always close your files, in some cases, due to buffering,
# changes made to a file may not show until you close the file.
f.close()

# write to file
f = open("demofile2.txt", "a")  # append
f.write("Now the file has more content!\n")
f.close()

f = open("demofile2.txt", "r")
print(f.read())

# overwrite
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("demofile3.txt", "r")
print(f.read())

# remove a file

fileName = "demofile4.txt"

f = open(fileName, "w")
f.write("Woops! I have deleted the content!")
f.close()

if os.path.exists(fileName):
    os.remove(fileName)
else:
    error = "The file {} does not exist"
    print(error.format(fileName))

# remove a folder:
# os.rmdir("myfolder")
# Note: You can only remove empty folders.
