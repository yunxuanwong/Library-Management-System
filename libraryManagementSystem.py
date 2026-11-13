import os 
def Date():
    return os.popen('date /t').read().strip()

def Time():
    return os.popen('time /t').read().strip()

def DueDate():
    # Use PowerShell to add 14 days to today's date
    cmd = 'powershell -Command "(Get-Date).AddDays(14).ToString(\'dd-MM-yyyy\')"' 
    return os.popen(cmd).read().strip()

print("Date:", Date())
print("Time:", Time())


# Admin:: Login authentication  ----------------------------------------------------------------------------------------------------------------------- DONE
def AdminLogin():
    userid = []
    username = []
    password = []
    role = []

    with open ("user.txt","r") as file:
        for line in file:
            data = line.strip().split("|")
            if len (data) == 4:
                userid.append(data[0])
                username.append(data[1])
                password.append(data[2])
                role.append(data[3])
    uid = input("Please enter Admin ID: ").strip()
    pwd = input("Please enter password: ").strip()

    if uid in userid:
        index = userid.index(uid)
        if password[index] == pwd and role[index].lower() == "admin":
            print("Login Successful.")
            return True
        else:
            print("Admin ID and password don't match.")
            return False
    else: 
        print("Login unsuccessful. Please try again.")
        return False
    
