import os
import mysql
import sqlalchemy as sql

ip = os.environ["MYSQL_HOST"]
username = os.environ["MYSQL_USERNAME"]
password = os.environ["MYSQL_PASSWORD"]
database = os.environ["MYSQL_DATABASE"]

engine = sql.create_engine('mysql://' + username + ':' + password + '@' + ip +'/' + database, echo=True)
connection = engine.connect()


##### EMPLOYEES 
## GET
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

## POST
def populateEmployees():
    connection.execute(sql.text("INSERT INTO `umbrella`.`employee` (`first_name`, `last_name`,`birth_date`, `job`, `department_code`, `hire_date`, `clearance_level`, `address`, `city`, `salary_code`) VALUES ('William', 'Birkin', '1962-07-04', 'Virologist', '1', '1977-04-25', '1', '123 Police Department', 'Raccoon City', '7');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`employee` (`first_name`, `last_name`,`birth_date`, `job`, `department_code`, `hire_date`, `clearance_level`, `address`, `city`, `salary_code`) VALUES ('Albert', 'Wesker', '1960-03-29', 'Researcher', '1', '1977-04-19', '1', '123 Police Department', 'Raccoon City', '7');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`employee` (`first_name`, `last_name`,`birth_date`, `job`, `department_code`, `hire_date`, `clearance_level`, `address`, `city`, `salary_code`) VALUES ('Oswell', 'Spencer', '1923-03-29', 'Chief Executive Officer', '2', '1969-02-21', '1', '456 Spencer Estate', 'Raccoon City', '7');"))


## DELETE
def deleteEmployee(id):
    connection.execute(sql.text("DELETE FROM employee WHERE emp_id = " + id))

def deleteEmployees():
    connection.execute(sql.text("DELETE FROM employee"))



##### DEPARTMENT 

## GET
def getAllDepartment():
    result = connection.execute(sql.text("select * from department"))
    totalInformation = ""
    for row in result:
        totalInformation += str(row) + "\n"
    return str(totalInformation)

def getSpecificDepartment(id):
    result = connection.execute(sql.text("SELECT * FROM department WHERE dept_id = " + id))
    totalInformation = ""
    for row in result:
        totalInformation += str(row) + "\n"
    return str(totalInformation)


## POST 
def populateDepartments():
    connection.execute(sql.text("INSERT INTO `umbrella`.`department` (`dept_name`, `dept_abb`) VALUES ('Executive', 'EXE');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`department` (`dept_name`, `dept_abb`) VALUES ('Research and Development', 'R&D');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`department` (`dept_name`, `dept_abb`) VALUES ('Marketing', 'MAR');"))



## DELETE
def deleteDepartment(id):
    connection.execute(sql.text("DELETE FROM department WHERE dept_id = " + id))

def deleteDepartments():
    connection.execute(sql.text("DELETE FROM deparmtent"))
