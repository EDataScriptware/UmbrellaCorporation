import os
import mysql
import sqlalchemy as sql
import json

ip = os.environ["MYSQL_HOST"]
username = os.environ["MYSQL_USERNAME"]
password = os.environ["MYSQL_PASSWORD"]
database = os.environ["MYSQL_DATABASE"]

engine = sql.create_engine('mysql://' + username + ':' + password + '@' + ip +'/' + database, echo=True)
connection = engine.connect()

##### EMPLOYEES 
## GET
def getAllEmployees():
    sqlObject = connection.execute(sql.text("select * from employee"))
    return sqlObject

def getSpecificEmployee(id):
    sqlObject = connection.execute(sql.text("SELECT * FROM employee WHERE emp_id = " + id))
    return sqlObject


def getEmployeeByDepartment(id):
    sqlObject = connection.execute(sql.text("SELECT * FROM employee WHERE department_code = " + id))
    return sqlObject


## POST
def populateEmployees():
    connection.execute(sql.text("INSERT INTO `umbrella`.`employee` (`first_name`, `last_name`,`birth_date`, `job`, `department_code`, `hire_date`, `clearance_level`, `address`, `city`, `salary_code`) VALUES ('William', 'Birkin', '1962-07-04', 'Virologist', '1', '1977-04-25', '1', '123 Police Department', 'Raccoon City', '7');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`employee` (`first_name`, `last_name`,`birth_date`, `job`, `department_code`, `hire_date`, `clearance_level`, `address`, `city`, `salary_code`) VALUES ('Albert', 'Wesker', '1960-03-29', 'Researcher', '1', '1977-04-19', '1', '123 Police Department', 'Raccoon City', '7');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`employee` (`first_name`, `last_name`,`birth_date`, `job`, `department_code`, `hire_date`, `clearance_level`, `address`, `city`, `salary_code`) VALUES ('Oswell', 'Spencer', '1923-03-29', 'Chief Executive Officer', '2', '1969-02-21', '1', '456 Spencer Estate', 'Raccoon City', '7');"))

def createEmployee(record):
    firstname = str(record['first_name'])
    middlename = str(record['middle_name'])
    lastname = str(record['last_name'])
    birthdate = str(record['birth_date'])
    jobTitle = str(record['job'])
    deptCode = str(record['department_code'])
    hireDate = str(record['hire_date'])
    clearance = str(record['clearance_level'])
    address = str(record['address'])
    city = str(record['city'])
    salary_code = str(record['salary_code'])

    connection.execute(sql.text("INSERT INTO `umbrella`.`employee` (`first_name`, `middle_name`, `last_name`,`birth_date`, `job`, `department_code`, `hire_date`, `clearance_level`, `address`, `city`, `salary_code`) VALUES ('" + firstname + "', '" + lastname + "', '" + middlename + "', '" + birthdate + "', '" + jobTitle + "', '" + deptCode + "', '" + hireDate + "', '" + clearance + "', '" + address + "', '" + city + "', '" + salary_code + "' )"))


## DELETE
def deleteEmployee(id):
    connection.execute(sql.text("DELETE FROM employee WHERE emp_id = " + id))

def deleteEmployees():
    connection.execute(sql.text("DELETE FROM employee"))

## PUT 
def updateEmployee(id, record):
    firstname = str(record['first_name'])
    middlename = str(record['middle_name'])
    lastname = str(record['last_name'])
    birthdate = str(record['birth_date'])
    jobTitle = str(record['job'])
    deptCode = str(record['department_code'])
    hireDate = str(record['hire_date'])
    clearance = str(record['clearance_level'])
    address = str(record['address'])
    city = str(record['city'])
    salary_code = str(record['salary_code'])

    connection.execute(sql.text("UPDATE employee SET first_name = '" + firstname + "', middle_name = '" + middlename + "', last_name = '" + lastname + "', birth_date = '" + birthdate + "', job = '" + jobTitle + "', department_code = '" + deptCode + "', hire_date = '" + hireDate + "', clearance_level = '" + clearance + "', address = '" + address + "', city = '" + city + "', salary_code = '" + salary_code + "' WHERE emp_id = " + str(id)))


##### DEPARTMENT 

## GET
def getAllDepartment():
    sqlObject = connection.execute(sql.text("select * from department"))
    return sqlObject

def getSpecificDepartment(id):
    sqlObject = connection.execute(sql.text("SELECT * FROM department WHERE dept_id = " + id))
    return sqlObject

## POST 
def populateDepartments():
    connection.execute(sql.text("INSERT INTO `umbrella`.`department` (`dept_name`, `dept_abb`) VALUES ('Executive', 'EXE');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`department` (`dept_name`, `dept_abb`) VALUES ('Research and Development', 'R&D');"))
    connection.execute(sql.text("INSERT INTO `umbrella`.`department` (`dept_name`, `dept_abb`) VALUES ('Marketing', 'MAR');"))

def createDepartment(record):
    deptName = str(record['dept_name'])
    deptAbb = str(record['dept_abb'])

    connection.execute(sql.text("INSERT INTO `umbrella`.`department` (`dept_name`, `dept_abb`) VALUES ('" + deptName + "', '" + deptAbb + "');"))


## DELETE
def deleteDepartment(id):
    connection.execute(sql.text("DELETE FROM department WHERE dept_id = " + id))

def deleteDepartments():
    connection.execute(sql.text("DELETE FROM deparmtent"))

## PUT 
def updateDepartment(id, record):
    deptName = str(record['dept_name'])
    deptAbb = str(record['dept_abb'])

    connection.execute(sql.text("UPDATE department SET dept_name = '" + deptName + "', dept_abb = '" + deptAbb + "' WHERE dept_id = " + str(id)))