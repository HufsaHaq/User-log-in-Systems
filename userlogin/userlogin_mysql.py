import MySQLdb

DB_HOST = 'moodle.wgs.org'
DB_USER = 'userlogin'
DB_PASSWORD = 'userlogin'
DB_NAME = 'userlogin'


def deletedatabase():

    print("Running deletedatabase")
    
    # connect to the database
    db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = db.cursor()

    cursor.execute('''DROP TABLE IF EXISTS table_users;''')
    
    print("Tables deleted")

    #save the database
    db.commit()  

    #dis-connect from the database
    db.close()
    
def createdatabase():

    print("Running createdatabase")

    # connect to the database
    db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = db.cursor()

    #create user table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS table_users(
    userID INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL);
    ''')
    
    #save the database
    db.commit()
    
    #dis-connect from the database
    db.close()

    print("Table created")

def populatedatabase():

    print("Running populatedatabase")

    # connect to the database
    db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = db.cursor()

    #populate the users table
    cursor.execute('''
    INSERT INTO table_users(username, password)
    VALUES
    ("Bill","billbill"),
    ("Ben","benben");
    ''')

    #save the database
    db.commit()
    
    #dis-connect from the database
    db.close()

    #self.csvimport()
    print("Populated the database")

def showmeall():

    print("Running showmeall")

    # connect to the database
    db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = db.cursor()

    # show the entries in the users table
    print("USERS TABLE")
    cursor.execute("SELECT * FROM table_users")
    results = cursor.fetchall()

    #dis-connect from the database
    db.close()

    for i in results:
        print(i)

    return results

def userlogin(username, password):

    # connect to the database
    db = MySQLdb.connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)
    cursor = db.cursor()

    mycommand = 'SELECT * FROM table_users WHERE username = %s'
    cursor.execute(mycommand,(username,))
    results = cursor.fetchall()

    #dis-connect from the database
    db.close()
    
    if results == ():
        return ["Error", "Username not found"]
    elif results[0][2] != password:
        return ["Error", "Password incorrect"]
    else:
        return ["Logged in", username]

def adduser(username, password1, password2):

    answer = ["Error", "code not done yet"]

    ############
    ############
    ############
    ############
    ############

    return answer


def updateuser(username, password1, password2):

    answer = ["Error", "code not done yet"]

    ############
    ############
    ############
    ############
    ############

    return answer

def deleteuser(username):

    answer = ["Error", "code not done yet"]

    ############
    ############
    ############
    ############
    ############

    return answer


###############################################
###############################################
# MAIN PROGRAM
if __name__ == "__main__":

    menu = "\nMENU\n1: delete\n2: create\n3: populate\n4: showmeall\n5: Login\n6: Add user\n7: Update user\n8: Delete user\n0: quit\n"
    
    choice = input(menu)

    while choice != "0":
        
        if choice =="1":
            # drop the users table from the database
            deletedatabase()
        elif choice == "2":
            # create database tables
            createdatabase()
        elif choice =="3":
            # insert default users for testing
            populatedatabase()
        elif choice =="4":
            # print each row of the users table
            showmeall()
        elif choice == "5":
            # login
            username = input("Username: ")
            password1 = input("Password: ")
            result = userlogin(username, password1)
            print(result)
        elif choice == "6":
            # add a new user
            username = input("Username: ")
            password1 = input("Password: ")
            password2 = input("Password: ")
            result = adduser(username, password1, password2)
            print(result)
        elif choice == "7":
            # update a users password
            username = input("Username: ")
            password1 = input("Password: ")
            password2 = input("Password: ")
            result = updateuser(username, password1, password2)
            print(result)
        elif choice == "8":
            # delete a user
            username = input("Username: ")
            result = deleteuser(username)
            print(result)
        else:
            print("Error")

        choice = input(menu)

    print("goodbye")
