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
                 "l_name VARCHAR(12) NOT NULL,"
                 "f_name VARCHAR(12) NOT NULL,"
                 "encoding VARCHAR(2000) NOT NULL);")


def check_user_id(user_id):
##    DONE!
##    DONE!
    # check if user exisit
    mycursor.execute("DELETE from user_data WHERE user_id = %i" %user_id)



def add_new_user(user_id, l_name, f_name, pic):
##    DONE!
##    DONE!
    # check if user exisit
    mycursor.execute("SELECT user_id FROM user_data WHERE user_id = %i" % user_id)
    flag = 0
    for row in mycursor.fetchall():
        flag = 1
    if flag ==1:
        print("This user already exist")
    else:
        mycursor.execute("INSERT INTO user_data (user_id, l_name, f_name, pic) VALUES (?,?,?,?)", (user_id, l_name, f_name, pic))
        print("New user added to database: ", mycursor.lastrowid)
        mydb.commit()

def delete_user(user_id):
    #Delete user info
##    Done!
##    Done!
    mycursor.execute("DELETE FROM user_data WHERE user_id = %i" %user_id)
    mydb.commit()


def change_pic(user_id, newpic):
    #change photo info of one user
##    Done!
##    Done!
    mycursor.execute("UPDATE user_data SET pic = %s WHERE user_id = %i" %(newpic, user_id))
    mydb.commit()


def get_row_count():
##   DONE!
##   DONE!
    # does not work in no rows
    counter = 0
    num = mycursor.execute("SELECT COUNT (*) FROM user_data")

    #if num.ISNULL():
     #   return 0
    return (len(list(mycursor)))




##write_encoding(123456, "ASDFZG")
add_new_user(123,"D","K","12345")
#print(get_row_count())
change_pic(123,67890)
#delete_user(123)
print(get_row_count())
delete_user(123)
print(get_row_count())
##print(check_user_id(1234))