# Admin:: Managebook  -----------------------------------------------------------------------------------------------------------------------   DONE
def ManageBooks():
    while True:
        print("\n======= BOOK MANAGEMENT MENU =======")
        print("1. Add New Book")
        print("2. Remove Book")
        print("3. Modify Book")
        print("4. Back")
        choice = input("Please enter your choice (1/2/3/4): ").strip()

        with open("booklist.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("Booklist is empty or missing data.")
            return

        header = lines[0].strip()
        data_lines = [line.strip() for line in lines[1:]]
        if choice == "1": 
            print("------- ADD NEW BOOK -------")
            print("\n-- Current Booklist --")
            for line in data_lines:
                print(line)

            with open("booklist.txt", "a") as file:
                if not data_lines[-1].endswith("\n"):
                    file.write("\n")
                isbn = input("Enter new book's ISBN: ").strip()
                title = input("Enter new book's title: ").strip()
                author = input("Enter new book's author: ").strip()
                quantity = input("Enter new book's quantity: ").strip()
                status = input("Enter new book's status: ").strip()

                file.write(f"{isbn}|{title}|{author}|{quantity}|{status}")
            print(f"Book {isbn} added successfully")

        elif choice == "2":  
            print("------- REMOVE BOOK -------")
            print("\n-- Current Booklist --")
            for line in data_lines:
                print(line.strip())

            isbn = input("\nPlease enter ISBN of the book to remove: ").strip()
            found = False
            updated_lines = []

            for line in data_lines:
                data = line.strip().split("|")
                if data[0].strip() == isbn:
                    found = True
                    print(f"Book {isbn} removed successfully.")
                    continue
                updated_lines.append(line.strip())

            if not found:
                print("ISBN not found.")
            else:
                with open("booklist.txt", "w") as file:
                    file.write(header + "\n")
                    for line in updated_lines:
                        file.write(line + "\n")

        elif choice == "3":
            print("------- MODIFY BOOK -------")
            print("\n-- Current Book Records --")
            for line in data_lines:
                print(line)

            isbn_to_modify = input("\nPlease enter ISBN of the book to modify: ").strip()
            found = False
            updated_lines = []

            for line in data_lines:
                data = line.split("|")
                if data[0] == isbn_to_modify:
                    found = True
                    print(f"\nFound record: {line}")

                    new_title = input(f"Enter new title (old: {data[1]}): ").strip() or data[1]
                    new_author = input(f"Enter new author (old: {data[2]}): ").strip() or data[2]
                    new_quantity = input(f"Enter new quantity (old: {data[3]}): ").strip() or data[3]
                    new_status = input(f"Enter new status (old: {data[4]}): ").strip() or data[4]

                    new_line = f"{data[0]}|{new_title}|{new_author}|{new_quantity}|{new_status}"
                    updated_lines.append(new_line)
                else:
                    updated_lines.append(line)

            if not found:
                print("ISBN not found.")
            else:
                with open("booklist.txt", "w") as file:
                    file.write(header + "\n")
                    for line in updated_lines:
                        file.write(line + "\n")
                print("Record updated successfully.")
        elif choice == "4" :
            break

# Admin:: Add user  -----------------------------------------------------------------------------------------------------------------------  DONE
def AddUser():
    with open("user.txt", "r") as file:
        content = file.read().strip("|")
        print("------- ADD NEW USER -------")
        print(content)

        with open("user.txt", "a") as file:
            if not content.endswith("\n") and len(content) > 0:
                file.write("\n")

            userid = input("Enter new UserID: ")
            name = input("Enter new username: ")
            password = input("Enter new user password: ")
            role = input("Enter new user's role: ")
            file.write(f"{userid}|{name}|{password}|{role}")
            print(f"New staff/member {name} have been added successfully.")

#Admin: Main logic  -----------------------------------------------------------------------------------------------------------------------------------
def AdminMainLogic():
    print("------- ADMIN LOGIN -------")
    loggedIn = AdminLogin()
    if loggedIn:
        while True:
            print("======= ADMIN MENU =======")
            print("1. Manage Book")
            print("2. User Management")
            print("3. Logout")
            print("--------------------------")
            
            choice = input("Please enter your choice (1/2/3): ")

            if choice == '1':
                ManageBooks()
            elif choice == '2':
                AddUser()
            elif choice == '3':
                print("------- ADMIN LOGOUT -------")
                confirm = input("Do you want to logout? (yes/no): ").strip().lower()
                if confirm == "yes":
                    print("Logging out...")
                    break
                else:
                    print("Logout cancelled.")
            else:
                print("Invalid choice. Please try again.")

# Staff: Login  ----------------------------------------------------------------------------------------------------------------------------------------
def StaffLogin():
    userid = []
    username = []
    password = []
    role = []

    with open ("user.txt","r") as file:
        for line in file:
            data = line.strip().split("|")
            if len (data) == 4:
                userid.append(data[0])
                username.append(data[1])
                password.append(data[2])
                role.append(data[3])

    uid = input("Please enter Staff ID: ").strip()
    pwd = input("Please enter password: ").strip()

    if uid in userid:
        index = userid.index(uid)
        if password[index] == pwd and role[index].lower() == "staff":
            print("Login Successful.")
            return True
        else:
            print("Staff ID and password don't match.")
            return False
    else: 
        print("Login unsuccessful. Please try again.")
        return False
            
# Staff: Issue book  -----------------------------------------------------------------------------------------------------------------------------------
def SearchBook():
    found = False
    booklist = []
    with open("booklist.txt", "r") as file:
        print("------- SEARCH BOOK -------")
        print(f"{'ISBN':<8} {'Book Name':<30} {'Author':<20} {'Quantity':<10} {'Status':<6}")
        print("-" * 80)
        for lines in file:
            data = lines.strip().split("|")
            isbn, title, author, quantity, status = data
            print(f"{isbn:<8} {title:<30} {author:<20} {quantity:<10} {status:<6}")
            booklist.append(data)

    answer = input("Please enter ISBN code/Book Name you want to search: ").strip()                
    for book in booklist:
        isbn, title, author, quantity, status = book
        if answer == isbn or answer in title:
            print("-- Book Found --")
            print(f"ISBN: {isbn}, Book Name: {title} , Author: {author}, Quantity: {quantity}, Status: {status}")
            found = True
            return book
    if not found:
        print("No books found.")
        
#update book Stock
def UpdateBookStock(isbnsearch):
    updated_quantity = []

    with open ("booklist.txt","r") as file:
        lines = file.readlines()
        
    for line in lines:
        data = line.strip().split("|")
        if len(data) < 5:
            continue

        isbn, title, author, quantity, status = data
        quantity = int(quantity)

        if isbnsearch == isbn:
            if quantity > 0:
                quantity -= 1
            if quantity == 0:  
                status = "no"    
            else:
                status = "yes"   
        updated_quantity.append(f"{isbn}|{title}|{author}|{quantity}|{status}\n")

    with open("booklist.txt", "w") as file:
        file.writelines(updated_quantity)
            
#issue book
def IssueBook(isbn, title, memberid):
    print("------- ISSUE BOOK -------")
    borrow = input("Are you comfirm to borrow the book?(yes/no): ")

    borrowed_date = Date()
    due_date = DueDate()
    
    if borrow.lower() == "yes":
        UpdateBookStock(isbn)

        #append currentlyborrow file
        with open ("currentlyborrow.txt","a") as file:
            file.write(f"{isbn}|{title}|{memberid}|{borrowed_date}|{due_date}\n")
            print(f"Borrow record added: ISBN {isbn}, Book Name {title} , Member ID {memberid}, Borrowed Date {borrowed_date}, Due Date {due_date}")
            print("Book borrowed successfully.")
    else: 
        print("Borrowing is cancelled.")  
        return

# Staff: Return book  ----------------------------------------------------------------------------------------------------------------------------------
#updatebookstock
def UpdateBookStock2(isbnsearch):
    updated_book = []

    with open ("booklist.txt","r") as file:
        lines = file.readlines()
        
        for line in lines:
            data = line.strip().split("|")
            if len(data) < 5:
                continue

            isbn, title, author, quantity, status = data
            quantity = int(quantity)

            if isbnsearch == isbn:
                quantity += 1
                status = "yes"   
            updated_book.append(f"{isbn}|{title}|{author}|{quantity}|{status}\n")

    with open("booklist.txt", "w") as file:
        file.writelines(updated_book)

def RemoveBook(isbnsearch):
    remove_book = []
    remove = False

    with open("currentlyborrow.txt","r") as file:
        lines = file.readlines()

        for line in lines:
            data = line.strip().split("|")
            if len(data) < 5:
                continue
                
            isbn, title, userid, borrowed_date, due_date = data
            if isbnsearch == isbn:
                remove = True
                continue
            else:
                remove_book.append(line)
    
    with open ("currentlyborrow.txt","w") as file:
        file.writelines(remove_book)

#return book
def ReturnBook(memberid):
    print("------- RETURN BOOK -------")

    with open("currentlyborrow.txt", "r") as file:
        lines = file.readlines()

    historylist = []
    print("-- Currently Borrowed Book --")
    print(f"{'ISBN':<8} {'Book Name':<30} {'Member ID':<10} {'Borrowed Date':<15} {'Due Date':<6}")
    print("-" * 80)
    for line in lines:
        data = line.strip().split("|")
        if len(data) < 5:
            continue
        isbn, title, userid, borrowed_date, due_date = data
        if memberid == userid:
            print(f"{isbn:<8} {title:<30} {userid:<10} {borrowed_date:<15} {due_date:<6}")
            historylist.append(data)
    
    record = False

    today = Date()
    borrowed_date = today
    time = Time()
    return_date = today
    return_time = time

    ans = input("Please enter Book ISBN/ Book Name you want to return: ").strip()
    comfirm = input("Are you comfirm to return the book?(yes/no): ")
    for records in historylist:
        isbn, title, userid, borrowed_date, due_date = records
        if (ans == isbn or ans in title ) and comfirm.lower() == "yes":
            record = True
            RemoveBook(isbn)
            UpdateBookStock2(isbn)
            #record in history.txt
            with open("history.txt", "a") as file:
                file.write(f"{isbn}|{title}|{memberid}|{borrowed_date}|{return_date}|{return_time}\n")
                print(f"Borrow record added: ISBN {isbn}, Book Name {title} , Member ID {memberid}, Borrowed Date {borrowed_date}, Return Date {return_date}, Return Time {return_time}")
                print(f"Book {title} is returned.")
            return records
        
    if not record:
        print("No books found.")

# Staff: Generate report  ------------------------------------------------------------------------------------------------------------------------------
def GenerateReport(memberid):
    print("-------- GENERATE REPORT -------")
    with open("history.txt", "r") as file:
        lines = file.readlines()

    historytable = []
    for line in lines:
        data = line.strip().split("|")
        if len(data) >= 6 :
            isbn = data[0]
            title = data[1]
            userid = data[2]
            borrowed_date = data[3]
            return_date = data[4]
            return_time = data[5]
            if userid == memberid:
                historytable.append((isbn, title, userid, borrowed_date, return_date, return_time))

    if historytable:
        print("-- Report --")
        print(f"{"ISBN": <9} {"Book Name": <29} {"Member ID": <10} {"Borrowed Date": <18} {"Return Date": <17} {"Return Time": <10}")
        print("-" * 100)
        for record in historytable:
            print(f"{record[0]:<10}{record[1]:<30}{record[2]:<11}{record[3]:<19}{record[4]:<18}{record[5]:<10}")

    else:
        print("You have no record.")  

# Staff: Main logic  -----------------------------------------------------------------------------------------------------------------------------------
def StaffMainLogic():
    print("------- STAFF LOGIN -------")
    loggedIn = StaffLogin()
    if loggedIn:
        while True:
            print("------- STAFF LOGGED IN -------")
            print("1. Manage Member")
            print("2. Logout")
            option = input("Please enter your choice (1/2):")
            if option == "1":

                memberid = input("Please enter Member ID to manage: ").strip()

                while True:
                    print("======= STAFF MENU ========")
                    print("1. Issue Book")
                    print("2. Return Book")
                    print("3. Search Book")
                    print("4. Generate Report")
                    print("5. Logout")
                    print("--------------------------")
                    
                    choice = input("Please enter your choice (1/2/3/4/5):")

                    if choice == '1':
                        while True:
                            book = SearchBook()
                            isbn, title, author, quantity, status = book
                            if status == "no":
                                print("Book is not available.")
                            else: 
                                IssueBook(isbn, title, memberid)
                            another = input("Do you want to borrow another book? (yes/no): ").strip().lower()
                            if another == "no":
                                break
                            elif another == "yes":
                                pass
                            else:
                                print("Please enter a valid response.")

                    elif choice == '2':
                        while True:
                            ReturnBook(memberid)
                            exit = input("Do you want to exit? (yes/no)： ").strip().lower()
                            if exit == "yes":
                                break

                    elif choice == "3":
                        while True:
                            SearchBook()
                            exit = input("Do you want to exit? (yes/no)：").strip().lower()
                            if exit == "yes":
                                break

                    elif choice == "4":
                        while True:
                            GenerateReport(memberid)
                            exit = input("Do you want to exit? (yes/no)： ").strip().lower()
                            if exit == "yes":
                                break

                    elif choice == '5':
                        print("=== Member Logout ===")
                        confirm = input("Do you want to logout of member? (yes/no): ").strip().lower()
                        if confirm == "yes":
                            print(f"Member {memberid} is logging out...")
                            break
                        else:
                            print("Logout cancelled.")
                    else:
                        print("Invalid choice. Please try again.")
            elif option == "2":
                print("Logging out...")
                break
            else:
                print("Please provide a valid input.")

# Member: Login  ---------------------------------------------------------------------------------------------------------------------------------------
def MemberLogin():
    userid = []
    username = []
    password = []
    role = []

    with open ("user.txt","r") as file:
        for line in file:
            data = line.strip().split("|")
            if len (data) == 4:
                userid.append(data[0])
                username.append(data[1])
                password.append(data[2])
                role.append(data[3])

    uid = input("Please enter Member ID: ").strip()
    pwd = input("Please enter password: ").strip()

    if uid in userid:
        index = userid.index(uid)
        if password[index] == pwd and role[index].lower() == "member":
            print("Login Successful.")
            return [userid[index], True]
        else:
            print("Member ID and password don't match.")
            return [userid[index], False]
    else: 
        print("Login unsuccessful. Please try again.")
        return ["", False]

# Member: Borrow book  ---------------------------------------------------------------------------------------------------------------------------------
#update book Stock
def UpdateBookStock(isbnsearch):
    updated_quantity = []

    with open ("booklist.txt","r") as file:
        lines = file.readlines()
        
    for line in lines:
        data = line.strip().split("|")
        if len(data) < 5:
            continue

        isbn, title, author, quantity, status = data
        quantity = int(quantity)

        if isbnsearch == isbn:
            if quantity > 0:
                quantity -= 1
            if quantity == 0:  
                status = "no"    
            else:
                status = "yes"   
        updated_quantity.append(f"{isbn}|{title}|{author}|{quantity}|{status}\n")

    with open("booklist.txt", "w") as file:
        file.writelines(updated_quantity)
        
def BorrowBook(isbn, title, userid):
    print("------- BORROW BOOK -------")
    borrow = input("Are you comfirm to borrow the book?(yes/no): ")

    due_date = DueDate()
    borrowed_date = Date()

    if borrow.lower() == "yes":
        UpdateBookStock(isbn)

        #append currentlyborrow file
        with open ("currentlyborrow.txt","a") as file:
            file.write(f"{isbn}|{title}|{userid}|{borrowed_date}|{due_date}\n")
            print(f"Borrow record added: ISBN {isbn}, Book Name {title} , Member ID {userid}, Borrowed Date {borrowed_date}, Due Date {due_date}")
            print(f"Book {title} borrowed successfully!")
    else: 
        print("Borrowing is cancelled.")  
        return
    
# Member: View borrowed history  -----------------------------------------------------------------------------------------------------------------------
def ViewBorrowedBooks(userid):
    print("------- VIEW HISTORY -------")

    found = False
    historytable = []

    with open("history.txt", "r") as file:
        for line in file:
            data = line.strip().split("|")
            if len(data) >= 5:
                found = True
                isbn = data[0]
                title = data[1]
                uid = data[2]
                borrowed_date = data[3]
                return_date = data[4]
                if userid == uid:
                    historytable.append((isbn, title, uid, borrowed_date, return_date))

        print("-- Borrowed books -- ")
        print(f"{"ISBN": <9} {"Book Name": <29} {"Member ID": <10} {"Borrowed Date": <14} {"Return Date": <15}")
        print("-" * 80)
        for record in historytable:
            print(f"{record[0]:<10}{record[1]:<30}{record[2]:<11}{record[3]:<15}{record[4]:<15}")

    if not found:
        print("You have no borrowed books.")  

#Member: Main logic  -----------------------------------------------------------------------------------------------------------------------------------
def MemberMainLogic():
    print("------- MEMBER LOGIN -------")
    userid, loggedIn = MemberLogin()
    if loggedIn:

        while True:
            print("======= MEMBER MENU =======")
            print("1. Borrow Book")
            print("2. View Borrowed History")
            print("3. Logout")
            print("--------------------------")
            
            choice = input("Please enter your choice (1/2/3): ")

            if choice == '1':
                while True:
                    book = SearchBook()
                    isbn, title, author, quantity, status = book
                    if status == "no":
                        print("Book is not available.")
                    else:
                        BorrowBook(isbn, title, userid)
                    another = input("Do you want to borrow another book? (yes/no): ").strip().lower()
                    if another == "no":
                        break
                    elif another == "yes":
                        pass
                    else:
                        print("Please enter a valid response.")

            elif choice == '2':
                while True:
                    ViewBorrowedBooks(userid)
                    exit = input("Do you want to exit? (yes/no)").strip().lower()
                    if exit == "yes":
                        break

            elif choice == '3':
                print("------- MEMBER LOGOUT -------")
                confirm = input("Do you want to logout? (yes/no): ").strip().lower()
                if confirm == "yes":
                    print("Logging out...")
                    break
                else:
                    print("Logout cancelled.")
            else:
                print("Invalid choice. Please try again.")

# Visitor: Book catalog display  -----------------------------------------------------------------------------------------------------------------------
def Catalog():
    print("------- BOOK CATALOG -------")
    print(f"{'ISBN':<8} {'Book Name':<30} {'Author':<20} {'Quantity':<10} {'Status':<6}")
    print("-" * 80)

    with open("booklist.txt", "r") as file:
        for line in file:
            data = line.strip().split("|")
            if len(data) >= 5:
                isbn = data[0]
                title = data[1]
                author = data[2]
                quantity = data[3]
                status = data[4]
                print(f"{isbn:<8} {title:<30} {author:<20} {quantity:<10} {status:<6}")
     
# Main logic  ------------------------------------------------------------------------------------------------------------------------------------------
def main():

    while True:
        print("====== Welcome to library system ======")
        print("1. Login")
        print("2. Visitor access")
        print("3. Exit")
        option = input("Please enter your option (1/2/3): ")

        if option == "1":
            print("1. Admin Login")
            print("2. Library staff Login")
            print("3. Library member Login")
            choice = input("Please enter your option (1/2/3): ")

            if choice == "1":
                AdminMainLogic()
            elif choice == "2":
                StaffMainLogic()
            elif choice == "3":
                MemberMainLogic()
            else:
                print("Login failed. Returning to homepage.....")

            
        elif option == "2":
            while True:
                print("======= VISITOR ACCESS =======")
                print("1. View book catalog")
                print("2. Search book")
                print("3. Exit to menu")
                Visitor_choice = input("Please enter an option (1/2/3): ")
                
                if Visitor_choice == "1":
                    Catalog()
                    input("Press enter to back: ")
                elif Visitor_choice == "2":
                    SearchBook()
                    input("Press enter to back: ")
                elif Visitor_choice == "3":
                    break

        elif option == "3":
            print("======= EXITING THE PROGRAM =======")
            for y in range(15, -15, -1):      
                for x in range(-30, 30):     
                    formula = ((x*0.05)**2 + (y*0.1)**2 - 1)**3 - (x*0.05)**2 * (y*0.1)**3
                    if formula <= 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print()
            break
main()