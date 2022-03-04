from common_function import *
from datetime import date

db, cur = None, None


def addData(customer_id, room_no):
    db, cur = connect()

    query = "INSERT INTO booking VALUES (%s, %s, %s, %s, %s)"

    print("\nEnter Booking Details")
    print("Customer ID:", customer_id)
    print("Room No.:", room_no)
    print("Booking date:", date.today())

    check_in = command("Check In (YYYY-MM-DD): ")
    check_out = command("Check Out (YYYY-MM-DD): ")
    booking_date = date.today()

    try:
        cur.execute(query, (room_no, customer_id, check_in, check_out, booking_date))
        db.commit()
        print("Booking details entered")
    except mysql.errors.DataError:
        italic("Please enter data in correct format")
        addData(customer_id, room_no)

    close(cur, db)


def deleteData(col, val):
    db, cur = connect()

    query = "SELECT * FROM booking WHERE {} = %s".format(col)
    cur.execute(query, (val,))

    fetched_data = cur.fetchall()[0]
    room_no = fetched_data[0]
    customer = fetched_data[1]

    query = "DELETE FROM booking WHERE {} = %s".format(col)
    cur.execute(query, (val,))
    db.commit()

    close(cur, db)
    return room_no, customer


def displayData():
    db, cur = connect()

    query = "SELECT * FROM booking"
    cur.execute(query)
    for x in cur.fetchall():
        print()
        print("Room No:", x[0])
        print("Customer:", x[1].capitalize())
        print("Check In:", x[2])
        print("Check Out:", x[3])
        print("Bookin Date:", x[4])
        print("="*25)

    close(cur, db)


def searchData(col, val):
    db, cur = connect()

    query = "SELECT * FROM booking WHERE {} = %s".format(col)
    cur.execute(query, (val,))

    fetched_data = cur.fetchall()[0]
    room_no = fetched_data[0]
    customer = fetched_data[1]

    print()
    print("Booking Details-")
    print("Room No:", fetched_data[0])
    print("Customer:", fetched_data[1].capitalize())
    print("Check In:", fetched_data[2])
    print("Check Out:", fetched_data[3])
    print("Bookin Date:", fetched_data[4])
    print("="*25)

    close(cur, db)
    return room_no, customer
