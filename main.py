# Importing module
import mysql.connector

mydb = mysql.connector.connect(
    host = "23.229.209.9",
    user = "mrbizchicken",
    password = "Jordan1504",
   database = "jordan"
)

mycursor = mydb.cursor()


def serach(mycursor, pram, vaule):


    mycursor.execute(f"SELECT * FROM Pokemon WHERE  {pram} = '{vaule}'")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)



def delete_card(mycursor, pram, value):
    mycursor.execute(f"DELETE FROM Pokemon WHERE {pram} = '{value}'")


def insert_card(mycursor, name, element, health):
    sql = "INSERT INTO Pokemon (id, name, element, health) VALUES (%s, %s, %s, %s)"
    val = (0, f"{name}", f"{element}", health)


    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


def show_table(mycursor):
    mycursor.execute('SELECT * FROM Pokemon')
    data = mycursor.fetchall ()
    for x in data:
      print(x)
insert_card(mycursor, "blastoise", "water", 300)
# serach(mycursor, "name", "charizard")
# delete_card(mycursor, "name", "charizard")
show_table(mycursor)
