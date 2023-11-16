import sqlite3

connection = sqlite3.connect('project.db')

cursor = connection.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS Kurs(ID, Kursname);')

cursor.execute('INSERT INTO Kurs VALUES (0, "Deutsch")')

result = cursor.execute('SELECT * FROM Kurs')
print(result.fetchall())