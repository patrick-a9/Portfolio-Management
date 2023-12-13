import sqlite3

# Crear una conexión a la base de datos
conn = sqlite3.connect('api.sqlite')
c = conn.cursor()

# Crear la tabla de usuarios
c.execute("""
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    mail TEXT UNIQUE,
    username TEXT UNIQUE,
    password TEXT
)
""")

# Crear la tabla de tickers
c.execute("""
CREATE TABLE Tickers (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    tickers TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(id)
)
""")

# Guardar (commit) los cambios
conn.commit()

# Cerrar la conexión a la base de datos
conn.close()