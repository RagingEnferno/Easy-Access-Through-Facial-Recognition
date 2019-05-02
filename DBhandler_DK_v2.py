import sqlite3

mydb = sqlite3.connect('Easy_Access')
mycursor = mydb.cursor()
print("Database opened")

mycursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
for x in mycursor:
    print(x)
print(mydb)

mycursor.execute("create table if not exists user_data"
                 "(user_id int (9) not null PRIMARY KEY, "
                 "encoding VARCHAR(2000) NOT NULL);")

#mycursor.execute("drop table user_data")
def check_user_id(user_id):
    # check if user exisit
    mycursor.execute("DELETE from user_data WHERE user_id = %i" %user_id)



def add_new_user(user_id, pic):
    # check if user exisit
    mycursor.execute("SELECT user_id FROM user_data WHERE user_id = %i" % user_id)
    flag = 0
    for row in mycursor.fetchall():
        flag = 1
    if flag ==1:
        print("This user already exist")
    else:
        mycursor.execute("INSERT INTO user_data (user_id, encoding) VALUES (?,?)", (user_id, pic))
        print("New user added to database: ", mycursor.lastrowid)
        mydb.commit()

def delete_user(user_id):
    #Delete user info
    mycursor.execute("DELETE FROM user_data WHERE user_id = %i" %user_id)
    mydb.commit()


def change_pic(user_id, newpic):
    #change photo info of one user
    mycursor.execute("UPDATE user_data SET encoding = %s WHERE user_id = %i" %(newpic, user_id))
    mydb.commit()



def get_row_count():
    #count number of rows
    num = mycursor.execute("SELECT COUNT (*) FROM user_data")
    for i in num:
        continue
    return i[0]

def get_encode():
    #returns ALL id and encode with two list
    id = []
    encode = []
    mycursor = mydb.cursor()
    ("Getting encoding")
    mycursor.execute("SELECT * FROM user_data")
    for row in mycursor.fetchall():
        id.append(row[0])           #user_id
        encode.append(row[1])       #encode
    mydb.commit()
    return id, encode






#TEST

add_new_user(123, "12345")
add_new_user(1234, "23456")
add_new_user(12345, "34567")
print(get_row_count())
##change_pic(123,67890)
####print(get_row_count())
####delete_user(123)
####delete_user(123)
##print(get_row_count())
####print(check_user_id(1234))
##
print(get_encode())
##



