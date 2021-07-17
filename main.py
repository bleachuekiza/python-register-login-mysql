import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testsqlinjection"
)

def login_verification():
    username = input('username :')
    password = input('password :')
    mycursor = mydb.cursor()
    sql = "select * from users where username = %s and password = %s"
    mycursor.execute(sql,[(username),(password)])
    results = mycursor.fetchone()
    if results:
        print('Login Success')
        print(results)
        print(type(results))
    else:
        print('Login fail username or password wrong')

def register():
    username = input('username :')
    password = input('password :')
    confirmpassword = input('confirm password :')
    if password == confirmpassword:
        print('password match')
    else:
        print('password not match')


def menu():
    print('[1]Login\n[2]Register')
    selecetmenu = int(input('Choice Menu :'))
    if selecetmenu == 1:
        login_verification()
    elif selecetmenu == 2:
        register()

if __name__ == "__main__":
    menu()