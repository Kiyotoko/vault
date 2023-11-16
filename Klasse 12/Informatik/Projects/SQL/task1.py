import sqlite3

connection = sqlite3.connect('project.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Kurs(ID, Kursname);')

print(cursor.execute('.tables'))
