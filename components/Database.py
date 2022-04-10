import sqlite3

def checkSetup():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='instructors'")
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return False
    return True

def setup():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Create Instructors Table
    create_instructors_table = """
        CREATE TABLE IF NOT EXISTS instructors (
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          hours INTEGER NOT NULL,
          schedule TEXT NOT NULL,
          active BOOLEAN NOT NULL DEFAULT 1 CHECK (
            active IN (0, 1)
          )
        );
    """
    # Create Rooms Table
    create_rooms_table = """
        CREATE TABLE IF NOT EXISTS rooms (
          id INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          type TEXT NOT NULL,
          schedule TEXT NOT NULL,
          active BOOLEAN NOT NULL DEFAULT 1 CHECK (
            active IN (0, 1)
          )
        );
    """


    cursor.execute(create_instructors_table)
    cursor.execute(create_rooms_table)
    conn.commit()
    conn.close()

def getConnection():
    return sqlite3.connect('database.db')