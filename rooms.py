from common_function import *


def addData():
    db, cur = connect()

    print("\nEnter Room Details-")

    query = "INSERT INTO rooms VALUES (%s, %s, %s)"
    room_no = command("Room No.: ")

    room_codes = {
        "1": "Single",
        "2": "Double",
        "3": "Triple",
        "4": "Quad",
        "5": "Twin"
    }
    print("\n".join(str((f"{x} - {y}")) for (x, y) in room_codes.items()))

    while True:
        room_type = command("Room Type: ")
        if int(room_type) in range(1, 6):
            break
        else:
            print("Please enter a valid response")

    cost = command("Cost: ")

    try:
        cur.execute(query, (room_no, room_codes[room_type], cost))
        db.commit()
        print("Customer details entered")
    except mysql.errors.IntegrityError:
        italic(room_no, "is preoccupied")
        addData()
    except mysql.errors.DatabaseError:
        italic("Please enter data in correct format")
        addData()

    close(cur, db)
    return room_no


def deleteData(col, val):
    db, cur = connect()

    query = "DELETE FROM rooms WHERE {} = %s".format(col)
    cur.execute(query, (val,))
    db.commit()

    close(cur, db)


def displayData():
    db, cur = connect()

    query = "SELECT * FROM rooms"
    cur.execute(query)
    for x in cur.fetchall():
        print()
        print("Room No:", x[0])
        print("Room Type:", x[1])
        print("Cost:", x[2])
        print("="*15)

    close(cur, db)


def searchData(col, val):
    db, cur = connect()

    query = "SELECT * FROM rooms WHERE {} = %s".format(col)
    cur.execute(query, (val,))
    fetched_data = cur.fetchall()[0]

    print()
    print("Room Details-")
    print("Room No:", fetched_data[0])
    print("Room Type:", fetched_data[1])
    print("Cost:", fetched_data[2])
    print("="*15)

    close(cur, db)
