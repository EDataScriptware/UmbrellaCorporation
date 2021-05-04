import os
import mysql
import sqlalchemy as sql

ip = os.environ["MYSQL_HOST"]
username = os.environ["MYSQL_USERNAME"]
password = os.environ["MYSQL_PASSWORD"]
database = os.environ["MYSQL_DATABASE"]

engine = sql.create_engine('mysql://' + username + ':' + password + '@' + ip +'/' + database, echo=True)
connection = engine.connect()

def getAllEmployees():
    result = connection.execute(sql.text("select * from employee"))
    totalInformation = ""
    for row in result:
        totalInformation += str(row) + "\n"
    return str(totalInformation)

def getSpecificEmployee(id):
    result = connection.execute(sql.text("SELECT * FROM employee WHERE emp_id = " + id))
    totalInformation = ""
    for row in result:
        totalInformation += str(row) + "\n"
    return str(totalInformation)