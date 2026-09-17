# =====================================================
#        ONLINE MOVIE TICKET BOOKING SYSTEM
# =====================================================

# ---------------- LOGIN SYSTEM ----------------

def login():
    username = "admin"
    password = "1234"

    print("\n======================================")
    print("        🔐 LOGIN SYSTEM")
    print("======================================")

    attempts = 3

    while attempts > 0:
        user_input = input("Enter Username: ")
        pass_input = input("Enter Password: ")

        if user_input == username and pass_input == password:
            print("\n✅ Login Successful!")
            print("Welcome to the Online Movie Ticket Booking System.")
            return True

        else:
            attempts -= 1
            print("\n❌ Invalid Username or Password!")
            print("Attempts Remaining:", attempts)

    print("\n🚫 Too many failed attempts.")
    print("Access Denied!")
    return False


# ---------------- MOVIE DATA ----------------

movies = {
    1: ("Avengers: Endgame", 200),
    2: ("KGF Chapter 2", 180),
    3: ("3 Idiots", 150),
    4: ("Dangal", 120),
    5: ("RRR", 220)
}


# ---------------- DISPLAY MOVIES ----------------

def display_movies():
    print("\n======================================")
    print("         🎬 AVAILABLE MOVIES")
    print("======================================")

    for number, details in movies.items():
        print(f"{number}. {details[0]} - ₹{details[1]} per ticket")

    print("======================================")


# ---------------- BOOK TICKETS ----------------

def book_tickets():
    display_movies()

    try:
        choice = int(input("\nEnter Movie Number: "))

        if choice in movies:

            movie_name, ticket_price = movies[choice]

            print(f"\n🎥 Selected Movie: {movie_name}")

            quantity = int(input("Enter Number of Tickets: "))

            if quantity > 0:

                total_price = ticket_price * quantity

                print("\n======================================")
                print("         🧾 BOOKING SUMMARY")
                print("======================================")

                print("Movie Name:", movie_name)
                print("Number of Tickets:", quantity)
                print("Price Per Ticket: ₹", ticket_price)
                print("Total Amount: ₹", total_price)

                print("======================================")

                confirm = input("\nConfirm Booking? (yes/no): ").lower()

                if confirm == "yes":
                    print("\n🎉 Booking Successful!")
                    print("Thank you for booking with us. 🙏")

                elif confirm == "no":
                    print("\n❌ Booking Cancelled.")

                else:
                    print("\n⚠️ Invalid Confirmation Choice.")

            else:
                print("\n⚠️ Number of tickets must be greater than zero.")

        else:
            print("\n❌ Invalid Movie Selection.")

    except ValueError:
        print("\n⚠️ Please enter a valid number.")


# ---------------- MAIN MENU ----------------

def main():
    while True:

        print("\n==============================================")
        print("     🎬 ONLINE MOVIE TICKET BOOKING SYSTEM")
        print("==============================================")

        print("1. 👀 View Movies")
        print("2. 🎟️ Book Tickets")
        print("3. 🚪 Exit")

        option = input("\nEnter Your Choice: ")

        if option == "1":

            display_movies()

        elif option == "2":

            book_tickets()

        elif option == "3":

            print("\n======================================")
            print("Thank you for using our system! 🙏")
            print("Have a great day! 🎬")
            print("======================================")
            break

        else:

            print("\n❌ Invalid Choice! Please try again.")


# ---------------- PROGRAM START ----------------

if login():
    main()
else:
    print("\nProgram Closed. Goodbye! 👋")