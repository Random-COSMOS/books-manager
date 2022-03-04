import mysql.connector as mysql


def connect():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="op360",
        database="hotel"
    )

    cur = db.cursor()

    return db, cur


def close(cur, db):
    cur.close()
    db.close()


def command(prompt):
    return input(prompt).lower()


def italic(text1, text2=""):
    print("\x1B[3m" + text1, text2 + "\x1B[0m")
