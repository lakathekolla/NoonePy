'''
Title : Python File Handling
Author : R M Lakruwan @ Noone
Date : 13 July 2019

Compatibality : Python 3
version : 1.0

'''
import os      # Operating system dependent functionality : For get file path, delete dir etc

# This is so simple using python 3
# (and for below that you may need to add some changes.)

# CREATE FILE
# METHOD 1  
def create_text_file_method_1() :
    # Create myfile1.txt on current directroy
    # 'x' - create will create a file, returns an error if the file exist
    try :
        file_name = "myfile1.txt"
        new_file = open(file_name , "x")
        print("New File Created : ", file_name )
        return new_file
    except :
        error_state = "FileExistsError: '" + file_name + "'"
        print(error_state)

# METHOD 2  
def create_text_file_method_2() :
    # Create myfile2.txt on current directroy
    # 'a' - append will create a file if the specified file does not exist
    file_name = "myfile2.txt"
    new_file = open(file_name , "a")
    print("New File Created : ", file_name )

    return new_file

# METHOD 3 
def create_text_file_method_3() :
    # Create myfile3.txt on current directroy
    # 'w' - write will create a file if the specified file does not exist
    file_name = "myfile3.txt"
    new_file = open(file_name , "w")
    print("New File Created : ", file_name )

    return new_file


# DELETE FILE
def delete_text_file(file_name) :
    # Delete 'file_name' on current directroy
    # 'w' - write will create a file if the specified file does not exist
    if os.path.exists(file_name):
        os.remove(file_name)
        print("Delete ", file_name , " Successfully... ")
    else:
        print("The file does not exist or File path des not exist")

# WRITE FILE
def add_text_as_newline(line , file_path) :
    # Open text file
    # 'a' - Append - will append to the end of the file
    
    text_file = open(file_path, "a")
    # If file has text lines , append the line as new line
    if(os.path.getsize(file_path) > 0) :
        text_file.write("\n" + line)
    # Else there are  no lines , append to fist line without new line 
    else:
         text_file.write(line)
    
    text_file.close()
    print("line : ", line)
    print( " Added Succesfully to " , file_path)

def add_text_as_overwrite(line , file_path) :
    # Open text file
    # 'w' - Write - will overwrite any existing content
    
    text_file = open(file_path, "w")
    # Dont care about exist text , add as whole new content
    text_file.write(line)
    
    text_file.close()
    print("line : ", line)
    print( " Overwrite Content Succesfully in " , file_path)

# READ FILE
# Read whole text
def text_read(file_path) :
    file = open(file_path, "r")
    # Read all from return array, this include newline char too
    my_text = file.readlines()
    file.close()

    return(my_text)

# Read a line
def text_line_read(file_path, line_number) :
    file = open(file_path, "r")
    # Read line from return array 
    myline = file.readlines()[ line_number]
    file.close()

    return(myline)

# Read char
def text_char_read(file_path, char_number) :
    file = open(file_path, "r")
    # Read line from return array 
    mychr = file.read(char_number)
    file.close()

    return(mychr)


'''
Demo Run :
Use as your will :) Good Luck
'''

# Create File
my_file_m1 = create_text_file_method_1()
my_file_m2 = create_text_file_method_2()
my_file_m3 = create_text_file_method_3()

# Delete File
#delete_text_file("myfile3.txt")

# Add text to file without overwrite
add_text_as_newline("Hi Python : First Line " , "myfile1.txt")
add_text_as_newline("Hi Python  : Second Line " , "myfile1.txt")

# Add text to file with overwrite
add_text_as_overwrite("Hi Python : First Line " , "myfile2.txt")
add_text_as_overwrite("Hi Python  : Overwritten Line " , "myfile2.txt")

# Read text File as lines
line = text_line_read("myfile1.txt", 0)
print(line)

# Read text File as file
txtfile = text_read("myfile1.txt")
print("Whole Content list : ",txtfile)
# You can filter text using .strip() :START END CHR Only or .replace("\n", "") :ANYWHERE in String
print("Text : ",txtfile[0])
print("Text : ",txtfile[1])
print("Text Filtered : " , txtfile[0].strip("\n"))
print("Text Filtered : " , txtfile[1].strip("\n"))

# Read text File as char
mychar = text_char_read("myfile1.txt", 1)
print("Your Char is : ",mychar)


