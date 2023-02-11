import sqlite3

# Establist a connection and a cursor
connection = sqlite3.connect("data_db.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)

# Query certain columns
cursor.execute("SELECT band, date FROM events WHERE band='Lions'")
rows = cursor.fetchall()
print(rows)

# Inserting new rows
#new_row1 = [('Cats', 'Cat city', '10.02.2023'), ('Knives', 'Knives city', '11.02.2023')]

#cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_row1) # ? ? ? so trije podatki v tuplu, drugi parameter new_row1 pa je kar hočemo vpisat v db
#connection.commit()