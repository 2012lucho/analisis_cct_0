import sqlite3

con = sqlite3.connect("dataset.db")
sqlite = con.cursor()


sqlite.execute("SELECT * from registros_encuesta")
registros = sqlite.fetchall()

sqlite.execute("SELECT dedicacion, count(dedicacion) as cantidad from registros_encuesta GROUP BY dedicacion")
tipos_dedicacion = sqlite.fetchall()

sqlite.execute("SELECT tipo_contrato, count(tipo_contrato) as cantidad from registros_encuesta GROUP BY tipo_contrato")
tipos_contrato = sqlite.fetchall()


print(sqlite.fetchall())


