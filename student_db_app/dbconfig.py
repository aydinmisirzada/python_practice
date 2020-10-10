import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime

class database:
    student_info = []

    conn = 0
    cursor = 0
    query = 0

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost',db='your_db',
                                           user='admin',password='admin')
            print("Connection to database established!")
        except mysql.connector.Error as error:
            print("Error:",error)

    def execute_query(self,type,query):
        if type == 'select':
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            student_info = self.cursor.fetchall()
            self.cursor.close()
            return student_info
        elif type == 'insert' or type=='update' or type=='delete':
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            self.cursor.close()
            self.conn.commit()
        else:
            print("Wrong query")


    def add_student(self,student):
        values = ""
        for i in student:
            values += f"'{i}', "
        self.query = f"INSERT INTO students VALUES({values}now(),NULL)"
        self.execute_query('insert',self.query)


    def update_student(self,student):
        self.query = f"UPDATE students SET first_name = '{student[0]}', last_name = '{student[1]}', email = '{student[2]}', street = '{student[3]}', city = '{student[4]}', state = '{student[5]}', zip = {student[6]}, phone = '{student[7]}', birth_date = '{student[8]}', sex = '{student[9]}' WHERE student_id = {student[10]}"
        self.execute_query('update',self.query)

    def delete_student(self,id):
        self.query = f"DELETE FROM students WHERE student_id = {id}"
        self.execute_query('delete',self.query)
