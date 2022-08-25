#Akinola Daramola Jr
#Programming Exercise 6.4
#Due Date: 07/24/2022


"""
Item Counter
Assume a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk.
Write a program that displays the number of names that are stored in the file.
(Hint: Open the file and read every string stored in it. Use a variable to keep a count of the number of items that are read from the file.)

"""



#Define maiin function
def main():
    #Creating object of file names.txt
    names_file = open('names.txt','r')
    
    #names = names_file.readline()

    #Initializing 'number_of_names' variable with value of 0
    number_of_names = 0

    #Constructing a for loop to iterate through all lines in 'names_file'
    for names in names_file:
        
        #For every line iterated in 'names_file', 'number_of_names' variable will increment 1 unit until iteration ends
        number_of_names +=1
        
    #Display total number of names in file    
    print(f"Number of names: {number_of_names:}")

    #Closing object 
    names_file.close()
    
#Call mainline function
main()
