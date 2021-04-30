"""
Replace the contents of this module docstring with your own details
Name:Vu Le Nguyen Phuong
Date started:23/04/2021
GitHub URL:
"""

''''Here are the global lists which will be used in the function, also the command to open the books.csv file. I 
import csv library just in case i have to use some of its function to interact with the csv file. one important list 
to notice is the FILE_LIST in which will store all valuable data from main_menu(), list_function, add_function() and 
mark_function() '''

REMAINDER = [1]
TOTAL_BOOK = [0]
book_list = open('books.csv', 'r')
FILE_LIST = book_list.readlines()

'''This is the main function of the program, here the main_menu function is triggered, lead the users to the main 
menu for interaction.  '''


def main():
    """..."""
    print("Reading Tracker 1.0 - by vu Le Nguyen Phuong")
    main_menu()


'''The main_menu function will display the options for users to choose and go directly to the three main functions, 
show lists (L), add a book(A), mark a book(M) and Quit(Q). After interacting with the programs, the Quit option 
will save all changes and then write to the books.csv file '''


def main_menu():
    print("Menu:")
    count_load = 0
    for lines in FILE_LIST:
        count_load += 1
    print(count_load, "books loaded")

    print("L - List books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
    menu = input(">>>").upper()
    while menu not in ["L", "A", "M", "Q"]:
        menu = input("Invalid, please re-enter and appropriate option: ").upper()
    if menu == "L":
        list_function()
    if menu == "A":
        add_function()
    if menu == "M":
        marked_function()
    else:
        confirm = input("Are you sure you want to quit? -(Y)es, (N)o ").upper()
        while confirm not in ["Y", "N"]:
            confirm = input("Invalid, please re-enter your option: (Y)es or (N)o").upper()
        if confirm == "Y":
            with open('books.csv', 'w') as book_list:
                for item in FILE_LIST:
                    book_list.write("{}".format(item))
            print("----Saving to your csv file----")
            print("-- Exited book. Have a nice day! --")
            quit()
        else:
            main_menu()


'''list_function show all the current books and its status(marked or need to be mark). All the data read inside the 
CSV files will be store inside a list for interaction and then write back to the csv file after all interactions are 
done. Because it is difficult to interact directly with the csv file through read and write command of Python, 
so i create a list (FILE_LIST) and import all csv data to it, users will interact and change the value inside the 
list and then after the program is closed, data inside the list will be writen it back to the csv file '''


def list_function():
    count = 0
    count_marked = 0

    list = []
    for lines in FILE_LIST:
        count += 1
        new_lines = lines.split(',')
        input_book = new_lines[0]
        input_author = new_lines[1]
        input_page = new_lines[2]
        mark = new_lines[3].replace("c", "*").replace("r", "").replace("\n", "")
        list.append(count)
        books_display = ("{:>2}. {:<1} {:<35} - {:<35} ({})".format(count, mark, input_book, input_author, input_page))
        print(books_display)

        if "*" in mark:
            count_marked += 1
    print("-" * 100)
    print("Total books marked: ", max(list))
    count_need = (max(list) - count_marked)
    REMAINDER.append(count_need)
    print(max(list) - count_marked, "books still to read")
    print(count_marked, "books learned")
    TOTAL_BOOK.append(max(list))
    print("-" * 100)
    main_menu()


'''' add_function allows users too add more books to the FILE_LIST list, so later on it can be displayed and 
formatted in the list_function() function '''


def add_function():
    mark_status = "r\n"
    title = input("Title: ")
    while title == "":
        print("Input can not be blank")
        title = input("Title: ")
    author = input("Author: ")
    while author == "":
        print("Input can not be blank")
        author = input("Author: ")
    test = True
    while test == True:
        try:
            page = int(input("Page: "))
            test = False
        except ValueError:
            print("Invalid input; enter a valid number")
    while page <= 0:
        print("Number must be > 0")
        test = True
        while test == True:
            try:
                page = int(input("Page: "))
                test = False
            except ValueError:
                print("Invalid input; enter a valid number")

    if REMAINDER[-1] == 0:
        REMAINDER.remove(REMAINDER[-1])
    final_result = ("{},{},{},{}".format(title, author, page, mark_status))
    FILE_LIST.append(final_result)
    print("{} by {} ,({} pages) added to Reading Tracker".format(title, author, page))
    print('-' * 100)
    main_menu()


''''marked_function() allows user to mark the completed books. If all the books are marked complete, there will be 
the print to show that there are no more books to learn '''


def marked_function():
    mark_status = "c\n"
    if min(REMAINDER) == 0:
        print('-' * 100)
        print("No more books to read!")
        print('-' * 100)
        main_menu()

    test = True
    while test == True:
        try:
            number = int(input("Enter the number of a book to be marked as marked: "))
            test = False
        except ValueError:
            print("Invalid input, please enter a number")
    if max(TOTAL_BOOK) == 0:
        print("-" * 100)
        print("Please load the list of books first by type in L in the main menu")
        print("Remember to load the list book for checking every time you make a change")
        print("-" * 100)
        main_menu()

    while number > max(TOTAL_BOOK) or number < 0:
        print("Please input the appropriate value!")
        number = int(input("Enter the number of the book to be marked as complete: "))

    rows = FILE_LIST[number - 1]
    new_list_rows = rows.split(",")
    book_name = new_list_rows[0]
    author_name = new_list_rows[1]
    page = new_list_rows[2]
    result = ("{},{},{},{}".format(book_name, author_name, page, mark_status))
    result_1 = ("'{} by {} from {}' is marked complete! Congratulation!".format(book_name, author_name, page))
    FILE_LIST.append(result)
    FILE_LIST.remove(FILE_LIST[number - 1])
    print(result_1)
    print("Remember to load the list book for checking every time you make a change")
    print('-' * 100)
    main_menu()


if __name__ == '__main__':
    main()
