import sqlite3

connection = sqlite3.connect('project.db')

cursor = connection.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS Kurs(ID, Kursname, LeiterID);')
# cursor.execute('CREATE TABLE IF NOT EXISTS Person(ID, Name, Vorname);')
# cursor.execute('CREATE TABLE IF NOT EXISTS Datei(ID, Kursname);')
# cursor.execute('CREATE TABLE IF NOT EXISTS Mitglied(PersonID, KursID)')

# cursor.execute('INSERT INTO Kurs VALUES (0, "Deutsch")')

def build_args(args: list[str]) -> str:
    build = ''
    for arg in args:
        build += str(arg) + ','
    return build[:-1]

def create_table(table: str, args: list[str]) -> None:
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {table}({build_args(args)});')

def insert_into(table: str, args: list[str]) -> None:
    cursor.execute(f'INSERT INTO {table} VALUES ({build_args(args)})')

create_table('Kurs', ['ID', 'Kursname', 'LeiterID'])
insert_into('Kurs', [1, '"Englisch"'])


result = cursor.execute('SELECT * FROM Kurs')
print(result.fetchall())