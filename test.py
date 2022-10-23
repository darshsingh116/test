import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor = mydb.cursor()

mycursor.execute("create database if not exists botbuck")
mycursor.execute("use botbuck")

#creating required tables

mycursor.execute("create table if not exists data(userid varchar(255) primary key, primo int,wish int)")
mydb.commit()

