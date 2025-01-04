#Exercise 1:Write a Python program to read a file and display its contents
file=open("File_1.txt",'r')
print(file.read())
# #Exercise 2:Write a Python program to copy the contents of one file to another file
source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")
try:
    with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
        dest.write(src.read())
    print(f"Contents copied from {source_file} to {destination_file}")
except FileNotFoundError:
    print("The source file does not exist.")
#Exercise 3:Write a Python program to read the content of a file and count the total number of words in that file.
filename = input("Enter the filename to read: ")
try:
    with open(filename, 'r') as file:
        contents = file.read()
        words = contents.split()
        print(f"Total number of words: {len(words)}")
except FileNotFoundError:
    print("The file does not exist.")
# #Exercise 4:Write a Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any exceptions that might occur
user_input = input("Enter a number: ")
try:
    number = int(user_input)
    print(f"You entered the number: {number}")
except ValueError:
    print("Invalid input. Please enter an integer.")
#Exercise 5:Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative.
try:
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    for num in numbers:
        if num < 0:
            raise ValueError("Negative integers are not allowed.")
    print("All integers are non-negative.")
except ValueError as e:
    print(e)
#Exercise 6:Write a Python program that prompts the user to input a list of integers and computes the average of those integers. Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message indicating that the program has finished running.
try:
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    average = sum(numbers) / len(numbers)
    print(f"The average is: {average}")
except ZeroDivisionError:
    print("The list is empty. Cannot compute average.")
except ValueError:
    print("Invalid input. Please enter integers only.")
finally:
    print("Program has finished running.")
#Exercise 7 :Write a Python program that prompts the user to input a filename and writes a string to that file. Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred.
filename = input("Enter the filename to write: ")
string_to_write = input("Enter the string to write to the file: ")
try:
    with open(filename, 'w') as file:
        file.write(string_to_write)
    print("String written to the file successfully!")
    print("Welcome!")
except Exception as e:
    print(f"An error occurred: {e}")


