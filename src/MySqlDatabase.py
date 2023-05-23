import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase"
)

print(mydb)

mycursor = mydb.cursor()

#sql = "INSERT INTO Persons (PersonID, LastName, FirstName, Address, City) VALUES (%s, %s, %s, %s, %s)"
#val = ("15", "John", "Doe", "Highway 2", "Prague")
#mycursor.execute(sql, val)

#mydb.commit()

#sql = "UPDATE Persons SET City = 'London' WHERE City IS NULL"

#mycursor.execute(sql)

mydb.commit()
