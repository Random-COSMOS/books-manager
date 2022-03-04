import mysql.connector as mysql
from common_function import *
import rooms
import customers
import booking

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="op360",
    database="hotel"
)

cur = db.cursor()

table_rooms = "CREATE TABLE IF NOT EXISTS rooms (roomNo INT PRIMARY KEY, roomType VARCHAR(30), cost INT)"
table_customers = "CREATE TABLE IF NOT EXISTS customers (customerId VARCHAR(10) PRIMARY KEY, customer VARCHAR(50), phoneNo CHAR(10), email VARCHAR(100), address VARCHAR(100), gender CHAR)"
table_booking = "CREATE TABLE IF NOT EXISTS booking (roomNo INT, customerId VARCHAR(10), checkIn DATE, checkOut DATE, bookingDate DATE, FOREIGN KEY (roomNo) REFERENCES rooms(roomNo), FOREIGN KEY (customerId) REFERENCES customers(customerId))"

cur.execute(table_rooms)
cur.execute(table_customers)
cur.execute(table_booking)

cur.close()
db.close()

while True:
    print()
    print("1 - Add")
    print("2 - Delete")
    print("3 - Display")
    print("4 - Search")
    print("5 - Exit")

    cmd = command("cmd> ")

    if cmd == "1":
        room_no = rooms.addData()
        customer_id = customers.addData(room_no)
        booking.addData(customer_id, room_no)

        print("Details Added ")
        print("Your Customer ID is", customer_id)

    elif cmd == "2":
        print()
        italic("Warning: It will delete all records related to the provided input")
        print("1 - Room No")
        print("2 - Customer Name")

        while True:
            col = command("Input: ")
            if int(col) in range(1, 3):
                col = "roomNo" if col == "1" else "customer"
                break
            else:
                print("Please enter a valid response")

        val = command("Value: ")

        try:
            room_no, customer = booking.deleteData(col, val)
            rooms.deleteData("roomNo", room_no)
            customers.deleteData("customer", customer)
        except IndexError:
            italic("Couldn't find the provided entry")

    elif cmd == "3":
        print()
        print("1 - Rooms")
        print("2 - Customer")
        print("3 - Booking")
        display = command("display: ")

        if display == "1":
            rooms.displayData()
        elif display == "2":
            customers.displayData()
        elif display == "3":
            booking.displayData()
        else:
            italic("Please enter a valid response")

    elif cmd == "4":
        print()
        print("1 - Room No")
        print("2 - Customer Name")

        while True:
            col = command("Search: ")
            if int(col) in range(1, 3):
                col = "roomNo" if col == "1" else "customer"
                break
            else:
                print("Please enter a valid response")

        val = command("Value: ")

        try:
            room_no, customer = booking.searchData(col, val)
            rooms.searchData("roomNo", room_no)
            customers.searchData("customerId", customer)
        except IndexError:
            italic("Couldn't find the provided entry")

    elif cmd == "5":
        break

    else:
        italic("Please enter a valid response")