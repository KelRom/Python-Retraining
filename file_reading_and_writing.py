# open a file for writing and create it if it doesn't exist
# sample_file = open("textfile.txt", "w+")
# writes to the file
# sample_file.write("This is some sample text in our sample file\n")
# close file when we are done using it
# sample_file.close()

# COMMENTED BECAUSE I DON'T WANT TO KEEP ADDING TO THE END OF THE FILE
# This will open the file and add content to the end of the file
# sample_file = open("textfile.txt", "a+")
# sample_file.write("This is some more sample text in our sample file\n")
# sample_file.write("This is even more sample text in our sample file\n")
# sample_file.close()

# this is working with reading files
sample_file = open("textfile.txt")
# check if the file is open for reading mode
if sample_file.mode == 'r':
    # contents = sample_file.read()
    # print(contents)
    file_lines = sample_file.readlines()
    for index, line in enumerate(file_lines):
        print(f"line number: {index + 1}, line contents: {line}")

sample_file.close()
