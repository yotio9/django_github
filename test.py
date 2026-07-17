import pathlib
import sqlite3

chemin_base = pathlib.Path(__file__).parent.parent / 'db.sqlite3'

conn=sqlite3.connect(chemin_base)
cursor=conn.cursor()
cursor.execute(" UPDATE pages_contact_message SET name='fred' WHERE id=1")
conn.commit()
conn.close()