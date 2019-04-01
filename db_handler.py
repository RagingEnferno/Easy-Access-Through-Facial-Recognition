import sqlite3

mydb = sqlite3.connect('Easy_Access')
mycursor = mydb.cursor()
print("Database opened")

mycursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for x in mycursor:
    print(x)
print(mydb)

mycursor.execute("create table if not exists test_encodings"
                 "(user_num int (9) not null PRIMARY KEY, "
                 "encodings VARCHAR(2500) NOT NULL);")

#mycursor.execute("drop table encodings")
def write_encoding(user_num, encoding):
    # uses test_encodings table for now

    print("Attempting to add encoding to database")
    sql = (f"INSERT INTO test_encodings (user_num, encodings) VALUES ({user_num}, '{encoding}')")
    #vals = (user_num, f"{encoding}")
    mycursor.execute(sql)

    print("Encoding Added to the 'test_encodings' database table in row:", mycursor.lastrowid)
    mydb.commit()
    mycursor.close()

def check_user_id(user_id):
    # check if user exisit
    sql = f"SELECT user_num FROM test_encodings WHERE user_num = {user_id};"
    mycursor.execute(sql)

    if mycursor.fetchone() is None:
        return 1
    elif mycursor.fetchone()[0]:
        return 0


def add_new_user(user_id, l_name, f_name):
    # check if user exisit
    sql = "SELECT user_num FROM test_encodings WHERE user_num = (num) VALUES (%s)"
    vals = user_id
    mycursor.execute(sql, vals)

    if mycursor.fetchone()[0]:
        print("This user already exist")
    else:
        sql = "INSERT INTO user_data (user_id, l_name, f_name) VALUES (%s, %s, %s)"
        vals = (user_id, l_name, f_name)
        mycursor.execute(sql, vals)

        print("New user added to database: ", mycursor.lastrowid)
        mydb.commit()


def get_encoding(row_num):
    #limiter cannot be less than 1
    if row_num is 0:
        print("Limiter must be larger than 1, auto updated to 1")
        row_num = 1

    mycursor = mydb.cursor()

    print("Getting encoding")
    sql = "SELECT * FROM test_encodings LIMIT %s, %s"
    vals = (row_num,row_num)
    mycursor.execute(sql, vals )
    row = mycursor.fetchone()
    print(row)
    print("encode only:", row[1])
    print("only user_id", row[0])
    mydb.commit()
    return row[1]

def get_row_count():
    sql = "SELECT * FROM test_encodings"
    return mycursor.rowcount
