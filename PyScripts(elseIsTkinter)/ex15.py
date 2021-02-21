from sys import argv #gets argv feature(module) from system
script, filename = argv #argv unpacks variables typed before running the script

txt = open(filename) #stores opened file from argv to a variable

print(f"Here's your file {filename}: ") #prints the name of the file
print(txt.read()) #prints opened file as it reads it

print("Type the filename again:")
file_again = input("> ") #waits user input for the filename

txt_again = open(file_again) # same stuff as in line 4

print(txt_again.read()) #same stuff as in line 7
txt.close() #closes opened txt file
txt_again.close() #closes opened txt_again file 
