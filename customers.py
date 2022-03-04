from common_function import *


def addData(room_no):
    db, cur = connect()

    print("\nEnter Customer Details-")

    query = "INSERT INTO customers VALUES (%s, %s, %s, %s, %s, %s)"
    customer = command("Customer Name: ")
    phone_no = command("Phone No: ")
    email = command("Email: ")
    address = command("Address: ")
    customer_id = customer[0:3] + room_no
    print(customer_id)

    while True:
        print("1 - Male")
        print("2 - Female")
        cmd = command("Gender: ")
        if cmd == "1":
            gender = "m"
            break
        elif cmd == "2":
            gender = "f"
            break
        else:
            print("Please enter a valid response \n")

    try:
        cur.execute(query, (customer_id, customer, phone_no, email, address, gender))
        db.commit()
        print("Customer details entered")
    except mysql.errors.IntegrityError:
        italic(customer.capitalize(), "already exists")
        addData(room_no)
    except mysql.errors.DatabaseError:
        italic("Please enter data in correct format")
        addData(room_no)

    close(cur, db)
    return customer_id


def deleteData(col, val):
    db, cur = connect()

    query = "DELETE FROM customers where {} = %s".format(col)
    cur.execute(query, (val,))
    db.commit()

    close(cur, db)

def displayData():
    db, cur = connect()

    query = "SELECT * FROM customers"
    cur.execute(query)
    for x in cur.fetchall():
        print()
        print("Customer:", x[0].capitalize())
        print("Phone No.:", x[1])
        print("Email:", x[2])
        print("Address:", x[3].capitalize())
        print("Gender:", x[4].capitalize())
        print("="*15)

    close(cur,db)

def searchData(col, val):
    db, cur = connect()

    query = "SELECT * FROM customers WHERE {} = %s".format(col)
    cur.execute(query,(val,))
    fetched_data = cur.fetchall()[0]

    print()
    print("Customer Details-")
    print("Customer:", fetched_data[0].capitalize())
    print("Phone No.:", fetched_data[1])
    print("Email:", fetched_data[2])
    print("Address:", fetched_data[3].capitalize())
    print("Gender:", fetched_data[4].capitalize())
    print("="*15)

    close(cur,db)
