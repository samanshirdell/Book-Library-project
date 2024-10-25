import csv
print("Welcome to the book project")

book_info = {}
members_info = {}

def analize(question):
    if question == 1:
        print("welcome to the register member part of library.")
        while True:
            name = input("Please enter your name: ").capitalize()
            l_name = input("Please enter your last name: ").capitalize()
            
            members_info[name] = l_name
            member_see = input("Your name is successfully submit in library. Do you want to see: (Yes/No)").lower()
            if member_see == "yes":
                for fname, lastname in members_info.items():
                    print(f"Name: {fname}, Last Name: {lastname}")
                register_another = input("Do you want to register another person: Type 'Yes' or 'No': ").lower()
                if register_another == "yes":
                    print("ALL RIGHT")
                    continue
                elif register_another == "no":
                    print("Okay. I'll returned menu for you.")
                    return main()
            elif member_see == "no":
                print("Oh Okay. So I returned menu")
                return main()
        
                
    elif question == 2:
        print("All right")
        while True:
            book_name = input("Please enter book name: ").capitalize()
            print("===============================")
            book_count = int(input("How many books do you add: "))
            print("===============================")
            
            while book_count <= 0:
                print("Please enter more than 0")
                book_count = int(input("How many books do you add: "))
            if book_name in book_info:
                book_info[book_name] += book_count
            else:
                book_info[book_name] = book_count
            
            print("===============================")
            print(f"{book_count} added of '{book_name}' added to library")
            print("===============================")
            
            see_info = input("Do you want to see information: Type 'Yes' or 'No': ").lower()
            if see_info == "yes":
                print("+ =============================== +")
                for book, count in book_info.items():
                    print(f"Book: {book}, Count: {count}")
                print("+ =============================== +")
                
                again = input("Do you want to add more books: Type 'Yes' or 'No': ").lower()
                if again == "yes":
                    with open("outputs.csv", "w", newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["Book Name", "Book Count"])
                        for key, val in book_info.items():
                            writer.writerow([key, val])
                    continue
                elif again == "no":
                    print("Okay thanks for visiting")
                    return main()
            elif see_info == "no":
                print("Okay No Problem. I'll be back to menu...")
                return main()
        
    
    elif question == 3:
        print("Welcome to remove part of books.")
        remove_book = input("Do you want to remove a book? Just type the book name: ").capitalize()
        if remove_book in book_info:
            del book_info[remove_book]
            print(f"'{remove_book}' with count fully has been removed and this book in not in library.")
            return main()
        else:
            print(f"'{remove_book}' not found in library.")
            return main()
        
    
    elif question == 4:
        print("Welcome to the search book of library.")
        book_search = input("Which book do you seach: Type book name: ").capitalize()
        if book_search in book_info:
            print(f"This {book_search} searched with {book_info[book_search]} count in library")
        elif book_search not in book_info:
            print(f"This {book_search} in not in library.")
        
        
    elif question == 5:
        print("Welcome to the \"Spend Book\" part of library.")
        
        while True:
            spend_book = input("Which book do you want take in library: ").capitalize()
            
            if spend_book in book_info:
                print(f"Okay, you selected {spend_book}.")
                spend_book_count = int(input("How many books do you want to take: "))
                
                while spend_book_count <= 0:
                    print("Invalid number. Please try again.")
                    spend_book_count = int(input("How many books do you want to take: "))
                
                if spend_book_count > book_info[spend_book]:
                    print(f"There aren't enough books of {spend_book} available in the library.")
                    continue
                
                book_info[spend_book] -= spend_book_count
                print(f"You have taken {spend_book_count} book of {spend_book}.")
                print(f"Now there are {book_info[spend_book]} book of {spend_book} left in the library.")
                
                break
            else:
                print(f"The book '{spend_book}' is not available in the library.")
                try_again = input("Would you like to try again? (Yes/No): ").lower()
                if try_again != "yes":
                    print("Returning to the main menu.")
                    return main() 
        

def main():
    title = "Welcome to the best library"
    title_len = len(title) + 4
    print("+" + "-" * (title_len - 2) + "+")
    print("| " + title + " |")
    print("+" + "-" * (title_len - 2) + "+")
    
    resources = """
    |   1. Register member
    |   2. Add Books
    |   3. Remove Book
    |   4. Search Book
    |   5. Spend Book
    """
    print(resources)
    
    questions = int(input("Please choose number between 1 to 4: "))
    analize(questions)

main()
